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
        
        
    def BuyCard(self, CardToBuy):
        return 
    
    def HoldCard(self, CardToHold):
        return 
    
    def Pass (self):
        return 
    
    def UseCardAbility (self, CardWithAbility):
        return 
    
    def DetermineAction(self, CardsInPlay):
        return 