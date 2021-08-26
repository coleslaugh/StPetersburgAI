'''
Created on Aug 25, 2021

@author: mikes
'''
from Deck import *
from Contents import *
from Card import *
from Player import *
from Board import *
from random import random



class Game(object):

    EndOfGame = False
    
    def __init__(self, GameID):
        self.GameID = GameID
        self.WorkerDeck = []
        self.BuildingDeck = []
        self.AristocratDeck = []
        self.CardsInPlay = []
        self.Players = []
        self.NumPlayers = PLAYERS_PER_GAME
        #Board = Board ()
                
    def GameSetup (self):
        self.CreateDecks()
        self.CreatePlayers()
        self.AssignMarkers()
        
    def CreatePlayers (self):   
        self.Players.append(Player (PLAYER_GREEN, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player (PLAYER_BLUE, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player (PLAYER_YELLOW, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player (PLAYER_RED, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        
    def CreateDecks (self):
        self.WorkerDeck = Deck (WORKER_CARDS, WORKER_CARD_TYPE)
        self.BuildingDeck = Deck (BUILDING_CARDS, BUILDING_CARD_TYPE)
        self.AristocratDeck = Deck (ARISTOCRAT_CARDS, ARISTOCRAT_CARD_TYPE)
        
        self.BuildingDeck.Shuffle()
        self.WorkerDeck.Shuffle()
        self.AristocratDeck.Shuffle()
        
    def AssignMarkers (self):
        Markers = [[PLAYER_MARKER_WORKER, random ()],[PLAYER_MARKER_BUIDLING, random()],[PLAYER_MARKER_ARISTOCRAT, random()],[PLAYER_MARKER_TRADING, random()]]
        Markers.sort(key=lambda x: x[1])
        
        for x in range(PLAYERS_PER_GAME):
            self.Players[x].Marker = Markers[x][0]

        self.Players.sort(key=lambda s: s.Marker, reverse=False)
        
    def DealCards (self, GamePhase):

        if GamePhase == WORKER_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                #print ("Dealing Worker Cards")
                self.CardsInPlay.append(self.WorkerDeck.Cards[self.WorkerDeck.TopCard])
                self.WorkerDeck.TopCard += 1
        
        if GamePhase == BUILDING_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                #print ("Dealing Building Cards")
                self.CardsInPlay.append(self.BuildingDeck.Cards[self.BuildingDeck.TopCard])
                self.BuildingDeck.TopCard += 1                
        
        if GamePhase == ARISTOCRAT_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                #print ("Dealing Aristocrat Cards")
                self.CardsInPlay.append(self.AristocratDeck.Cards[self.AristocratDeck.TopCard])
                self.AristocratDeck.TopCard += 1   
                
        return              

    def ProcessPhaseActions (self, Phase):
        for x in range(len(self.Players)) :
            PlayerAction = []  # [Action, Card]
            PlayerAction = self.Players[x].DetermineAction (self.CardsInPlay)
        
        return
    
    def ProcessPhaseScoring (self, Phase):
        return
    
    def RotateCards (self):
        
        return 
    
    def RotatePlayers (self):
        return 
    
    
        

                
                