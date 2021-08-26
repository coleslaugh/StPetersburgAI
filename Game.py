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
        
        WorkerDeck = Deck (WORKER_CARDS, WORKER_CARD_TYPE)
        WorkerDeck.GetCardNames()

            
