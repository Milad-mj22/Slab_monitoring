# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eror_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys


from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import texts
import detect_lenguage

ui2, _ = loadUiType("confirm_btn.ui")


class UI_confirm_window(QMainWindow, ui2):
    global widgets
    widgets_eror = ui2
    sign=0
    def __init__(self):
        super(UI_confirm_window, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        
        self.set_language()
        self.set_text()
        
     #   sys.exit(app.exec())
    def set_text(self,msg=''):
        self.label.setText(texts.MESSAGES['logout_message'][self.language])

    def activate_(self):
        self.no_btn.clicked.connect(self.close_win)
        self.yes_btn.clicked.connect(self.yes)
    def close_win(self):
        self.close()
    def yes(self):
        self.close()
        return True

    def set_language(self):
        self.language = detect_lenguage.language()
        if self.language=='Persian(فارسی)':
            detect_lenguage.confirm_window(self)
            


if __name__ == "__main__":
    app = QApplication()
    win = UI_confirm_window()
    win.show()
    sys.exit(app.exec())