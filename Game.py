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
                        BOARD_UPPER_ROW, BOARD_LOWER_ROW, PLAYER_ACTIVE_CARD, PLAYERS, PHASES, MARKERS,
                        TRADING_CARDS, TRADING_CARD_TYPE, TAX_MAN_ID, MARIINSKIJ_THEATER_ID,
    PHASE_WORKER)
from Player import Player



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
            
        print ("Markers are Assigned: " +   PLAYERS[0][1] + "-" + MARKERS[self.Players[0].Marker][1] + " "  + 
                                            PLAYERS[1][1] + "-" + MARKERS[self.Players[1].Marker][1] + " "  + 
                                            PLAYERS[2][1] + "-" + MARKERS[self.Players[2].Marker][1] + " "  + 
                                            PLAYERS[3][1] + "-" + MARKERS[self.Players[3].Marker][1])

        #self.Players.sort(key=lambda s: s.Marker, reverse=False)
        
    def DealCards (self, GamePhase):
        print ("Starting to Deal Cards for the " + PHASES[GamePhase][1] + " - Worker Deck Top Card:" + str(self.WorkerDeck.TopCard) + " Building Deck Top Card: " + str(self.BuildingDeck.TopCard) + " Aristocrat Deck Top Card: " + str(self.AristocratDeck.TopCard) + " Trading Deck Top Card: " + str(self.TradingDeck.TopCard))
        print ("Cards to deal: " + str(MAX_CARDS_ON_BOARD - len(self.CardsInPlay)))
        CardsDelt = ""
        if GamePhase == WORKER_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                if self.WorkerDeck.TopCard < len (self.WorkerDeck.Cards) :
                    self.CardsInPlay.append(self.WorkerDeck.Cards[self.WorkerDeck.TopCard])
                    CardsDelt = CardsDelt + ", " + self.WorkerDeck.Cards[self.WorkerDeck.TopCard].CardName 
                    self.WorkerDeck.TopCard += 1
                if self.WorkerDeck.TopCard >= len (self.WorkerDeck.Cards) :
                    self.EndOfGame = True
                    print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt + " Worker Deck Empty. Game will Terminate at the end of the phase")
                    return
        
        if GamePhase == BUILDING_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                if self.BuildingDeck.TopCard < len (self.BuildingDeck.Cards) :
                    self.CardsInPlay.append(self.BuildingDeck.Cards[self.BuildingDeck.TopCard])
                    CardsDelt = CardsDelt + ", " + self.BuildingDeck.Cards[self.BuildingDeck.TopCard].CardName
                    self.BuildingDeck.TopCard += 1
                if self.BuildingDeck.TopCard >= len (self.BuildingDeck.Cards) :
                    print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt + " Building Deck Empty. Game will Terminate at the end of the phase")
                    self.EndOfGame = True
                    return            
        
        if GamePhase == ARISTOCRAT_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                if self.AristocratDeck.TopCard < len (self.AristocratDeck.Cards) :
                    self.CardsInPlay.append(self.AristocratDeck.Cards[self.AristocratDeck.TopCard])
                    CardsDelt = CardsDelt + ", " + self.AristocratDeck.Cards[self.AristocratDeck.TopCard].CardName
                    self.AristocratDeck.TopCard += 1
                if self.AristocratDeck.TopCard >= len (self.AristocratDeck.Cards) :
                    self.EndOfGame = True
                    print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt + " Aristocrat Deck Empty. Game will Terminate at the end of the phase")
                    return          
        if GamePhase == TRADING_CARD_TYPE :
            while len (self.CardsInPlay) < MAX_CARDS_ON_BOARD :
                if self.TradingDeck.TopCard < len (self.TradingDeck.Cards) :
                    self.CardsInPlay.append(self.TradingDeck.Cards[self.TradingDeck.TopCard])
                    CardsDelt = CardsDelt + ", " + self.TradingDeck.Cards[self.TradingDeck.TopCard].CardName
                    self.TradingDeck.TopCard += 1
                if self.TradingDeck.TopCard >= len (self.TradingDeck.Cards) :
                    self.EndOfGame = True
                    print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt + " Aristocrat Deck Empty. Game will Terminate at the end of the phase")
                    return 
        print ("Cards delt for the " + PHASES[GamePhase][1] +  CardsDelt)

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
    
    def ProcessPhaseActions (self, Phase):
        
        # Assign order of play for current phase based on who has the marker.
        
        CurrentPhasePlayers = self.AssignCurrentPhaseOrder(Phase)
        
        
        for Player in CurrentPhasePlayers :
            
            # CANNOT ASSUME AT THIS POINT THAT INDEX IN CurrentPhasePlayers is the same as Player ID.
            
            # Determine Card Costs here and pass it to Determine Action
            
            # Determine which cards in play the current player can Buy a card with the money he has
            
            # Determine which cards the Current player can upgrade a card
            
            # Determine if the current player can hold a card (i.e Does he have open slots) and which cards can be held
            
            # Determine if the current player has the Observatory and which decks can be drawn from. Must check if it's been used this round
               
            # Build a list of allowed actions BUY, HOLD, PASS, OBVS, UPGRADE to send to the DetermineAction Function
            
            # Create a multi dimensional list of actions and Objects [[ACTION_BUY][Card],[ACTION_BUY][Card], [ACTION_UPGRADE][Upgrade Card][Replaced Card]
            
            PlayerAction, SelectedCard = Player.DetermineAction(self.CardsInPlay)
            
            if PlayerAction == ACTION_BUY :
                self.ProcessBuyAction(Player, SelectedCard)
                
            if PlayerAction == ACTION_HOLD :
                Player.HoldCard(SelectedCard)
                self.CardsInPlay.remove(SelectedCard)
                 
            if PlayerAction == ACTION_PASS :
                Player.Pass()
    
    def ProcessBuyAction (self, Player, SelectedCard):
        if Player.Money >= SelectedCard.CardCost :
            Player.BuyCard(SelectedCard)
            self.CardsInPlay.remove(SelectedCard)
            Player.Money -= SelectedCard.CardCost
            print  (PLAYERS[Player.ID][1] + " bought a " + SelectedCard.CardName + " for " + str(SelectedCard.CardCost) + " money. Player Remaining Money: " + str(Player.Money))
        else :
            print  (PLAYERS[Player.ID][1] + " could not afford to buy a " + SelectedCard.CardName + ". Player Money: " + str(Player.Money) + " Card Cost: " + str(SelectedCard.CardCost))
    
    
    def ProcessPhaseScoring (self, Phase):
        #print("Scoring " + PHASES[Phase][1])
        #Process Scores for normal Cards
        for Player in self.Players :
            for Card in Player.Hand:
                if (Card.CardType == Phase and Card.CardStatus == PLAYER_ACTIVE_CARD):
                    Player.Money += Card.MoneyEarned
                    Player.Score += Card.VPEarned
                    #print(PLAYERS[Player.ID][1] + " earned " + str(Card.MoneyEarned) + " money and scored " + str(Card.VPEarned) + " VP using a " + Card.CardName + ". New Money: " + str(Player.Money) + " New Score: " + str(Player.Score))
        
            # Process Scores for Special Cards
            Workers = sum (Card.CardType == WORKER_CARD_TYPE for Card in Player.Hand)
            Aristocrats = sum (Card.CardType == ARISTOCRAT_CARD_TYPE for Card in Player.Hand)
            for Card in Player.Hand :
                # Tax Man
                if (Card.CardType == Phase and Card.CardStatus == PLAYER_ACTIVE_CARD and Card.CardID == TAX_MAN_ID):
                    Player.Money += Workers
                    #print(PLAYERS[Player.ID][1] + " earned " + str(Card.MoneyEarned) + " money and scored " + str(Card.VPEarned) + " VP using a " + Card.CardName + ". New Money: " + str(Player.Money) + " New Score: " + str(Player.Score))
                # Mariinskij Theater
                if (Card.CardType == Phase and Card.CardStatus == PLAYER_ACTIVE_CARD and Card.CardID == MARIINSKIJ_THEATER_ID):
                    Player.Money += Aristocrats       
                    #print(PLAYERS[Player.ID][1] + " earned " + str(Card.MoneyEarned) + " money and scored " + str(Card.VPEarned) + " VP using a " + Card.CardName + ". New Money: " + str(Player.Money) + " New Score: " + str(Player.Score))
            
    
    def RotateCards (self):
        for c in self.CardsInPlay :
            if c.Row == BOARD_UPPER_ROW :
                c.Row = BOARD_LOWER_ROW
            else :
                self.CardsInPlay.remove(c)
    
    def RotateMarkers (self):
        TempMarker = self.Players[PLAYER_4].Marker 
        self.Players[PLAYER_4].Marker = self.Players[PLAYER_3].Marker
        self.Players[PLAYER_3].Marker = self.Players[PLAYER_2].Marker
        self.Players[PLAYER_2].Marker = self.Players[PLAYER_1].Marker
        self.Players[PLAYER_1].Marker = TempMarker
        print ("Markers are Rotated: " +    PLAYERS[PLAYER_1][1] + "-" + MARKERS[self.Players[PLAYER_1].Marker][1] + " "  + 
                                            PLAYERS[PLAYER_2][1] + "-" + MARKERS[self.Players[PLAYER_2].Marker][1] + " "  + 
                                            PLAYERS[PLAYER_3][1] + "-" + MARKERS[self.Players[PLAYER_3].Marker][1] + " "  + 
                                            PLAYERS[PLAYER_4][1] + "-" + MARKERS[self.Players[PLAYER_4].Marker][1])
        return 
            
         
    
    
        

                
                