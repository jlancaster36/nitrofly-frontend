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
import sys
import subprocess
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QDir, Qt, QUrl, QSize

from customWidgets import *
from userData import *

import ctypes
myappid = u'NitroK.Nitrofly.Frontend.0.5' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

sys.dont_write_bytecode = True

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Nitrofly")
        MainWindow.resize(800, 600)
        MainWindow.setWindowIcon(QIcon(r"assets\NF Logo NC.png"))
        self.MainWindow = MainWindow
        

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
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setStyleSheet("background: transparent;")
        #May change later to just hide scrollbar
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        # self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 72, 77))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setStyleSheet(
                        "QPushButton{qproperty-icon: url(assets/buttons/add-icon.png);}" 
                        "QPushButton::hover {background-color : rgba(0, 0, 0, .5);}")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.verticalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignVCenter)

        ####################

        self.populate_consoles()
        ####################

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
        self.files.setStyleSheet(
            "QPushButton{qproperty-icon: url(assets/buttons/file-icon.png);}" 
            "QPushButton::hover {background-color : rgba(0, 0, 0, .5);}")
        self.files.setText("")
        self.files.setIconSize(QtCore.QSize(24, 24))
        self.files.setObjectName("files")
        self.files.clicked.connect(self.selectRomDir)
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
        self.horizontalLayout.addWidget(self.rightText,2)

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
        self.gameGrid.setOriginCorner(0)
        
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
        
        path = os.path.dirname(os.path.abspath(__file__)) + "/metadata/3DS/videos/Pokemon Alpha Sapphire (USA) (En,Ja,Fr,De,Es,It,Ko) (Rev 2) Decrypted.mp4"
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
        self.populate_gallery()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


    def populate_consoles(self):
        self.consoleButtons = {}
        with open("userData/consoles.json") as file:
            consoles = json.load(file)
        
        for c in consoles.keys():
            if consoles[c]["active"] != True:
                continue
            
            btn = ConsoleButton(c ,self.scrollAreaWidgetContents)
            self.verticalLayout_4.addWidget(btn, 0, QtCore.Qt.AlignVCenter)
            btn.clicked.connect(self.filterGallery)
            self.consoleButtons[c] = btn
        
        print(self.consoleButtons)
    
    # TODO: implement console/handheld filter
    def populate_gallery(self, filter = None):
        self.galleryButtons = {}
        with open("userData/roms.json") as file:
            gallery = json.load(file)
        
        #Had to be made global to manage grid in other functions
        self.row = 0
        self.col = 0
        for item in [i for i in gallery.keys()]:
            self.newbtn = GalleryButton(item, self.getMarquee(), self.scrollAreaWidgetContents_2)
            self.gameGrid.addWidget(self.newbtn, self.row, self.col, Qt.AlignLeft)
            # self.gameGrid.addWidget(self.newbtn)
            self.newbtn.clicked.connect(self.newbtn.getRomName)
            self.galleryButtons[item] = self.newbtn
            #TODO: QT wants to stretch widgets when you don't add to specific row
            # Find a way to set number of cols dynamicly without breaking everything.
            # Right now on a larger screen there's a ton of empty space            
            self.col += 1
            if self.col % 5 == 0:
                self.row += 1
                self.col = 0
    
    def filterGallery(self):
        system = self.MainWindow.sender().system
        print(f"filtering by {system}")
        for k in self.galleryButtons.keys():
            if self.galleryButtons[k].system != system:
                self.galleryButtons[k].hide()
            else:
                self.galleryButtons[k].show()

    def add_click(self, button):
        print("Add Clicked")
        self.breath_button(button)

    def video_setup(self):
        self.media.setLayout(self.vidWrapperLayout)
        self.videos = VideoPlayer()
        self.vidWrapperLayout.addWidget(self.videos)
        # self.videos.hide()

    def label_setup(self):
        self.ltWrapperLayout = QVBoxLayout()
        self.leftText.setLayout(self.ltWrapperLayout)
        self.mediaLabel = ResizingLabel(w)
        self.mediaLabel.setText("Select a Game")
        
        ## BELOW IS HOW TO GET NATIVE RESOLUTION
        # screen = app.primaryScreen()
        # size = screen.size()
        # print(size.width(), size.height())

        self.mediaLabel.setStyleSheet('color: rgb(255,255,255); font: Arial')
        self.ltWrapperLayout.addWidget(self.mediaLabel)

        self.rtWrapperLayout = QVBoxLayout()
        self.rightText.setLayout(self.rtWrapperLayout)
        self.rtLabel = QLabel()
        self.rtLabel.setText("Moree")
        self.rtWrapperLayout.addWidget(self.rtLabel)
    
    def getMarquee(self):
        return (self.mediaLabel, self.rtLabel, self.videos)

    def selectRomDir(self):
        selectDirectory(self)
        # FIXME: Populate gallery does not erase the old buttons when repopulating with new rom data
        oldGallery = self.galleryButtons.keys()
        self.softPopulate(oldGallery)
        self.populate_gallery()
    
    # Adds only new elements to gallery given old Gallery keys
    # TODO: Rewrite the orginal populate gallery function so that we dont need this
    def softPopulate(self, oldGallery):
        with open("userData/roms.json") as file:
            gallery = json.load(file)
        
        for item in [i for i in gallery.keys()]:
            if item not in oldGallery:
                self.newbtn = GalleryButton(item, self.getMarquee(), self.scrollAreaWidgetContents_2)
                self.gameGrid.addWidget(self.newbtn, self.row, self.col, Qt.AlignLeft)
                # self.gameGrid.addWidget(self.newbtn)
                self.newbtn.clicked.connect(self.newbtn.getRomName)
                self.galleryButtons[item] = self.newbtn
                #TODO: QT wants to stretch widgets when you don't add to specific row
                # Find a way to set number of cols dynamicly without breaking everything.
                # Right now on a larger screen there's a ton of empty space            
                self.col += 1
                if self.col % 5 == 0:
                    self.row += 1
                    self.col = 0



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    # t = threading.Thread(target = ui.videos.resizeContent)
    # t.start()
    sys.exit(app.exec_())