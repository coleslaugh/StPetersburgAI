'''
Created on Aug 25, 2021

@author: mikes
'''
from Game import *
from Card import *
from Contents import *

new_game = Game (1)


new_game.GameSetup()


while not new_game.EndOfGame :
    
    new_game.DealCards(WORKER_CARD_TYPE)
    new_game.ProcessPhaseActions(PHASE_WORKER)
    new_game.ProcessPhaseScoring(PHASE_WORKER)
    
    new_game.DealCards (BUILDING_CARD_TYPE)
    new_game.ProcessPhaseActions(PHASE_BUILDING)
    new_game.ProcessPhaseScoring(PHASE_BUILDING)
    
    new_game.DealCards (ARISTOCRAT_CARD_TYPE)
    new_game.ProcessPhaseActions(PHASE_ARISTOCRAT)
    new_game.ProcessPhaseScoring(PHASE_ARISTOCRAT)
    
    new_game.DealCards (TRADING_CARD_TYPE)
    new_game.ProcessPhaseActions(PHASE_TRADING)
    
    new_game.RotateCards ()
    new_game.RotatePlayers ()
    
    
    
    
    

print("Displaying Player Order")

print(new_game.Players[0].Marker)
print(new_game.Players[1].Marker)
print(new_game.Players[2].Marker)
print(new_game.Players[3].Marker)

'''
print("Displaying Worker Deck")
for x in range (len(new_game.WorkerDeck.Cards)) :
    print (new_game.WorkerDeck.Cards[x].CardOrder, new_game.WorkerDeck.Cards[x].CardName)   
print("Displaying Building Deck")
for x in range (len(new_game.BuildingDeck.Cards)) :
    print (new_game.BuildingDeck.Cards[x].CardOrder, new_game.BuildingDeck.Cards[x].CardName)   
print("Displaying Aristocrat Deck")
for x in range (len(new_game.AristocratDeck.Cards)) :
    print (new_game.AristocratDeck.Cards[x].CardOrder, new_game.AristocratDeck.Cards[x].CardName)   

print("Displaying Cards in Play")    
for x in range (len(new_game.CardsInPlay)) :
    print (new_game.CardsInPlay[x].CardName)
    '''   