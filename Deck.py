'''
Created on Aug 25, 2021

@author: mikes
'''
from Card import *



class Deck(object):
    
    DeckType = 0
    TopCard = 0
    Cards = []


    def __init__(self, CardDefs, DeckType):
        '''
        Constructor
        '''
        x = 0
        i = 0
        self.DeckType = DeckType
        self.TopCard = 0

        for x in CardDefs :
            i=0
            while i < x[1] :
                self.Cards.append(Card(x[0]))
                i += 1
                


                
    def GetCardNames (self):
        for x in self.Cards :
            print (x.CardName)