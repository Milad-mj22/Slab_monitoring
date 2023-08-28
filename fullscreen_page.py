from MyQR import myqr as mq
import sys
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import cv2
import sqlite3
from sqlite3 import Error




#camera_-------------------
def setup_camera(self):
    """Initialize camera.
    """
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()
    cur.execute('select * from camera1')
    records = cur.fetchall()
    for row in records:
        cam_1=row[0]
        cam_2=row[1]
        cam_3=row[2]
        cam_4=row[3]
    conn.commit()
    conn.close()      
    self.capture_1 = cv2.VideoCapture(0)
    #  self.capture_2 = cv2.VideoCapture(0)
    # self.capture_3 = cv2.VideoCapture(0)
    # self.capture_4 = cv2.VideoCapture(0)
    # self.capture.set(cv2.CV_CAP_PROP_FRAME_WIDTH, self.video_size.width())
    # self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, self.video_size.height())

    # self.timer = QTimer()
    # self.timer.timeout.connect(self.video)
    # self.timer.start(30)
def select_camera(self,num):
    if num==1:
        self.stackedWidget.setCurrentWidget(self.page_cam_1)
        self.capture_1.release()
        self.setup_camera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.video_cam_1)
        self.timer.start(30)
        print('hiasdwqd')
    if num==2:
        self.stackedWidget.setCurrentWidget(self.page_cam_2)
        self.capture_1.release()
        self.setup_camera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.video_cam_2)
        self.timer.start(30)
    if num==3:
        self.stackedWidget.setCurrentWidget(self.page_cam_3)
        self.capture_1.release()
        self.setup_camera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.video_cam_3)
        self.timer.start(30)
    if num==4:
        self.stackedWidget.setCurrentWidget(self.page_cam_4)
        self.capture_1.release()
        self.setup_camera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.video_cam_4)
        self.timer.start(30)
        
def video_cam_1(self):
    ret, self.frame = self.capture_1.read()
    if ret :
        self.scale_live_1=150
        height, width, channels = self.frame.shape
        centerX,centerY=int(height/2),int(width/2)
        radiusX,radiusY= int(self.scale_live_1*height/100),int(self.scale_live_1*width/100)
        minX,maxX=centerX-radiusX,centerX+radiusX
        minY,maxY=centerY-radiusY,centerY+radiusY
    
        frame_live_cam_1 = self.frame[minX:maxX, minY:maxY]
        frame_live_cam_1 = cv2.resize(frame_live_cam_1, (width, height)) 
        frame_live_cam_1 = cv2.cvtColor(frame_live_cam_1, cv2.COLOR_BGR2RGB)
        frame_live_cam_1 = cv2.flip(frame_live_cam_1, 1)
        self.image_live_cam_1 = QImage(frame_live_cam_1,frame_live_cam_1.shape[1], frame_live_cam_1.shape[0],frame_live_cam_1.strides[0], QImage.Format_RGB888)
        #  self.image_label_1.setPixmap(QPixmap.fromImage(image_live_cam_1))
        # self.live_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_1))
        self.label_2.setPixmap(QPixmap.fromImage(self.image_live_cam_1))

def video_cam_2(self):
    ret, self.frame = self.capture_1.read()
    if ret :
        self.scale_live_1=150
        height, width, channels = self.frame.shape
        centerX,centerY=int(height/2),int(width/2)
        radiusX,radiusY= int(self.scale_live_1*height/100),int(self.scale_live_1*width/100)
        minX,maxX=centerX-radiusX,centerX+radiusX
        minY,maxY=centerY-radiusY,centerY+radiusY
    
        frame_live_cam_1 = self.frame[minX:maxX, minY:maxY]
        frame_live_cam_1 = cv2.resize(frame_live_cam_1, (width, height)) 
        frame_live_cam_1 = cv2.cvtColor(frame_live_cam_1, cv2.COLOR_BGR2RGB)
        frame_live_cam_1 = cv2.flip(frame_live_cam_1, 1)
        self.image_live_cam_1 = QImage(frame_live_cam_1,frame_live_cam_1.shape[1], frame_live_cam_1.shape[0],frame_live_cam_1.strides[0], QImage.Format_RGB888)
        #  self.image_label_1.setPixmap(QPixmap.fromImage(image_live_cam_1))
        # self.live_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_1))
        self.label_3.setPixmap(QPixmap.fromImage(self.image_live_cam_1))

def video_cam_3(self):
    ret, self.frame = self.capture_1.read()
    if ret :
        self.scale_live_1=150
        height, width, channels = self.frame.shape
        centerX,centerY=int(height/2),int(width/2)
        radiusX,radiusY= int(self.scale_live_1*height/100),int(self.scale_live_1*width/100)
        minX,maxX=centerX-radiusX,centerX+radiusX
        minY,maxY=centerY-radiusY,centerY+radiusY
    
        frame_live_cam_1 = self.frame[minX:maxX, minY:maxY]
        frame_live_cam_1 = cv2.resize(frame_live_cam_1, (width, height)) 
        frame_live_cam_1 = cv2.cvtColor(frame_live_cam_1, cv2.COLOR_BGR2RGB)
        frame_live_cam_1 = cv2.flip(frame_live_cam_1, 1)
        self.image_live_cam_1 = QImage(frame_live_cam_1,frame_live_cam_1.shape[1], frame_live_cam_1.shape[0],frame_live_cam_1.strides[0], QImage.Format_RGB888)
        #  self.image_label_1.setPixmap(QPixmap.fromImage(image_live_cam_1))
        # self.live_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_1))
        self.label_5.setPixmap(QPixmap.fromImage(self.image_live_cam_1))

def video_cam_4(self):
    ret, self.frame = self.capture_1.read()
    if ret :
        self.scale_live_1=150
        height, width, channels = self.frame.shape
        centerX,centerY=int(height/2),int(width/2)
        radiusX,radiusY= int(self.scale_live_1*height/100),int(self.scale_live_1*width/100)
        minX,maxX=centerX-radiusX,centerX+radiusX
        minY,maxY=centerY-radiusY,centerY+radiusY
    
        frame_live_cam_1 = self.frame[minX:maxX, minY:maxY]
        frame_live_cam_1 = cv2.resize(frame_live_cam_1, (width, height)) 
        frame_live_cam_1 = cv2.cvtColor(frame_live_cam_1, cv2.COLOR_BGR2RGB)
        frame_live_cam_1 = cv2.flip(frame_live_cam_1, 1)
        self.image_live_cam_1 = QImage(frame_live_cam_1,frame_live_cam_1.shape[1], frame_live_cam_1.shape[0],frame_live_cam_1.strides[0], QImage.Format_RGB888)
        #  self.image_label_1.setPixmap(QPixmap.fromImage(image_live_cam_1))
        # self.live_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_1))
        self.label_7.setPixmap(QPixmap.fromImage(self.image_live_cam_1))

def buttonClick(self):
    # GET BUTTON CLICKED
    btn = self.sender()
    btnName = btn.objectName()
    # SHOW HOME PAGE
    if btnName == "cam_1_btn":
        print('page_1') 
        self.select_camera(1)
    if btnName == "cam_2_btn":
        print('page_2') 
        self.select_camera(2)
    if btnName == "cam_3_btn":
        print('page_3') 
        self.select_camera(3)
    if btnName == "cam_4_btn":
        print('page_4') 
        self.select_camera(4)


