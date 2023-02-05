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
        # print (f"creating button for  {self.system}")

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
    
    def __repr__(self) -> str:
        return f"{self.system} button"
    
    def __str__(self) -> str:
        return f"{self.system} button"


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
        self.graphicsView.setStyleSheet("background: transparent;")
        bounds = QRectF(self.scene.sceneRect())
        self.graphicsView.centerOn(bounds.center())

        self.scene.addItem(self.videoItem)
        layout = QVBoxLayout()
        layout.addWidget(self.graphicsView)
        self.setLayout(layout)
        self.mediaPlayer.setVideoOutput(self.videoItem)
        self.counter = 0
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.resizeContent()
    
    def play(self, path: str):
        # print("PLAYING FROM" + path)
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
        # print (f"creating button for  {self.name}")

    def setImage(self, type: GalleryImage = GalleryImage.BOX2D):
        self.type = type
        if self.romData[self.name][type.value] == False:
            #TODO: ADD Default art
            print(f"Metadata for {type} : {self.name} not found, setting default")
            return
        
        path     = self.paths[self.type] + "/" + self.name + ".png"
        suppPath = self.paths[GalleryImage.SUPPORT] + "/" + self.name + ".png"
        # print('setting supprot path: ' + suppPath)

        if self.system in ["3DS", "NDS", "GBA"]:
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
        else:
            self.setStyleSheet(
                "QPushButton{"
                    "border-image: url("+path+");"
                    "background-repeat: no-repeat;"
                    "width: 128px;"
                    "height: 179px;"
                    "}" 
                "QPushButton::hover {"
                    # "background-color : rgba(0, 0, 0, .5);"
                    "border-image: url("+suppPath+");"
                    "width: 128px;"
                    "height: 128px;"
                    "}")

        self.sizePolicy().setHorizontalStretch(0)
    
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


        path     = self.paths[self.type] + "/" + self.name + ".png"
        suppPath = self.paths[GalleryImage.SUPPORT] + "/" + self.name + ".png"
        
        # TODO: Set image size depending on support image size
        self.setStyleSheet(
                "QPushButton{"
                    "border-image: url("+suppPath+");"
                    "background-repeat: no-repeat;"
                    "width: 128px;"
                    "height: 128px;"
                    "}")
                    
        return super().enterEvent(QEvent)


    # Resets the size and image of the gallary button when not hovered over
    def leaveEvent(self, QEvent):
        path     = self.paths[self.type] + "/" + self.name + ".png"
        suppPath = self.paths[GalleryImage.SUPPORT] + "/" + self.name + ".png"
        self.setImage(self.type)


# This class if for a label that resizes according to changing window sizes.
# main_window is the ui's main window
class ResizingLabel(QLabel):
    def __init__(self, main_window, parent = None) -> None:
        super().__init__(parent)
        self.main_window = main_window
    def resizeEvent(self, a0: QResizeEvent) -> None:

        width = self.main_window.width()
        height = self.main_window.height()

        magnitudeWidth = 0.25 * width
        magnitudeHeight = 0.15 * height

        # widthDiff = a0.size().width() - a0.oldSize().width()
        # heightDiff = a0.size().height() - a0.oldSize().height()
        # print(widthDiff, heightDiff)

        magnitude = (int) (math.sqrt(magnitudeWidth + magnitudeHeight) / 2)
    
        font = QFont('Arial', magnitude)
        self.setFont(font)
        return super().resizeEvent(a0)
        