'''
Created on Aug 25, 2021

@author: mikes
'''
import sys

from Board import Board
from PyQt5 import QtWidgets
                       

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Author: Mike Slaugh
#----------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    GameBoard = Board()
    GameBoard.setupUi(MainWindow)
    GameBoard.SetupBoard()
    GameBoard.btnStart.clicked.connect(GameBoard.StartButtonClick)  
    MainWindow.show()
    app.exec()