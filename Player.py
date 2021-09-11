'''
Created on Aug 25, 2021

@author: mikes
'''
import sys

from Contents import PLAYER_ACTIVE_CARD, PLAYER_HELD_CARD, ACTION_BUY, ACTION_PASS, PLAYERS,\
    CARPENTER_WORKSHOP_ABILITY, GOLD_SMELTER_ABILITY, BOARD_LOWER_ROW,\
    ARISTOCRAT_CARD_TYPE, BUILDING_CARD_TYPE, IS_UPGRADABLE, IS_NOT_UPGRADABLE,\
    ACTION_HOLD, WAREHOUSE_ID, WAREHOUSE_BONUS_CARDS, WORKER_CARD_TYPE,\
    CLASS_ALL, TRADING_CARD_TYPE, ACTION_UPGRADE, OBSERVATORY_ID, PUB_ID
from random import randint
from select import select



class Player(object):
   
    
    def __init__(self, ID, Name ,Color, Money, Score, Marker):
        self.ID = ID
        self.Name = Name
        self.Color = Color
        self.Money = Money
        self.Score = Score
        self.Marker = Marker
        self.Hand = []
        self.hasPassed = False
        self.HeldCards = 0
        self.WarehouseBonus = 0
        self.ObservatoryBonus = 0
        self.PubBonus = 0
        self.UniqueAristrocrats = 0
        
    def BuyCard(self, card_to_buy):
        
        if card_to_buy.CardStatus == PLAYER_HELD_CARD :
            self.HeldCards -= 1
        
        # Check to see if the Card was a unique aristocrat. Must be done before card is added to the Hand
        UniqueAristrocrat = True
        if card_to_buy.CardType == ARISTOCRAT_CARD_TYPE :
            print ("Player buying Aristocrat Card Checking for Uniqueness")
            for Card in self.Hand :
                if Card.CardID == card_to_buy.CardID and Card.CardStatus == PLAYER_ACTIVE_CARD :
                    UniqueAristrocrat = False
                    
            if UniqueAristrocrat == True :
                self.UniqueAristrocrats += 1
                print ("Aristocrat was unique adding to total. New Total: " + str(self.UniqueAristrocrats))
        
        # Add the Card to the hand
        card_to_buy.CardStatus = PLAYER_ACTIVE_CARD
        self.Hand.append(card_to_buy)
                
        # Activate Bonus for Special Card
        if card_to_buy.CardID == WAREHOUSE_ID :
            self.WarehouseBonus = WAREHOUSE_BONUS_CARDS
            
        if card_to_buy.CardID == OBSERVATORY_ID :
            self.ObservatoryBonus = 1
            
        if card_to_buy.CardID == PUB_ID :
            self.PubBonus = 1
        
        Player.hasPassed = False
        #print(PLAYERS[self.ID][1] + " bought a " + card_to_buy.CardName)
    
    def UpgradeCard (self, TradingCard, TargetCard):
        
        if TradingCard.CardStatus == PLAYER_HELD_CARD :
            self.HeldCards -= 1
            
        # Check to see if the Upgrade Card produced a unique aristocrat. Only way to produce Unique Aristocrat is to upgrade a duplicate
        UniqueAristrocrat = False
        if TradingCard.CardType == ARISTOCRAT_CARD_TYPE :
            print ("Player Upgrading Aristocrat Card Checking for Uniqueness")
            for Card in self.Hand :
                if Card != TargetCard and Card.CardID == TargetCard.CardID and Card.CardStatus == PLAYER_ACTIVE_CARD :
                    UniqueAristrocrat = True
                    
            if UniqueAristrocrat == True :
                self.UniqueAristrocrats += 1
                print ("Aristocrat was unique adding to total. New Total: " + str(self.UniqueAristrocrats))   
        
        TradingCard.CardStatus = PLAYER_ACTIVE_CARD
        self.Hand.append(TradingCard)
        self.Hand.remove(TargetCard)
              
        if TargetCard.CardID == WAREHOUSE_ID :
            self.WarehouseBonus = 0
            
        if TargetCard.CardID == OBSERVATORY_ID :
            self.ObservatoryBonus = 0
            
        if TargetCard.CardID == PUB_ID :
            self.PubBonus = 0
        
        Player.hasPassed = False       

    
    def HoldCard(self, card_to_hold):
        card_to_hold.CardStatus = PLAYER_HELD_CARD
        self.Hand.append(card_to_hold)
        self.HeldCards += 1
        Player.hasPassed = False
    
    def Pass (self):
        self.hasPassed = True
        return 
     
    def UseCardAbility (self, card_with_ability):
        return 
    
    
    def DetermineCardCosts (self, CardsInPlay):
        
        GoldSmelterAdjustment = 0
        CarpenterWorkshopAdjustment = 0
        
        # Reset Discounted Cost
        for Card in CardsInPlay :
            Card.DiscountedCost = Card.CardCost  
       
        # Find out if the Player has the Gold Smelter or the Carpenter Workshop Cards
        for Card in self.Hand :

            if Card.SpecialAbility == GOLD_SMELTER_ABILITY and Card.CardStatus == PLAYER_ACTIVE_CARD:
                GoldSmelterAdjustment = 1  
            if Card.SpecialAbility == CARPENTER_WORKSHOP_ABILITY and Card.CardStatus == PLAYER_ACTIVE_CARD:
                CarpenterWorkshopAdjustment = 1
                
        for Card in CardsInPlay :
            # Apply Discount for duplicates between the Cards in Play and the Players Hand
            for PlayerCard in self.Hand :
                if Card.CardID == PlayerCard.CardID and PlayerCard.CardStatus == PLAYER_ACTIVE_CARD:
                    Card.DiscountedCost -= 1
            
            # Apply Discount for being in the lower row
            if Card.Row == BOARD_LOWER_ROW :
                Card.DiscountedCost -= 1
                
            # Apply Discount for the Gold Smelter
            if Card.CardType == ARISTOCRAT_CARD_TYPE :
                Card.DiscountedCost -= GoldSmelterAdjustment
                
            # Apply Discount for the Carpenter Workshop
            if Card.CardType == BUILDING_CARD_TYPE :
                Card.DiscountedCost -= CarpenterWorkshopAdjustment

        # Apply the Minimum Card Cost
        for Card in CardsInPlay :
            if Card.DiscountedCost <= 0 :
                Card.DiscountedCost = 1
                     
        return CardsInPlay 
    
    def DetermineBuyableCards (self, CardsInPlay):
        
        BuyableCards = []
        
        # Get Buyable Cards from the Board. Player must have more money than the discounted cost and the card needs to 
        # be upgradable i.e. a Worker, Building or Aristocrat card. Trading Cards are bought through the Upgrade function
        for Card in CardsInPlay :
            if Card.DiscountedCost <= self.Money and Card.isUpgradable == IS_UPGRADABLE :
                BuyableCards.append(Card)
        
        # Get Buyable Cards being held in the players hand
        for Card in self.Hand :
            if Card.DiscountedCost <= self.Money and Card.CardStatus == PLAYER_HELD_CARD and Card.isUpgradable == IS_UPGRADABLE  :
                BuyableCards.append(Card)
        
        return BuyableCards
            
    def DetermineHoldableCards (self, CardsInPlay):
        HoldableCards = []
        
        # Get Cards that can be held from the Board. Player will only hold card if he cant afford it otherwise he will buy the card 
        # Any Trading Card can be held regardless of whether or not the player can buy it. Trading Card final cost is determined by the card being upgraded
        for Card in CardsInPlay :
            if Card.DiscountedCost > self.Money and Card.isUpgradable == IS_UPGRADABLE :
                HoldableCards.append(Card)
            if Card.CardType  == TRADING_CARD_TYPE :
                HoldableCards.append(Card)
        
        return HoldableCards    
    
    def DetermineUpgradeableCardPairs (self, CardsInPlay):
        
        try :
            TargetCards = []
            TradingCards = []
            UpgradeableCardPairs = []
            
            # Find all  Trading Cards in Play. Upgrade Cost to be calculated later
            for Card in CardsInPlay :
                if Card.isUpgradable == IS_NOT_UPGRADABLE :
                    TradingCards.append(Card)
            
            # Find all Trading Cards being held in the players hand. Upgrade Cost to be calculated later
            for Card in self.Hand :
                if Card.CardStatus == PLAYER_HELD_CARD and Card.isUpgradable == IS_NOT_UPGRADABLE  :
                    TradingCards.append(Card)
                    
            # Find all active cards in the players hand that can be upgraded
            for Card in self.Hand :
                if Card.CardStatus == PLAYER_ACTIVE_CARD and Card.isUpgradable == IS_UPGRADABLE  :
                    TargetCards.append(Card)
                    
            # Make Upgrade Pairs
            for TradingCard in TradingCards :
                for TargetCard in TargetCards :
                    if (TradingCard.CardClass == TargetCard.CardClass) or (TradingCard.CardType == WORKER_CARD_TYPE and TargetCard.CardClass == CLASS_ALL) :
                        
                        # Determine the Upgrade cost and check if the player can afford it
                        TradingCardCost = TradingCard.DiscountedCost - TargetCard.UpgradeValue
                        if TradingCardCost < 1 :
                            TradingCardCost = 1
                        
                        if TradingCardCost <= self.Money :
                            UpgradeableCardPairs.append([TradingCard, TargetCard])
            
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
            
        return UpgradeableCardPairs
    
    def DetermineAction(self, Actions):
        
        SelectedAction = Actions [randint(0, len(Actions)-1)]
        
        if SelectedAction[0] == ACTION_BUY :
            #print(PLAYERS[self.ID][1] + " decided to buy " + SelectedAction[1].CardName)
            return ACTION_BUY, SelectedAction[1]
        
        if SelectedAction[0] == ACTION_HOLD:
            return ACTION_HOLD, SelectedAction[1]
        
        if SelectedAction[0] == ACTION_UPGRADE :
            return ACTION_UPGRADE, SelectedAction[1]
        
        if SelectedAction[0] == ACTION_PASS :
            return ACTION_PASS, []
