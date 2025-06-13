# python -m venv .venv
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QPixmap          # For Fonts
from PyQt5.QtCore import Qt                     # For alignment



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shuttle Dashboard")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon("assets/icons/profile.png"))
        
        
        #self.label_1 = QLabel("Hello Word", self)
        
        #label = QLabel("Hello", self)
        #label.setFont(QFont("Arial", 30))
        #label.setGeometry(0, 0, 500, 100)
        #label.setStyleSheet("color: blue; background-color: red;")
        
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignVCenter)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignHCenter) 
        
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        
        #image = QLabel(self)
        #image.setGeometry(0, 0, 500, 500)
        
        #pixmap = QPixmap("assets/icons/profile.png")
        #image.setPixmap(pixmap)
        #image.setScaledContents(True)
        
        #self.initUI()
        
        # RADIO GROUPS
        #self.radio1 = QRadioButton("Visa", self)
        #self.radio2 = QRadioButton("MasterCard", self)
        #self.radio3 = QRadioButton("Gift Card", self)
        
        #self.radio4 = QRadioButton("In-Store", self)
        #self.radio5 = QRadioButton("Online", self)
        #self.radio6 = QRadioButton("Later", self)
        
        #self.button_group1 = QButtonGroup(self)
        #self.button_group2 = QButtonGroup(self)
        
        #self.checkBox = QCheckBox("Do you like food?", self)    # CHECKBOX
        
        #self.checkBox.setChecked(False)
        #self.checkBox.stateChanged.connect(self.checkBox_changed)   # Connect CheckBox with function
        
        #self.initUIPushButton()
        #self.QRadioButtonUI()
        
        self.line_edit = QLineEdit(self)            # TEXT BOX
        self.button = QPushButton("Submit", self)
        self.lineEditUI()
        
    
    def lineEditUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(210, 10, 100, 40)
        self.button.setStyleSheet("font-size: 25px; font-family: Arial;")
        self.line_edit.setStyleSheet("font-size: 25px; font-family: Arial;")
    
        self.line_edit.setPlaceholderText("Enter your name")
        
        self.button.clicked.connect(self.submit)
    
    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")
        #print("You Clicked The Button")
    
    def QRadioButtonUI(self): 
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        self.radio6.setGeometry(0, 250, 300, 50)
        
        self.setStyleSheet("QRadioButton{""font-size: 40px; font-family: Arial; padding: 10px""}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        self.button_group2.addButton(self.radio6)
        
        
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        
    
    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")
    
    def initUIPushButton(self):
        self.checkBox.setGeometry(0, 0, 500, 100)
        self.checkBox.setStyleSheet("font-size:30px; font-family: Arial;")
    
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) 
        
        self.label_1.setGeometry(150, 300, 200, 100)
        self.label_1.setStyleSheet("font-size: 50px;")
    
    def on_click(self):
        print("Button Clicked!")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        
        self.label_1.setText("Goodbye")
    
    def initUI(self):
        central_Widget = QWidget()
        self.setCentralWidget(central_Widget)
        
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        
        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        
        # Vertical Display
        
        #vbox = QVBoxLayout()
        #
        #vbox.addWidget(label1)
        #vbox.addWidget(label2)
        #vbox.addWidget(label3)
        #vbox.addWidget(label4)
        #vbox.addWidget(label5)
        #
        #central_Widget.setLayout(vbox)
        
        # Horizontal Display
        
        #hbox = QHBoxLayout()
        #hbox.addWidget(label1)
        #hbox.addWidget(label2)
        #hbox.addWidget(label3)
        #hbox.addWidget(label4)
        #hbox.addWidget(label5)
        #
        #central_Widget.setLayout(hbox)
        
        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)
        grid.addWidget(label5, 1, 2)
        
        central_Widget.setLayout(grid)
        
    def checkBox_changed(self, state):
        if state == Qt.Checked:
            print("You Like Food")
        else:
            print("You Do Not Like Food")    

    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()