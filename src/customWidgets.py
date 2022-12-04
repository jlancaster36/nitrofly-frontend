import sys
from enum import Enum
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import glob
import os


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
        # self.resizeContent()

    def play(self):
        path = os.path.dirname(os.path.abspath(__file__)) + "/metadata/3DSmedia/videos/Fire Emblem - Awakening (USA) Decrypted.mp4"
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            pass
        else:
            # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/Users/lancaster/Documents/Nitrofly/nitrofly-frontend/src/test.mp4')))
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
            self.mediaPlayer.play()
            self.counter += 1
    
    # def play(self, path: str):
    #     path = os.path.dirname(os.path.abspath(__file__)) + "/metadata/3DSmedia/videos/Pokemon Alpha Sapphire (USA) (En,Ja,Fr,De,Es,It,Ko) (Rev 2) Decrypted.mp4"
    #     if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
    #         pass
    #     else:
    #         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/Users/lancaster/Documents/Nitrofly/nitrofly-frontend/src/test.mp4')))
    #         self.mediaPlayer.play()
    #         self.counter += 1
    
    def resizeContent(self):
        # self.show()
        bounds = QRectF(self.scene.sceneRect())
        self.graphicsView.fitInView(self.videoItem, Qt.KeepAspectRatio)
        # self.videoItem.setSize(QSizeF(self.parent.geometry().width(), self.parent.geometry().height()))
        self.graphicsView.centerOn(bounds.center())

        self.play()

    # def resizeEvent(self, a0: QResizeEvent) -> None:
    #     super().resizeEvent(a0)
    #     # self.videoItem.setSize(QSizeF(self.parent.geometry().width(), self.parent.geometry().height()))
    #     self.graphicsView.fitInView(self.videoItem, Qt.KeepAspectRatio)

class VerySimpleMediaPlayer(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.open_file_button = QPushButton("Open file")
        self.open_file_button.clicked.connect(self.open_file)

        self.media_player = QMediaPlayer(self)
        self.media_widget = QVideoWidget(self)
        self.media_player.setVideoOutput(self.media_widget)
        self.media_widget.show()

        layout = QVBoxLayout()
        layout.addWidget(self.open_file_button)
        layout.addWidget(self.media_widget)
        self.setLayout(layout)

    def open_file(self):
        filepath = '/Users/lancaster/Documents/Nitrofly/nitrofly-frontend/src/test.mp4'
        print("playing")
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(filepath)))
        self.media_player.setVolume(20)  # not too loud
        self.media_player.play()