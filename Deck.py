#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Deck Class - Contains Cards
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------

from Card import Card

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Deck Class
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    
class Deck(object):
    
    def __init__(self, CardDefs, DeckType):
        x = 0
        i = 0
        self.Cards = []
        self.DeckType = DeckType
        self.TopCard = 0

        for x in CardDefs :
            i=0
            while i < x[1] :
                self.Cards.append(Card(x[0]))
                i += 1

    def Shuffle (self):
        self.Cards.sort(key=lambda s: s.CardOrder, reverse=False)
        
    def GetCardNames (self):
        for x in self.Cards :
            print (x.CardName)