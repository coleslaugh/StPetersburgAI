#----------------------------------------------------------------------------------------------------------------------------------------------------------
# St. Petersburg Machine Learning Simulation
# Author: Mike Slaugh
# Version 1.0 10/9/2021
#----------------------------------------------------------------------------------------------------------------------------------------------------------

import sys

from Board import Board
from PyQt5 import QtWidgets
                       
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    GameBoard = Board()
    GameBoard.setupUi(MainWindow)
    GameBoard.SetupBoard()
    GameBoard.btnStart.clicked.connect(GameBoard.StartButtonClick)  
    MainWindow.show()
    app.exec()