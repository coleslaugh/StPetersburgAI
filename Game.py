'''
Created on Aug 25, 2021

@author: mikes
'''
from Deck import *
from Contents import *
from Card import *


class Game(object):
    
    GameID = 0
    WorkerDeck = []
    BuildingDeck = []
    AristocratDeck = []

    def __init__(self, GameID):
        self.GameID = GameID
        
        
                
    def GameSetup (self):
        
        self.WorkerDeck = Deck (WORKER_CARDS, WORKER_CARD_TYPE)
        self.WorkerDeck.Shuffle()
        for x in range (len(self.WorkerDeck.Cards)) :
            print (self.WorkerDeck.Cards[x].CardOrder, self.WorkerDeck.Cards[x].CardName)
            
            
        #self.BuildingDeck = Deck (BUILDING_CARDS, BUILDING_CARD_TYPE)
        #self.AristocratDeck = Deck (ARISTOCRAT_CARDS, ARISTOCRAT_CARD_TYPE)
        
        

            
