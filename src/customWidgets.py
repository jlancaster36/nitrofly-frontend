import sys
from enum import Enum
from PyQt5.QtGui import *

class Console(Enum):
    SNES = 1
    N64  = 2
    GCN  = 3
    WII  = 4
    GBA  = 5
    NDS  = 6
    _3DS = 7
    PSP  = 8
    PS1  = 9
    PS2  = 10




class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()

# Example Instance:
#   button = PicButton(QPixmap("image.png"))

def create_console(console: Console):
    
    pass




