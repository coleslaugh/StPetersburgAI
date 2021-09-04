'''
Created on Aug 25, 2021

@author: mikes
'''
from random import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from Deck import Deck
from Contents import (  PLAYER_1, PLAYER_2, PLAYER_3, PLAYER_4, 
                        PLAYER_BLUE, PLAYER_GREEN, PLAYER_YELLOW, PLAYER_RED, 
                        PLAYERS_PER_GAME, WORKER_CARDS, BUILDING_CARDS, ARISTOCRAT_CARDS, 
                        WORKER_CARD_TYPE, BUILDING_CARD_TYPE, ARISTOCRAT_CARD_TYPE, 
                        PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, PLAYER_MARKER_ARISTOCRAT, 
                        PLAYER_MARKER_TRADING, PLAYER_MARKER_BUIDLING, 
                        PLAYER_MARKER_WORKER, MAX_CARDS_ON_BOARD,
                        ACTION_BUY, ACTION_HOLD, ACTION_PASS,
                        BOARD_UPPER_ROW, BOARD_LOWER_ROW)
from Player import Player

class Game(object):

    def __init__(self, GameID):
        self.GameID = GameID
        self.WorkerDeck = []
        self.BuildingDeck = []
        self.AristocratDeck = []
        self.CardsInPlay = []
        self.Players = []
        self.EndOfGame = False
        self.NumPlayers = PLAYERS_PER_GAME
                
    def GameSetup (self):
        self.CreateDecks()
        self.CreatePlayers()
        self.AssignMarkers()

        
    def CreatePlayers (self):   
        self.Players.append(Player(PLAYER_1, PLAYER_GREEN, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player(PLAYER_2, PLAYER_BLUE, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player(PLAYER_3, PLAYER_YELLOW, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        self.Players.append(Player(PLAYER_4, PLAYER_RED, PLAYER_STARTING_MONEY, PLAYER_STARTING_SCORE, 0))
        
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
                self.CardsInPlay.append(self.WorkerDeck.Cards[self.WorkerDeck.TopCard])
                self.WorkerDeck.TopCard += 1
        
        if GamePhase == BUILDING_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                self.CardsInPlay.append(self.BuildingDeck.Cards[self.BuildingDeck.TopCard])
                self.BuildingDeck.TopCard += 1                
        
        if GamePhase == ARISTOCRAT_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                self.CardsInPlay.append(self.AristocratDeck.Cards[self.AristocratDeck.TopCard])
                self.AristocratDeck.TopCard += 1   
        return              

    def ProcessPhaseActions (self, Phase):
        for x in range(len(self.Players)) :
            PlayerAction, SelectedCard = self.Players[x].DetermineAction(self.CardsInPlay)
            if PlayerAction == ACTION_BUY :
                self.Players[x].BuyCard(SelectedCard)
                self.CardsInPlay.remove(SelectedCard)
                
            if PlayerAction == ACTION_HOLD :
                self.Players[x].HoldCard(SelectedCard)
                self.CardsInPlay.remove(SelectedCard)
                
            if PlayerAction == ACTION_PASS :
                self.Players[x].Pass()
            #PlayerAction = []  # [Action, Card]
            #PlayerAction = self.Players[x].DetermineAction (self.CardsInPlay)
        

    
    def ProcessPhaseScoring (self, Phase):
        return
    
    def RotateCards (self):
        for c in self.CardsInPlay :
            c.Row = BOARD_LOWER_ROW
    
    def RotatePlayers (self):
        return 
    
    
        

                
                