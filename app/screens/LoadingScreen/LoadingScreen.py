import sys
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QPixmap          # For Fonts
from PyQt5.QtCore import Qt                     # For alignment

''' ERROR FILE HANDLING '''
from file_handling import *

class LoadingScreen():      
    def __init__(self, main_window):
        self.main_window = main_window
    
    def LoadingScreen(self):    
        central_Widget = QWidget()
        self.main_window.setCentralWidget(central_Widget)
        
        
        label1 = QLabel("#1", central_Widget)
        label2 = QLabel("#2", central_Widget)
        label3 = QLabel("#3", central_Widget)
        label4 = QLabel("#4", central_Widget)
        label5 = QLabel("#5", central_Widget)
       
        
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)
        
        central_Widget.setLayout(grid)
        
        stylesheet = file_handling.load_stylesheet("screens/LoadingScreen/LoadingScreen.css")
        central_Widget.setStyleSheet(stylesheet)