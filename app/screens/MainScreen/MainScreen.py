import sys
import os
import time
import psutil

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QFont, QPixmap                              # For Fonts
from PyQt5.QtCore import Qt, QTimer, QTime, QSize, pyqtSignal       # For alignment


''' ERROR FILE HANDLING '''
from file_handling import file_handling

''' IMPORT AUTH FOLDER HERE '''
from auth.SessionManager import SessionManager

class MainScreen(QtWidgets.QWidget):
    switch_screen_signal = pyqtSignal(int)  # Using Signals and Slots for decoupling approach
    
    def __init__(self, parent=None, SESSION_MANAGER=None):
        super().__init__(parent)
        self.auth = SESSION_MANAGER
        self.MainScreen()
        
    def MainScreen(self): 
        central_Widget = QWidget()
        central_Widget.setObjectName("central_Widget")
        layout = QVBoxLayout(central_Widget)
        layout.setObjectName("layout")
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        #self.main_window.setCentralWidget(central_Widget)
        
        ''' HEAD WIDGET ''' 
        # USES SPACE BETWEEN
        HEADER_widget = QWidget()
        HEADER_layout = QHBoxLayout()
        HEADER_widget.setLayout(HEADER_layout)
        HEADER_widget.setObjectName("HEADER_widget")
        HEADER_widget.setFixedHeight(57)
        
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        #self.time_label = QLabel("00:00")
        self.time_label = QLabel("00:00 AM")
        self.time_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.time_label.setObjectName("TIME_LABEL")
        
        #left_widget = QLabel("Left")
        self.LOCATION_UNIQUE_ID = QLabel("Battery:")
        self.LOCATION_UNIQUE_ID.setObjectName("LOCATION_UNIQUE_ID")
        self.LOCATION_UNIQUE_ID.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        LOCATION_UNIQUE_ID_layout = QVBoxLayout() 
        LOCATION_UNIQUE_ID_widget = QWidget()
        LOCATION_UNIQUE_ID_widget.setFixedWidth(230)
        LOCATION_UNIQUE_ID_widget.setFixedHeight(48)

        LOCATION_UNIQUE_ID_widget.setObjectName("LOCATION_UNIQUE_ID_widget")
        LOCATION_UNIQUE_ID_layout.addWidget(self.LOCATION_UNIQUE_ID)
        #LOCATION_UNIQUE_ID_layout.addWidget(BATTERY_LIFE)
        LOCATION_UNIQUE_ID_widget.setLayout(LOCATION_UNIQUE_ID_layout)
        
        HEADER_layout.addWidget(self.time_label)
        #HEADER_layout.addItem(spacer)  # The spacer will push left and right widgets apart
        HEADER_layout.addWidget(LOCATION_UNIQUE_ID_widget)
        
        HEADER_layout.setContentsMargins(10, 0, 10, 0)
        HEADER_layout.setSpacing(0)
        
        layout.addWidget(HEADER_widget)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.batteryLife()
        
        ''' BODY WIDGET '''
        BODY_widget = QWidget()
        BODY_layout = QVBoxLayout()
        BODY_layout.setContentsMargins(0, 0, 0, 0)
        BODY_layout.setSpacing(0)
        BODY_widget.setLayout(BODY_layout)
        BODY_widget.setObjectName("BODY_widget")
        
        # CURTAIN HEADER HERE
        CURTAINS_TOP_widget = QWidget()
        CURTAINS_TOP_widget.setObjectName("CURTAINS_TOP_widget")
        CURTAINS_TOP_layout = QHBoxLayout()
        CURTAINS_TOP_layout.setContentsMargins(-0, 0, 20, 0)
        CURTAINS_TOP_layout.setSpacing(0)
        CURTAINS_TOP_widget.setFixedHeight(45)
        CURTAINS_TOP_widget.setLayout(CURTAINS_TOP_layout)
        
        # TERMINAL_TITLE
        TERMINAL_TITLE = QLabel("Terminal")
        TERMINAL_TITLE.setObjectName("TERMINAL_TITLE")
        TERMINAL_TITLE.setAlignment(Qt.AlignCenter)
        TERMINAL_TITLE_widget = QWidget()
        TERMINAL_TITLE_layout = QVBoxLayout()
        TERMINAL_TITLE_layout.addWidget(TERMINAL_TITLE)
        TERMINAL_TITLE_layout.setContentsMargins(0, 0, 0, 0)
        TERMINAL_TITLE_layout.setSpacing(0)
        TERMINAL_TITLE_widget.setFixedWidth(300)
        TERMINAL_TITLE_widget.setLayout(TERMINAL_TITLE_layout)
        TERMINAL_TITLE_widget.setObjectName("TERMINAL_TITLE_widget")
        CURTAINS_TOP_layout.addWidget(TERMINAL_TITLE_widget)
        
        # QUEUEING PASSENGERS
        QUEUEING_PASSENGERS = QLabel("Queueing Passengers")
        QUEUEING_PASSENGERS.setObjectName("QUEUEING_PASSENGERS")
        QUEUEING_PASSENGERS.setAlignment(Qt.AlignCenter)
        QUEUEING_PASSENGERS_widget = QWidget()
        QUEUEING_PASSENGERS_layout = QVBoxLayout()
        QUEUEING_PASSENGERS_layout.addWidget(QUEUEING_PASSENGERS)
        QUEUEING_PASSENGERS_layout.setContentsMargins(0, 0, 0, 0)
        QUEUEING_PASSENGERS_layout.setSpacing(0)
        QUEUEING_PASSENGERS_widget.setFixedWidth(300)
        QUEUEING_PASSENGERS_widget.setLayout(QUEUEING_PASSENGERS_layout)
        QUEUEING_PASSENGERS_widget.setObjectName("QUEUEING_PASSENGERS_widget")
        CURTAINS_TOP_layout.addWidget(QUEUEING_PASSENGERS_widget)
        
        
        
        CURTAINS_BOTTOM_widget = QWidget()
        CURTAINS_BOTTOM_widget.setObjectName("CURTAINS_BOTTOM_widget")
        CURTAINS_BOTTOM_widget.setFixedHeight(45)
        
        
        # TODO: Put destination here
        BODY_main_content_widget = QWidget()
        BODY_main_content_widget.setObjectName("BODY_main_content_widget")
        BODY_main_content_layout = QVBoxLayout()
        BODY_main_content_widget.setLayout(BODY_main_content_layout)
        BODY_main_content_layout.setAlignment(Qt.AlignTop)
        BODY_main_content_layout.setContentsMargins(0, 0, 0, 0)

        
        # TODO: MAKE THE INDIVIDUAL ROWS
        ######################## DUMMY CONTENT HERE ########################

        # FOR NOW, DATA IS PRELOADED
        self.dummyData = {"SAS": 2, "SAFAD": 3, "SOE": 3, "PORTAL": 7}

        """ ROW ELEMENT """
        INFO_ROW_1_widget = QWidget()
        INFO_ROW_1_widget.setObjectName("INFO_ROW_1_widget")
        INFO_ROW_1_layout = QHBoxLayout()
        INFO_ROW_1_layout.setContentsMargins(-0, 0, 20, 0)
        INFO_ROW_1_layout.setSpacing(0)
        INFO_ROW_1_widget.setFixedHeight(45)
        INFO_ROW_1_widget.setLayout(INFO_ROW_1_layout)
        
        # TERMINAL TITLE
        TERMINAL_TITLE_N1 = QLabel("SAS")  # Number 
        TERMINAL_TITLE_N1.setObjectName("TERMINAL_TITLE_N1")
        TERMINAL_TITLE_N1.setAlignment(Qt.AlignCenter)
        TERMINAL_TITLE_N1_widget = QWidget()
        TERMINAL_TITLE_N1_layout = QVBoxLayout()
        TERMINAL_TITLE_N1_layout.addWidget(TERMINAL_TITLE_N1)
        TERMINAL_TITLE_N1_layout.setContentsMargins(0, 0, 0, 0)
        TERMINAL_TITLE_N1_layout.setSpacing(0)
        TERMINAL_TITLE_N1_widget.setFixedWidth(300)
        TERMINAL_TITLE_N1_widget.setLayout(TERMINAL_TITLE_N1_layout)
        TERMINAL_TITLE_N1_widget.setObjectName("TERMINAL_TITLE_widget")
        INFO_ROW_1_layout.addWidget(TERMINAL_TITLE_N1_widget)        # TODO: ADD TO INDEPENDENT ROW
        
        # QUEUEING PASSENGERS
        QUEUEING_PASSENGERS_N1 = QLabel("3")     # Number of queuing passengers
        QUEUEING_PASSENGERS_N1.setObjectName("QUEUEING_PASSENGERS_N1")
        QUEUEING_PASSENGERS_N1.setAlignment(Qt.AlignCenter)
        QUEUEING_PASSENGERS_N1_widget = QWidget()
        QUEUEING_PASSENGERS_N1_layout = QVBoxLayout()
        QUEUEING_PASSENGERS_N1_layout.addWidget(QUEUEING_PASSENGERS_N1)
        QUEUEING_PASSENGERS_N1_layout.setContentsMargins(0, 0, 0, 0)
        QUEUEING_PASSENGERS_N1_layout.setSpacing(0)
        QUEUEING_PASSENGERS_N1_widget.setFixedWidth(300)
        QUEUEING_PASSENGERS_N1_widget.setLayout(QUEUEING_PASSENGERS_N1_layout)
        QUEUEING_PASSENGERS_N1_widget.setObjectName("QUEUEING_PASSENGERS_N1_widget")
        INFO_ROW_1_layout.addWidget(QUEUEING_PASSENGERS_N1_widget)      # TODO: ADD TO INDEPENDENT ROW
        
        
        for key, value in self.dummyData.items():
            #print(f"Key: {key}, Value: {value}")
            print("Hello world")




        
        BODY_main_content_layout.addWidget(INFO_ROW_1_widget)       # TODO: Add info rows here
        
        
        BODY_layout.addWidget(CURTAINS_TOP_widget)
        BODY_layout.addWidget(BODY_main_content_widget)
        BODY_layout.addWidget(CURTAINS_BOTTOM_widget)
        
        layout.addWidget(BODY_widget)
        
        ''' BOTTOM WIDGET '''
        BOTTOM_widget = QWidget()
        BOTTOM_layout = QHBoxLayout()
        BOTTOM_layout.setContentsMargins(20, 0, 20, 0)
        BOTTOM_layout.setSpacing(0)
        BOTTOM_widget.setLayout(BOTTOM_layout)
        BOTTOM_widget.setObjectName("BOTTOM_widget")
        BOTTOM_widget.setFixedHeight(100)
        
        BOTTOM_widget_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # PROFILE
        PROFILE_widget = QWidget()
        PROFILE_widget.setObjectName("PROFILE_widget")
        PROFILE_layout = QHBoxLayout()
        PROFILE_widget.setLayout(PROFILE_layout)
        PROFILE_widget.setFixedWidth(572)
        PROFILE_layout.setSpacing(10)
        
        
        USERICON_label = QLabel("Novell")
        USERICON_label_pixmap = QPixmap("assets/images/Icon-Image.png")
        USERICON_scaled_pixmap = USERICON_label_pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        USERICON_label.setPixmap(USERICON_scaled_pixmap)
        USERICON_label.setScaledContents(True)
        USERICON_label.setFixedWidth(100)
        
        # PROFILE-CONTAINER
        PROFILECONTAINER_widget = QWidget()
        PROFILECONTAINER_widget.setObjectName("PROFILECONTAINER_widget")
        PROFILECONTAINER_layout = QVBoxLayout()
        PROFILECONTAINER_layout.setContentsMargins(0, 0, 0, 0)
        
        self.DRIVERNAME_label = QLabel("#")       # TODO: Uncomment this
        #DRIVERNAME_label = QLabel(self.auth.get_current_username())
        #DRIVERNAME_label.setFixedWidth(30)
        self.DRIVERNAME_label.setObjectName("DRIVERNAME_label")
        
        #SHUTTLE_label = QLabel("Shuttle Dashboard 1")
        self.SHUTTLE_label = QLabel("--")
        #SHUTTLE_label.setFixedWidth(30)
        self.SHUTTLE_label.setObjectName("SHUTTLE_label")
        
        
        #self.updateMainScreen() # TODO: This is a dummy
        
        
        PROFILECONTAINER_layout.addWidget(self.DRIVERNAME_label)
        PROFILECONTAINER_layout.addWidget(self.SHUTTLE_label)
        
        PROFILECONTAINER_widget.setLayout(PROFILECONTAINER_layout)
        
        PROFILE_layout.addWidget(USERICON_label)
        PROFILE_layout.addWidget(PROFILECONTAINER_widget)
        
        
        # LOGOUT BUTTON
        
        LOGOUT_widget = QWidget()
        LOGOUT_widget.setObjectName("LOGOUT_widget")
        LOGOUT_layout = QVBoxLayout()
        LOGOUT_layout.setAlignment(Qt.AlignRight)
        LOGOUT_widget.setLayout(LOGOUT_layout)

        
        self.LOGOUT_button = QPushButton()
        self.LOGOUT_button.setObjectName("LOGOUT_button")
        LOGOUT_icon = QIcon("assets/icons/Logout")
        self.LOGOUT_button.setIcon(LOGOUT_icon)
        self.LOGOUT_button.setIconSize(QSize(32, 32))
        self.LOGOUT_button.setText(" Logout")
        self.LOGOUT_button.setStyleSheet("padding: 10px;")
        self.LOGOUT_button.setFixedWidth(160)
        self.LOGOUT_button.setFixedHeight(60)
        self.LOGOUT_button.clicked.connect(self.on_LOGOUT_button_clicked)
        
        self.clicked_buttons = set() # Keep track of clicked buttons
        
        LOGOUT_layout.addWidget(self.LOGOUT_button)
        
        BOTTOM_layout.addWidget(PROFILE_widget)
        #BOTTOM_layout.addItem(BOTTOM_widget_spacer)
        BOTTOM_layout.addWidget(LOGOUT_widget)
        layout.addWidget(BOTTOM_widget)
        
        stylesheet = file_handling.load_stylesheet("screens/MainScreen/MainScreen.css")
        #central_Widget.setStyleSheet(stylesheet)
        self.setStyleSheet(stylesheet)
        
        self.setLayout(layout)
        
    
    def update_time(self):
        #current_time = QTime.currentTime().toString("hh:mm:ss")
        current_time = QTime.currentTime().toString("hh:mm AP")
        self.time_label.setText(current_time)
        
              
    def on_LOGOUT_button_clicked(self):
        print("Hello World")
        #self.auth.logout()                     # 
        #self.switch_screen_signal.emit(0)      # TODO
        
        self.switch_screen_signal.emit(2)       # TODO: Make changes here later
        
        # THIS STATE WILL THE BUTTON PERPETUALLY ACTIVE
        '''
        if self.LOGOUT_button not in self.clicked_buttons:
            self.LOGOUT_button.setStyleSheet("#LOGOUT_button { background-color: red; }")
            self.clicked_buttons.add(self.LOGOUT_button)
        else:
            self.LOGOUT_button.setStyleSheet("#LOGOUT_button { background-color: lightgray; }")
            self.clicked_buttons.remove(self.LOGOUT_button)
        '''
        
    def batteryLife(self):
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                status = "Charging" if battery.power_plugged else "Discharging"
                #self.LOCATION_UNIQUE_ID.setText(f"Battery: {percent:.0f}% ({status})")
                self.LOCATION_UNIQUE_ID.setText(f"Battery Life: {percent:.0f}%")
            else:
                self.LOCATION_UNIQUE_ID.setText("Battery info not available.")
        except Exception as e:
            self.LOCATION_UNIQUE_ID.setText(f"Error: {e}")
        
    def __update__(self):       # Trigger update
        print("Screen Updated!")
        ''' DRIVERNAME_label, SHUTTLE_label'''
        #self.DRIVERNAME_label.setText(self.auth.get_current_username())
        self.DRIVERNAME_label.setText(self.auth.get_AppInfo("_username"))
        self.SHUTTLE_label.setText(self.auth.get_AppInfo("_shuttleName"))
        print("Update MainScreen")


    # TODO
    # In the body_content_widget, the elements background must appear in a [#FFFFFF, #C0C0C0, #FFFFFF, #C0C0C0, ...] manner
    # Make a function to automatically fetch data from database upon login
    # Make a function that automatically updates number of passenger if there are changes from the evTrak
