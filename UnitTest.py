'''
Created on Aug 25, 2021

@author: mikes
'''
from Game import *
from Card import *
from Contents import WORKER_CARD_TYPE

new_game = Game (1)
new_game.GameSetup()
new_game.DealCards(WORKER_CARD_TYPE)


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