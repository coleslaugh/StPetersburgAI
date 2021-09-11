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
from time import sleep


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

        self.PhaseLeaderLabels = []
        self.PhaseLeaderLabels.append(self.lblPhaseLeader_Player1)
        self.PhaseLeaderLabels.append(self.lblPhaseLeader_Player2)
        self.PhaseLeaderLabels.append(self.lblPhaseLeader_Player3)
        self.PhaseLeaderLabels.append(self.lblPhaseLeader_Player4)
        

        for x in range(len(self.CardSlots)) :
            self.CardSlots[x][0].setScaledContents(True)
            self.CardSlots[x][1].setScaledContents(True)

       
    def StartButtonClick (self):
        self.ClearBoard()
        print("-------------------------------------------------------------Starting Game-------------------------------------------------------------")
        self.listStatus.addItem(QListWidgetItem("Creating Game"))
        self.New_Game = Game (1)
        self.listStatus.addItem(QListWidgetItem("Setting Up Game"))
        self.New_Game.GameSetup()
        self.AddDeckstoGameBoard()
        self.RefreshPlayerIDs()
        self.RefreshPlayerColors()
        self.RefreshMoney()
        self.RefreshVictoryPoints()
        self.listStatus.addItem(QListWidgetItem("Game Setup Complete"))
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
        self.groupBoxPlayer1.setTitle("Player 1")
        self.groupBoxPlayer2.setTitle("Player 2")
        self.groupBoxPlayer3.setTitle("Player 3")
        self.groupBoxPlayer4.setTitle("Player 4")
        self.listCardsInPlay.clear()
        
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
            
        self.listStatus.addItem(QListWidgetItem("Adding Trading Deck to Board"))
        for x in self.New_Game.TradingDeck.Cards :
            self.listDeck_Trading.addItem(QListWidgetItem(x.CardName))
    
    def RefreshPlayerHands(self):
        
        #Clear the Player List Widgets before adding the cards again
        for x in range(len(self.PlayerCardLists)) :
            self.PlayerCardLists[x].clear()
        
        for Player in self.New_Game.Players :
            if Player.ID == PLAYER_1 :
                for Card in Player.Hand :
                    if Card.CardStatus == PLAYER_ACTIVE_CARD :
                        self.listCards_Player1.addItem(QListWidgetItem(Card.CardName))
                    else:
                        self.listCards_Player1.addItem(QListWidgetItem(Card.CardName + " - Held"))
            if Player.ID == PLAYER_2 :
                for Card in Player.Hand :
                    if Card.CardStatus == PLAYER_ACTIVE_CARD :
                        self.listCards_Player2.addItem(QListWidgetItem(Card.CardName))
                    else:
                        self.listCards_Player2.addItem(QListWidgetItem(Card.CardName + " - Held"))
            if Player.ID == PLAYER_3 :
                for Card in Player.Hand :
                    if Card.CardStatus == PLAYER_ACTIVE_CARD :
                        self.listCards_Player3.addItem(QListWidgetItem(Card.CardName))
                    else:
                        self.listCards_Player3.addItem(QListWidgetItem(Card.CardName + " - Held"))
            if Player.ID == PLAYER_4 :
                for Card in Player.Hand :
                    if Card.CardStatus == PLAYER_ACTIVE_CARD :
                        self.listCards_Player4.addItem(QListWidgetItem(Card.CardName))
                    else:
                        self.listCards_Player4.addItem(QListWidgetItem(Card.CardName + " - Held"))             

    def RefreshPlayerColors (self):
        self.lblColor_Player1.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[0].Color][1])
        self.lblColor_Player2.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[1].Color][1])
        self.lblColor_Player3.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[2].Color][1])
        self.lblColor_Player4.setText("Color: " + PLAYER_COLORS [self.New_Game.Players[3].Color][1])
    
    def RefreshPlayerIDs (self):
        self.groupBoxPlayer1.setTitle("PLayer 1 - " + self.New_Game.Players[0].Name + " ID: " + str(self.New_Game.Players[0].ID))
        self.groupBoxPlayer2.setTitle("PLayer 2 - " + self.New_Game.Players[1].Name + " ID: " + str(self.New_Game.Players[1].ID))
        self.groupBoxPlayer3.setTitle("PLayer 3 - " + self.New_Game.Players[2].Name + " ID: " + str(self.New_Game.Players[2].ID))
        self.groupBoxPlayer4.setTitle("PLayer 4 - " + self.New_Game.Players[3].Name + " ID: " + str(self.New_Game.Players[3].ID))
    
    def RefreshPlayerPhases(self):
        
        for PhaseLeaderLabel in self.PhaseLeaderLabels :
            PhaseLeaderLabel.clear()
        
        for p in self.New_Game.Players :
            if p.ID == PLAYER_1 :
                self.lblPhaseLeader_Player1.setText("Phase Leader: " + PHASES [p.Marker][1])
            if p.ID == PLAYER_2 :
                self.lblPhaseLeader_Player2.setText("Phase Leader: " + PHASES [p.Marker][1])
            if p.ID == PLAYER_3 :
                self.lblPhaseLeader_Player3.setText("Phase Leader: " + PHASES [p.Marker][1])
            if p.ID == PLAYER_4 :
                self.lblPhaseLeader_Player4.setText("Phase Leader: " + PHASES [p.Marker][1])
        
     
    def RefreshCardsInPlay(self):

        #Clear the Upper and Lower Card Rows
        for x in range(len(self.CardSlots)) :
            self.CardSlots[x][0].clear()
            self.CardSlots[x][1].clear()
            
        self.listCardsInPlay.clear()
            
        for x in range (len(self.New_Game.CardsInPlay)) :
            self.CardSlots[x][self.New_Game.CardsInPlay[x].Row].setPixmap(QPixmap(":/Cards/" + str(self.New_Game.CardsInPlay[x].CardID) + ".png"))
            
        for x in self.New_Game.CardsInPlay:
            self.listCardsInPlay.addItem(QListWidgetItem(x.CardName))
               
    def RefreshMoney (self):
        for Player in self.New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblMoney_Player1.setText("Money: " + str(Player.Money))
            if Player.ID == PLAYER_2 :
                self.lblMoney_Player2.setText("Money: " + str(Player.Money))
            if Player.ID == PLAYER_3 :
                self.lblMoney_Player3.setText("Money: " + str(Player.Money))
            if Player.ID == PLAYER_4 :
                self.lblMoney_Player4.setText("Money: " + str(Player.Money))    
    
    def RefreshVictoryPoints (self):
        for Player in self.New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblVP_Player1.setText("Victory Points: " + str(Player.Score))
            if Player.ID == PLAYER_2 :
                self.lblVP_Player2.setText("Victory Points: " + str(Player.Score))
            if Player.ID == PLAYER_3 :
                self.lblVP_Player3.setText("Victory Points: " + str(Player.Score))
            if Player.ID == PLAYER_4 :
                self.lblVP_Player4.setText("Victory Points: " + str(Player.Score))
                
    def RefreshHeldCards (self):
        for Player in self.New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblHeldCards_Player1.setText("Held Cards: " + str(Player.HeldCards))
            if Player.ID == PLAYER_2 :
                self.lblHeldCards_Player2.setText("Held Cards: " + str(Player.HeldCards))
            if Player.ID == PLAYER_3 :
                self.lblHeldCards_Player3.setText("Held Cards: " + str(Player.HeldCards))
            if Player.ID == PLAYER_4 :
                self.lblHeldCards_Player4.setText("Held Cards: " + str(Player.HeldCards))
    
    def RefreshUniqueAristocrate (self):
        for Player in self.New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblAristocrats_Player1.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))
            if Player.ID == PLAYER_2 :
                self.lblAristocrats_Player2.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))
            if Player.ID == PLAYER_3 :
                self.lblAristocrats_Player3.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))
            if Player.ID == PLAYER_4 :
                self.lblAristocrats_Player4.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))        
    
    def RefreshBoard (self):
        self.RefreshCardsInPlay()
        self.RefreshPlayerHands()
        self.RefreshPlayerPhases()
        self.RefreshMoney()
        self.RefreshVictoryPoints()
        self.RefreshHeldCards()
        self.RefreshUniqueAristocrate()
    
    def RunGame (self):
        Round_Count = 1
        Max_Phase = 5
        while not self.New_Game.EndOfGame :
            try :
                print("----------------------------------------------- Starting Round "+ str(Round_Count) + "  -----------------------------------------------")
                print("----------------------- Starting Worker Phase -----------------------")
                self.New_Game.DealCards(WORKER_CARD_TYPE)
                self.New_Game.ProcessPhaseActions(PHASE_WORKER)
                self.New_Game.ProcessPhaseScoring(PHASE_WORKER)
    
                print("----------------------- Starting Building Phase -----------------------")
                self.New_Game.DealCards (BUILDING_CARD_TYPE)
                self.New_Game.ProcessPhaseActions(PHASE_BUILDING)
                self.New_Game.ProcessPhaseScoring(PHASE_BUILDING)
        
                print("----------------------- Starting Aristocrat Phase -----------------------")
                self.New_Game.DealCards (ARISTOCRAT_CARD_TYPE)
                self.New_Game.ProcessPhaseActions(PHASE_ARISTOCRAT)
                self.New_Game.ProcessPhaseScoring(PHASE_ARISTOCRAT)
        
                print("----------------------- Starting Trading Phase -----------------------")
                self.New_Game.DealCards (TRADING_CARD_TYPE)
                self.New_Game.ProcessPhaseActions(PHASE_TRADING)
                
                print("----------------------- Round Cleanup -----------------------")
                self.New_Game.RotateCards ()
                self.New_Game.RotateMarkers ()
                self.RefreshBoard()
                sleep(1)
                #self.New_Game.RotatePlayers ()
                print("----------------------------------------------- Completed Round "+ str(Round_Count) + " -----------------------------------------------")
                self.listStatus.addItem(QListWidgetItem("Completed Round "+ str(Round_Count)))
                
                Round_Count += 1
            
            except :
                print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
            #if Phase_Count == Max_Phase :
            #    self.New_Game.EndOfGame = True    
        
        print ("----------------------- Processing final point adjustments -----------------------")
        
        self.New_Game.ProcessEndofGameActions()
        self.RefreshBoard()
        
        print("------------------------------------------------------------- Game Completed -------------------------------------------------------------")
                  
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    
    GameBoard = Board()
    GameBoard.setupUi(MainWindow)
    GameBoard.SetupBoard()
    GameBoard.btnStart.clicked.connect(GameBoard.StartButtonClick)  
    MainWindow.show()
    app.exec()
   