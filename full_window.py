import sys
from PyQt5.QtGui import *
from cv2 import ROTATE_180, ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE
import cv2
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import zooming
from PyQt5 import QtCore, QtGui, QtWidgets

os.environ["QT_FONT_DPI"] = "96"
ui, _ = loadUiType("full_window.ui")


class UI_full_screen_window(QMainWindow, ui):
    global widgets
    widgets = ui


    def __init__(self):
        super(UI_full_screen_window, self).__init__()
        self.setupUi(self)

        flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        # self.statusBar()
        self.activate_()

        # self.label.mousePressEvent = self.clickmouse
    

        self.scale_cam_1=1
        self.temp()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)


    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    def minimize(self):
        self.showMinimized()
        self.center()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().windowHandle().screen()
        center_loc = screen.geometry().center()
        print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())

    def close_win(self):
        
        self.close()
        # sys.exit()

    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def temp(self):

        alert = cv2.imread('images/alert.png')
        self.set_image(alert)

    def set_image(self,image):
        self.image=image
        self.image_live_cam_1 = QImage(self.image,self.image.shape[1], self.image.shape[0],self.image.strides[0], QImage.Format_BGR888 )
        # self.label.setPixmap(QPixmap.fromImage(self.image_live_cam_1))



    def clickmouse(self,event):
        # if self.btn_cam1_sing=='pause':
       # print('right123')
            if event.button() == Qt.RightButton:
                self.scale_cam_1=1
                print('right')
                y=round(self.scale_cam_1,2)
                text='x'+str(y)
                # self.live_cam_1_zoom.setText(text)
                # self.live_cam_1_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
                # self.D_cam_1_zoom.setText(text)
                # self.D_cam_1_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
            elif event.button() == Qt.LeftButton:
                self.scale_cam_1=self.scale_cam_1*1.1
                y=round(self.scale_cam_1,2)
                text='x'+str(y)

                # self.live_cam_1_zoom.setText(text)
                # self.live_cam_1_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                # self.D_cam_1_zoom.setText(text)
                # self.D_cam_1_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.x_live_1 = event.pos().x()
                self.y_live_1 = event.pos().y() 
                w=self.label.width()
                h=self.label.height()
                h,w,_=self.image.shape
                h=h/self.label.height()
                w=w/self.label.width()
                self.x_live_1=self.x_live_1*w
                self.y_live_1=self.y_live_1*h
            # try:
            self.cam_zoom(self.image,self.scale_cam_1,self.x_live_1,self.y_live_1,self.label)
            # except:
            #     print('zoom with eror nothing')
    def cam_zoom(self,image,scale_cam,x_relative,y_relative,label,live =False):


        x=image
        x=zooming.zoomin(x,scale_cam,(x_relative,y_relative))
        if not live:
            y = QImage(x,x.shape[1], x.shape[0],x.strides[0], QImage.Format_BGR888 )
            
            label.setPixmap(QPixmap.fromImage(y))






if __name__ == "__main__":
    app = QApplication()
    win = UI_full_screen_window()
    win.show()
    sys.exit(app.exec())
    




