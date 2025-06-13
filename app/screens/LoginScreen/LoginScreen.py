import sys
import os
import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap, QMovie, QMouseEvent
from PyQt5.QtGui import QFont                   # For Fonts
from PyQt5.QtCore import Qt, QTimer, pyqtSignal         # For alignment

''' ERROR FILE HANDLING '''
from file_handling import file_handling

''' IMPORT AUTH FOLDER HERE '''
from auth.SessionManager import SessionManager


class LoginScreen(QtWidgets.QWidget):    
    switch_screen_signal = pyqtSignal(int)  # Using Signals and Slots for decoupling approach
    
    def __init__(self, parent=None, initialLoading=False, SESSION_MANAGER=None):
        super().__init__(parent)
        self.loadStyles()
        self.GIF_LOADING_LABEL = None # Initialize to None. For GIF Label
        self.isLoading = initialLoading
        self.auth = SESSION_MANAGER
        self.LoginScreen()
    
    def loadStyles(self):
        stylesheet = file_handling.load_stylesheet("screens/LoginScreen/LoginScreen.css")
        self.setStyleSheet(stylesheet)
    
    def LoginScreen(self):
        ''' PARENT LAYOUT ''' 
        SELF_LAYOUT = QVBoxLayout()   
        SELF_LAYOUT.setSpacing(0)
        SELF_LAYOUT.setContentsMargins(0, 0, 0, 0)
        
        
        self.CENTRAL_WIDGET = QWidget()
        self.CENTRAL_WIDGET.setObjectName("CENTRAL_WIDGET")
        self.CENTRAL_LAYOUT = QVBoxLayout(self.CENTRAL_WIDGET)   

        self.CENTRAL_LAYOUT.setContentsMargins(0, 0, 0, 0)
        self.CENTRAL_LAYOUT.setSpacing(0)

        SELF_LAYOUT.addWidget(self.CENTRAL_WIDGET)
        
        ''' TOP WIDGET '''
        # DISPALY UNIVERSITY IMAGE
        UNIVERSITY_LABEL = QLabel(self.CENTRAL_WIDGET)
        UNIVERSITY_LABEL.setFixedHeight(145)
        UNIVERSITY_LABEL.setObjectName("university_title")
        UNIVERSITY_LABEL_pixmap = QPixmap("assets/images/USC_logo.png")
        scaled_pixmap = UNIVERSITY_LABEL_pixmap.scaled(500, 1000, Qt.KeepAspectRatio)
        #UNIVERSITY_LABEL.setPixmap(UNIVERSITY_LABEL_pixmap)
        UNIVERSITY_LABEL.setPixmap(scaled_pixmap)
        UNIVERSITY_LABEL.setAlignment(Qt.AlignCenter)
        self.CENTRAL_LAYOUT.addWidget(UNIVERSITY_LABEL)  # PUSH
        
        
        ''' MIDDLE WIDGET '''
        self.MIDDLE_layout = QVBoxLayout()
        self.MIDDLE_widget = QWidget()
        self.MIDDLE_widget.setFixedHeight(131)
        self.MIDDLE_widget.setLayout(self.MIDDLE_layout)
        self.MIDDLE_widget.setObjectName("MIDDLE_widget")   
        
        #self.refreshWidgets()
        self.updateMiddleWidget(self.isLoading)


        self.CENTRAL_LAYOUT.addWidget(self.MIDDLE_widget)
        
        ''' BOTTOM WIDGET '''
        BOTTOM_layout = QVBoxLayout()
        BOTTOM_widget = QWidget()
        BOTTOM_widget.setLayout(BOTTOM_layout)
        BOTTOM_widget.setObjectName("bottom_widget")
        BOTTOM_widget.setFixedHeight(100)
        self.CENTRAL_LAYOUT.addWidget(BOTTOM_widget)     # PUSH
        
        
        self.setLayout(SELF_LAYOUT)
        
        #self.update()
        
    def updateMiddleWidget(self, isLoading):
        if isLoading == True:
            self.refreshWidgets()
            print("Is Loading")
            self.GIF_LOADING_LABEL = QLabel()
            self.loading("assets/gif/loading.gif")
            self.MIDDLE_layout.addWidget(self.GIF_LOADING_LABEL, alignment=Qt.AlignCenter)
            
            QTimer.singleShot(2000, self.changeScreen)  #   TEMPORARY TIMER FOR LOADING, ACTS AS SIMULATION
            #self.changeScreen()

        else:
            self.refreshWidgets()
            print("Is Not Loading")
            # DISPALY SHUTTLE 1 DASHBOARD
            dashboard_title_label = QLabel("Shuttle 1 Dashboard")
            dashboard_title_label.setObjectName("dashboard_title")
            dashboard_title_label.setAlignment(Qt.AlignCenter)
            self.MIDDLE_layout.addWidget(dashboard_title_label)
            
            # DISPLAY PLACE YOUR ID IN THE DRIVER READER
            dashboard_subtext_label = QLabel("Place your driver ID in the reader")
            dashboard_subtext_label.setObjectName("DASHBOARD_subtext")
            dashboard_subtext_label.setAlignment(Qt.AlignCenter)
            self.MIDDLE_layout.addWidget(dashboard_subtext_label)

        print("END")
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.isLoading = True
            
            ''' DUMMY LOGIN HERE '''
            self.auth.login("admin", "password123", "SHUTTLE 1")     # LOGIN HERE. ONLY DUMMY
            self.updateMiddleWidget(self.isLoading)

    def refreshWidgets(self):
        print(f"Initial Widget Count: {self.MIDDLE_layout.count()}")

        # Iterate in reverse to safely remove items
        # Also, check if the item contains a widget and delete it
        while self.MIDDLE_layout.count() > 0:
            item = self.MIDDLE_layout.takeAt(0) # Use takeAt(0) to remove from the beginning
            if item.widget():
                widget = item.widget()
                # Stop any GIF movies before deleting the label
                if isinstance(widget, QLabel) and hasattr(widget, '_movie') and widget._movie:
                    widget._movie.stop()
                    widget._movie = None # Clear the movie reference
                widget.deleteLater() # Schedule for deletion
            del item # Delete the layout item itself

        print(f"Updated Widget Count: {self.MIDDLE_layout.count()}")
        # After clearing, also ensure the GIF_LOADING_LABEL reference is cleared if it was the one removed
        if self.GIF_LOADING_LABEL is not None and self.GIF_LOADING_LABEL.parent() is None:
            self.GIF_LOADING_LABEL = None
    
        
    def loading(self, path):
        self.LOADING = QMovie(path)
        self.GIF_LOADING_LABEL.setMovie(self.LOADING)
        self.LOADING.start()
              
    # TODO: Once this function is exectuted, data at MainScreen.py must be refreshed
    def changeScreen(self):
        print("CHANGE SCREEN")
        self.isLoading = False
        self.updateMiddleWidget(self.isLoading)
        self.GIF_LOADING_LABEL = None # Re-initialize to None. For GIF Label
        #self.DRIVERNAME_label.setText("Hello World")
        self.switch_screen_signal.emit(1) 
        
        
    def __update__(self):       # Trigger update
        print("Screen Updated!")    
        