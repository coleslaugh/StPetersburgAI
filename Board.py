'''
Created on Aug 25, 2021

@author: mikes
'''

from MainWindow import Ui_MainWindow
import sys

from PyQt5.Qt import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

from Game import Game
from Contents import (  WORKER_CARD_TYPE, PHASE_WORKER,
                        BUILDING_CARD_TYPE, PHASE_BUILDING,
                        ARISTOCRAT_CARD_TYPE, PHASE_ARISTOCRAT,
                        TRADING_CARD_TYPE, PHASE_TRADING)


class Board(Ui_MainWindow):

    def __init__(self):        
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        super().setupUi(self.MainWindow)
        self.btnStart.clicked.connect(self.ButtonClick)
             
      
    def Display(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())
    
    def ButtonClick (self):
        
        #self.label_3.SetText("clicked")
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
            # Delete this line when running the game
            new_game.EndOfGame = True
                
                
if __name__ == "__main__":
    GameBoard = Board()
    GameBoard.Display()
    