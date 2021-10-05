'''
Created on Sep 14, 2021

@author: mikes
'''
from random import randint
import pandas as pd
import numpy as numpy
import sys

from Contents import  ACTIONS, ACTION_BUY, DECKS, TRADING_CARDS,\
    WORKER_CARD_TYPE, CLASS_ALL, MAX_POINTS_TO_BUY, \
    BRAIN_ROUNDS, BRAIN_PHASES, ACTION_HOLD, ACTION_UPGRADE, ACTION_OBSERVATORY, \
    ACTION_PUB, ACTION_PASS, PLAYER_HELD_CARD, \
    LUMBERJACK_CARD, POPE_CARD, AUTHOR_CARD, CARD_TYPES, PHASE_WORKER, PLAYERS,\
    ARISTOCRAT_CARDS, BRAIN_MAX_ACTION_VALUE, BRAIN_MIN_ACTION_VALUE,\
    ARISTOCRAT_CARD_TYPE, BRAIN_PENALTY_HELD_CARD, BRAIN_REWARD_BUY_HELD_CARD,\
    BRAIN_REWARD_BUY_UNIQUE_ARISTOCRAT, BRAIN_REWARD_HOLD_UNIQUE_ARISTOCRAT,\
    BRAIN_REWARD_MONEY_VALUE, BRAIN_REWARD_VP_VALUE,\
    BRAIN_REWARD_CARD_MULTIPLIER, CARPENTER_WORKSHOP_ID, GOLD_SMELTER_ID,\
    MARIINSKIJ_THEATER_ID, TAX_MAN_ID

from Card import Card


class Brain (object):

    def __init__(self, PLayerID):
        self.PlayerID = PLayerID
        self.indexes = []
        self.cols = []
        self.Action_Dataframe = []
        self.default_value = 0
        self.default_pass_value = 0
        self.epsilon = 0
        self.epsilon_max = 0
        self.epsilon_min =0
        self.target_score = 0
        self.rewards_value = 0
        self.rewards_bands = 0
        #self.rewards_increment = 0
        self.penalty_value = 0
        self.penalty_bands = 0
        #self.penalty_increment = 0
        
      
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Brain Initialization functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    def InitializeBrain (self, Brain_Settings):
               
        self.epsilon = Brain_Settings['Epsilon']
        self.epsilon_increment = Brain_Settings['Epsilon Increment']
        self.epsilon_max = Brain_Settings['Epsilon Max']
        self.epsilon_min = Brain_Settings['Epsilon Min']
        
        self.rewards_value = Brain_Settings['Reward Value']
        self.rewards_bands = Brain_Settings['Reward Bands']
        
        self.penalty_value = Brain_Settings['Penalty Value']
        self.penalty_bands = Brain_Settings['Penalty Bands']
        
        self.target_score = Brain_Settings['Target Score']
        
        self.default_value = Brain_Settings['Default Action Value']
        self.default_pass_value = Brain_Settings['Default Pass Value']
        
        self.LoadBrain()

    
    def UpdateTargetScore (self, Brain_Settings):
        self.target_score = Brain_Settings['Target Score']
        self.rewards_bands = Brain_Settings['Reward Bands']
        #self.rewards_increment = reward_increment
        self.penalty_bands = Brain_Settings['Penalty Bands']
        #self.penalty_increment = penalty_increment
        
    
    def UpdateEpsilon (self, Brain_Settings):
        
        if Brain_Settings['Epsilon'] >= Brain_Settings['Epsilon Max'] :
            self.epsilon = Brain_Settings['Epsilon Max']
        else :
            self.epsilon = Brain_Settings['Epsilon']
        
        if Brain_Settings['Epsilon'] <= Brain_Settings['Epsilon Min'] :
            self.epsilon = Brain_Settings['Epsilon Min']
        else :
            self.epsilon = Brain_Settings['Epsilon']

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Data Frame Initialization functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def InitializeActionDataFrame (self):
        self.GetNamedIndexes()
        self.GetColumns()
        self.Action_Dataframe = pd.DataFrame(self.default_value, index=self.indexes, columns=self.cols)
        self.SetDefaultValues ()
    
    def SetDefaultPassValue (self):
        self.Action_Dataframe[ACTIONS[ACTION_PASS][1]] = self.default_pass_value
    
    def SetDefaultValues (self) :
        self.SetDefaultPassValue ()
    
    def GetNamedIndexes (self):
        Phase_Index = BRAIN_PHASES
        Round_Index = BRAIN_ROUNDS

        for round_num in Round_Index :
            self.indexes.append(round_num)
        
        
        '''for round_num in Round_Index :
            for phase in Phase_Index :
                self.indexes.append(round_num + phase)
        '''
        print (self.indexes)

        
    def GetBuyColumns (self):
    
        for Deck in DECKS :
            if Deck[0] != TRADING_CARDS :
                for Card in Deck[0] :
                    c = ACTIONS[ACTION_BUY][1] + "-" + Card[0]['Name']
                    self.cols.append(c)
                    if Deck[0] == ARISTOCRAT_CARDS :
                        c = ACTIONS[ACTION_BUY][1] + "-" + Card[0]['Name'] + "-Unique"
                        self.cols.append(c)

    def GetBuyHoldColumns (self):
    
        for Deck in DECKS :
            if Deck[0] != TRADING_CARDS :
                for Card in Deck[0] :
                    c = ACTIONS[ACTION_BUY][1] + "-" + ACTIONS[ACTION_HOLD][1] + "-" + Card[0]['Name']
                    self.cols.append(c)
                    if Deck[0] == ARISTOCRAT_CARDS :
                        c = ACTIONS[ACTION_BUY][1] + "-" + ACTIONS[ACTION_HOLD][1] + "-" + Card[0]['Name'] + "-Unique"
                        self.cols.append(c) 

    def GetHoldColumns (self):
    
        for Deck in DECKS :
            for Card in Deck[0] :
                c = ACTIONS[ACTION_HOLD][1] + "-" + Card[0]['Name']
                self.cols.append(c)
                if Deck[0] == ARISTOCRAT_CARDS :
                    c = ACTIONS[ACTION_HOLD][1] + "-" + Card[0]['Name'] + "-Unique"
                    self.cols.append(c)
                if Deck[0] == TRADING_CARDS :
                    if Card[0]['Card Type'] == ARISTOCRAT_CARD_TYPE : 
                        c = ACTIONS[ACTION_HOLD][1] + "-" + Card[0]['Name'] + "-Unique"
                        self.cols.append(c)

    def GetUpgradeColumns (self):
        for TradingCard in TRADING_CARDS :
            for Deck in DECKS :
                if Deck[0] != TRADING_CARDS :
                    for TargetCard in Deck[0] :
                        if (TradingCard[0]['Class'] == TargetCard[0]['Class']) or (TradingCard[0]['Card Type'] == WORKER_CARD_TYPE and TargetCard[0]['Class'] == CLASS_ALL) :
                            c = ACTIONS[ACTION_UPGRADE][1] + "-" + TradingCard[0]['Name'] + "-" + TargetCard[0]['Name']
                            self.cols.append(c)
                            #Add Columns for Upgrading Aristocrats resulting in +1 unique Aristrocrats
                            if Deck[0] == ARISTOCRAT_CARDS :
                                c = ACTIONS[ACTION_UPGRADE][1] + "-" + TradingCard[0]['Name'] + "-" + TargetCard[0]['Name'] + "-Unique"
                                self.cols.append(c)
        
    def GetUpgradeHoldColumns (self):
        for TradingCard in TRADING_CARDS :
            for Deck in DECKS :
                if Deck[0] != TRADING_CARDS :
                    for TargetCard in Deck[0] :
                        if (TradingCard[0]['Class'] == TargetCard[0]['Class']) or (TradingCard[0]['Card Type'] == WORKER_CARD_TYPE and TargetCard[0]['Class'] == CLASS_ALL) :
                            c = ACTIONS[ACTION_UPGRADE][1] + "-" + ACTIONS[ACTION_HOLD][1] + "-" + TradingCard[0]['Name'] + "-" + TargetCard[0]['Name']
                            self.cols.append(c)
                            #Add Columns for Upgrading Aristocrats resulting in +1 unique Aristrocrats
                            if Deck[0] == ARISTOCRAT_CARDS :
                                c = ACTIONS[ACTION_UPGRADE][1] + "-" + ACTIONS[ACTION_HOLD][1] + "-" + TradingCard[0]['Name'] + "-" + TargetCard[0]['Name'] + "-Unique"
                                self.cols.append(c)
    
    
    def GetObservatoryColumns (self):
        for CardType in CARD_TYPES :
            self.cols.append(ACTIONS[ACTION_OBSERVATORY][1] + "-" + CardType[1])
    
    def GetPubColumns (self):
        for x in range(0,MAX_POINTS_TO_BUY + 1) :
            self.cols.append(ACTIONS[ACTION_PUB][1] + "-" + str(x))

    
    def GetPassColumn (self):
        self.cols.append(ACTIONS[ACTION_PASS][1])
    
    
    def GetColumns (self):
        self.GetBuyColumns()
        self.GetBuyHoldColumns()
        self.GetHoldColumns()
        self.GetUpgradeColumns()
        self.GetUpgradeHoldColumns()
        self.GetObservatoryColumns()
        self.GetPubColumns()
        self.GetPassColumn()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Data Frame Load/Save Functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    def SaveBrain (self):
        self.Action_Dataframe.to_csv('./' + PLAYERS[self.PlayerID][1] + ' - brain.csv', index=True)
        
    def LoadBrain (self):
        try:
            self.Action_Dataframe = pd.read_csv ('./' + PLAYERS[self.PlayerID][1] + ' - brain.csv', index_col=0)
        except FileNotFoundError :
            self.InitializeActionDataFrame()
            self.Action_Dataframe.to_csv('./' + PLAYERS[self.PlayerID][1] + ' - brain.csv', index=True)

    def ReplaceBrain (self, Dataframe):
        self.Action_Dataframe = Dataframe
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions to give Rewards and Penalties for Actions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def DetermineFinalScoreRewards (self, FinalScore):
        Reward = 0
        
        if FinalScore == self.target_score :
            Reward = 0
        if FinalScore > self.target_score :
            Reward = self.rewards_value
        if FinalScore > self.target_score + self.rewards_bands :
            Reward = 2 * self.rewards_value
        if FinalScore > self.target_score + (2 * self.rewards_bands) :
            Reward = 3 * self.rewards_value
        
        if FinalScore < self.target_score :
            Reward = self.penalty_value
        if FinalScore < self.target_score - self.penalty_bands :
            Reward = 2 * self.penalty_value
        if FinalScore < self.target_score - (2 * self.penalty_bands) :
            Reward = 3 * self.penalty_value
    
        return Reward
    
    def DetermineKeptHeldCardPenalty (self, Action, Hand):
        
        Reward = 0
        
        if Action[0] == ACTION_HOLD :
            for Card in Hand :
                if Card.CardStatus == PLAYER_HELD_CARD :
                    if Card == Action[1] :
                        Reward = BRAIN_PENALTY_HELD_CARD
        return Reward
    
    def DetermineBuyHeldCardRewards (self, Action):
        
        Reward = 0
        
        if Action[0] == ACTION_BUY :
            if Action [2] == PLAYER_HELD_CARD :
                Reward = BRAIN_REWARD_BUY_HELD_CARD
        
        return Reward
    
    def DetermineUniqueAristocratRewards (self, Action):
        
        Reward = 0
        
        if Action[0] == ACTION_BUY or Action[0] == ACTION_UPGRADE :
            if Action [3] == True :
                Reward = BRAIN_REWARD_BUY_UNIQUE_ARISTOCRAT
                
        if Action[0] == ACTION_HOLD :
            if Action [2] == True :
                Reward = BRAIN_REWARD_HOLD_UNIQUE_ARISTOCRAT
        
        return Reward
    
    def DetermineCardRewards (self, Action) :
        
        Reward = 0
        
        if Action[0] == ACTION_BUY :
            Reward = round((((Action[1].MoneyEarned * BRAIN_REWARD_MONEY_VALUE)+(Action[1].VPEarned * BRAIN_REWARD_VP_VALUE))/(Action[1].CardCost)) * BRAIN_REWARD_CARD_MULTIPLIER, 0) 
        
        if Action[0] == ACTION_UPGRADE :
            TradingCard = Action[1][0]
            TargetCard = Action[1][1]
            Cost = TradingCard.CardCost - TargetCard.CardCost
            
            if TradingCard.CardID == CARPENTER_WORKSHOP_ID or TradingCard.CardID == GOLD_SMELTER_ID or TradingCard.CardID == MARIINSKIJ_THEATER_ID or TradingCard.CardID == TAX_MAN_ID :
                Money = 3
            else : 
                Money = TradingCard.MoneyEarned - TargetCard.MoneyEarned
            
            VP = TradingCard.VPEarned - TargetCard.VPEarned
            
            if Cost < 1 : Cost = 1
            
            Reward = round((((Money * BRAIN_REWARD_MONEY_VALUE)+(VP * BRAIN_REWARD_VP_VALUE))/(Cost)) * BRAIN_REWARD_CARD_MULTIPLIER, 0)
        
        return int(Reward)
    
    def UpdateRewards (self, ActionsTaken, FinalScore, Hand):
        
        try :
            ScoreReward = self.DetermineFinalScoreRewards (FinalScore)
            
            for ActionTaken in ActionsTaken :
            
                Action = ActionTaken[0]
                Round = ActionTaken[1]
                EndOfGame = ActionTaken[3]
                StateIndex = self.DetermineStateIndex(Round, EndOfGame)
                ActionCol =  self.DetermineActionCol(Action)
                
                Reward = ScoreReward
                Reward += self.DetermineKeptHeldCardPenalty (Action, Hand)
                Reward += self.DetermineBuyHeldCardRewards(Action)
                Reward += self.DetermineUniqueAristocratRewards(Action)
                Reward += self.DetermineCardRewards (Action)
                # Only update Dataframe for non-pass actions
                if Action[0] != ACTION_PASS :
                    self.Action_Dataframe.at[StateIndex, ActionCol] += Reward
                    
                    if self.Action_Dataframe.loc[StateIndex, ActionCol] < BRAIN_MIN_ACTION_VALUE :
                        self.Action_Dataframe.at[StateIndex, ActionCol] = BRAIN_MIN_ACTION_VALUE
                    if self.Action_Dataframe.loc[StateIndex, ActionCol] > BRAIN_MAX_ACTION_VALUE :
                        self.Action_Dataframe.at[StateIndex, ActionCol] = BRAIN_MAX_ACTION_VALUE
            return
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
            
#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Select Best Action Functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    def DetermineStateIndex (self, CurrentRound, EndOfGame):
        
        Round_Index = CurrentRound - 1
        
        if Round_Index > 5 :
            Round_Index = 5
        
        if EndOfGame == True :
            Round_Index = 6
        
        #df_CurrentState = BRAIN_ROUNDS[Round_Index] + BRAIN_PHASES[CurrentPhase]
        df_CurrentState = BRAIN_ROUNDS[Round_Index]
        
        return df_CurrentState
    
    
    def DetermineActionCol (self, Action):
               
        try :
            Current_Action = ACTIONS[Action[0]][1]
    
            if Action[0] == ACTION_BUY :
                if Action[3] == True :
                    Unique = "-Unique"
                else:
                    Unique = ""
                    
                if Action [2] == PLAYER_HELD_CARD :
                    df_CurrentAction = Current_Action + '-' + ACTIONS[ACTION_HOLD][1] + '-' + Action[1].CardName + Unique
                else :
                    df_CurrentAction = Current_Action + '-' + Action[1].CardName + Unique
            
            if Action[0] == ACTION_HOLD:
                if Action[2] == True :
                    Unique = "-Unique"
                else :
                    Unique = ""    
                df_CurrentAction = Current_Action + '-' + Action[1].CardName + Unique
            
            if Action[0] == ACTION_UPGRADE :
                if Action[3] == True :
                    Unique = "-Unique"
                else :
                    Unique = ""              
                
                if Action[2] == PLAYER_HELD_CARD :
                    df_CurrentAction = Current_Action + '-' + ACTIONS[ACTION_HOLD][1] + '-' + Action[1][0].CardName + '-' + Action[1][1].CardName + Unique
                else :
                    df_CurrentAction = Current_Action + '-' + Action[1][0].CardName + '-' + Action[1][1].CardName + Unique
                
            
            if Action[0] == ACTION_OBSERVATORY :
                df_CurrentAction = Current_Action + '-' + CARD_TYPES[Action[1]][1]       
    
            if Action[0] == ACTION_PUB :
                df_CurrentAction = Current_Action + '-' + str(Action[1])  
                
            if Action[0] == ACTION_PASS :
                df_CurrentAction = Current_Action
    
            #print (df_CurrentAction)
            
            return df_CurrentAction
        
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
    
    def DetermineActionRewards(self, Actions, CurrentRound, EndOfGame):
        
        try :
            Action_Rewards = []
            State_Index = self.DetermineStateIndex(CurrentRound, EndOfGame)
            
            
            for Action in Actions :
                ActionCol = self.DetermineActionCol(Action)
                Reward = self.Action_Dataframe.loc[State_Index, ActionCol]
                Action_Rewards.append([Reward, Action])
                #print (State_Index, ActionCol, Reward)
            
            return Action_Rewards
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
            
    def SelectBestAction (self, Actions, CurrentRound, CurrentPhase, EndOfGame):
        
        try:
            Action_Rewards = self.DetermineActionRewards(Actions, CurrentRound, EndOfGame)
            #print (Action_Rewards)
            Action_Reward_Indexes = []
            for Action_Reward in Action_Rewards :
                Action_Reward_Indexes.append(Action_Reward[0])
            
            Best_Action_Index = numpy.argwhere(Action_Reward_Indexes == numpy.amax(Action_Reward_Indexes))
            
            explore = numpy.random.binomial(1, self.epsilon)
            
            if explore == 1 :
                # Explore
                BestAction = Actions [randint(0, len(Actions)-1)]
            else :
                # Exploit
                
                Best_Action_Index = Best_Action_Index.flatten().tolist()
                Best_Action_Index = Best_Action_Index [randint(0, len(Best_Action_Index)-1)]
                BestAction = Actions[Best_Action_Index]
                #BestAction = Actions [Best_Action_Index]
            
            return BestAction  
        
        except :
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2].tb_lineno))
    