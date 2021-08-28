'''
Created on Aug 25, 2021

@author: mikes
'''

class Player(object):
   
    
    def __init__(self, Color, Money, Score, Marker):
        self.Color = Color
        self.Money = Money
        self.Score = Score
        self.Marker = Marker
        self.Hand = []
        
    def BuyCard(self, card_to_buy):
        return 
    
    def HoldCard(self, card_to_hold):
        return 
    
    def Pass (self):
        return 
    
    def UseCardAbility (self, card_with_ability):
        return 
    
    def DetermineAction(self, cards_in_play):
        return 