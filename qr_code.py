from MyQR import myqr as mq
import sys
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

ui2, _ = loadUiType("qr_code2.ui")


class UI_qr_code(QMainWindow, ui2):
    global widgets
    widgets_eror = ui2
    image_glob=0
    close_sign=0
    def __init__(self):
        super(UI_qr_code, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.qr_gen()
        
    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)
    def close_win(self):
        self.close_sign=1
        self.close()
    def qr_gen(url_2='https://dorsa-co.ir/'):
        url='https://dorsa-co.ir/'
        mq.run(words = url,
        version = 6,
        picture = 'golden-logo-site.png',
        colorized = True,
        save_name = 'topcoder.png')

if __name__ == "__main__":
    app = QApplication()
    win = UI_qr_code()
    win.show()
    sys.exit(app.exec())
