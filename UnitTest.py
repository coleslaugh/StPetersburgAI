'''
Created on Aug 25, 2021

@author: mikes
'''
from Card import Card
from Player import Player
from Game import Game

from Contents import *





if __name__ == '__main__':
    
    New_Game = Game (1)
    New_Game.CreatePlayers ()
    
    
    New_Game.Players[0].Hand.append(Card (CARPENTER_WORKSHOP_CARD))
    New_Game.Players[0].Hand.append(Card (GOLD_SMELTER_CARD))
    New_Game.Players[0].Hand.append(Card (SHIP_BUILDER_CARD))
    New_Game.Players[0].Hand.append(Card (SHEPHERD_CARD))
    New_Game.Players[0].Hand.append(Card (GOLD_MINER_CARD))
    New_Game.Players[0].Hand.append(Card (CUSTOMS_HOUSE_CARD))
    New_Game.Players[0].Hand.append(Card (LIBRARY_CARD))
    New_Game.Players[0].Hand.append(Card (LUMBERJACK_CARD))
    New_Game.Players[0].Hand.append(Card (SECRETARY_CARD))
    New_Game.Players[0].Hand.append(Card (CONTROLLER_CARD))
    
    New_Game.CardsInPlay.append(Card (FUR_TRAPPER_CARD))
    New_Game.CardsInPlay.append(Card (LUMBERJACK_CARD))
    New_Game.CardsInPlay.append(Card (GOLD_MINER_CARD))
    New_Game.CardsInPlay.append(Card (CUSTOMS_HOUSE_CARD))
    New_Game.CardsInPlay.append(Card (CUSTOMS_HOUSE_CARD))
    New_Game.CardsInPlay.append(Card (SECRETARY_CARD))
    New_Game.CardsInPlay.append(Card (CONTROLLER_CARD))
    New_Game.CardsInPlay.append(Card (SHEPHERD_CARD))
    
    New_Game.CardsInPlay[0].Row = BOARD_UPPER_ROW
    New_Game.CardsInPlay[1].Row = BOARD_UPPER_ROW
    New_Game.CardsInPlay[2].Row = BOARD_LOWER_ROW
    New_Game.CardsInPlay[3].Row = BOARD_UPPER_ROW
    New_Game.CardsInPlay[4].Row = BOARD_LOWER_ROW
    New_Game.CardsInPlay[5].Row = BOARD_UPPER_ROW
    New_Game.CardsInPlay[6].Row = BOARD_LOWER_ROW
    New_Game.CardsInPlay[7].Row = BOARD_LOWER_ROW
    
    CardsInPlay_PlayerCosts = New_Game.Players[0].DetermineCardCosts(New_Game.CardsInPlay)
    
    for Card in CardsInPlay_PlayerCosts :
        print ("Card Name - " + Card.CardName + " : New Card Cost - "+ str(Card.CardCost))
    
    
    
    
    
    
    
    TestPlayer = Player

