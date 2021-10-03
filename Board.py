#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Board Class - Contains GUI Elements
# Worker Class - Contains Thread
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
import time
import math

from PyQt5.Qt import QListWidgetItem, QPixmap, QObject, pyqtSignal, QThread

from Game import Game
from Contents import PLAYER_1, PLAYER_2, PLAYER_3, PLAYER_4, PLAYER_COLORS, PLAYER_ACTIVE_CARD, \
    PHASES, PHASE_WORKER, PHASE_BUILDING, PHASE_ARISTOCRAT, PHASE_TRADING,\
    DEFAULT_GAMES_PER_SESSION, BRAIN_EPSILON, BRAIN_EPSILON_INCREMENT,\
    BRAIN_EPSILON_INCREMENT_INTERVAL, BRAIN_EPSILON_MAX, BRAIN_EPSILON_MIN,\
    BRAIN_REWARD_VALUE, BRAIN_REWARD_BANDS, BRAIN_PENALTY_VALUE,\
    BRAIN_PENALTY_BANDS, BRAIN_TARGET_SCORE, BRAIN_TARGET_SCORE_INCREMENT,\
    BRAIN_DEFAULT_VALUE, BRAIN_PASS_DEFAULT_VAULE, BRAIN_RESET_INTERVAL,\
    BRAIN_TARGET_SCORE_INCREMENT_INTERVAL

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
        self.episode_avg_scores = [[PLAYER_1,0,0],[PLAYER_2,0,0],[PLAYER_3,0,0],[PLAYER_4,0,0]]
        
        self.Brain_Settings = {
            'Epsilon':0, 
            'Epsilon Increment' : 0, 
            'Epsilon Increment Interval' : 0,
            'Epsilon Max' : 0,
            'Epsilon Min' : 0,
            'Reward Value' : 0,
            'Reward Bands' : 0,
            'Penalty Value' : 0,
            'Penalty Bands' : 0,
            'Target Score' : 0,
            'Target Score Increment' : 0,
            'Target Score Increment Interval' : 0,
            'Default Action Value' : 0,
            'Default Pass Value' : 0,
            'Brain Reset Interval' : 0
            }
        
        super().__init__()
    
    def RunGame (self):
        
        try :
            Current_Game_Count = 1
    
            while Current_Game_Count <= self.Total_Games : 
                print("------------------------------------------------------------- Starting Game "+ str(Current_Game_Count) + " -------------------------------------------------------------")
                
                # Create and Setup a new Game
                self.New_Game = Game (Current_Game_Count)
                self.New_Game.GameSetup()
                
                # Setup initial values for the Player's brains
                for Player in self.New_Game.Players :                  
                    Player.Brain.InitializeBrain (self.Brain_Settings)

                # Adjust Target Score every N games
                if Current_Game_Count % self.Brain_Settings['Target Score Increment Interval'] == 0:
                    self.Brain_Settings['Target Score'] += self.Brain_Settings['Target Score Increment']
                    self.refreshgamestatus.emit ("Updating Brains: Target Score - " + str(self.Brain_Settings['Target Score']))
                    for Player in self.New_Game.Players :
                        Player.Brain.UpdateTargetScore (self.Brain_Settings) 
   
                # Adjust epsilon value every N games
                if Current_Game_Count % self.Brain_Settings['Epsilon Increment Interval'] == 0:
                    self.Brain_Settings['Epsilon'] += self.Brain_Settings['Epsilon Increment']
                    self.refreshgamestatus.emit ("Updating Brains: Epsilon - " + str(self.Brain_Settings['Epsilon']))
                    for Player in self.New_Game.Players :
                        Player.Brain.UpdateEpsilon (self.Brain_Settings)
                
                # Update the UI
                self.adddeckstogame[Game].emit(self.New_Game)
                self.refreshboard[Game].emit(self.New_Game)
                Round_Count = 1
                
                while not self.New_Game.EndOfGame :

                    print("----------------------------------------------- Starting Round "+ str(Round_Count) + "  -----------------------------------------------")
                    print("----------------------- Starting Worker Phase -----------------------")
                    self.New_Game.DealCards(PHASE_WORKER)
                    self.New_Game.ProcessPhaseActions(PHASE_WORKER, Round_Count)
                    self.New_Game.ProcessPhaseScoring(PHASE_WORKER)
                    #self.refreshboard[Game].emit(self.New_Game)
                    #time.sleep(self.sleep_between_phases)
                                        
                    print("----------------------- Starting Building Phase -----------------------")
                    self.New_Game.DealCards (PHASE_BUILDING)
                    self.New_Game.ProcessPhaseActions(PHASE_BUILDING, Round_Count)
                    self.New_Game.ProcessPhaseScoring(PHASE_BUILDING)
                    #self.refreshboard[Game].emit(self.New_Game)
                    #time.sleep(self.sleep_between_phases)                    
            
                    print("----------------------- Starting Aristocrat Phase -----------------------")
                    self.New_Game.DealCards (PHASE_ARISTOCRAT)
                    self.New_Game.ProcessPhaseActions(PHASE_ARISTOCRAT, Round_Count)
                    self.New_Game.ProcessPhaseScoring(PHASE_ARISTOCRAT)
                    #self.refreshboard[Game].emit(self.New_Game)
                    #time.sleep(self.sleep_between_phases)    
            
                    print("----------------------- Starting Trading Phase -----------------------")
                    self.New_Game.DealCards (PHASE_TRADING)
                    self.New_Game.ProcessPhaseActions(PHASE_TRADING, Round_Count)
                    #self.refreshboard[Game].emit(self.New_Game)
                    #time.sleep(self.sleep_between_phases)
                    
                    print("----------------------- Round Cleanup -----------------------")
                    self.New_Game.RotateCards ()
                    self.New_Game.RotateMarkers ()
                    self.refreshboard[Game].emit(self.New_Game)
                    #time.sleep(self.sleep_between_phases)
    
                    print("----------------------------------------------- Completed Round "+ str(Round_Count) + " -----------------------------------------------")
                    
                    Round_Count += 1
                                    
                print ("----------------------- Processing final point adjustments -----------------------")
                
                self.New_Game.ProcessEndofGameActions()
                
                # Update Players Average Score
                self.episode_avg_scores = self.New_Game.UpdateAvgScores(self.episode_avg_scores)
                
                self.refreshgamestatus.emit ("Completed Game " + str(Current_Game_Count))
                self.refreshboard[Game].emit(self.New_Game)
                
                # Only Save the brain in the simulation is still exploring
                if self.Brain_Settings['Epsilon'] > 0.01 :
                    self.New_Game.SavePlayersBrains()
                    
                    # Replace the poorest performing Brains with the Best performing Brain every N games
                    if Current_Game_Count % self.Brain_Settings['Brain Reset Interval'] == 0:
                        self.New_Game.ResetPlayersBrains(self.episode_avg_scores)
                        self.refreshgamestatus.emit ("Refreshing Player Brains: " + str (self.episode_avg_scores))
                        #Reset the Average Score Counter
                        self.episode_avg_scores = [[PLAYER_1,0,0],[PLAYER_2,0,0],[PLAYER_3,0,0],[PLAYER_4,0,0]]

                time.sleep(.3)
                                
                print("------------------------------------------------------------- Game " + str(Current_Game_Count) + " Completed -------------------------------------------------------------")
             
                Current_Game_Count += 1
            
            print("------------------------------------------------------------- Simulation Completed -------------------------------------------------------------")
            self.finished.emit()    
        
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))

    def flush (self):
        pass

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Board Class
# Establishes UI elements and Threads
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    
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
        self.lineEpsilon_Value.setText(str (BRAIN_EPSILON))
        self.lineEpsilon_Increment.setText(str(BRAIN_EPSILON_INCREMENT))
        self.lineEpsilon_Interval.setText(str(BRAIN_EPSILON_INCREMENT_INTERVAL))
        self.lineEpsilon_Max.setText(str(BRAIN_EPSILON_MAX))
        self.lineEpsilon_Min.setText(str(BRAIN_EPSILON_MIN))
        
        self.lineReward_Value.setText(str(BRAIN_REWARD_VALUE))
        self.lineReward_Bands.setText(str(BRAIN_REWARD_BANDS))
        
        self.linePenalty_Value.setText(str(BRAIN_PENALTY_VALUE))
        self.linePenalty_Bands.setText(str(BRAIN_PENALTY_BANDS))
        
        self.lineTarget_Value.setText(str(BRAIN_TARGET_SCORE))
        self.lineTarget_Increment.setText(str(BRAIN_TARGET_SCORE_INCREMENT))
        self.lineTarget_Interval.setText(str(BRAIN_TARGET_SCORE_INCREMENT_INTERVAL))
        
        self.lineBrain_Default.setText(str(BRAIN_DEFAULT_VALUE))
        self.lineBrain_Pass_Default.setText(str(BRAIN_PASS_DEFAULT_VAULE))
        self.lineBrain_Reset_Interval.setText(str(BRAIN_RESET_INTERVAL))
        
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    # Functions to setup and run the game
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def StartButtonClick (self):
        
        try :
            print("------------------------------------------------------------- Starting Simulation -------------------------------------------------------------")
            self.listStatus.addItem(QListWidgetItem("------------------------------------------------------------- Starting Simulation -------------------------------------------------------------"))
            
            self.thread = QThread ()
            self.worker = Worker (int(self.lineNumGames.text()))
            self.InitilizeWorkerSettings()
            
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
              
    def InitilizeWorkerSettings (self):
        
        self.worker.Brain_Settings['Epsilon'] = float(self.lineEpsilon_Value.text ())
        self.worker.Brain_Settings['Epsilon Increment'] = float(self.lineEpsilon_Increment.text ())
        self.worker.Brain_Settings['Epsilon Increment Interval'] = int(self.lineEpsilon_Interval.text ())
        self.worker.Brain_Settings['Epsilon Max'] = int(self.lineEpsilon_Max.text())
        self.worker.Brain_Settings['Epsilon Min'] = int(self.lineEpsilon_Min.text())
        
        self.worker.Brain_Settings['Reward Value'] = int(self.lineReward_Value.text())
        self.worker.Brain_Settings['Reward Bands'] = int(self.lineReward_Bands.text())
        
        self.worker.Brain_Settings['Penalty Value'] = int(self.linePenalty_Value.text())
        self.worker.Brain_Settings['Penalty Bands'] = int(self.linePenalty_Bands.text())
        
        self.worker.Brain_Settings['Target Score'] = int(self.lineTarget_Value.text())
        self.worker.Brain_Settings['Target Score Increment'] = int(self.lineTarget_Increment.text())
        self.worker.Brain_Settings['Target Score Increment Interval'] = int(self.lineTarget_Interval.text())
        
        self.worker.Brain_Settings['Default Action Value'] = int(self.lineBrain_Default.text())
        self.worker.Brain_Settings['Default Pass Value'] = int(self.lineBrain_Pass_Default.text())
        self.worker.Brain_Settings['Brain Reset Interval'] = int(self.lineBrain_Reset_Interval.text())
        
        return 
    
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
                self.lblVP_Player1.setText("Victory Points: " + str(Player.Score) + " - Avg : " + str(math.trunc(Player.AverageScore)))
            if Player.ID == PLAYER_2 :
                self.lblVP_Player2.setText("Victory Points: " + str(Player.Score) + " - Avg : " + str(math.trunc(Player.AverageScore)))
            if Player.ID == PLAYER_3 :
                self.lblVP_Player3.setText("Victory Points: " + str(Player.Score) + " - Avg : " + str(math.trunc(Player.AverageScore)))
            if Player.ID == PLAYER_4 :
                self.lblVP_Player4.setText("Victory Points: " + str(Player.Score) + " - Avg : " + str(math.trunc(Player.AverageScore)))
                

                
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
    
       
