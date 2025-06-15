from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QFont, QPixmap, QMouseEvent                    # For Fonts
from PyQt5.QtCore import Qt, QTimer, QTime, QSize, pyqtSignal       # For alignment


''' ERROR FILE HANDLING '''
from file_handling import file_handling


''' IMPORT AUTH FOLDER HERE '''
from auth.SessionManager import SessionManager


# This logout screen will display "Thank you {drivername}" then will go back to the loginscreen
class LogoutScreen(QtWidgets.QWidget):
    switch_screen_signal = pyqtSignal(int)  # Using Signals and Slots for decoupling approach

    def __init__(self, parent=None, SESSION_MANAGER=None):
        super().__init__(parent)
        self.loadStyles()
        self.auth = SESSION_MANAGER
        self.LogoutScreen()
        
    def loadStyles(self):
        stylesheet = file_handling.load_stylesheet("screens/LogoutScreen/LogoutScreen.css")
        self.setStyleSheet(stylesheet)
    
    def LogoutScreen(self):
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
        
        
        # LOGOUT MESSAGE HERE
        self.dashboard_logout_label = QLabel("#####")     # TODO: Must display loggeed in name here
        self.dashboard_logout_label.setObjectName("dashboard_logout")
        self.dashboard_logout_label.setAlignment(Qt.AlignCenter)
        self.MIDDLE_layout.addWidget(self.dashboard_logout_label)
        
        
        #self.refreshWidgets()
        #self.updateMiddleWidget(self.isLoading)        # TODO: Needs fixing


        self.CENTRAL_LAYOUT.addWidget(self.MIDDLE_widget)
        
        ''' BOTTOM WIDGET '''
        BOTTOM_layout = QVBoxLayout()
        BOTTOM_widget = QWidget()
        BOTTOM_widget.setLayout(BOTTOM_layout)
        BOTTOM_widget.setObjectName("bottom_widget")
        BOTTOM_widget.setFixedHeight(100)
        self.CENTRAL_LAYOUT.addWidget(BOTTOM_widget)     # PUSH
        
        
        self.setLayout(SELF_LAYOUT)
        
    def changeScreen(self):     # GO BACK TO LOGIN SCREEN
        print("CHANGE SCREEN")
        self.switch_screen_signal.emit(0)
        
    # TODO: Wait 5 seconds. Change this later to a while loop until all transactions are OK!
    def __update__(self):
        print("LogoutScreen")
        self.dashboard_logout_label.setText(f"Thank you for your session {self.auth.get_AppInfo("_username")}")
        print("Screen Updated!")


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            ''' DUMMY LOGOUT HERE '''
            print("Logout Screen Pressed")
            self.auth.logout()     # LOGOUT HERE
            self.changeScreen()