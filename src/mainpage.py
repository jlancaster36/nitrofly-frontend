# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NFtest.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# from assets import asiimov_rc
# import buttons_rc
import os
import pathlib
import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl, QSize

from customWidgets import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{border-image: url(assets/asiimov2.png);}")
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.consoleSelect = QtWidgets.QFrame(self.centralwidget)
        self.consoleSelect.setMaximumSize(QtCore.QSize(100, 16777215))
        self.consoleSelect.setStyleSheet("#consoleSelect{"
        "background-color: rgba(0,0,0,.6);"
        "border: 0;}")
        self.consoleSelect.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.consoleSelect.setFrameShadow(QtWidgets.QFrame.Raised)
        self.consoleSelect.setObjectName("consoleSelect")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.consoleSelect)
        self.verticalLayout.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        #Setting up Console Select scroll Area
        self.scrollArea_2 = QtWidgets.QScrollArea(self.consoleSelect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setStyleSheet("background: transparent;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 72, 77))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setStyleSheet(
                        "QPushButton{qproperty-icon: url(assets/buttons/add-icon.png);}" 
                        "QPushButton::hover {background-color : rgba(0, 0, 0, .5);}")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # self.pushButton.clicked.connect(lambda: self.setup_video(r"/Fire Emblem - Awakening (USA) Decrypted.mp4"))
        self.verticalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignVCenter)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_2, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addWidget(self.consoleSelect)

        self.gameSelect = QtWidgets.QFrame(self.centralwidget)
        self.gameSelect.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameSelect.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameSelect.setObjectName("gameSelect")
        self.gameSelect.setStyleSheet("border:0;")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gameSelect)

        self.verticalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.subtoolbar = QtWidgets.QFrame(self.gameSelect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtoolbar.sizePolicy().hasHeightForWidth())
        self.subtoolbar.setSizePolicy(sizePolicy)
        self.subtoolbar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.subtoolbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.subtoolbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subtoolbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subtoolbar.setObjectName("subtoolbar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.subtoolbar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.hideConsoles = QtWidgets.QPushButton(self.subtoolbar)
        self.hideConsoles.setStyleSheet("qproperty-icon: url(assets/buttons/white-menu.png);\n"
"background-color: transparent;")
        self.hideConsoles.setText("")
        self.hideConsoles.setIconSize(QtCore.QSize(24, 24))
        self.hideConsoles.setObjectName("hideConsoles")

        self.horizontalLayout_5.addWidget(self.hideConsoles)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.settings = QtWidgets.QPushButton(self.subtoolbar)
        self.settings.setStyleSheet("qproperty-icon: url(assets/buttons/cog.png);\n"
"background: transparent;")
        self.settings.setText("")
        self.settings.setIconSize(QtCore.QSize(24, 24))
        self.settings.setObjectName("settings")

        self.horizontalLayout_5.addWidget(self.settings)
        self.files = QtWidgets.QPushButton(self.subtoolbar)
        self.files.setStyleSheet("background: transparent;\n"
"qproperty-icon: url(assets/buttons/file-icon.png);")
        self.files.setText("")
        self.files.setIconSize(QtCore.QSize(24, 24))
        self.files.setObjectName("files")
        self.horizontalLayout_5.addWidget(self.files)

        self.emulators = QtWidgets.QPushButton(self.subtoolbar)
        self.emulators.setStyleSheet("background: transparent;\n"
"qproperty-icon: url(assets/buttons/menu-rounded.png);")
        self.emulators.setText("")
        self.emulators.setIconSize(QtCore.QSize(24, 24))
        self.emulators.setObjectName("emulators")
        self.horizontalLayout_5.addWidget(self.emulators)

        self.verticalLayout_3.addWidget(self.subtoolbar,1)
        self.gameMarquee = QtWidgets.QFrame(self.gameSelect)
        self.gameMarquee.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gameMarquee.setAutoFillBackground(False)
        self.gameMarquee.setStyleSheet("#gameMarquee{\n"
"    background-color: rgba(0,0,0, .6);\n"
"}")
        self.gameMarquee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameMarquee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gameMarquee.setObjectName("gameMarquee")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gameMarquee)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftText = QtWidgets.QFrame(self.gameMarquee)
        self.leftText.setStyleSheet("border-imageurl:(assets/buttons/GCNicon.png);\n"
"background-repeat: no-repeat;\n"
"")
        self.leftText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftText.setObjectName("leftText")
        self.horizontalLayout.addWidget(self.leftText,3)
        self.media = QtWidgets.QFrame(self.gameMarquee)
        self.media.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.media.setFrameShadow(QtWidgets.QFrame.Raised)
        self.media.setObjectName("media")
        self.media.setStyleSheet("border:0;")
        self.horizontalLayout.addWidget(self.media,4)

        self.rightText = QtWidgets.QFrame(self.gameMarquee)
        self.rightText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightText.setObjectName("rightText")
        self.horizontalLayout.addWidget(self.rightText,3)

        self.verticalLayout_3.addWidget(self.gameMarquee,3)
        self.scrollArea = QtWidgets.QScrollArea(self.gameSelect)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("background:transparent;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 683, 365))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.gameGrid = QtWidgets.QGridLayout()
        self.gameGrid.setObjectName("gameGrid")
        self.verticalLayout_2.addLayout(self.gameGrid)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea,6)
        self.horizontalLayout_3.addWidget(self.gameSelect)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        ###### Imported video code
        
        path = os.path.dirname(os.path.abspath(__file__)) + "/metadata/3DSmedia/videos/Pokemon Alpha Sapphire (USA) (En,Ja,Fr,De,Es,It,Ko) (Rev 2) Decrypted.mp4"
        # fileName = "C:/Projects/ROM DUMP/3DS/3DSmedia/videos/Pokemon Alpha Sapphire (USA) (En,Ja,Fr,De,Es,It,Ko) (Rev 2) Decrypted.mp4"
        fileName = path
        print(path)
        # path = "/Users/lancaster/Documents/Nitrofly/nitrofly-frontend/src/test.mp4"

        # if fileName != '':
        #     self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
        #     self.mediaPlayer.play()

        self.label_setup()

        self.vidWrapperLayout = QVBoxLayout()
        self.video_setup()
        self.pushButton.clicked.connect(self.videos.resizeContent)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def breath_button(self, button):
        # anim = QtCore.QPropertyAnimation(button, b"geomtery")
        # anim.setDuration(100)
        # anim.setStartValue(QtCore.QRect(awidth=32, aheight=32))
        # anim.setEndValue(QtCore.QRect(awidth=48, aheight=48))
        # anim.start()

        # anim = QtCore.QPropertyAnimation(button, b"geomtery")
        # anim.setDuration(100)
        # anim.setStartValue(QtCore.QRect(awidth=48, aheight=48))
        # anim.setEndValue(QtCore.QRect(awidth=32, aheight=32))
        # anim.start()
        pass

    def slide(self):
        pass

    def populate_consoles(self):
        pass
    
    def populate_gallery(self, filter):
        pass

    def add_click(self, button):
        print("Add Clicked")
        self.breath_button(button)

    # def setup_video(self, fileName):
    #     path = QDir.currentPath() + "/metadata/videos"
    #     if fileName != '':
    #         print(path + fileName)
    #         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path + fileName)))
    #         self.mediaPlayer.play()

    def video_setup(self):
        self.media.setLayout(self.vidWrapperLayout)
        self.videos = VideoPlayer()
        self.vidWrapperLayout.addWidget(self.videos)
        # self.videos.hide()

    def label_setup(self):
        self.ltWrapperLayout = QVBoxLayout()
        self.leftText.setLayout(self.ltWrapperLayout)
        self.mediaLabel = QLabel()
        self.mediaLabel.setText("Text")
        self.ltWrapperLayout.addWidget(self.mediaLabel)

        self.rtWrapperLayout = QVBoxLayout()
        self.rightText.setLayout(self.rtWrapperLayout)
        self.rtLabel = QLabel()
        self.rtLabel.setText("Moree")
        self.rtWrapperLayout.addWidget(self.rtLabel)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.showMaximized()
    # t = threading.Thread(target = ui.videos.resizeContent)
    # t.start()
    sys.exit(app.exec_())