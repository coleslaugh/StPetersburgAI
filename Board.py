'''
Created on Aug 25, 2021

@author: mikes
'''


import sys
import time

#from PyQt5.Qt import QMainWindow, QApplication
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

from Game import Game
from Contents import *
from PyQt5.Qt import QListWidgetItem, QPixmap
from MainWindow import Ui_MainWindow


class Board(Ui_MainWindow):
    def SetupBoard (self):

        self.CardSlots = []
        self.CardSlots.append([self.Card_Upper_1, self.Card_Lower_1])
        self.CardSlots.append([self.Card_Upper_2, self.Card_Lower_2])
        self.CardSlots.append([self.Card_Upper_3, self.Card_Lower_3])
        self.CardSlots.append([self.Card_Upper_4, self.Card_Lower_4])
        self.CardSlots.append([self.Card_Upper_5, self.Card_Lower_5])
        self.CardSlots.append([self.Card_Upper_6, self.Card_Lower_6])
        self.CardSlots.append([self.Card_Upper_7, self.Card_Lower_7])
        self.CardSlots.append([self.Card_Upper_8, self.Card_Lower_8])
        
        self.PlayerCardLists = []
        self.PlayerCardLists.append(self.listCards_Player1)
        self.PlayerCardLists.append(self.listCards_Player2)
        self.PlayerCardLists.append(self.listCards_Player3)
        self.PlayerCardLists.append(self.listCards_Player4)

        for x in range(len(self.CardSlots)) :
            self.CardSlots[x][0].setScaledContents(True)
            self.CardSlots[x][1].setScaledContents(True)

       
    def StartButtonClick (self):
        self.ClearBoard()
        print("Starting Game")
        self.listStatus.addItem(QListWidgetItem("Creating Game"))
        self.New_Game = Game (1)
        self.listStatus.addItem(QListWidgetItem("Setting Up Game"))
        self.New_Game.GameSetup()
        self.listStatus.addItem(QListWidgetItem("Game Setup Complete"))
        self.AddDeckstoGameBoard()
        self.AddPlayerstoGameBoard()
        self.RefreshMoney()
        self.RefreshVictoryPoints()
        self.RunGame()
        
    def ClearBoard (self):
        self.listStatus.clear()
        self.listDeck_Worker.clear()
        self.listDeck_Building.clear ()
        self.listDeck_Aristocrat.clear ()
        self.listDeck_Trading.clear()
        self.listCards_Player1.clear()
        self.listCards_Player2.clear()
        self.listCards_Player3.clear()
        self.listCards_Player4.clear()
        
    def AddDeckstoGameBoard (self):
        
        self.listStatus.addItem(QListWidgetItem("Adding Worker Deck to Board"))
        for x in self.New_Game.WorkerDeck.Cards :
            self.listDeck_Worker.addItem(QListWidgetItem(x.CardName))
        
        self.listStatus.addItem(QListWidgetItem("Adding Building Deck to Board"))
        for x in self.New_Game.BuildingDeck.Cards :
            self.listDeck_Building.addItem(QListWidgetItem(x.CardName))
            
        self.listStatus.addItem(QListWidgetItem("Adding Aristocrat Deck to Board"))
        for x in self.New_Game.AristocratDeck.Cards :
            self.listDeck_Aristocrat.addItem(QListWidgetItem(x.CardName))
            
    def AddPlayerHandstoGameBoard(self):
        
        #Clear the Player List Widgets before adding the cards again
        for x in range(len(self.PlayerCardLists)) :
            self.PlayerCardLists[x].clear()
        
        for p in self.New_Game.Players :
            if p.ID == PLAYER_1 :
                for x in p.Hand :
                    self.listCards_Player1.addItem(QListWidgetItem(x.CardName))
            if p.ID == PLAYER_2 :
                for x in p.Hand :
                    self.listCards_Player2.addItem(QListWidgetItem(x.CardName))
            if p.ID == PLAYER_3 :
                for x in p.Hand :
                    self.listCards_Player3.addItem(QListWidgetItem(x.CardName))
            if p.ID == PLAYER_4 :
                for x in p.Hand :
                    self.listCards_Player4.addItem(QListWidgetItem(x.CardName))             

    def AddPlayerstoGameBoard (self):
        self.lblColor_Player1.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[0].Color][1])
        self.lblColor_Player2.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[1].Color][1])
        self.lblColor_Player3.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[2].Color][1])
        self.lblColor_Player4.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[3].Color][1])
    
        self.lblPhaseLeader_Player1.setText("Phase Leader: " + PHASES [self.New_Game.Players[0].Marker][1])
        self.lblPhaseLeader_Player2.setText("Phase Leader: " + PHASES [self.New_Game.Players[1].Marker][1])
        self.lblPhaseLeader_Player3.setText("Phase Leader: " + PHASES [self.New_Game.Players[2].Marker][1])
        self.lblPhaseLeader_Player4.setText("Phase Leader: " + PHASES [self.New_Game.Players[3].Marker][1])
     
    def AddCardsInPlaytoGameBoard(self):

        for x in range(len(self.CardSlots)) :
            self.CardSlots[x][0].clear()
            self.CardSlots[x][1].clear()
            
        for x in range (len(self.New_Game.CardsInPlay)) :
            self.CardSlots[x][self.New_Game.CardsInPlay[x].Row].setPixmap(QPixmap(":/Cards/" + str(self.New_Game.CardsInPlay[x].CardID) + ".png"))
            
               
    def RefreshMoney (self):
        self.lblMoney_Player1.setText("Money: " + str(self.New_Game.Players[0].Money))
        self.lblMoney_Player2.setText("Money: " + str(self.New_Game.Players[1].Money))
        self.lblMoney_Player3.setText("Money: " + str(self.New_Game.Players[2].Money))
        self.lblMoney_Player4.setText("Money: " + str(self.New_Game.Players[3].Money))
    
    def RefreshVictoryPoints (self):
        self.lblVP_Player1.setText("Victory Points: " + str(self.New_Game.Players[0].Score))
        self.lblVP_Player2.setText("Victory Points: " + str(self.New_Game.Players[1].Score))
        self.lblVP_Player3.setText("Victory Points: " + str(self.New_Game.Players[2].Score))
        self.lblVP_Player4.setText("Victory Points: " + str(self.New_Game.Players[3].Score))
    
    def RunGame (self):
        while not self.New_Game.EndOfGame :
  
            self.New_Game.DealCards(WORKER_CARD_TYPE)
            self.AddCardsInPlaytoGameBoard()

            self.New_Game.ProcessPhaseActions(PHASE_WORKER)
            self.AddPlayerHandstoGameBoard()
            self.AddCardsInPlaytoGameBoard()
 
                        
            #self.New_Game.ProcessPhaseScoring(PHASE_WORKER)
    
            self.New_Game.DealCards (BUILDING_CARD_TYPE)

            self.New_Game.ProcessPhaseActions(PHASE_BUILDING)
            self.AddPlayerHandstoGameBoard()
            self.AddCardsInPlaytoGameBoard()

            #self.New_Game.ProcessPhaseScoring(PHASE_BUILDING)
    
            self.New_Game.DealCards (ARISTOCRAT_CARD_TYPE)
            self.New_Game.ProcessPhaseActions(PHASE_ARISTOCRAT)
            self.AddPlayerHandstoGameBoard()
            self.AddCardsInPlaytoGameBoard()
            #self.New_Game.ProcessPhaseScoring(PHASE_ARISTOCRAT)
    
            #self.New_Game.DealCards (TRADING_CARD_TYPE)
            #self.New_Game.ProcessPhaseActions(PHASE_TRADING)
    
            self.New_Game.RotateCards ()
            self.New_Game.DealCards(WORKER_CARD_TYPE)
            self.AddCardsInPlaytoGameBoard()
            #self.New_Game.RotatePlayers ()
            # Delete this line when running the game
            self.New_Game.EndOfGame = True    
            
                  
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    GameBoard = Board()
    GameBoard.setupUi(MainWindow)
    GameBoard.SetupBoard()
    GameBoard.btnStart.clicked.connect(GameBoard.StartButtonClick)  
    MainWindow.show()
    app.exec()
