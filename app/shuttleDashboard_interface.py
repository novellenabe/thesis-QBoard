# python -m venv .venv
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon, QMouseEvent
from PyQt5.QtGui import QFont, QPixmap          # For Fonts
from PyQt5.QtCore import Qt, pyqtSignal                    # For alignment

''' ERROR FILE HANDLING '''
from file_handling import file_handling


''' IMPORT SCREENS HERE '''
from screens.LoadingScreen.LoadingScreen import LoadingScreen
from screens.LoginScreen.LoginScreen import LoginScreen
from screens.MainScreen.MainScreen import MainScreen
from screens.LogoutScreen.LogoutScreen import LogoutScreen

import time

''' IMPORT AUTH FOLDER HERE '''
from auth.SessionManager import SessionManager

''' SETUP VARIABLES '''
screen_width = 1024
screen_height = 518

#TODO: CHANGE shuttleDashboard to Qboard when finished
#TODO: TODO FETCH DATA HERE 

class MainWindow(QtWidgets.QMainWindow):
    loadingChanged = pyqtSignal(bool)
    #screenChanged = pyqtSignal(int)
    
    updateMainScreen = pyqtSignal(bool)
    
    def __init__(self):
        super().__init__()
        
        self.auth = SessionManager("1", "evTrak")   # USER AUTHENTICATION HERE
                
        self._isLoading = False # LOADING STATE HERE
        
        self.setWindowTitle("Shuttle Dashboard")
        self.setGeometry(700, 300, screen_width, screen_height) 
        self.setWindowIcon(QIcon("assets/icons/profile.png"))
        

        #self.setStyleSheet("background-color: white; border: 10px solid #50A747;")     # GOAL: REMOVE THIS AND INITIALIZE THIS IN THE FILE

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        #self.loading_screen = LoadingScreen(self)
        #self.login_screen = LoginScreen(self, self.isLoading)
        self.login_screen = LoginScreen(self, SESSION_MANAGER=self.auth)
        self.main_screen = MainScreen(self, SESSION_MANAGER=self.auth)
        self.logout_screen = LogoutScreen(self, SESSION_MANAGER=self.auth)
        #self.loading_screen = LoadingScreen(self)   # TO BE MADE
        
        self.main_screen.switch_screen_signal.connect(self.swtich_to_screen)
        
        #TODO: You can remove this later
        #self.loadingChanged.connect(self.login_screen.updateLoadingState)               # IMPORTANT
        self.login_screen.switch_screen_signal.connect(self.swtich_to_screen)
        self.logout_screen.switch_screen_signal.connect(self.swtich_to_screen)
        
        self.auth.loggedIn.connect(self.update_MainScreen_Content)        
        #self.screenChanged.connect(self.login_screen.changeScreen)                      # TEST
        
        # --- NEW: Connect current changed signal to detect screen loads ---
        # TODO: Write code here
        
        # Connect session maanger signal to update UI
        #self.auth.loggedIn.connect(self.update_ui_on_login)
        #self.auth.loggedOut.connect(self.update_ui_on_logout)
        
        
        # SCREEN STACK HERE [login, main, logout]
        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.main_screen)
        self.stacked_widget.addWidget(self.logout_screen)
        
        
        
        # NOTE: Connect currentChanged signal to detect screen loads
        self.stacked_widget.currentChanged.connect(self.on_screen_changed)
        
        self.swtich_to_screen(0)    # INITIAL RENDER. CHANGE VALUE
        
        
        #self.showFullScreen()
        
    # TODO: Create on_screen_changed
    
    def update_MainScreen_Content(self):
        print("Hello World")
    
    '''
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            #self.setStyleSheet("")
            #self.isLoading = True
            #self.swtich_to_screen(1)    
            #time.sleep(3)
            #self.isLoading = True
            print("PRESSED")
    '''
    
    # This function will go to another screen
    def swtich_to_screen(self, index):
        self.stacked_widget.setCurrentIndex(index)
    
    # This function will detect if the screen is being changed
    def on_screen_changed(self, index):
        current_widget = self.stacked_widget.widget(index)     # TODO: Un-comment this to make dynamic
        
        #current_widget = self.stacked_widget.widget(1)          # Update trigger currently only set to MainScreen.py
        
        if isinstance(current_widget, QtWidgets.QWidget): # Ensure it's one of our custom screens
            print(f"MainWindow: Detected screen change to index {index} ({current_widget.__class__.__name__})")
            #current_widget.on_show() # Call the screen's specific loading/refresh logic
            current_widget.__update__()
        else:
            print(f"MainWindow: Screen at index {index} is not a BaseScreen instance.")
            
    
    ''' ================================================ '''
    '''
    @property
    def isLoading(self):
        print("Property")
        return self._isLoading
        
        
    @isLoading.setter
    def isLoading(self, value): 
        print("setter")
        if self._isLoading != value:
            print("OK!")
            self._isLoading = value
            self.loadingChanged.emit(self._isLoading)
            #self.screenChanged.emit(1)
    '''
     
    '''
    self.login_screen = LoginScreen(self, self._isLoading)
    self.loadingChanged.connect(self.login_screen.updateLoadingState)
    '''
    
    ''' ================================================ '''
    
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()