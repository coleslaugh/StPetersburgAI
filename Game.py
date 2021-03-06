#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Game Class - Contains Decks and Players
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------

from random import random
import numpy as numpy
import sys

from Deck import Deck
from Player import Player

from Contents import PLAYERS, PLAYER_1, PLAYER_2, PLAYER_3, PLAYER_4, \
    PLAYER_BLUE, PLAYER_GREEN, PLAYER_YELLOW, PLAYER_RED, \
    PLAYERS_PER_GAME, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, \
    WORKER_CARDS, BUILDING_CARDS, ARISTOCRAT_CARDS, TRADING_CARDS, \
    WORKER_CARD_TYPE, BUILDING_CARD_TYPE, ARISTOCRAT_CARD_TYPE, TRADING_CARD_TYPE, \
    PHASES, PHASE_WORKER, PHASE_BUILDING, PHASE_ARISTOCRAT, PHASE_TRADING, \
    MARKERS,PLAYER_MARKER_WORKER, PLAYER_MARKER_BUIDLING, PLAYER_MARKER_ARISTOCRAT, PLAYER_MARKER_TRADING, \
    ACTIONS, ACTION_BUY, ACTION_HOLD, ACTION_PASS, ACTION_UPGRADE, ACTION_OBSERVATORY, ACTION_PUB, \
    BOARD_UPPER_ROW, BOARD_LOWER_ROW, \
    PLAYER_ACTIVE_CARD, PLAYER_HELD_CARD, PENALTY_HELD_CARD, PLAYER_DELT_CARD, PLAYER_DRAW_CARD, \
    TAX_MAN_ID, MARIINSKIJ_THEATER_ID, MAX_CARDS_TO_HOLD, \
    MONEY_PER_VP, ARISTOCRAT_SCORING, CLASS_ALL, MAX_CARDS_ON_BOARD, \
    PUB_ABILITY, OBSERVATORY_ABILITY, IS_UPGRADABLE
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Game Class
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    
class Game(object):

    def __init__(self, GameID):
        self.GameID = GameID
        self.WorkerDeck = []
        self.BuildingDeck = []
        self.AristocratDeck = []
        self.TradingDeck = []
        self.CardsInPlay = []
        self.Players = []
        self.EndOfGame = False
        self.NumPlayers = PLAYERS_PER_GAME
        self.CurrentRound = 0
        self.CurrentPhase = 0

                
    def GameSetup (self):
        self.CreateDecks()
        self.CreatePlayers()
        self.AssignMarkers()

    def CreatePlayers (self):   
        self.Players.append(Player(PLAYER_1, "Mike", PLAYER_GREEN, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player(PLAYER_2, "Allen", PLAYER_BLUE, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player(PLAYER_3, "Susan", PLAYER_YELLOW, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player(PLAYER_4, "Stacey", PLAYER_RED, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        
    def CreateDecks (self):
        self.WorkerDeck = Deck (WORKER_CARDS, WORKER_CARD_TYPE)
        self.BuildingDeck = Deck (BUILDING_CARDS, BUILDING_CARD_TYPE)
        self.AristocratDeck = Deck (ARISTOCRAT_CARDS, ARISTOCRAT_CARD_TYPE)
        self.TradingDeck = Deck (TRADING_CARDS, TRADING_CARD_TYPE)
                
        self.BuildingDeck.Shuffle()
        self.WorkerDeck.Shuffle()
        self.AristocratDeck.Shuffle()
        self.TradingDeck.Shuffle()
        
    def AssignMarkers (self):
        Markers = [[PLAYER_MARKER_WORKER, random ()],[PLAYER_MARKER_BUIDLING, random()],[PLAYER_MARKER_ARISTOCRAT, random()],[PLAYER_MARKER_TRADING, random()]]
        Markers.sort(key=lambda x: x[1])
        
        for x in range(PLAYERS_PER_GAME):
            self.Players[x].Marker = Markers[x][0]
            
        print ("Markers are Assigned: " +   PLAYERS[0][1] + "-" + MARKERS[self.Players[0].Marker][1] + " : "  + 
                                            PLAYERS[1][1] + "-" + MARKERS[self.Players[1].Marker][1] + " : "  + 
                                            PLAYERS[2][1] + "-" + MARKERS[self.Players[2].Marker][1] + " : "  + 
                                            PLAYERS[3][1] + "-" + MARKERS[self.Players[3].Marker][1])
       
    def DealCards (self, GamePhase):
        print ("Starting to Deal Cards for the " + PHASES[GamePhase][1] + " - Worker Deck Top Card - " + str(self.WorkerDeck.TopCard) + " : Building Deck Top Card - " + str(self.BuildingDeck.TopCard) + " : Aristocrat Deck Top Card - " + str(self.AristocratDeck.TopCard) + " : Trading Deck Top Card - " + str(self.TradingDeck.TopCard))
        print ("Cards to deal: " + str(MAX_CARDS_ON_BOARD - len(self.CardsInPlay)))
        CardsDelt = ""
        
        if GamePhase == PHASE_WORKER :
            ActiveDeck = self.WorkerDeck
        if GamePhase == PHASE_BUILDING :
            ActiveDeck = self.BuildingDeck
        if GamePhase == PHASE_ARISTOCRAT :
            ActiveDeck = self.AristocratDeck
        if GamePhase == PHASE_TRADING :
            ActiveDeck = self.TradingDeck
        
        while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
            if ActiveDeck.TopCard < len (ActiveDeck.Cards) :
                ActiveDeck.Cards[ActiveDeck.TopCard].CardStatus = PLAYER_DELT_CARD
                self.CardsInPlay.append(ActiveDeck.Cards[ActiveDeck.TopCard])
                CardsDelt = CardsDelt + " : " + ActiveDeck.Cards[ActiveDeck.TopCard].CardName 
                ActiveDeck.TopCard += 1
            if ActiveDeck.TopCard >= len (ActiveDeck.Cards) :
                self.EndOfGame = True
                print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt + " : Deck Empty. Game will Terminate at the end of the phase")
                return
                
        print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt)

    def RotateCards (self):
    
        CardsDiscarded = ""
        CardsLowered = ""
        for Card in self.CardsInPlay[:] :
            if Card.Row == BOARD_UPPER_ROW :
                Card.Row = BOARD_LOWER_ROW
                CardsLowered = CardsLowered + " : " + Card.CardName
            else :
                CardsDiscarded = CardsDiscarded + " : " + Card.CardName
                self.CardsInPlay.remove(Card)
                
        print ("Cards moved to the bottom row" +  CardsLowered)
        print ("Cards discarded from the Game" +  CardsDiscarded)
    
    def AssignCurrentPhaseOrder (self, Phase):
        
        CurrentPhasePlayers = []
        # Find the player with the right marker
        CurrentPhasePlayers.append(next(Player for Player in self.Players if Player.Marker == Phase))
        SecondPlayerID = (CurrentPhasePlayers[0].ID + 1) % PLAYERS_PER_GAME
        ThirdPlayerID = (CurrentPhasePlayers[0].ID + 2) % PLAYERS_PER_GAME
        ForthPlayerID = (CurrentPhasePlayers[0].ID + 3) % PLAYERS_PER_GAME
        
        CurrentPhasePlayers.append(self.Players[SecondPlayerID])
        CurrentPhasePlayers.append(self.Players[ThirdPlayerID])
        CurrentPhasePlayers.append(self.Players[ForthPlayerID])
        
        return CurrentPhasePlayers
    
    def RotateMarkers (self):
        TempMarker = self.Players[PLAYER_4].Marker 
        self.Players[PLAYER_4].Marker = self.Players[PLAYER_3].Marker
        self.Players[PLAYER_3].Marker = self.Players[PLAYER_2].Marker
        self.Players[PLAYER_2].Marker = self.Players[PLAYER_1].Marker
        self.Players[PLAYER_1].Marker = TempMarker
        print ("Markers are Rotated: " +    PLAYERS[PLAYER_1][1] + "-" + MARKERS[self.Players[PLAYER_1].Marker][1] + " : "  + 
                                            PLAYERS[PLAYER_2][1] + "-" + MARKERS[self.Players[PLAYER_2].Marker][1] + " : "  + 
                                            PLAYERS[PLAYER_3][1] + "-" + MARKERS[self.Players[PLAYER_3].Marker][1] + " : "  + 
                                            PLAYERS[PLAYER_4][1] + "-" + MARKERS[self.Players[PLAYER_4].Marker][1])
        return 
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    # Phase Action Functions
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    def ProcessPhaseActions (self, Phase, Round_Count):
        
        # Assign order of play for current phase based on who has the marker.
        CurrentPhasePlayers = self.AssignCurrentPhaseOrder(Phase)
        self.CurrentRound = Round_Count
        self.CurrentPhase = Phase
        try :
        
            while not (CurrentPhasePlayers[PLAYER_1].hasPassed == True and CurrentPhasePlayers[PLAYER_2].hasPassed == True and CurrentPhasePlayers[PLAYER_3].hasPassed == True and CurrentPhasePlayers[PLAYER_4].hasPassed == True) :
                for Player in CurrentPhasePlayers :
                    # Determine Card Costs here and pass it to Determine Action
                    Player.DetermineCardCosts(self.CardsInPlay)
    
                    # Determine which Aristocrats on the board are unique to the player. Sets the Unique Aristocrat Flag
                    Player.DetermineUniqueAristocrats(self.CardsInPlay)
                    
                    # Determine which cards in play the current player can Buy with the money he has
                    BuyableCards = Player.DetermineBuyableCards(self.CardsInPlay)
                    
                    # Determine which cards in play the Current player can hold
                    HoldableCards = Player.DetermineHoldableCards(self.CardsInPlay)
                    
                    # Determine which cards the current player can upgrade with the money he has
                    UpgradableCards = Player.DetermineUpgradeableCardPairs (self.CardsInPlay)
                    
                    # Determine if the current player has the Observatory and which decks can be drawn from. Must check if it's been used this round
                    if Phase == PHASE_BUILDING and Player.ObservatoryBonus == OBSERVATORY_ABILITY and Player.UsedObservatory == False :
                        DrawDecks = []
                        DrawDecks = Player.DetermineObservatoryAction(self.WorkerDeck.TopCard, self.BuildingDeck.TopCard, self.AristocratDeck.TopCard, self.TradingDeck.TopCard)
                        
                    # Create a list of actions and Objects [[ACTION_BUY][Card],[ACTION_BUY][Card], [ACTION_UPGRADE][Upgrade Card][Replaced Card],[ACTION_HOLD][Card],[ACTION_OBSERVATORY][WORKER_DECK]]
                    Actions = [] 
                    
                    # Add Buyable Cards to the Actions List
                    for Card in BuyableCards :
                        Actions.append([ACTION_BUY, Card, Card.CardStatus, Card.isUniqueAristocrat])
                    
                    # Add Holdable cards to Actions list considering if the player has the warehouse
                    if Player.HeldCards < (MAX_CARDS_TO_HOLD + Player.WarehouseBonus) :
                        for Card in HoldableCards :
                            Actions.append ([ACTION_HOLD, Card, Card.isUniqueAristocrat])
                            
                    # Add Upgradable Card Pairs to the Actions List
                    for CardPair in UpgradableCards :
                        if CardPair[1].CardType == ARISTOCRAT_CARD_TYPE :
                            Actions.append([ACTION_UPGRADE, CardPair, CardPair[0].CardStatus, not CardPair[1].isUniqueAristocrat])   
                        else:
                            Actions.append([ACTION_UPGRADE, CardPair, CardPair[0].CardStatus, False])
                            
                    # Add which decks the Observatory can be use to draw from to the Actions List
                    if Phase == PHASE_BUILDING and Player.ObservatoryBonus == OBSERVATORY_ABILITY and Player.UsedObservatory == False :
                        for DrawDeck in DrawDecks :
                            Actions.append([ACTION_OBSERVATORY, DrawDeck])
                    
                    # Add the Pass Action to the Actions List
                    Actions.append ([ACTION_PASS])
                    
                    # Give the Actions list to the player and get a decision back
                    PlayerAction, SelectedCard = Player.DetermineAction(Actions, self.CurrentRound, self.CurrentPhase, self.EndOfGame)
                    
                    if PlayerAction == ACTION_BUY :
                        #print  (PLAYERS[Player.ID][1] + "  has chosen to " + ACTIONS[PlayerAction][1] + " a " + SelectedCard.CardName)
                        self.ProcessBuyAction(Player, SelectedCard)
                        
                    if PlayerAction == ACTION_HOLD :
                        #print  (PLAYERS[Player.ID][1] + "  has chosen to " + ACTIONS[PlayerAction][1] + " a " + SelectedCard.CardName)
                        self.ProcessHoldAction(Player, SelectedCard)
                        
                    if PlayerAction == ACTION_UPGRADE :
                        #print  (PLAYERS[Player.ID][1] + "  has chosen to " + ACTIONS[PlayerAction][1] + " a " + SelectedCard[1].CardName + " with a " + SelectedCard[0].CardName)
                        self.ProcessUpgradeAction(Player, SelectedCard)
                        
                    if PlayerAction == ACTION_OBSERVATORY :
                        #print  (PLAYERS[Player.ID][1] + "  has chosen to use the observatory and draw from the " + ACTIONS[PlayerAction][1] + " a " + SelectedCard[1].CardName + " with a " + SelectedCard[0].CardName)
                        self.ProcessObservatoryAction(Player, SelectedCard)
                        
                    if PlayerAction == ACTION_PASS :
                        #print (PLAYERS[Player.ID][1] + " has chosen to Pass")
                        self.ProcessPassAction(Player)
                        
    
            # Reset the Passed Flag for the players
            for Player in self.Players :
                Player.hasPassed = False
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

    def ProcessBuyAction (self, Player, SelectedCard):
        
        if Player.Money >= SelectedCard.DiscountedCost :
            if SelectedCard.CardStatus == PLAYER_HELD_CARD :
                print (PLAYERS[Player.ID][1] + " is buying a held card: " + SelectedCard.CardName)
                Remove_Card_From_Board = False
            
            if SelectedCard.CardStatus == PLAYER_DRAW_CARD :
                print (PLAYERS[Player.ID][1] + " is buying a card drawn from the observatory: " + SelectedCard.CardName)
                Remove_Card_From_Board = False
            
            if SelectedCard.CardStatus == PLAYER_DELT_CARD :
                print (PLAYERS[Player.ID][1] + " is buying a card from the board: " + SelectedCard.CardName)
                Remove_Card_From_Board = True
            
            Player.BuyCard(SelectedCard)
            
            # Remove Card from Cards In Play if the Card was not Held or Drawn
            if Remove_Card_From_Board == True :
                self.CardsInPlay.remove(SelectedCard)

            Player.Money -= SelectedCard.DiscountedCost
            
            print  (PLAYERS[Player.ID][1] + " bought a " + SelectedCard.CardName + " for " + str(SelectedCard.DiscountedCost) + " money. Player Remaining Money: " + str(Player.Money))
        else :
            print  (PLAYERS[Player.ID][1] + " could not afford to buy a " + SelectedCard.CardName + ". Player Money: " + str(Player.Money) + " Card Cost: " + str(SelectedCard.DiscountedCost))

    def ProcessHoldAction (self, Player, SelectedCard):
        
        if Player.HeldCards < (MAX_CARDS_TO_HOLD + Player.WarehouseBonus) :
            
            if SelectedCard.CardStatus == PLAYER_DRAW_CARD :
                print (PLAYERS[Player.ID][1] + " is holding a card from the Observatory: " + SelectedCard.CardName)
                Remove_Card_From_Board = False
            
            if SelectedCard.CardStatus == PLAYER_DELT_CARD :
                print (PLAYERS[Player.ID][1] + " is holding a card from the board: " + SelectedCard.CardName)
                Remove_Card_From_Board = True
            
            Player.HoldCard(SelectedCard)
            
            if Remove_Card_From_Board == True :
                self.CardsInPlay.remove(SelectedCard)

            print  (PLAYERS[Player.ID][1] + " held a " + SelectedCard.CardName + " : Total held cards - " + str(Player.HeldCards))
        else :
            print  (PLAYERS[Player.ID][1] + " attempted to hold a " + SelectedCard.CardName + " : Total held cards - " + str(Player.HeldCards))

    def ProcessUpgradeAction (self, Player, SelectedCardPair):

        TradingCard = SelectedCardPair[0]
        TargetCard = SelectedCardPair[1]
        
        TradingCardCost = TradingCard.DiscountedCost - TargetCard.UpgradeValue
        
        if TradingCardCost < 1 :
            TradingCardCost = 1
        
        if Player.Money >= TradingCardCost :
            if TradingCard.CardStatus == PLAYER_HELD_CARD :
                Remove_Card_From_Board = False
                
            if TradingCard.CardStatus == PLAYER_DRAW_CARD :
                Remove_Card_From_Board = False
                
            if TradingCard.CardStatus == PLAYER_DELT_CARD :
                Remove_Card_From_Board = True
            
            Player.UpgradeCard(TradingCard, TargetCard)
            
            if Remove_Card_From_Board == True :
                self.CardsInPlay.remove(TradingCard)

            Player.Money -= TradingCardCost
            
            print  (PLAYERS[Player.ID][1] + " upgraded a " + TargetCard.CardName + " with a " + TradingCard.CardName + " for " + str(TradingCardCost) + " money. Player Remaining Money: " + str(Player.Money))
        else :
            print  (PLAYERS[Player.ID][1] + " could not afford to upgrade a " + TargetCard.CardName + " with a " + TradingCard.CardName + ". Player Money: " + str(Player.Money) + " Upgrade Cost: " + str(TradingCardCost))
    
    def ProcessObservatoryAction (self, Player, SelectedCardType):  
        
        try : 
            # Get Card from Selected Deck and advance the top card
            if SelectedCardType == WORKER_CARD_TYPE :
                SelectedCard = self.WorkerDeck.Cards[self.WorkerDeck.TopCard]
                self.WorkerDeck.TopCard += 1
            if SelectedCardType == BUILDING_CARD_TYPE :
                SelectedCard = self.BuildingDeck.Cards[self.BuildingDeck.TopCard]
                self.BuildingDeck.TopCard += 1
            if SelectedCardType == ARISTOCRAT_CARD_TYPE :
                SelectedCard = self.AristocratDeck.Cards[self.AristocratDeck.TopCard]
                self.AristocratDeck.TopCard += 1
            if SelectedCardType == TRADING_CARD_TYPE :
                SelectedCard = self.TradingDeck.Cards[self.TradingDeck.TopCard]
                self.TradingDeck.TopCard += 1    
            
            print  (PLAYERS[Player.ID][1] + " used the Observatory to draw from a deck : Card Selected -  " + SelectedCard.CardName) 
                
            Actions = []   
    
            # Find the discounted cost of the card
            Player.DetermineCardCosts (list([SelectedCard]))
            
            # Determine if the Drawn card is a unique Aristocrat
            Player.DetermineUniqueAristocrats(list([SelectedCard]))
            
            # if the player has the money to buy the card add a Buy Action to the actions list
            if Player.Money >= SelectedCard.DiscountedCost and SelectedCard.isUpgradable == IS_UPGRADABLE :
                print  (PLAYERS[Player.ID][1] + " has the option to buy the card : Card Selected -  " + SelectedCard.CardName)
                Actions.append([ACTION_BUY, SelectedCard, SelectedCard.CardStatus, SelectedCard.isUniqueAristocrat])
                
            # If the player do not have the money to buy the card add a Hold Action to the actions list
            if Player.Money < SelectedCard.DiscountedCost and SelectedCard.isUpgradable == IS_UPGRADABLE :
                if Player.HeldCards < (MAX_CARDS_TO_HOLD + Player.WarehouseBonus) :
                    print  (PLAYERS[Player.ID][1] + " has the option to hold the card : Card Selected -  " + SelectedCard.CardName)
                    Actions.append([ACTION_HOLD, SelectedCard, SelectedCard.isUniqueAristocrat])
                    
            # Add Actions if the card was a Trading Card
            
            if SelectedCardType == TRADING_CARD_TYPE :
                for TargetCard in Player.Hand :
                    if (TargetCard.CardClass == SelectedCard.CardClass and TargetCard.isUpgradable == IS_UPGRADABLE and TargetCard.CardStatus == PLAYER_ACTIVE_CARD) or (SelectedCard.CardType == WORKER_CARD_TYPE and TargetCard.CardClass == CLASS_ALL and TargetCard.isUpgradable == IS_UPGRADABLE and TargetCard.CardStatus == PLAYER_ACTIVE_CARD) :
                        # Determine the Upgrade cost and check if the player can afford it
                        TradingCardCost = SelectedCard.DiscountedCost - TargetCard.UpgradeValue
                        if TradingCardCost < 1 :
                            TradingCardCost = 1
                            
                        if TradingCardCost <= Player.Money :
                            print  (PLAYERS[Player.ID][1] + " has the option to upgrade the card : Card Selected -  " + SelectedCard.CardName + " : Target Card - " + TargetCard.CardName)
                            if TargetCard.CardType == ARISTOCRAT_CARD_TYPE :
                                Actions.append([ACTION_UPGRADE,list([SelectedCard, TargetCard]), SelectedCard.CardStatus, not TargetCard.isUniqueAristocrat])
                            else :
                                Actions.append([ACTION_UPGRADE,list([SelectedCard, TargetCard]), SelectedCard.CardStatus, False])
    
            print  (PLAYERS[Player.ID][1] + " has the option to discard (Pass) the card : Card Selected -  " + SelectedCard.CardName)
            Actions.append([ACTION_PASS])
            
    
            # Send the Action List to the Processor to get a decision
            PlayerAction, SelectedCard = Player.DetermineAction(Actions, self.CurrentRound, self.CurrentPhase, self.EndOfGame)   
                        
            
            if PlayerAction == ACTION_BUY :
                print  (PLAYERS[Player.ID][1] + "  has chosen to " + ACTIONS[PlayerAction][1] + " a " + SelectedCard.CardName)
                SelectedCard.CardStatus = PLAYER_DRAW_CARD
                self.ProcessBuyAction(Player, SelectedCard)
                 
            if PlayerAction == ACTION_HOLD :
                print  (PLAYERS[Player.ID][1] + "  has chosen to " + ACTIONS[PlayerAction][1] + " a " + SelectedCard.CardName)
                SelectedCard.CardStatus = PLAYER_DRAW_CARD
                self.ProcessHoldAction(Player, SelectedCard)
                 
            if PlayerAction == ACTION_UPGRADE :
                print  (PLAYERS[Player.ID][1] + "  has chosen to " + ACTIONS[PlayerAction][1] + " a " + SelectedCard[1].CardName + " with a " + SelectedCard[0].CardName)
                SelectedCard[0].CardStatus = PLAYER_DRAW_CARD
                self.ProcessUpgradeAction(Player, SelectedCard)
                 
            if PlayerAction == ACTION_PASS :
                print (PLAYERS[Player.ID][1] + " has chosen to Pass")
                self.ProcessPassAction(Player)
                
            Player.Score -= 1
            Player.UsedObservatory = True
            print (PLAYERS[Player.ID][1] + " is losing a point for using the Observatory. Will get it back in the scoring round. New Score: " + str(Player.Score))
            
            return
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
        
    def ProcessPassAction (self, Player):
        Player.Pass()
        print (PLAYERS[Player.ID][1] + " has passed")
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    # End of Phase and Pub Scoring Functions
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    def ProcessPhaseScoring (self, Phase):
        print("Scoring " + PHASES[Phase][1])
        #Process Scores for normal Cards
        for Player in self.Players :
            for Card in Player.Hand:
                if (Card.CardType == Phase and Card.CardStatus == PLAYER_ACTIVE_CARD):
                    Player.Money += Card.MoneyEarned
                    Player.Score += Card.VPEarned
                    print(PLAYERS[Player.ID][1] + " earned " + str(Card.MoneyEarned) + " money and scored " + str(Card.VPEarned) + " VP using a " + Card.CardName + ". New Money: " + str(Player.Money) + " New Score: " + str(Player.Score))
        
            # Process Scores for Special Cards
            Workers = sum ((Card.CardType == WORKER_CARD_TYPE and Card.CardStatus == PLAYER_ACTIVE_CARD) for Card in Player.Hand)
            Aristocrats = sum ((Card.CardType == ARISTOCRAT_CARD_TYPE and Card.CardStatus == PLAYER_ACTIVE_CARD) for Card in Player.Hand)
            for Card in Player.Hand :
                # Tax Man
                if (Card.CardType == Phase and Card.CardStatus == PLAYER_ACTIVE_CARD and Card.CardID == TAX_MAN_ID):
                    Player.Money += Workers
                    print(PLAYERS[Player.ID][1] + " earned " + str(Workers) + " money and scored " + str(Card.VPEarned) + " VP using a " + Card.CardName + ". New Money: " + str(Player.Money) + " New Score: " + str(Player.Score))
                # Mariinskij Theater
                if (Card.CardType == Phase and Card.CardStatus == PLAYER_ACTIVE_CARD and Card.CardID == MARIINSKIJ_THEATER_ID):
                    Player.Money += Aristocrats       
                    print(PLAYERS[Player.ID][1] + " earned " + str(Aristocrats) + " money and scored " + str(Card.VPEarned) + " VP using a " + Card.CardName + ". New Money: " + str(Player.Money) + " New Score: " + str(Player.Score))
        
        # Process Pub point Buying and reset the Used Observatory attribute
        if Phase == PHASE_BUILDING :
            self.ProcessPubScoring()
            
            for Player in self.Players :
                Player.UsedObservatory = False
            
            
    def ProcessPubScoring (self):
        
        #Check to see if anyone has the Pub
        for Player in self.Players :
            OldScore = 0
            OldMoney = 0
            
            if Player.PubBonus == PUB_ABILITY :
                Actions = []
                OldScore = Player.Score
                OldMoney = Player.Money
                for x in range (0, 6) :
                    if Player.Money >= x * 2 :
                        Actions.append ([ACTION_PUB, x])
                    
                # Give the Actions list to the player and get a decision back
                PlayerAction, Points = Player.DetermineAction(Actions, self.CurrentRound, self.CurrentPhase, self.EndOfGame)
                
                if PlayerAction == ACTION_PUB :
                    Player.Money -= (Points * 2)
                    Player.Score += Points 
                    print (PLAYERS[Player.ID][1] + " used the Pub and bought " + str(Points) + " points : Old Score - " + str(OldScore) + " New Score - " + str(Player.Score) + " : Old Money - " + str(OldMoney) + " : New Money - " + str(Player.Money))
        return
    
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    # End of Game Scoring Functions
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    def ProcessEndofGameActions (self):
        self.ProcessAristocratScoring()
        self.ProcessPointBuying()
        self.ProcessPointReductions()
    
    def ProcessAristocratScoring (self):
        
        for Player in self.Players :
            Player.Score += ARISTOCRAT_SCORING [Player.UniqueAristrocrats]
            print(PLAYERS[Player.ID][1] + " has " + str(Player.UniqueAristrocrats) + " unique aristocrats and scores " + str(ARISTOCRAT_SCORING [Player.UniqueAristrocrats]) + " Victory Points : New VP - " + str(Player.Score))
        return
    
    def ProcessPointBuying (self):
        
        PointsBought = 0
        
        for Player in self.Players :
            print(PLAYERS[Player.ID][1] + " is cashing out his money for points. Current Money - " + str(Player.Money) + " : Current VP - " + str(Player.Score))
            while Player.Money >= MONEY_PER_VP :
                PointsBought += 1
                Player.Score += 1
                Player.Money -= MONEY_PER_VP
            print(PLAYERS[Player.ID][1] + " bought " + str(PointsBought) + " victory points : New Score - " + str(Player.Score))
        
        return
    
    def ProcessPointReductions (self):
        
        for Player in self.Players :
            Player.Score += Player.HeldCards * PENALTY_HELD_CARD
            print(PLAYERS[Player.ID][1] + " held " + str(Player.HeldCards) + " cards at the end of the game : Penalty " + str(Player.HeldCards * PENALTY_HELD_CARD) + " : Final Score - " + str(Player.Score))
        
        return
    

    def ResetPlayersBrains (self, Episode_Average_Scores) :
        
        High_Score = numpy.argmax(Episode_Average_Scores, axis=0)
        High_Player_ID = Episode_Average_Scores[High_Score[2]][0]
        
        for Player in self.Players :
            if Player.ID == High_Player_ID :
                High_Player = Player 
        
        for Player in self.Players :
            Player.Brain.ReplaceBrain(High_Player.Brain.Action_Dataframe)
            Player.Brain.SaveBrain()

    
    
    def SavePlayersBrains (self):
        for Player in self.Players :
            Player.SaveBrain()
        
    def UpdateAvgScores (self, Episode_Scores):
        avg_episode_scores = []
        
        for avg_score in Episode_Scores :
            for Player in self.Players :
                if avg_score[0] == Player.ID :
                    num_games = avg_score[1]
                    new_num_games = num_games + 1
                    player_avg_score = avg_score[2]
                    new_player_avg_score = ((player_avg_score * num_games) + Player.Score)/(new_num_games)
                    avg_episode_scores.append([Player.ID, new_num_games, new_player_avg_score])
                    Player.AverageScore = new_player_avg_score
        
        return avg_episode_scores
        

                
                