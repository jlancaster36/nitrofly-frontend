# Sys is always needed
import sys
# QtCore will be needed for some slider properties
from PyQt5.QtCore import Qt
# QtWidgets includes many typical objects
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout,
                             QLineEdit, QLabel, QRadioButton,
                             QSpinBox, QSlider)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NITROFLY EMULATION FRONTEND')

        settingsBar = QHBoxLayout()
        settingsButton = QPushButton("Settings")
        # settingsButton.setStyleSheet
        settingsButton.clicked(self.settings())

        
    def settings(self):
        print("Gathering Metadata...")
        

if __name__ == '__main__':
    # Always include the following code to initialize your application.
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())