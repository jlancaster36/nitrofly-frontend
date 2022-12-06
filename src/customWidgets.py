import sys
from enum import Enum
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import glob
import os
import json
import math


class Console(Enum):
    SNES = 1
    N64  = 2
    GCN  = 3
    WII  = 4
    GBA  = 5
    NDS  = 6
    DS3  = 7
    PSP  = 8
    PS1  = 9
    PS2  = 10

class GalleryImage(Enum):
    BOX3D = "box3d"
    BOX2D = "box2d"
    SUPPORT = "support"
    VIDEO = "videos"


# class PicButton(QButtons.QAbstractButton):
#     def __init__(self, pixmap, parent=None):
#         super(PicButton, self).__init__(parent)
#         self.pixmap = pixmap

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawPixmap(event.rect(), self.pixmap)

#     def sizeHint(self):
#         return self.pixmap.size()

# Example Instance:
#   button = PicButton(QPixmap("image.png"))


# Add console emulators to persistent data
def addNewConsole(console: Console):
    pass

# Add Roms from a directory
def addNewRoms():
    pass


class ConsoleButton(QtWidgets.QPushButton):
    def __init__(self, system, parent = None) -> None:

        self.system = system
        super().__init__(parent)

        with open("userData/consoles.json", "r") as file:
            consoles = json.load(file)

        imagePath = consoles[system]["image"]
        self.setImage(imagePath)
        print (f"creating button for  {self.system}")

    def setImage(self, imagePath: str):
        self.setStyleSheet(
            "QPushButton{qproperty-icon: url("+ imagePath +");}" 
            "QPushButton::hover {background-color : rgba(0, 0, 0, .5);}")
        
        self.setIconSize(QSize(48, 48))
        pass
    
    def getSystem(self):
        return self.system
    
    def filter(self):
        print("Filtering by " + self.system)


class VideoPlayer(QWidget):

    def __init__(self, parent:QWidget = None):
        super(VideoPlayer, self).__init__(parent)
        self.parent = parent
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoItem = QGraphicsVideoItem()

        # aspectRatio = float(parent.geometry().width()) / float(parent.geometry().height())
        # normFactor = aspectRatio * (.75)
        self.videoItem.setSize(QSizeF(800, 600))


        # self.videoItem.setSize(QSizeF(parent.geometry().width(), parent.geometry().height()))
        self.scene = QGraphicsScene(self)
        self.graphicsView = QGraphicsView(self.scene)
        self.graphicsView.fitInView(self.videoItem, Qt.KeepAspectRatio)
        bounds = QRectF(self.scene.sceneRect())
        self.graphicsView.centerOn(bounds.center())

        self.scene.addItem(self.videoItem)
        layout = QVBoxLayout()
        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
        self.mediaPlayer.setVideoOutput(self.videoItem)
        self.counter = 0
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.resizeContent()

    # def play(self, path="C:/Projects/ROM DUMP/3DS/3DSmedia/videos/Pokemon Alpha Sapphire (USA) (En,Ja,Fr,De,Es,It,Ko) (Rev 2) Decrypted.mp4"):
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         pass
    #     else:
    #         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
    #         self.mediaPlayer.play()
    #         self.counter += 1
    
    def play(self, path: str):
        print("PLAYING FROM " + path)
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            pass
        else:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            self.mediaPlayer.play()
            self.counter += 1
    
    def resizeContent(self):
        # self.show()
        bounds = QRectF(self.scene.sceneRect())
        self.graphicsView.fitInView(self.videoItem, Qt.KeepAspectRatio)
        # self.videoItem.setSize(QSizeF(self.parent.geometry().width(), self.parent.geometry().height()))
        self.graphicsView.centerOn(bounds.center())


        # self.play()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.graphicsView.fitInView(self.videoItem, Qt.KeepAspectRatio)

class GalleryButton(QtWidgets.QPushButton):
    def __init__(self, name, marq: tuple[QLabel, QLabel, VideoPlayer], parent = None) -> None:
        super().__init__(parent)

        with open("userData/roms.json", "r") as file:
            self.romData = json.load(file)

        self.name = name
        self.system = self.romData[name]["system"]
        self.paths = {
            GalleryImage.BOX3D: f"metadata/{self.system}/box3d",
            GalleryImage.BOX2D: f"metadata/{self.system}/box2dfront",
            GalleryImage.SUPPORT: f"metadata/{self.system}/support"
        }
        self.marq = marq
        self.setImage()
        print (f"creating button for  {self.name}")

    def setImage(self, type: GalleryImage = GalleryImage.BOX2D):
        if self.romData[self.name][type.value] == False:
            #TODO: ADD Default art
            print(f"Metadata for {type} : {self.name} not found, setting default")
            return
        
        path     = self.paths[type] + "/" + self.name + ".png"
        suppPath = self.paths[GalleryImage.SUPPORT] + "/" + self.name + ".png"
        # print('setting supprot path: ' + suppPath)

        self.setStyleSheet(
            "QPushButton{"
                "border-image: url("+path+");"
                "background-repeat: no-repeat;"
                "width: 128px;"
                "height: 128px;"
                "}" 
            "QPushButton::hover {"
                # "background-color : rgba(0, 0, 0, .5);"
                "border-image: url("+suppPath+");"
                "}")
        self.sizePolicy().setHorizontalStretch(0)

        self.setIconSize(QSize(128, 128))
    
    def getRomName(self):
        print(self.name)
        return self.name
    
    # Single fuction to load preview metadata when rom is selected
    def selected(self):
        print("Hovering over " + self.name)
        pass
        
    def enterEvent(self, QEvent) -> None:
        left = self.marq[0]
        right = self.marq[1]
        video = self.marq[2]
        video.mediaPlayer.stop()
        box = QPixmap(self.paths[GalleryImage.BOX3D] + "/" + self.name + ".png")

        size = right.geometry().size()
        right.setPixmap(box.scaled(right.width(), right.height(), Qt.KeepAspectRatio))
        left.setText(self.name)
        left.setWordWrap(True)
        # right.resize(size)
        right.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        left.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # right.setScaledContents(True)

        path = "/metadata/" + self.system + "/videos/" + self.name + ".mp4"
        path = os.path.dirname(os.path.abspath(__file__)) + path
        video.resizeContent()
        video.play(path)


        return super().enterEvent(QEvent)

class labelFunctionality(QLabel):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
    def resizeEvent(self, a0: QResizeEvent) -> None:
        #print(a0.size())

        magnitude = (int) (math.sqrt(a0.size().height() + a0.size().width()) / 2)
        font = QFont('Arial', magnitude)
        print(self.size())
        self.setFont(font)

        return super().resizeEvent(a0)
        