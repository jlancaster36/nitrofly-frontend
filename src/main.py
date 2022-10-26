# Sys is always needed
import sys
from PyQt6.QtCore import Qt
# QtWidgets includes many typical objects
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QLineEdit, QLabel, QRadioButton,
                             QSpinBox, QSlider, QMainWindow,
                             QMenu)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NITROFLY EMULATION FRONTEND')

        # settings = self.addToolBar("Settings")
        # help = self.addToolBar("Help")

        mainBox = QVBoxLayout()
        
        settingsBar = QHBoxLayout()
        settingsButton = QPushButton("Settings")
        # settingsButton.setStyleSheet
        settingsButton.clicked.connect((self.settings))
        settingsBar.addWidget(settingsButton)

        mainWidget = QWidget()
        mainWidget.setLayout(settingsBar)
        self._createMenuBar()
        self.setCentralWidget(mainWidget)

    def settings(self):
        print("Gathering Metadata...")

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu(" &File", self)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu(" &Edit")
        helpMenu = menuBar.addMenu(" &Help")

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())