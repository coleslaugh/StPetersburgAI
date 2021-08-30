'''
Created on Aug 25, 2021

@author: mikes
'''

from MainWindow import Ui_MainWindow
import sys
from PyQt5.Qt import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

class Board(object):

    def __init__(self):
        
        #self.app = QApplication(sys.argv)
        #self.MainWindow = QMainWindow
        #self.GameBoard = Ui_MainWindow()
        #self.GameBoard.setupUi(self.MainWindow)

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
      
    def Display(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())
    
        