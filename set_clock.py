
import sys
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *

ui2, _ = loadUiType("set_clock.ui")


class UI_set_clock(QMainWindow, ui2):
    global widgets
    widgets_eror = ui2
    image_glob=0
    close_sign=0
    def __init__(self):
        super(UI_set_clock, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()

        self.up_sec.clicked.connect(self.sec)
        self.down_sec.clicked.connect(self.sec)
        self.up_min.clicked.connect(self.min)
        self.down_min.clicked.connect(self.min)
        self.up_hour.clicked.connect(self.hour)
        self.down_hour.clicked.connect(self.hour)
        

        self.select_btn.clicked.connect(self.select)

    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)
    def close_win(self):
        self.close()


    def sec(self):

        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'up_sec':
            text = self.label_sec.text()

            if text=='59':
                self.up_min.click()
                self.label_sec.setText('00')
            else:
                self.label_sec.setText(str(int(text)+1))


        if btnName == 'down_sec':
            text = self.label_sec.text()
            if text=='0' or text=='00':
                self.down_min.click()
                self.label_sec.setText('59')
            else:
                self.label_sec.setText(str(int(text)-1))



    def min(self):
    
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'up_min':
            text = self.label_min.text()

            if text=='59':
                self.up_hour.click()
                self.label_min.setText('00')
            else:
                self.label_min.setText(str(int(text)+1))


        if btnName == 'down_min':
            text = self.label_min.text()
            if text=='0' or text=='00':
                self.down_hour.click()
                self.label_min.setText('59')
            else:
                self.label_min.setText(str(int(text)-1))

    def hour(self):
    
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'up_hour':
            text = self.label_hour.text()
            print(text)
            if int(text)<24:
                self.label_hour.setText(str(int(text)+1))


        if btnName == 'down_hour':
            text = self.label_hour.text()
            if int(text)>0:
                self.label_hour.setText(str(int(text)-1))


    def select(self):

        parms_list = [self.label_hour,self.label_min,self.label_sec]
        time = []
        for parm in parms_list:

            if int(parm.text())<10 and int(parm.text())>0:
                time.append(str('0'+str(parm.text())))
            else:
                time.append(str(parm.text()))


        self.time = time[0]+':'+time[1]+':'+time[2]
        print(self.time)
        return self.time


if __name__ == "__main__":
    app = QApplication()
    win = UI_set_clock()
    win.show()
    sys.exit(app.exec())