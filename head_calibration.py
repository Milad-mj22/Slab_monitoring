
import sys


from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from camera_setting_window import *
import detect_lenguage

import texts


import colors_pallete

import sys
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *


import cv2
import PySide6.QtCore as sQtCore



# from PySide6.QtGui import QImage as sQImage
ui, _ = loadUiType("head_calibraion.ui")

DEFAULT_SIZE = (1000,500)
DEBUG=False

class UI_calibration_window(QMainWindow, ui):
    global widgets
    widgets_eror = ui
    sign=0
    def __init__(self):
        super(UI_calibration_window, self).__init__()
        self.setupUi(self)
        self.setMouseTracking(True)
        self._old_pos = None
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint )#| Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)

        self.conn = sqlite3.connect('settings.db')
        self.cur = conn.cursor()


        self.activate_()
        self.label_head_calibration.mousePressEvent = self.clickmouse
        self.label_head_calibration.mouseReleaseEvent = self.Releasemouse


        self.btn_save.clicked.connect(self.save_parms)

        self.load_parms()

        if DEBUG:
            img = cv2.imread('detection/images2/1 (41).png')
            self.set_image(img)
        

    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)


    def close_win(self):
        self.close()

    def set_language(self):
        if detect_lenguage.language()=='Persian(فارسی)':
            detect_lenguage.setting_window(self)


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and not self.isMaximized():
            
            # accept event only on top and side bars
            if event.position().y()<=self.frame_9.height() :#or event.position().x()<=self.side_bar.width():
                self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = sQtCore.QPoint(event.globalPosition().toPoint() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPosition().toPoint()

    def clickmouse(self,event):
        if event.button() == Qt.LeftButton:
            self.first_Mouse_X = event.x()
            self.first_Mouse_Y = event.y()

            self.first_x = self.redo_size(self.first_Mouse_X,axis =0)
            self.first_y = self.redo_size(self.first_Mouse_Y,axis =1)


            self.lineEdit_first_x.setText(str(self.first_x))
            self.lineEdit_first_y.setText(str(self.first_y))


    def Releasemouse(self, event):
        if event.button() == Qt.LeftButton:
            self.Mouse_X = event.x()
            self.Mouse_Y = event.y()

            self.end_x= self.redo_size(self.Mouse_X,axis =0)
            self.end_y= self.redo_size(self.Mouse_Y,axis =1)
            self.lineEdit_end_x.setText(str(self.end_x))
            self.lineEdit_end_y.setText(str(self.end_y))
            self.read_image()



    def read_image(self):
        
        img_ = self.draw_rect(self.image.copy())
        self.show_image(img_)


    def show_image(self,image):
        height, width, channels = image.shape
        bytesPerLine = channels * width
        qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.label_head_calibration.setPixmap(QPixmap.fromImage(qImg))


        


    def set_image(self,image):

        self.input_image_shape = image.shape
        self.real_image = image
        self.image = cv2.resize(image,DEFAULT_SIZE)
        self.show_image(self.image)

    def draw_rect(self,image):
        end_point = (self.Mouse_X,self.Mouse_Y)
        start_point = (self.first_Mouse_X,self.first_Mouse_Y)
        color = (50,50,255)
        thickness = 2
        image = cv2.rectangle(image, start_point, end_point, color, thickness)


        image_ = cv2.rectangle(self.real_image, (self.first_x,self.first_y), (self.end_x,self.end_y), color, thickness)
        cv2.imwrite('test.jpg',image_)

        return image

    def redo_size(self,input,axis=0):
        if axis==0:
            ret = input*self.input_image_shape[1]/DEFAULT_SIZE[axis]
        if axis==1:
            ret = input*self.input_image_shape[0]/DEFAULT_SIZE[axis]
        return int(ret)




    def save_parms(self):

        first_x = self.lineEdit_first_x.text()
        first_y = self.lineEdit_first_y.text()
        end_x = self.lineEdit_end_x.text()
        end_y = self.lineEdit_end_y.text()

        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()

        parms = {'first_x':first_x,'first_y':first_y,'end_x':end_x,'end_y':end_y}
        for parm in parms:
            sql = "UPDATE calibration SET {} = '{}' WHERE side = 'head'".format(parm,parms[parm])
            cur.execute(sql) 
            conn.commit()

        self.show_mesagges(self.show_messages,text=texts.MESSAGES['saved']['English'])

    def show_mesagges(self, label_name, text="", level=0, clearable=True, prefix=True):
        """
        this function is used to show input message in input label, also there is a message level determining the color of label, and a timer to clear meesage after a while

        Inputs:
            label_name: label element name to show the message in
            text: input message to show (in string)
            level: level of the message (in int), its a value betweem [0, 2] determining the bakground color of message label
            clearable: a boolean value determining whater to clear the message after timeout or not
            prefix: a boolean value determinign wheater to show the message prefix or not

        Returns: None
        """

        if text != "":
            if level == 0:
                label_name.setText(text)
                # label_name.setStyleSheet("color:{}".format(color))
            #
            if level == 1:
                if prefix:
                    label_name.setText(text)
                else:
                    label_name.setText(text)
                label_name.setStyleSheet(
                    "background-color: %s; color:white;"
                    % (colors_pallete.warning_yellow)
                )
            #
            if level >= 2:
                if prefix:
                    label_name.setText(text)
                else:
                    label_name.setText(text)
                label_name.setStyleSheet(
                    "background-color: %s; color:white;" % (colors_pallete.failed_red)
                )

            #
            if clearable:
                self.show_mesagges_thread_lock = True

                # timer to clear the message
                #print("show_mesagges_thread_lock True")
                QTimer.singleShot(5000, lambda: self.show_mesagges(label_name))

        else:
            label_name.setText(text)



    def load_parms(self):

        self.cur.execute('select * from calibration')
        records = self.cur.fetchall()
        self.lineEdit_first_x.setText(str(records[0][1]))
        self.lineEdit_first_y.setText(str(records[0][2]))
        self.lineEdit_end_x.setText(str(records[0][3]))
        self.lineEdit_end_y.setText(str(records[0][4]))
        
if __name__ == "__main__":
    app = QApplication()
    win = UI_calibration_window()
    win.show()
    sys.exit(app.exec())
