#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Board Class - Contains GUI Elements
# Worker Class - Contains Thread
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import time

from PyQt5.Qt import QListWidgetItem, QPixmap, QObject, pyqtSignal,\
    QThread

from Game import Game
from Contents import *

from MainWindow import Ui_MainWindow


#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Worker Class
# Function to Run the Game
#----------------------------------------------------------------------------------------------------------------------------------------------------------

class Worker (QObject):    
    finished = pyqtSignal ()
    refreshboard = pyqtSignal (Game)
    refreshgamestatus = pyqtSignal (str)
    adddeckstogame = pyqtSignal (Game)
    
    def __init__(self, total_games):
        self.Total_Games = total_games
        self.sleep_between_phases = 0.02
        self.epsilon = BRAIN_EPSILON
        self.epsilon_increment_interval = BRAIN_EPSILON_INCREMENT_INTERVAL
        self.epsilon_increment = BRAIN_EPSILON_INCREMENT
        self.epsilon_max = BRAIN_EPSILON_MAX
        self.epsilon_min = BRAIN_EPSILON_MIN
        self.target_score = BRAIN_TARGET_SCORE
        self.target_score_increment = BRAIN_TARGET_SCORE_INCREMENT
        self.target_score_increment_interval = BRAIN_TARGET_SCORE_INCREMENT_INTERVAL
        self.reward_bands = BRAIN_REWARD_BANDS
        self.reward_increment = BRAIN_REWARD_INCREMENT
        self.penalty_bands = BRAIN_PENALTY_BANDS
        self.penalty_increment = BRAIN_PENALTY_INCREMENT

        super().__init__()
    
    def RunGame (self):
        
        try :
            Current_Game_Count = 1
    
            while Current_Game_Count <= self.Total_Games : 
                print("------------------------------------------------------------- Starting Game "+ str(Current_Game_Count) + " -------------------------------------------------------------")
                
                self.New_Game = Game (Current_Game_Count)
                self.New_Game.GameSetup()
                
                # Setup initial values for the brain
                for Player in self.New_Game.Players :                  
                    Player.Brain.InitializeBrain (self.epsilon, self.epsilon_increment, self.epsilon_max, self.epsilon_min, self.target_score, self.reward_bands, self.reward_increment, self.penalty_bands, self.penalty_increment)
                
                # Reset Target values every N games
                if Current_Game_Count % self.target_score_increment_interval == 0:
                    self.target_score += self.target_score_increment
                    self.refreshgamestatus.emit ("Updating Brains: Target Score - " + str(self.target_score))
                    for Player in self.New_Game.Players :
                        Player.Brain.UpdateTargetScore (self.target_score, self.reward_bands, self.reward_increment, self.penalty_bands, self.penalty_increment) 
   
                # Adjust epsilon every N games
                if Current_Game_Count % self.epsilon_increment_interval == 0:
                    self.epsilon += self.epsilon_increment
                    self.refreshgamestatus.emit ("Updating Brains: Epsilon - " + str(self.epsilon))
                    for Player in self.New_Game.Players :
                        Player.Brain.UpdateEpsilon (self.epsilon, self.epsilon_max, self.epsilon_min)
                
                self.adddeckstogame[Game].emit (self.New_Game)
                self.refreshboard[Game].emit(self.New_Game)
                Round_Count = 1
                
                while not self.New_Game.EndOfGame :

                    print("----------------------------------------------- Starting Round "+ str(Round_Count) + "  -----------------------------------------------")
                    print("----------------------- Starting Worker Phase -----------------------")
                    self.New_Game.DealCards(WORKER_CARD_TYPE)
                    self.New_Game.ProcessPhaseActions(PHASE_WORKER, Round_Count)
                    self.New_Game.ProcessPhaseScoring(PHASE_WORKER)
                    self.refreshboard[Game].emit(self.New_Game)
                    time.sleep(self.sleep_between_phases)
        
                    print("----------------------- Starting Building Phase -----------------------")
                    self.New_Game.DealCards (BUILDING_CARD_TYPE)
                    self.New_Game.ProcessPhaseActions(PHASE_BUILDING, Round_Count)
                    self.New_Game.ProcessPhaseScoring(PHASE_BUILDING)
                    self.refreshboard[Game].emit(self.New_Game)
                    time.sleep(self.sleep_between_phases)
            
                    print("----------------------- Starting Aristocrat Phase -----------------------")
                    self.New_Game.DealCards (ARISTOCRAT_CARD_TYPE)
                    self.New_Game.ProcessPhaseActions(PHASE_ARISTOCRAT, Round_Count)
                    self.New_Game.ProcessPhaseScoring(PHASE_ARISTOCRAT)
                    self.refreshboard[Game].emit(self.New_Game)
                    time.sleep(self.sleep_between_phases)
            
                    print("----------------------- Starting Trading Phase -----------------------")
                    self.New_Game.DealCards (TRADING_CARD_TYPE)
                    self.New_Game.ProcessPhaseActions(PHASE_TRADING, Round_Count)
                    self.refreshboard[Game].emit(self.New_Game)
                    time.sleep(self.sleep_between_phases)
                    
                    print("----------------------- Round Cleanup -----------------------")
                    self.New_Game.RotateCards ()
                    self.New_Game.RotateMarkers ()
                    self.refreshboard[Game].emit(self.New_Game)
                    time.sleep(self.sleep_between_phases)
    
                    print("----------------------------------------------- Completed Round "+ str(Round_Count) + " -----------------------------------------------")
                    
                    Round_Count += 1
                                    
                print ("----------------------- Processing final point adjustments -----------------------")
                
                self.New_Game.ProcessEndofGameActions()
                self.refreshboard[Game].emit(self.New_Game)
                time.sleep(.5)
                # Only Save the brain in the simulation is still exploring
                if self.epsilon > 0.01 :
                    self.New_Game.SavePlayersBrains()
                self.refreshboard[Game].emit(self.New_Game)
                time.sleep(self.sleep_between_phases)
                self.refreshgamestatus.emit ("Completed Game " + str(Current_Game_Count))
                
                print("------------------------------------------------------------- Game " + str(Current_Game_Count) + " Completed -------------------------------------------------------------")
             
                Current_Game_Count += 1
            
            print("------------------------------------------------------------- Simulation Completed -------------------------------------------------------------")
            self.finished.emit()    
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

    def flush (self):
        pass


class Board(Ui_MainWindow):
    def SetupBoard (self):

        # Sets up lists of objects the application will be interacting with
       
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

        self.lineNumGames.setText(str(DEFAULT_GAMES_PER_SESSION))

    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    # Functions to setup and run the game
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def StartButtonClick (self):
        
        try :
            print("------------------------------------------------------------- Starting Simulation -------------------------------------------------------------")
            self.listStatus.addItem(QListWidgetItem("------------------------------------------------------------- Starting Simulation -------------------------------------------------------------"))
            
            self.thread = QThread ()
            self.worker = Worker (int(self.lineNumGames.text()))
            self.worker.moveToThread(self.thread)
            
            self.thread.started.connect(self.worker.RunGame)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.adddeckstogame[Game].connect(self.AddDeckstoGameBoard)
            self.worker.refreshboard[Game].connect(self.RefreshBoard)
            self.worker.refreshgamestatus.connect(self.RefreshGameStatus)
            
            self.thread.start()
            
            self.ClearBoard()
            self.btnStart.setEnabled(False)
            self.thread.finished.connect(lambda: self.btnStart.setEnabled(True))
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
              
    def AddDeckstoGameBoard (self, New_Game):
        
        #self.listStatus.addItem(QListWidgetItem("Adding Worker Deck to Board"))
        for x in New_Game.WorkerDeck.Cards :
            self.listDeck_Worker.addItem(QListWidgetItem(x.CardName))
        
        #self.listStatus.addItem(QListWidgetItem("Adding Building Deck to Board"))
        for x in New_Game.BuildingDeck.Cards :
            self.listDeck_Building.addItem(QListWidgetItem(x.CardName))
            
        #self.listStatus.addItem(QListWidgetItem("Adding Aristocrat Deck to Board"))
        for x in New_Game.AristocratDeck.Cards :
            self.listDeck_Aristocrat.addItem(QListWidgetItem(x.CardName))
            
        #self.listStatus.addItem(QListWidgetItem("Adding Trading Deck to Board"))
        for x in New_Game.TradingDeck.Cards :
            self.listDeck_Trading.addItem(QListWidgetItem(x.CardName))
    
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    # Functions for updating the UI to reflect the current game state
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def RefreshGameStatus (self, Game_Message):
        self.listStatus.addItem(QListWidgetItem(Game_Message))
        self.listStatus.scrollToBottom()
    
    def RefreshPlayerIDs (self, New_Game):
        self.groupBoxPlayer1.setTitle("PLayer 1 - " + New_Game.Players[0].Name + " ID: " + str(New_Game.Players[0].ID))
        self.groupBoxPlayer2.setTitle("PLayer 2 - " + New_Game.Players[1].Name + " ID: " + str(New_Game.Players[1].ID))
        self.groupBoxPlayer3.setTitle("PLayer 3 - " + New_Game.Players[2].Name + " ID: " + str(New_Game.Players[2].ID))
        self.groupBoxPlayer4.setTitle("PLayer 4 - " + New_Game.Players[3].Name + " ID: " + str(New_Game.Players[3].ID))
    
    def RefreshPlayerColors (self, New_Game):
        self.lblColor_Player1.setText("Color: " + PLAYER_COLORS [New_Game.Players[0].Color][1])
        self.lblColor_Player2.setText("Color: " + PLAYER_COLORS [New_Game.Players[1].Color][1])
        self.lblColor_Player3.setText("Color: " + PLAYER_COLORS [New_Game.Players[2].Color][1])
        self.lblColor_Player4.setText("Color: " + PLAYER_COLORS [New_Game.Players[3].Color][1])

    def RefreshCardsInPlay(self, New_Game):

        #Clear the Upper and Lower Card Rows
        for x in range(len(self.CardSlots)) :
            self.CardSlots[x][0].clear()
            self.CardSlots[x][1].clear()
            
        self.listCardsInPlay.clear()
            
        for x in range (len(New_Game.CardsInPlay)) :
            self.CardSlots[x][New_Game.CardsInPlay[x].Row].setPixmap(QPixmap(":/Cards/" + str(New_Game.CardsInPlay[x].CardID) + ".png"))
            
        for x in New_Game.CardsInPlay:
            self.listCardsInPlay.addItem(QListWidgetItem(x.CardName))
    
    def RefreshPlayerHands(self, New_Game):
        
        #Clear the Player List Widgets before adding the cards again
        for x in range(len(self.PlayerCardLists)) :
            self.PlayerCardLists[x].clear()
        
        for Player in New_Game.Players :
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
    
    def RefreshPlayerPhases(self, New_Game):
        
        for PhaseLeaderLabel in self.PhaseLeaderLabels :
            PhaseLeaderLabel.clear()
        
        for p in New_Game.Players :
            if p.ID == PLAYER_1 :
                self.lblPhaseLeader_Player1.setText("Phase Leader: " + PHASES [p.Marker][1])
            if p.ID == PLAYER_2 :
                self.lblPhaseLeader_Player2.setText("Phase Leader: " + PHASES [p.Marker][1])
            if p.ID == PLAYER_3 :
                self.lblPhaseLeader_Player3.setText("Phase Leader: " + PHASES [p.Marker][1])
            if p.ID == PLAYER_4 :
                self.lblPhaseLeader_Player4.setText("Phase Leader: " + PHASES [p.Marker][1])           
    
    def RefreshMoney (self, New_Game):
        for Player in New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblMoney_Player1.setText("Money: " + str(Player.Money))
            if Player.ID == PLAYER_2 :
                self.lblMoney_Player2.setText("Money: " + str(Player.Money))
            if Player.ID == PLAYER_3 :
                self.lblMoney_Player3.setText("Money: " + str(Player.Money))
            if Player.ID == PLAYER_4 :
                self.lblMoney_Player4.setText("Money: " + str(Player.Money))    
    
    def RefreshVictoryPoints (self, New_Game):
        for Player in New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblVP_Player1.setText("Victory Points: " + str(Player.Score))
            if Player.ID == PLAYER_2 :
                self.lblVP_Player2.setText("Victory Points: " + str(Player.Score))
            if Player.ID == PLAYER_3 :
                self.lblVP_Player3.setText("Victory Points: " + str(Player.Score))
            if Player.ID == PLAYER_4 :
                self.lblVP_Player4.setText("Victory Points: " + str(Player.Score))
                
    def RefreshHeldCards (self, New_Game):
        for Player in New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblHeldCards_Player1.setText("Held Cards: " + str(Player.HeldCards))
            if Player.ID == PLAYER_2 :
                self.lblHeldCards_Player2.setText("Held Cards: " + str(Player.HeldCards))
            if Player.ID == PLAYER_3 :
                self.lblHeldCards_Player3.setText("Held Cards: " + str(Player.HeldCards))
            if Player.ID == PLAYER_4 :
                self.lblHeldCards_Player4.setText("Held Cards: " + str(Player.HeldCards))
    
    def RefreshUniqueAristocrate (self, New_Game):
        for Player in New_Game.Players :
            if Player.ID == PLAYER_1 :
                self.lblAristocrats_Player1.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))
            if Player.ID == PLAYER_2 :
                self.lblAristocrats_Player2.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))
            if Player.ID == PLAYER_3 :
                self.lblAristocrats_Player3.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))
            if Player.ID == PLAYER_4 :
                self.lblAristocrats_Player4.setText("Unique Aristocrats: " + str(Player.UniqueAristrocrats))        
    
    def RefreshBoard (self, New_Game):
        self.RefreshPlayerIDs(New_Game)
        self.RefreshPlayerColors(New_Game)
        self.RefreshCardsInPlay(New_Game)
        self.RefreshPlayerHands(New_Game)
        self.RefreshPlayerPhases(New_Game)
        self.RefreshMoney(New_Game)
        self.RefreshVictoryPoints(New_Game)
        self.RefreshHeldCards(New_Game)
        self.RefreshUniqueAristocrate(New_Game)
    
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
    
       
