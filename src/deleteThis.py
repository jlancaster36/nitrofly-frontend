from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,
                             QLabel, QFileDialog, QStyle, QVBoxLayout, QFrame)
import sys
import glob

class VideoWindow(QMainWindow):
    def __init__(self):
        super(VideoWindow, self).__init__()
        self.setWindowTitle('QMediaPlayer TEST')
        self.resize(640, 480)

         # QMediaPlayer
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('/Users/lancaster/Documents/Nitrofly/nitrofly-frontend/src/test.mp4')))

         # Set widget
        self.wrapperLayout = QVBoxLayout()
        self.videoWidget = QVideoWidget(self.wrapperLayout)
        self.videoWidget.setGeometry(self.pos().x(), self.pos().y(), self.width(), self.height())
        self.setCentralWidget(self.wrapperLayout)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

         # Play
        self.mediaPlayer.play()

class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("PyQt5 Video Player")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
 
        self.playButton = QPushButton()
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
 
        self.openButton = QPushButton("Open Video")   
        self.openButton.clicked.connect(self.openFile)
 
        widget = QWidget(self)
        # self.setCentralWidget(widget)
 
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.openButton)
        layout.addWidget(self.playButton)
 
        widget.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
 
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())
 
        print(fileName)
        if fileName != '':
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))
 
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()


if __name__ == '__main__':
     app = QApplication([])
     window = VideoWindow()
     window.show()
     sys.exit(app.exec_())
