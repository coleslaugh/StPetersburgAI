'''
Created on Sep 14, 2021

@author: mikes
'''
from random import randint
import pandas as pd
import numpy as numpy
import sys

from Contents import WORKER_CARDS, ACTIONS, ACTION_BUY, DECKS, TRADING_CARDS,\
    WORKER_CARD_TYPE, CLASS_ALL, MAX_POINTS_TO_BUY, BRAIN_DEFAULT_VALUE,\
    BRAIN_ROUNDS, BRAIN_PHASES, ACTION_HOLD, ACTION_UPGRADE, ACTION_OBSERVATORY,\
    ACTION_PUB, ACTION_PASS, BRAIN_EPSILON, PHASE_BUILDING, PHASE_ARISTOCRAT,\
    LUMBERJACK_CARD, POPE_CARD, AUTHOR_CARD, CARD_TYPES, PHASE_WORKER, PLAYERS,\
    BRAIN_TARGET_SCORE, BRAIN_REWARD_BANDS, BRAIN_PASS_DEFAULT_VAULE,\
    BRAIN_TARGET_SCORE_INCREMENT, BRAIN_TARGET_SCORE_INCREMENT_INTERVAL
    


from Card import Card



class Brain (object):

    def __init__(self, PLayerID):
        self.PlayerID = PLayerID
        self.indexes = []
        self.cols = []
        self.Action_Dataframe = []
        self.epsilon = 0
        self.epsilon_max = 0
        self.epsilon_min =0
        self.target_score = 0
        self.rewards_bands = 0
        self.rewards_increment = 0
        self.penalty_bands = 0
        self.penalty_increment = 0

        self.LoadBrain()
      
    def InitializeBrain (self, epsilon, epsilon_increment, epsilon_max, epsilon_min, target_score, reward_bands, reward_increment, penalty_bands, penalty_increment):
        self.epsilon = epsilon
        self.epsilon_increment = epsilon_increment
        self.epsilon_max = epsilon_max
        self.epsilon_min = epsilon_min
        self.target_score = target_score
        self.rewards_bands = reward_bands
        self.rewards_increment = reward_increment
        self.penalty_bands = penalty_bands
        self.penalty_increment = penalty_increment
        return 
    
    def UpdateTargetScore (self, target_score, reward_bands, reward_increment, penalty_bands, penalty_increment):
        self.target_score = target_score
        self.rewards_bands = reward_bands
        self.rewards_increment = reward_increment
        self.penalty_bands = penalty_bands
        self.penalty_increment = penalty_increment
        
    def UpdateEpsilon (self, epsilon, epsilon_max, epsilon_min):
        
        if epsilon >= epsilon_max :
            self.epsilon = epsilon_max
        else :
            self.epsilon = epsilon 
        
        if epsilon <= epsilon_min :
            self.epsilon = epsilon_min
        else :
            self.epsilon = epsilon

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Data Frame Initialization functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def InitializeActionDataFrame (self):
        self.GetNamedIndexes()
        self.GetColumns()
        self.Action_Dataframe = pd.DataFrame(BRAIN_DEFAULT_VALUE, index=self.indexes, columns=self.cols)
        self.SetDefaultValues ()
    
    def SetDefaultPassValue (self):
        self.Action_Dataframe[ACTIONS[ACTION_PASS][1]] = BRAIN_PASS_DEFAULT_VAULE
        #ACTIONS[ACTION_PASS][1]

    
    def SetDefaultValues (self) :
        self.SetDefaultPassValue ()
    
    def GetNamedIndexes (self):
        Phase_Index = BRAIN_PHASES
        Round_Index = BRAIN_ROUNDS

        for round_num in Round_Index :
            for phase in Phase_Index :
                self.indexes.append(round_num + phase)
        
        print (self.indexes)

        
    def GetBuyColumns (self):
    
        for Deck in DECKS :
            if Deck[0] != TRADING_CARDS :
                for Card in Deck[0] :
                    c = ACTIONS[ACTION_BUY][1] + "-" + Card[0]['Name']
                    self.cols.append(c)

  
    def GetHoldColumns (self):
    
        for Deck in DECKS :
            for Card in Deck[0] :
                c = ACTIONS[ACTION_HOLD][1] + "-" + Card[0]['Name']
                self.cols.append(c)

    def GetUpgradeColumns (self):
        for TradingCard in TRADING_CARDS :
            for Deck in DECKS :
                if Deck[0] != TRADING_CARDS :
                    for TargetCard in Deck[0] :
                        if (TradingCard[0]['Class'] == TargetCard[0]['Class']) or (TradingCard[0]['Card Type'] == WORKER_CARD_TYPE and TargetCard[0]['Class'] == CLASS_ALL) :
                            c = ACTIONS[ACTION_UPGRADE][1] + "-" + TradingCard[0]['Name'] + "-" + TargetCard[0]['Name']
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
        self.GetHoldColumns()
        self.GetUpgradeColumns()
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

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Update Brain Functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    def UpdateRewards (self, ActionsTaken, FinalScore):
        
        Reward = 0
        
        if FinalScore == self.target_score :
            Reward = 0
        if FinalScore > self.target_score :
            Reward = self.rewards_increment
        if FinalScore > self.target_score + self.rewards_bands :
            Reward = 2 * self.rewards_increment
        if FinalScore > self.target_score + (2 * self.rewards_bands) :
            Reward = 3 * self.rewards_increment
        
        '''if FinalScore < self.target_score :
            Reward = self.penalty_increment
        if FinalScore < self.target_score - self.penalty_bands :
            Reward = 2 * self.penalty_increment'''
        if FinalScore < self.target_score - (2 * self.penalty_bands) :
            Reward = 3 * self.penalty_increment
        
        for ActionTaken in ActionsTaken :
        
            Action = ActionTaken[0]
            Round = ActionTaken[1]
            Phase = ActionTaken[2]
            EndOfGame = ActionTaken[3]
        
            StateIndex = self.DetermineStateIndex(Round, Phase, EndOfGame)
            ActionCol =  self.DetermineActionCol(Action)
            
            if Action[0] != ACTION_PASS :
                self.Action_Dataframe.at[StateIndex, ActionCol] += Reward
                if self.Action_Dataframe.loc[StateIndex, ActionCol] < 0 :
                    self.Action_Dataframe.at[StateIndex, ActionCol] = 0
                if self.Action_Dataframe.loc[StateIndex, ActionCol] > 100 :
                    self.Action_Dataframe.at[StateIndex, ActionCol] = 100
        return

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# Select Best Action Functions
#----------------------------------------------------------------------------------------------------------------------------------------------------------
    def DetermineStateIndex (self, CurrentRound, CurrentPhase, EndOfGame):
        
        Round_Index = CurrentRound - 1
        
        if Round_Index > 5 :
            Round_Index = 5
        
        if EndOfGame == True :
            Round_Index = 6
        
        df_CurrentState = BRAIN_ROUNDS[Round_Index] + BRAIN_PHASES[CurrentPhase]
        
        return df_CurrentState
    
    
    def DetermineActionCol (self, Action):
        #ACTIONS = [[ACTION_BUY, "Buy"], [ACTION_HOLD, "Hold"], [ACTION_PASS, "Pass"],[ACTION_UPGRADE, "Upgrade"],[ACTION_OBSERVATORY, "Observatory"], [ACTION_PUB, "Use the Pub"] ]
        
        Current_Action = ACTIONS[Action[0]][1]

        if Action[0] == ACTION_BUY or Action[0] == ACTION_HOLD:
            df_CurrentAction = Current_Action + '-' + Action[1].CardName
        
        if Action[0] == ACTION_UPGRADE :
            df_CurrentAction = Current_Action + '-' + Action[1][0].CardName + '-' + Action[1][1].CardName
        
        if Action[0] == ACTION_OBSERVATORY :
            df_CurrentAction = Current_Action + '-' + CARD_TYPES[Action[1]][1]       

        if Action[0] == ACTION_PUB :
            df_CurrentAction = Current_Action + '-' + str(Action[1])  
            
        if Action[0] == ACTION_PASS :
            df_CurrentAction = Current_Action

        #print (df_CurrentAction)
        
        return df_CurrentAction

    
    def DetermineActionRewards(self, Actions, CurrentRound, CurrentPhase, EndOfGame):
        
        Action_Rewards = []
        State_Index = self.DetermineStateIndex(CurrentRound, CurrentPhase, EndOfGame)
        
        
        for Action in Actions :
            ActionCol = self.DetermineActionCol(Action)
            Reward = self.Action_Dataframe.loc[State_Index, ActionCol]
            Action_Rewards.append([Reward, Action])
            #print (State_Index, ActionCol, Reward)
        
        return Action_Rewards
    
    def SelectBestAction (self, Actions, CurrentRound, CurrentPhase, EndOfGame):
        
        Action_Rewards = self.DetermineActionRewards(Actions, CurrentRound, CurrentPhase, EndOfGame)
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
    
    
if __name__ == "__main__":

    my_brain= Brain (1)
    my_brain.SaveBrain()
    
    Actions = []
    Card1 = Card(LUMBERJACK_CARD)
    TradingCard = Card (POPE_CARD)
    TargetCard = Card (AUTHOR_CARD)
    
    CardPair = [TradingCard, TargetCard]
    
    
    
   
    Actions.append([ACTION_BUY, Card1])
    Actions.append([ACTION_HOLD, Card1])
    Actions.append([ACTION_UPGRADE, CardPair])
    Actions.append([ACTION_OBSERVATORY, WORKER_CARD_TYPE])
    Actions.append([ACTION_PUB, 3])
    Actions.append([ACTION_PASS])
    
    my_brain.SelectBestAction(Actions, 3, PHASE_WORKER, False)
    my_brain.SaveBrain()
    
    #my_brain.DetermineStateIndex(8, PHASE_ARISTOCRAT, True)
    
    #my_brain.DetermineActionCol([ACTION_BUY, my_card])
    #my_brain.DetermineActionCol([ACTION_HOLD, my_card])
    #my_brain.DetermineActionCol([ACTION_UPGRADE, CardPair])
    
    #my_brain.DetermineActionCol([ACTION_OBSERVATORY, WORKER_CARD_TYPE])
    #my_brain.DetermineActionCol([ACTION_PUB, 3])
    #my_brain.DetermineActionCol([ACTION_PASS])
    
    
    #value = my_brain.Action_Dataframe.loc['3W','Buy-Lumber Jack']
    #mylist = list(value.split(","))
    #print (int(mylist[0])+1)
    #my_brain.Action_Dataframe.at['3W','Buy-Lumber Jack'] = 25
    #my_brain.Action_Dataframe.at['3W','Buy-Lumber Jack'] += 25
    #my_brain.SaveBrain()
    #print(df.loc['2W','B1'])
    #print (my_brain.Action_Dataframe)
    