'''
Created on Aug 25, 2021

@author: mikes
'''
from Contents import PLAYER_ACTIVE_CARD, PLAYER_HELD_CARD, ACTION_BUY, ACTION_PASS, PLAYERS
from random import randint

class Player(object):
   
    
    def __init__(self, ID, Color, Money, Score, Marker):
        self.ID = ID
        self.Color = Color
        self.Money = Money
        self.Score = Score
        self.Marker = Marker
        self.Hand = []
        
    def BuyCard(self, card_to_buy):
        card_to_buy.CardStatus = PLAYER_ACTIVE_CARD
        self.Hand.append(card_to_buy)
        #print(PLAYERS[self.ID][1] + " bought a " + card_to_buy.CardName)
    
    def HoldCard(self, card_to_hold):
        card_to_hold.CardStatus = PLAYER_HELD_CARD
        self.Hand.append(card_to_hold)
    
    def Pass (self):
        return 
     
    def UseCardAbility (self, card_with_ability):
        return 
    
    def DetermineAction(self, cards_in_play):
        
        #print(PLAYERS[self.ID][1] + " decided to by " + cards_in_play[selectedCard].CardName)
        if len (cards_in_play) > 0 :
            selectedCard = randint(0, len(cards_in_play)-1)
            return ACTION_BUY, cards_in_play[selectedCard]
        else :
            return ACTION_PASS, None