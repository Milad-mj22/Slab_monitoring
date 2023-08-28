

import sys
from PyQt5.QtGui import *
from cv2 import ROTATE_180, ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE
from numpy.random.mtrand import random
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import numpy as np
import cv2
import sqlite3
from sqlite3 import Error
#from pylon_final import get_camear_by_serial
#from eror_window import *
from setting_window import *
import database
from pypylon import pylon
import cv2
from datetime import date, time, datetime
from login_window import *
from confirm_window import *
from default_setting_window import *
from eror_window import UI_eror_window
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import time

import xlwt

#from test3 import Window
#from fullscreen_cam_window import *
import detect_lenguage

import label_sizing
import color
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import Camera_utils
from pylon2 import connection
# from pylon2 import pylon_cam
import pypylon.pylon as py  

from pypylon import genicam

from PIL import ImageQt
from PIL import Image
import zooming
import numpy
import scipy
import get_pano

from modules import app_settings
import jdatetime
import time as tm 
import threading
import camera_connection
import camera_get_len
from backup_window import UI_backup_window
from backend import date_funcs,loging_func
# from detection.detection_color import slab_detection

from PySide6.QtGui import QImage as sQImage
from PySide6.QtGui import QPixmap as sQPixmap

import edge_top,edge_side
import PySide6.QtCore as sQtCore
 
from detection.motion_detection import Slab_Detection
from PySide6.QtWidgets import QMessageBox as sQMessageBox

from backend import storage_manament
import full_window

import set_clock,colors_pallete
from pyqt_calender import calender_ui

from PIL import Image, ImageEnhance

import image_processing
import photoviewer
import texts
import plc_connection

from head_calibration import UI_calibration_window

# os.environ["QT_FONT_DPI"] = "200"
os.environ["QT_FONT_DPI"] = "96"
ui, _ = loadUiType("main_window.ui")

DEBUG=False

class UI_main_window(QMainWindow, ui):
    global widgets
    widgets = ui
    image_live_cam_1=False
    image_glob_2=False
    image_glob_3=False
    image_glob_4=False
    frame_1=0
    frame_2=0
    problem=[]
    scale_live_1=200
    scale_live_2=200
    start_grabbing_sign=0
    fnt_time = QFont('Open Sans', 30, QFont.Bold)
    fnt_date = QFont('Open Sans', 8, QFont.Bold)
    last_btn='live_btn'
    btn_cam2_sing='play'
    btn_cam1_sing='play'
    btn_cam3_sing='play'
    btn_cam4_sing='play'
    retey_connection=0       #retry for connect to camera

    x_live_1,x_live_2,x_live_3,x_live_4=0,0,0,0
    y_live_1,y_live_2,y_live_3,y_live_4=0,0,0,0
    scale_cam_1=1
    scale_cam_2=1
    scale_cam_3=1
    scale_cam_4=1

    rotate_D_cam_1=0
    rotate_fulll_screen=0

    wait=False

    imgs=[]

    capture_sign=True
    create_path=True
    capturing_mode=''

    Is_login=False

    t=0


    def __init__(self):
        super(UI_main_window, self).__init__()
        self.setupUi(self)
        # connect to other windows
        self.window_login = UI_login_window()
        self.window_confirm =UI_confirm_window()
        self.window_setting = UI_setting_window()
        self.window_default=UI_default_setting_window()
        self.window_backup=UI_backup_window()
        self.calib_win = UI_calibration_window()
        self.win=0
        self.camera_panorama_cont=0
        
        #DEBUG
        self.itr=0
        self.sensor_detect=False
        self.dict_plc={}
        self.dict_plc['slab_id'] = 'test'
        self.frame_number=0


        #calibration

        self.load_camera_1_calibration()



        flags = Qt.WindowFlags(Qt.FramelessWindowHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        # self.statusBar()
        
        self.timerwrite=0

        self.mode=False


        
        self.activate_()
        self.cam_names()
        self.set_language()
        self.label_sizing()
        # self.set_font()
        self.set_size_animation()

        self.connect_btn.clicked.connect(self.buttonClick)
        self.disconnect_btn.clicked.connect(self.buttonClick)
        # self.save_btn.clicked.connect(self.buttonClick)
        self.setting_btn.clicked.connect(self.buttonClick)
        self.user_btn.clicked.connect(self.buttonClick)
        self.toggleButton.clicked.connect(self.buttonClick)
        self.logout_btn.clicked.connect(self.buttonClick)
        self.page_live_dataset_btn.clicked.connect(self.buttonClick)
        self.live_btn.clicked.connect(self.buttonClick)
        self.page_aboutus_btn.clicked.connect(self.buttonClick)
        self.panorama_btn.clicked.connect(self.buttonClick)

        self.live_cam_1_capture.clicked.connect(self.buttonClick)
        self.live_cam_2_capture.clicked.connect(self.buttonClick)
        self.live_cam_3_capture.clicked.connect(self.buttonClick)
        self.live_cam_4_capture.clicked.connect(self.buttonClick)
        self.D_cam_1_capture.clicked.connect(self.buttonClick)
        self.D_cam_2_capture.clicked.connect(self.buttonClick)
        self.D_cam_3_capture.clicked.connect(self.buttonClick)
        self.D_cam_4_capture.clicked.connect(self.buttonClick)
        self.fs_cam__capture.clicked.connect(self.buttonClick)
        
        self.automatic_btn.clicked.connect(self.buttonClick)
        self.manual_btn.clicked.connect(self.buttonClick)
    
        self.start_capture.clicked.connect(self.buttonClick)
        self.stop_capture.clicked.connect(self.buttonClick)
        
        
        self.backup_btn.clicked.connect(self.buttonClick)



        
        
        


        self.page_report_btn.clicked.connect(self.report_page)
        # self.request_btn.clicked.connect(self.table_report_request)
        # self.search_id_btn.clicked.connect(self.search_id)
        # self.search_line_btn.clicked.connect(self.search_line)
        # self.search_date.clicked.connect(self.func_search_date)
        # self.search_time.clicked.connect(self.func_search_time)
        # self.search_weight.clicked.connect(self.func_search_weight)
        # self.search_width.clicked.connect(self.func_search_width)
        self.full_search.clicked.connect(self.full_search_func)
        self.btn_now_time.clicked.connect(self.time_now)
        self.export_btn.clicked.connect(self.savefile)
        self.table_report_page_setup()

        self.window_login.login_btn.clicked.connect(self.buttonClick)
        
        self.right_box_btn.clicked.connect(self.buttonClick)


        
        self.stackedWidget.setCurrentWidget(self.page_live)
        self.page_fullscreen.clicked.connect(self.full_screen_page)
        self.page_fullscreen.clicked.connect(self.set_first_full)

        self.table()
        # self.report_page()
        self.header()

        self.set_capturing_time()
        self.set_live_refresh_rate()
        self.set_image_details()

        # self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000) # update every second
     #   self.showTime()

        self.detect_image=cv2.imread('images/check.png')
        self.nodetect_image=cv2.imread('images/circle.png')


        self.detect_image_path='images/circle_green.png'
        self.nodetect_image_path='images/circle_red.png'



        self.timer_fullscreen = QTimer(self)

 
        self.timer_fullscreen.timeout.connect(self.show_full_screen)

        self.set_page_style()
        color.color(self)
        


        #event_double_click-----------------

        self.live_image_label_1.mousePressEvent = self.clickmouse
        self.datalive_image_label_1.mousePressEvent = self.clickmouse
        self.live_image_label_2.mousePressEvent = self.clickmouse_2
        self.datalive_image_label_2.mousePressEvent = self.clickmouse_2
        self.live_image_label_3.mousePressEvent = self.clickmouse_3
        self.datalive_image_label_3.mousePressEvent = self.clickmouse_3
        self.live_image_label_4.mousePressEvent = self.clickmouse_4
        self.datalive_image_label_4.mousePressEvent = self.clickmouse_4


        self.fullscreen_label.mousePressEvent = self.clickmouse_full_screen


        self.live_image_label_5.mousePressEvent = self.show_full_window

        # head calibration UI

        self.window_setting.calibration_settings.clicked.connect(self.show_ui_calibration)
        self.calib_win.btn_getpicture.clicked.connect(self.update_calibration_image)


    #    self.window_default.save_close.clicked.connect(self.refresh)
        self.window_setting.window_defult.save_close_btn.clicked.connect(self.buttonClick)
        self.window_setting.window_defult.save_close_btn.clicked.connect(self.refresh) 
        self.refresh_btn.clicked.connect(self.refresh)

    #fullscree
        self.fs1_btn.clicked.connect(self.fs_1)
        self.D_fs1_btn.clicked.connect(self.fs_1)
        self.cam_1_btn.clicked.connect(self.fs_1)

        self.fs2_btn.clicked.connect(self.fs_2)
        self.D_fs2_btn.clicked.connect(self.fs_2)
        self.cam_2_btn.clicked.connect(self.fs_2)

        self.fs3_btn.clicked.connect(self.fs_3)
        self.D_fs3_btn.clicked.connect(self.fs_3)
        self.cam_3_btn.clicked.connect(self.fs_3)

        self.fs4_btn.clicked.connect(self.fs_4)
        self.D_fs4_btn.clicked.connect(self.fs_4)
        self.cam_4_btn.clicked.connect(self.fs_4)
        # self.cam_4_btn.clicked.connect(self.test)
        # self.x='image_live_cam_1'
        # self.test()
        # self.P_fs_1_btn.clicked.connect(self.fullscreen_panorama_cam_1)
        # self.P_fs_2_btn.clicked.connect(self.fullscreen_panorama_cam_2)

        self.defect_list()
        self.set_plc_values()



    #play_pause
        self.live_cam_1_play.clicked.connect(self.play_cam_1) 
        self.D_cam_1_play.clicked.connect(self.play_cam_1) 
        self.live_cam_2_play.clicked.connect(self.play_cam_2)
        self.D_cam_2_play.clicked.connect(self.play_cam_2)
        self.live_cam_3_play.clicked.connect(self.play_cam_3)
        self.D_cam_3_play.clicked.connect(self.play_cam_3)
        self.live_cam_4_play.clicked.connect(self.play_cam_4)
        self.D_cam_4_play.clicked.connect(self.play_cam_4)

        self.live_cam_1_pause.clicked.connect(self.pause_cam_1)
        self.D_cam_1_pause.clicked.connect(self.pause_cam_1)
        self.live_cam_2_pause.clicked.connect(self.pause_cam_2)
        self.D_cam_2_pause.clicked.connect(self.pause_cam_2)
        self.live_cam_3_pause.clicked.connect(self.pause_cam_3)
        self.D_cam_3_pause.clicked.connect(self.pause_cam_3)
        self.live_cam_4_pause.clicked.connect(self.pause_cam_4)
        self.D_cam_4_pause.clicked.connect(self.pause_cam_4)
        
        self.D_cam_1_rotate.clicked.connect(self.rotate)
        self.fs_cam__rotate.clicked.connect(self.rotate_fullscreen)

        self.slab_rate_manual.clicked.connect(self.buttonClick)
        self.slab_id_manual.clicked.connect(self.buttonClick)
        self.slab_line_manual.clicked.connect(self.buttonClick)
        self.slab_width_manual.clicked.connect(self.buttonClick)
        self.slab_lenght_manual.clicked.connect(self.buttonClick)
        self.slab_thickness_manual.clicked.connect(self.buttonClick)
        
        # self.window_get.confirm_btn.clicked.connect(self.show_data)


        self.thread_capturing=threading.Timer(self.capturing_time,self.func_start_capture)


        self.temp_list=[self.temp_cam1,self.temp_cam2,self.temp_cam3,self.temp_cam4]


        self.available_cams=camera.Collector()
        # list_cam=obj.serialnumber()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_available_cams)
        self.timer.start(5000) 


        self.live_timer = QTimer(self)
        self.live_timer.timeout.connect(self.show_cams)
        # self.live_timer.start(5000) 

        # coonect toogle frame camera

        self.toogle_cam_1.clicked.connect(self.buttonClick)
        self.toogle_cam_2.clicked.connect(self.buttonClick)
        self.toogle_cam_3.clicked.connect(self.buttonClick)
        self.toogle_cam_4.clicked.connect(self.buttonClick)

        self.camera_frame_dict={1:(self.frame_26,self.toogle_cam_1),2:(self.frame_23,self.toogle_cam_2),3:(self.frame_25,self.toogle_cam_3),4:(self.frame_51,self.toogle_cam_4)}
        # logger object to get log from everything is happening in the program
        self.logger = loging_func.app_logger(name='slab_monitoring-app_logger', log_mainfolderpath='./app_logs', console_log=True)
        self.logger.create_new_log(message='UI object for setting app created.')
        self.logger.create_new_log(message='UI object initialized and setting app loaded.')


        self.continue_last_slab=False

        
        self.prev_mode=True
        self.retry_change_mode=0

        self._old_pos = None

        #connect table

        self.table_report.clicked.connect(self.get_table_value)

        #detection
        self.slab_detection_obj = Slab_Detection()
        self.slab_detection_obj_side = Slab_Detection(change_state_n_trys=6)

        self.calibrate_btn.clicked.connect(self.do_calibrate)

        self.manage_space_main()
        self.photoviewer_obj = photoviewer.PhotoViewer()
        self.full_window_obj = full_window.UI_full_screen_window()
        self.full_window_obj.photoviewer_obj = photoviewer.PhotoViewer()
        # self.full_window_obj.photoviewer_obj = photoviewer.PhotoViewer()

        


        # search btns
        self.obj_clock = set_clock.UI_set_clock()
        self.obj_calender = calender_ui.UI_calender_window()

        self.tool_start_time.clicked.connect(self.show_time)
        self.tool_end_time.clicked.connect(self.show_time)

        self.tool_start_calender.clicked.connect(self.show_calender)
        self.tool_end_calender.clicked.connect(self.show_calender)

        self.obj_clock.select_btn.clicked.connect(self.set_time)
        self.obj_calender.select_btn.clicked.connect(self.set_date)


        self.serials=[]

        self.image_process_obj = image_processing.UI_image_processing()

        self.image_process_obj.set_ui_obj(self)
        self.image_process_obj.connect_value_change()
        self.image_process_obj.fetch_data()

        # self.brightness_cam_1=0
        # self.brightness_cam_2=0
        # self.brightness_cam_3=0
        # self.brightness_cam_4=0

        self.live_cam_1_setting.clicked.connect(self.show_spec_page_image_process)
        self.live_cam_2_setting.clicked.connect(self.show_spec_page_image_process)
        self.live_cam_3_setting.clicked.connect(self.show_spec_page_image_process)
        self.live_cam_4_setting.clicked.connect(self.show_spec_page_image_process)



        self.frame_23.setDisabled(False)
        self.frame_26.setDisabled(False)
        self.frame_24.setDisabled(False)
        self.frame_25.setDisabled(False)
        self.frame_30.setDisabled(False)
        self.frame_27.setDisabled(False)
        self.frame_28.setDisabled(False)
        self.frame_29.setDisabled(False)
        self.live_cam_1_setting.setDisabled(False)


        self.clear_checkboxes_btn.clicked.connect(self.clear_check_box_table)
        self.edit_btn.clicked.connect(self.edit_table)
        

        self.big_label ='head'
        self.checkBox_top.clicked.connect(self.set_big_label)
        self.checkBox_head.clicked.connect(self.set_big_label)

        self.one_flag=True



        self.full_window_obj.checkBox_mesh.clicked.connect(self.show_full_window)

        self.show_mesagges_thread_lock = (
            False  # flag to dont run another thread until one is available
        )
        self.records_table_report=False
        self.user_manual_btn.clicked.connect(self.open_user_manual_file)
        self.connect_btn.click()
        self.maxiButton.click()
        self.manual_btn.click()
        self.automatic_btn.click()


        self.flag_calibration=False
        self.save_image_head=False


    def show_ui_calibration(self):
        self.calib_win.show()
        self.update_calibration_image()

    def update_calibration_image(self):
        self.calib_win.set_image(self.image_1)


    def show_grid_fullscreen(self):
        print('asdwwqwq')
        # if self.full_window_obj.checkBox_mesh.isChecked():
        #         self.show_full_window(self.image_head_old)
        # else:
        #         self.show_full_window(self.image_head)
    def set_first_full(self):
        try:
            # self.fs_1()
            self.fs1_btn.click()
        except:
            pass


    def show_spec_page_image_process(self):
        btn = self.sender()
        btnName = btn.objectName()
        print(btnName)

        page_num = btnName.split('_')[-2]
        print('page_num',page_num)

        self.image_process_obj.set_page(page_num)

        self.image_process_obj.show()




    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and not self.isMaximized():
            
            # accept event only on top and side bars
            if event.position().y()<=self.toolBar.height() :#or event.position().x()<=self.side_bar.width():
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



    def test(self):

        x=cv2.imread('myqr.png')
        self.cam.stream()
        # Thread(target=self.cam.stream()).start()
        self.cam.show()
        x=self.cam.np_image
        # print('x',x)
        self.x = QImage(x,x.shape[1], x.shape[0],x.strides[0], QImage.Format_BGR888 )
        # if self.last_btn=='live_btn':
        self.live_image_label_2.setPixmap(QPixmap.fromImage(self.x))

    def refresh(self):
        print('refresh')
        self.cam_names()
        self.set_language()
        self.table()
        self.label_sizing()
        self.set_capturing_time()
        self.set_image_details()
        self.window_login = UI_login_window()
        self.window_confirm =UI_confirm_window()
        self.window_setting = UI_setting_window()
        self.window_default=UI_default_setting_window()
        # if self.start_grabbing_sign==1:
        #     self.collector.stop_grabbing()
        color.color(self)
        self.set_language()
        


        # self.set_font()
        self.set_size_animation()


    def set_image_details(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from path')
        records = cur.fetchall()   
        self.parent_dir=(records[0][0])
        self.parent_dir_imed=(records[1][0])
        self.format_image=(records[0][3])
        self.format_image_imed=(records[1][3])


        cur.execute('select * from refresh_rate')
        records = cur.fetchall()   
        self.panorama_lenght=int((records[0][3]))
        print('panorama_lenght',self.panorama_lenght)
        print(self.parent_dir)       

        cur.execute('select * from two_cam')
        records = cur.fetchall()   
        self.two_cam=str((records[0][0]))

        # print(self.parent_dir)   



    def set_capturing_time(self):

        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from capturing_time')
        records = cur.fetchall()   
        self.capturing_time=(int(records[0][1])/1000)

        if DEBUG:
            self.capturing_time = 0.5



    def set_live_refresh_rate(self):
    
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from live_refresh_rate')
        records = cur.fetchall()   
        self.live_refresh_rate=(int(records[0][1]))
        # print('live_recfresh_rate  ',self.live_refresh_rate)




    def label_sizing(self):
        label_sizing.size(self)

    def set_size_animation(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from table_width')
        records = cur.fetchall()   
  
        self.left_size_menu=int(records[0][0])
        self.right_size_menu=int(records[0][1])

    def set_font(self):
        """Initialize fonts.
        """
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from font')
        records = cur.fetchall()

        conn.close()
        f="QWidget[	font: {}pt "'{}'";    background-color: rgb(100,100,100);]".format(records[0][1],records[0][0])
        f=f.replace('[','{').replace(']','}')


        self.centralwidget.setStyleSheet(f)

        self.fnt_time = QFont('Open Sans', records[0][1]+10, QFont.Bold)
 


    def set_language(self):
        self.language = detect_lenguage.language()
        if self.language=='Persian(فارسی)':
            detect_lenguage.main_window(self)
            

        
    def getPos(self , event):
        self.x_live_1 = event.pos().x()
        self.y_live_1 = event.pos().y() 
        print('x,y',self.x_live_1,self.y_live_1,event,self)
       # self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)
      #  self.label_2.setPixmap(QPixmap.fromImage(self.image_live_cam_1))

        self.cam.get_location(self.x_live_1,self.y_live_1)
        self.cam.zoom_in()

#zooom-------------
    def clickmouse(self,event):
        # if self.btn_cam1_sing=='pause':
       # print('right123')
            if event.button() == Qt.RightButton:
                self.scale_cam_1=1
                print('right')
                y=round(self.scale_cam_1,2)
                text='x'+str(y)
                self.live_cam_1_zoom.setText(text)
                self.live_cam_1_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
                self.D_cam_1_zoom.setText(text)
                self.D_cam_1_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
            elif event.button() == Qt.LeftButton:
                self.scale_cam_1=self.scale_cam_1*1.1
                y=round(self.scale_cam_1,2)
                text='x'+str(y)

                self.live_cam_1_zoom.setText(text)
                self.live_cam_1_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.D_cam_1_zoom.setText(text)
                self.D_cam_1_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.x_live_1 = event.pos().x()
                self.y_live_1 = event.pos().y() 
                h,w,_=self.cameras[self.cam_1].getPictures().shape
                h=h/self.live_image_label_1.height()
                w=w/self.live_image_label_1.width()
                self.x_live_1=self.x_live_1*w
                self.y_live_1=self.y_live_1*h
            try:
                self.cam_zoom(self.image_cam1,self.scale_cam_1,self.x_live_1,self.y_live_1,self.live_image_label_1,self.datalive_image_label_1)
            except:
                print('zoom with eror nothing')
    def cam_zoom(self,image,scale_cam,x_relative,y_relative,label,label2,live =False):


        x=image
        x=zooming.zoomin(x,scale_cam,(x_relative,y_relative))
        if not live:
            y = QImage(x,x.shape[1], x.shape[0],x.strides[0], QImage.Format_BGR888 )
            
            label.setPixmap(QPixmap.fromImage(y))
            label2.setPixmap(QPixmap.fromImage(y))
        # self.d_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_1))
  
        return x



    def show_full_window(self,event=False):
        # image_head
        # try:
            if self.full_window_obj.checkBox_mesh.isChecked():
                image = self.image_head_old
            else:
                image = self.image_head
            # cv2.imshow('a',self.image_head_old)
            # cv2.imshow('b',self.image_head)
            # cv2.waitKey(0)
            # self.full_window_obj.create_photo_viewer_obj()
            # self.full_window_obj.set_image(self.image_head)

            a = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
            # win.setPhoto(pixmap=a)

            self.full_window_obj.photoviewer_obj.setPhoto(a)

            # self.full_window_obj.photoviewer_obj.show()

            self.full_window_obj.frame_3.layout().addWidget(self.full_window_obj.photoviewer_obj)

            # self.photoviewer_obj.setPhoto(image)
        # except:
        #     self.full_window_obj.set_image(self.image_1)
            self.full_window_obj.showMaximized()
            # self.full_window_obj.show()







    def clickmouse_2(self,event):
        # if self.btn_cam2_sing=='pause':
        # print('right123')
            self.clickmouse(event)
            if event.button() == Qt.RightButton:
                self.scale_cam_2=1
                print('right')
                y=round(self.scale_cam_2,2)
                text='x'+str(y)
                self.live_cam_2_zoom.setText(text)
                self.live_cam_2_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
                self.D_cam_2_zoom.setText(text)
                self.D_cam_2_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
            elif event.button() == Qt.LeftButton:
                self.scale_cam_2=self.scale_cam_2*1.1
                y=round(self.scale_cam_2,2)
                text='x'+str(y)
                self.live_cam_2_zoom.setText(text)
                self.live_cam_2_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.D_cam_2_zoom.setText(text)
                self.D_cam_2_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.x_live_2 = event.pos().x()
                self.y_live_2 = event.pos().y() 
                h,w,_=self.cameras[self.cam_2].getPictures().shape
                h=h/self.live_image_label_2.height()
                w=w/self.live_image_label_2.width()
                self.x_live_2=self.x_live_2*w
                self.y_live_2=self.y_live_2*h
            try:
                self.cam_zoom(self.image_cam2,self.scale_cam_2,self.x_live_2,self.y_live_2,self.live_image_label_2,self.datalive_image_label_2)
            except:
                print('zoom with eror nothing')

    def clickmouse_3(self,event):
        # if self.btn_cam3_sing=='pause':
            # print('right123')
            if event.button() == Qt.RightButton:
                self.scale_cam_3=1
                print('right')
                text='x'+str(self.scale_cam_3)
                self.live_cam_3_zoom.setText(text)
                self.live_cam_3_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
                self.D_cam_3_zoom.setText(text)
                self.D_cam_3_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
            elif event.button() == Qt.LeftButton:
                self.scale_cam_3=self.scale_cam_3*1.1
                y=round(self.scale_cam_3,2)
                text='x'+str(y)
                self.live_cam_3_zoom.setText(text)
                self.live_cam_3_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.D_cam_3_zoom.setText(text)
                self.D_cam_3_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.x_live_3 = event.pos().x()
                self.y_live_3 = event.pos().y() 
                h,w,_=self.cameras[self.cam_3].getPictures().shape
                h=h/self.live_image_label_3.height()
                w=w/self.live_image_label_3.width()
                self.x_live_3=self.x_live_3*w
                self.y_live_3=self.y_live_3*h
            try:
                self.cam_zoom(self.image_cam3,self.scale_cam_3,self.x_live_3,self.y_live_3,self.live_image_label_3,self.datalive_image_label_3)
            except:
                print('zoom with eror nothing')


    def clickmouse_4(self,event):
        # if self.btn_cam4_sing=='pause':
            # print('right123')
            if event.button() == Qt.RightButton:
                self.scale_cam_4=1
                print('right')
                text='x'+str(self.scale_cam_4)
                self.live_cam_4_zoom.setText(text)
                self.live_cam_4_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
                self.D_cam_4_zoom.setText(text)
                self.D_cam_4_zoom.setStyleSheet("QLabel { color: rgb(1, 100, 54); }")
            elif event.button() == Qt.LeftButton:
                self.scale_cam_4=self.scale_cam_4*1.1
                y=round(self.scale_cam_4,2)
                text='x'+str(y)
                self.live_cam_4_zoom.setText(text)
                self.live_cam_4_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.D_cam_4_zoom.setText(text)
                self.D_cam_4_zoom.setStyleSheet("QLabel { color: rgb(150, 50, 50); }")
                self.x_live_4 = event.pos().x()
                self.y_live_4 = event.pos().y() 
                h,w,_=self.cameras[self.cam_4].getPictures().shape
                h=h/self.live_image_label_4.height()
                w=w/self.live_image_label_4.width()
                self.x_live_4=self.x_live_4*w
                self.y_live_4=self.y_live_4*h
            try:
                self.cam_zoom(self.image_cam4,self.scale_cam_4,self.x_live_4,self.y_live_4,self.live_image_label_4,self.datalive_image_label_4)
            except:
                print('zoom with eror nothing')


    def clickmouse_full_screen(self,event):

        if self.last_btn=='fs1_btn':
            self.clickmouse_1(event)
        elif self.last_btn=='fs2_btn':
            self.clickmouse_2(event)
        elif self.last_btn=='fs3_btn':
            self.clickmouse_3(event)
        elif self.last_btn=='fs4_btn':
            self.clickmouse_4(event)






    def set_page_style(self):
        conn=self.create_connection('settings.db')
        cur = conn.cursor()
        cur.execute('select * from setstyle')
        rec = cur.fetchall()

        conn.commit()
        conn.close()    
        app.setStyle(str(rec[0][0]))
#windows connect----------------------
    def eror_window(self,msg,level):
        self.window_eror = UI_eror_window()
       # self.ui2= UI_eror_window()
        self.window_eror.show()
        self.window_eror.set_text(msg,level)
       
    def setting_window(self):

        if self.Is_login:
            from PyQt5.QtGui import QIcon, QPixmap
        
            self.window_setting.show()

        else:
            self.eror_window(msg=texts.MESSAGES['Please_Login'][self.language],level=2)

     
    def login_window(self):
        

        self.window_login.show()
        self.id=self.window_login.id

    def confirm_window(self,def_name):
        self.window_confirm.show()
        if def_name =='logout':
            self.window_confirm.set_text(msg='logout')
            self.window_confirm.yes_btn.clicked.connect(self.logout)


    def get_data(self,name):

        # self.window_get.show()
        pass
        self.last_detail=name

    def show_data(self):
        self.window_get.close()
        if self.last_detail=='slab_id':
            print('slab_id')
            self.slab_id.setText(self.window_get.lineEdit.text())
        if self.last_detail=='slab_line':
            print('slab_line')
            self.slab_line.setText(self.window_get.lineEdit.text())
        if self.last_detail=='slab_width':
            print('slab_width')
            self.slab_width.setText(self.window_get.lineEdit.text())
        if self.last_detail=='slab_lenght':
            print('slab_lenght')
            self.slab_lenght.setText(self.window_get.lineEdit.text())
        if self.last_detail=='slab_thickness':
            print('slab_thickness')
            self.slab_thickness.setText(self.window_get.lineEdit.text())




    def login(self):
        user_id=self.window_login.login()
        self.user_btn.setText(user_id)

        self.logout_btn.setDisabled(False)
        self.window_setting.user_btn.setText(user_id)

        self.window_backup.user_btn.setText(user_id)

        print('login')
        self.Is_login=True
        self.window_setting.login_welcome.setText('Access level : Operator')
    
    def logout(self):
        print('logout succesfull')
        self.user_btn.setText('Guest')
        self.logout_btn.setDisabled(True)
        self.window_login.label_2.setText("")
        self.Is_login=False
        
    def showTime(self):
        

        self.label_time.setFont(self.fnt_time)
        self.label_date.setFont(self.fnt_date)

        currentTime = QTime.currentTime()

        self.displayTxt_time = currentTime.toString('hh:mm:ss')

        self.label_time.setText(self.displayTxt_time)


        current_date=jdatetime.date.today()    
        self.current_date=str(current_date)

        self.label_date.setText(self.current_date) 

        if DEBUG:
            self.itr+=1

            if self.itr>4:
                self.sensor_detect=True
            if self.itr>8:
                self.sensor_detect=False
                self.itr=0

    def activate_(self):
        self.closeButton.clicked.connect(self.close_win)
        self.miniButton.clicked.connect(self.minimize)
        self.maxiButton.clicked.connect(self.maxmize_minimize)

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def open_close_menu(self):
        enable=False

        try:
            print('try_toggle')

            # GET WIDTH
            width = self.leftMenu.width()
            
            maxExtend = self.left_size_menu
            standard = 44

            # SET MAX WIDTH
            if width == 44:
                print('OPEN')
                self.toggleButton.setIcon(QPixmap.fromImage('images\menu.png'))
                widthExtended = maxExtend
                if enable:
                    self.leftMenu.setMaximumWidth(self.left_size_menu+44)
                    

            else:
                self.toggleButton.setIcon(QPixmap.fromImage('images\menu_close.png'))
                print('Close')
                widthExtended = standard
                if enable:
                    self.leftMenu.setMaximumWidth(44)

            if enable==False:
            # ANIMATION
                self.animation_2 = QPropertyAnimation(self.leftMenu, b"minimumWidth")
                self.animation_2.setDuration(app_settings.Settings.TIME_ANIMATION)
                self.animation_2.setStartValue(width)
                self.animation_2.setEndValue(widthExtended)
                self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
                self.animation_2.start()
        except:
            print('eror')
        self.center()

    def open_close_camera_bar(self,cam_num):
        enable=False

        this_frame=self.camera_frame_dict[cam_num][0]
        this_btn=self.camera_frame_dict[cam_num][1]

        print('this_frame',this_frame)

        # try:
        print('try_toggle')

        # GET WIDTH
        height = this_frame.height()
        
        maxExtend = 50
        standard = 0

        # SET MAX WIDTH
        if height == 0:
            print('OPEN')
            # self.toggleButton.setIcon(QPixmap.fromImage('images\menu.png'))
            img = 'images\chevron - up.png'
            this_btn.setIcon(QIcon(img))
            heightExtended = maxExtend
            # if enable:
                # self.leftMenu.setMaximumWidth(self.left_size_menu+44)
                

        else:
            # self.toggleButton.setIcon(QPixmap.fromImage('images\menu_close.png'))
            print('Close')

            img = 'images\chevron - down.png'
            this_btn.setIcon(QIcon(img))

            heightExtended = standard


        if enable==False:
        # ANIMATION
            self.animation_2 = QPropertyAnimation(this_frame, b"maximumHeight")
            self.animation_2.setDuration(app_settings.Settings.TIME_ANIMATION)
            self.animation_2.setStartValue(height)
            self.animation_2.setEndValue(heightExtended)
            self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation_2.start()

            # self.animation_2 = QPropertyAnimation(this_frame, b"minimumHeight")
            # self.animation_2.setDuration(app_settings.Settings.TIME_ANIMATION)
            # self.animation_2.setStartValue(height)
            # self.animation_2.setEndValue(heightExtended)
            # self.animation_2.setEasingCurve(QEasingCurve.InOutQuart)
            # self.animation_2.start()
        # except:
        #     print('eror')
        # self.center()



    def right_box_func(self):
        enable=False
        print('right_box')
        # GET WIDTH
        try:
            width = self.right_frame.width()
            maxExtend = self.right_size_menu
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                print('OPEN')

                img = ('images\chevron - Copy.png')
                self.right_box_btn.setIcon(QIcon(img))

                widthExtended = maxExtend
                if enable:
                    print(self.right_size_menu+44)
                    self.right_frame.setMaximumWidth(self.right_size_menu+44)
                print('closeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
                # QTimer.singleShot(10000, self.right_box_func)
            else:

                img = ('images\chevron.png')
                self.right_box_btn.setIcon(QIcon(img))
                print('Close')
                widthExtended = standard
                if enable:
                    print(0)
                    self.right_frame.setMaximumWidth(0)


            # ANIMATION
            if enable==False:
                self.animation_3 = QPropertyAnimation(self.right_frame, b"minimumWidth")
                self.animation_3.setDuration(app_settings.Settings.TIME_ANIMATION)
                self.animation_3.setStartValue(width)
                self.animation_3.setEndValue(widthExtended)
                self.animation_3.setEasingCurve(QEasingCurve.InOutQuart)
                self.animation_3.start()
        except:
            print('eror')

        self.center()

    def center(self):
        frame_geo = self.frameGeometry()
        screen = self.window().windowHandle().screen()
        center_loc = screen.geometry().center()
        print(center_loc)
        frame_geo.moveCenter(center_loc)
        self.move(frame_geo.topLeft())
        # self.move(frame_geo.moveTop)

    def header(self):
        # GET WIDTH
        width = self.label_3.width()
        maxExtend = 310
        standard = 0

        # SET MAX WIDTH
        if width == 0:
            print('start')
            widthExtended = maxExtend
            print(widthExtended)
        else:
            print('Close')
            widthExtended = standard
            print(widthExtended)

        # ANIMATION
        self.animation = QPropertyAnimation(self.label_3, b"minimumWidth")
        self.animation.setDuration(3000)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()


    def minimize(self):
        self.showMinimized()
        self.center()

    def close_win(self):

        
        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['Exit'][self.language])

        if ret:

            if self.start_grabbing_sign==1:
                self.disconnect_func()
                
            self.close()
            sys.exit()

    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


   
#camera------------------




    def initialize_cams(self):
        """Initialize camera.
        """
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from cameras_serial')
        records = cur.fetchall()

        
        for row in records:
            self.cam_1=str(row[0])
            self.cam_2=str(row[1])
            self.cam_3=str(row[2])
            self.cam_4=str(row[3])

        conn.close()   
        self.extract_cmas_data()





    def extract_cmas_data(self):

        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from cameras')
        self.cams_detail = cur.fetchall()

        
        conn.commit()
        conn.close()    


        return self.cams_detail

    def rotate(self):
        self.rotate_D_cam_1+=1
        print(self.rotate_D_cam_1)

    def rotate_image(self,image,i):


        # print(i)
        if i ==1:
            image=cv2.rotate(image,ROTATE_90_COUNTERCLOCKWISE)
        if i==2:
            image=cv2.rotate(image,ROTATE_180)
        if i==3:
            image=cv2.rotate(image,ROTATE_90_CLOCKWISE)
            
        return image

    def get_picture_cam_1(self):
            self.image_1 = self.cameras[self.cam_1].getPictures()
            # self.image_1 = self.adjust_contrast_brightness(self.image_1,contrast=self.contrast_cam_1/50,brightness=self.brightness_cam_1,sharpness=self.sharpness_cam_1,hsv=self.hsv_cam_1)
            self.image_1 = self.cam_zoom(self.image_1,self.scale_cam_1,self.x_live_1,self.y_live_1,self.live_image_label_1,self.datalive_image_label_1,live=True)
            self.thread_get_picture_cam_1.start()


    def create_random_image(self):
        img = np.zeros((1920,1800,3),dtype=np.uint8)
        img[:,:] = np.random.randint(0,150)

        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # org
        org = (50, 50)

        fontScale = 1
        
        # Blue color in BGR
        color = (255, 0, 0)
        
        # Line thickness of 2 px
        thickness = 2
        
        # Using cv2.putText() method
        img = cv2.putText(img,  self.dict_plc['slab_id']+'  frame : '+str(self.frame_number), org, font, 
                        fontScale, color, thickness, cv2.LINE_AA)


        return img
    

    def load_camera_1_calibration(self):

        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from calibration')
        records = cur.fetchall()

        self.camera_1_calibration_parms = records[0]






    def camera_1(self):
            

            if DEBUG:
                self.image_1 = self.create_random_image()
            else:
                self.image_1 = self.cameras[self.cam_1].getPictures()
            
            self.image_clear = self.image_1
            if self.checkBox_mesh.checkState() :#or self.checkBox_mesh.checkState().value==2:
                self.image_1 = self.draw_grid(self.image_1)
            frame =self.image_1
            frame= frame[self.camera_1_calibration_parms[2]:self.camera_1_calibration_parms[4],self.camera_1_calibration_parms[1]:self.camera_1_calibration_parms[3]]
            # cv2.imshow('f',frame)
            # cv2.waitKey(1)
            # self.image_1 = frame
            # if self.checkBox_cam_1.isChecked():
            #     self.image_1 = self.adjust_contrast_brightness(self.image_1,contrast=self.contrast_cam_1/50,brightness=self.brightness_cam_1,sharpness=self.sharpness_cam_1,hsv=self.hsv_cam_1)
            self.image_1 = self.cam_zoom(self.image_1,self.scale_cam_1,self.x_live_1,self.y_live_1,self.live_image_label_1,self.datalive_image_label_1,live=True)
            # self.image_live_cam_1 = QImage(self.image_1,self.image_1.shape[1], self.image_1.shape[0],self.image_1.strides[0], QImage.Format_BGR888 )
            self.image_live_cam_1 = QImage(self.image_1,self.image_1.shape[1], self.image_1.shape[0],self.image_1.strides[0], QImage.Format_BGR888 )


            # cv2.imshow('f',self.image_1)
            # cv2.waitKey(1)

            #////////////detection

            res, msg, contours , detect_ret = self.slab_detection_obj.detect_slab(current_frame=frame.copy(),thresh=15,mode = self.mode)
            # print('msg ' ,msg, 'detect ',detect_ret,res)
            # #//////////////////////

            if DEBUG:
                detect_ret = self.sensor_detect
                msg = 'debug detext'



            if  detect_ret:
                # self.mode=True
                print('detect cam 1')
                print('msg ' ,msg, 'detect ',detect_ret)
                self.change_color_detect(detect=True,num=0)

                self.set_label()
                self.one_flag=False

            if self.last_btn=='live_btn': 
                if self.big_label == 'head':        
                    self.live_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_1))
                else:
                    self.live_image_label_2.setPixmap(QPixmap.fromImage(self.image_live_cam_1))





    def set_label(self):
        # self.image_head = self.image_1
        self.image_head = self.image_clear
        self.image_head_old = self.image_1
        self.image_head_old = self.draw_grid(self.image_head_old)

        # self.image_head = self.image_head[50:-450,400:-450 ]
        # self.image_head = self.image_head[50:-450,400:-450 ]
        # if self.checkBox_mesh.checkState():
        image = self.image_head_old
        # else:
        #     image = self.image_head
        self.image_head_rotate=cv2.rotate(image,ROTATE_90_COUNTERCLOCKWISE)
        self.image_head_rotate = QImage(self.image_head_rotate,self.image_head_rotate.shape[1], self.image_head_rotate.shape[0],self.image_head_rotate.strides[0], QImage.Format_BGR888 )
        
        self.live_image_label_5.setPixmap(QPixmap.fromImage(self.image_head_rotate))
        # self.save_img_panorama(self.image_head,1,str(self.slab_id.text()))
        if not DEBUG:
            if self.full_window_obj.checkBox_mesh.isChecked():
                self.show_full_window()
            else:
                self.show_full_window()
            
            threading.Timer(2,self.close_full_window).start()

        self.save_image_head=True

        # self.calibration()

        
    def draw_grid(self,img , grid_shape=(15,10),color = (255,0,0) , thickness = 1):
        h,w,_ = img.shape
        row,col = grid_shape
        dy,dx = h/row,w/col

        for x in np.linspace(start=dx , stop=w-dx,num=col-1):
            x = int(round(x))
            cv2.line(img,(x,0),(x,h),color=color,thickness=thickness)

        for y in np.linspace(start=dy , stop=h-dy,num=row-1):
            y = int(round(y))
            cv2.line(img,(0,y),(w,y),color=color,thickness=thickness)

        return img




    def close_full_window(self):

        self.full_window_obj.closeButton.click()




 
    def camera_2(self):

        # try:
            # print('cam2',self.cam_2)
            if DEBUG:
                self.image_2 = self.create_random_image()
            else:
                self.image_2=self.cameras[self.cam_2].getPictures()
            # self.image_2=cv2.rotate(self.image_2,ROTATE_90_COUNTERCLOCKWISE)
            if self.checkBox_cam_2.isChecked():
                self.image_2 = self.adjust_contrast_brightness(self.image_2,contrast=self.contrast_cam_2/50,brightness=self.brightness_cam_2,sharpness=self.sharpness_cam_2,hsv=self.hsv_cam_2,b=self.b_cam_2,g=self.g_cam_2,r=self.r_cam_2)
            # # self.image_2 = self.image_1
            if self.checkBox_mesh.checkState():
                self.image_2 = self.draw_grid(self.image_2)


            self.image_2 = self.cam_zoom(self.image_2,self.scale_cam_2,self.x_live_2,self.y_live_2,self.live_image_label_2,self.datalive_image_label_2,live=True)

            self.image_live_cam_2 =  QImage(self.image_2,self.image_2.shape[1], self.image_2.shape[0],self.image_2.strides[0], QImage.Format_BGR888 )
            # threading.Timer(0.5,self.set_label).start()
            # self.set_label()
            if self.last_btn=='live_btn':
                if self.big_label == 'top':
                    self.live_image_label_1.setPixmap(QPixmap.fromImage(self.image_live_cam_2))
                else:
                    self.live_image_label_2.setPixmap(QPixmap.fromImage(self.image_live_cam_2))

            else:
                self.datalive_image_label_2.setPixmap(QPixmap.fromImage(self.image_live_cam_2))
            # print('cam2',self.cam_2)
        # except:
        #     print('eror cam2')
        #     pass

    def camera_3(self):

        # try:
            if DEBUG:
                self.image_3 = self.create_random_image()
            else:
                self.image_3=self.cameras[self.cam_3].getPictures()
            if self.checkBox_cam_3.isChecked():
                self.image_3 = self.adjust_contrast_brightness(self.image_3,contrast=self.contrast_cam_3/50,brightness=self.brightness_cam_3,sharpness=self.sharpness_cam_3,hsv=self.hsv_cam_3,b=self.b_cam_3,g=self.g_cam_3,r=self.r_cam_3)
            # self.image_3 = self.adjust_contrast_brightness(self.image_3)
            # self.image_3 = self.image_1
            self.image_3=cv2.flip(self.image_3,1)
            self.image_3 = self.cam_zoom(self.image_3,self.scale_cam_3,self.x_live_3,self.y_live_3,self.live_image_label_3,self.datalive_image_label_3,live=True)           
            x=self.image_3

            self.image_live_cam_3 = QImage(x,x.shape[1], x.shape[0],x.strides[0], QImage.Format_BGR888 )
            
            if self.last_btn=='live_btn':
                self.live_image_label_3.setPixmap(QPixmap.fromImage(self.image_live_cam_3))
            else:
                self.datalive_image_label_3.setPixmap(QPixmap.fromImage(self.image_live_cam_3))
        # except:
        #     # print('eror cam 3')
        #     pass

    def camera_4(self):    

        # try:
            if DEBUG:
                self.image_4 = self.create_random_image()
            else:
                self.image_4=self.cameras[self.cam_4].getPictures()
            # self.image_4=cv2.flip(self.image_4,1)
            if self.checkBox_cam_4.isChecked():
                self.image_4 = self.adjust_contrast_brightness(self.image_4,contrast=self.contrast_cam_4/50,brightness=self.brightness_cam_4,sharpness=self.sharpness_cam_4,hsv=self.hsv_cam_4,b=self.b_cam_4,g=self.g_cam_4,r=self.r_cam_4)

            self.image_4 = self.cam_zoom(self.image_4,self.scale_cam_4,self.x_live_4,self.y_live_4,self.live_image_label_4,self.datalive_image_label_4,live=True)
            frame =self.image_4
            frame = frame[0:200, 200:600]



            #////////////detection

            res, msg, contours , detect_ret = self.slab_detection_obj_side.detect_slab(current_frame=frame.copy(),thresh=10,mode = self.mode)



            #////////////

            #///////////



            if DEBUG:
                res = self.sensor_detect



            # print('ressssss',res)

            if  res:
                if not self.mode:
                    
                    print('detect cam 4')
                    
                    
                    # if not self.mode:
                    self.mode=True
                    self.set_slab_detect(num=4)
                    self.fault_slab_id = self.slab_id.text()

                    if self.save_image_head:

                        self.save_img_panorama(self.image_head,1,str(self.slab_id.text()))  # save head image
                        self.save_image_head = False
                    
                    self.frame_number = 0


            else:
                if self.mode:
                    self.mode=False
                    # self.retry_change_mode+=1
                    self.set_slab_detect(num=4)
                    print('no slab  cam 4')

                    # self.calibration()


            x=self.image_4
 
            self.image_live_cam_4 = QImage(x,x.shape[1], x.shape[0],x.strides[0], QImage.Format_BGR888 )
            if self.last_btn=='live_btn':
                self.live_image_label_4.setPixmap(QPixmap.fromImage(self.image_live_cam_4))
            else:
                self.datalive_image_label_4.setPixmap(QPixmap.fromImage(self.image_live_cam_4))
        
        # except:
        #     print('eror cam 4')
        #     pass

    def set_slab_detect(self,num=0):


            if self.mode:
                print('True')
                self.change_color_detect(num=num,detect=True)
                self.retry_change_mode=0
                # self.thread_capturing.start()
                if self.capturing_mode=='auto':
                    self.func_start_capture()

            if not self.mode :
                # if self.retry_change_mode>10:
                    # self.mode=False
                    print('set slab aFalse')
                    self.change_color_detect(detect=False,num=num)
                    self.retry_change_mode=0
                    self.func_stop_capture()
                    self.calibration()


                
        # self.prev_mode=self.mode                

    def change_color_detect(self,num=0,detect=True):
        if detect:
            image=self.detect_image
            path = self.detect_image_path

            # self.func_stop_scapture()
        else:
            print('image no detect')
            image=self.nodetect_image
            path = self.nodetect_image_path

            # if self.capturing_mode=='auto' and self.capture_sign:
            #     self.func_start_capture()
        if num==0:
            self.set_pixmap(self.cam1_sign_detect,path)
        else:
            self.set_pixmap(self.cam1_sign_detect,path)
            self.set_pixmap(self.cam2_sign_detect,path)
            self.set_pixmap(self.cam3_sign_detect,path)
            self.set_pixmap(self.cam4_sign_detect,path)


    def setup_camera(self):

        self.report_label.setText('Connecting')
        

        frame_id = 0

        elapsed_time_pause = 0
        time=0

        self.fps_val.setText(str(time))
        self.start_grabbing_sign=1
        # try:
        self.cameras={}
        self.cams=[self.cam_1,self.cam_2,self.cam_3,self.cam_4]

        try:
            if DEBUG:
                print(self.cams[0],'exposure=',self.cams_detail[0][1], 'gain',self.cams_detail[0][0])
            collector = camera_connection.Collector(self.cams[0],exposure=self.cams_detail[0][1], gain=self.cams_detail[0][0], trigger=False, delay_packet=int(self.cams_detail[0][2]),\
                packet_size=int(self.cams_detail[0][5]),frame_transmission_delay=int(self.cams_detail[0][6]),width=int(self.cams_detail[0][3]),height=int(self.cams_detail[0][4]),\
                    offet_x=int(self.cams_detail[0][8]),offset_y=int(self.cams_detail[0][9]),manual=True)
            collector.start_grabbing()
            if DEBUG:
                print(self.cams[0],'Grabed')
            self.cameras[self.cams[0]]=collector
        except:
            print('eror create connection 0')

        try:
            if DEBUG:
                print(self.cams[1],'exposure=',self.cams_detail[1][1], 'gain',self.cams_detail[1][0])
            collector = camera_connection.Collector(self.cams[1],exposure=self.cams_detail[1][1], gain=self.cams_detail[1][0], trigger=False, delay_packet=int(self.cams_detail[1][2]),\
                packet_size=int(self.cams_detail[1][5]),frame_transmission_delay=int(self.cams_detail[1][6]),width=int(self.cams_detail[1][3]),height=int(self.cams_detail[1][4]),\
                    offet_x=int(self.cams_detail[1][8]),offset_y=int(self.cams_detail[1][9]),manual=True)
            collector.start_grabbing()
            if DEBUG:
                print(self.cams[1],'Grabed')
            self.cameras[self.cams[1]]=collector
        except:
            print('eror create connection 1')

        try:
            if DEBUG:
                print(self.cams[2],'exposure=',self.cams_detail[2][1], 'gain',self.cams_detail[2][0])
            collector = camera_connection.Collector(self.cams[2],exposure=self.cams_detail[2][1], gain=self.cams_detail[2][0], trigger=False, delay_packet=int(self.cams_detail[2][2]),\
                packet_size=int(self.cams_detail[2][5]),frame_transmission_delay=int(self.cams_detail[2][6]),width=int(self.cams_detail[2][3]),height=int(self.cams_detail[2][4]),\
                    offet_x=int(self.cams_detail[2][8]),offset_y=int(self.cams_detail[2][9]),manual=True)
            collector.start_grabbing()
            if DEBUG:
                print(self.cams[2],'Grabed')
            self.cameras[self.cams[2]]=collector
        except:
            print('eror create connection 2')

        try:
            if DEBUG:
                print(self.cams[3],'exposure=',self.cams_detail[3][1], 'gain',self.cams_detail[3][0])
            collector = camera_connection.Collector(self.cams[3],exposure=self.cams_detail[3][1], gain=self.cams_detail[3][0], trigger=False, delay_packet=int(self.cams_detail[3][2]),\
                packet_size=int(self.cams_detail[3][5]),frame_transmission_delay=int(self.cams_detail[3][6]),width=int(self.cams_detail[3][3]),height=int(self.cams_detail[3][4]),\
                    offet_x=int(self.cams_detail[3][8]),offset_y=int(self.cams_detail[3][9]),manual=True)
            collector.start_grabbing()
            if DEBUG:
                print(self.cams[3],'Grabed')
            self.cameras[self.cams[3]]=collector
        except:
            print('eror create connection 3')

        print('all cameras variable created')

        self.fps_val.setText(str(time))
        #enable frames
        self.frame_23.setDisabled(False)
        self.frame_26.setDisabled(False)
        self.frame_24.setDisabled(False)
        self.frame_25.setDisabled(False)
        self.frame_30.setDisabled(False)
        self.frame_27.setDisabled(False)
        self.frame_28.setDisabled(False)
        self.frame_29.setDisabled(False)
        
        self.time_fps=0
        x=tm.time()
        self.report_label.setText('Connected')
        # cv2.waitKey(1000)
        self.report_label.setText('')
        self.set_live_refresh_rate()
        self.live_timer.start(self.live_refresh_rate)


    




    def show_cams(self): 
            

            # time.sleep(5)


            self.time_fps=0
            if self._running:

                # print('runing')

                # try:
                    self.start_grabbing_sign=1
                    # while True:
                    x=tm.time() 

                    if self.btn_cam1_sing=='play':
                        # try:
                            self.camera_1()
                        # except:
                        #     # print('eror cam 1')
                        #     pass

                 
                    if self.btn_cam2_sing=='play':
                        try:
                            self.camera_2()
                        except:
                            # print('eror cam 2')
                            pass

                    if self.btn_cam3_sing=='play':
                        try:
                            self.camera_3()
                        except:
                            # print('eror cam 3')
                            pass


                    if self.btn_cam4_sing=='play':
                        # try:
                            self.camera_4()
                        # except:
                        #     # print('eror cam 4')
                        #     pass

                    self.frame_number+=1

                    y=tm.time()
                    # t=t-x
                    try:
                        y=y-x
                        y=1/y
                        y=round(y,2)

                        self.fps_val.setText(str(y))
                    except:
                        pass
                    if self._running ==False:
                        print('stop')
                        cv2.waitKey(1000)
            if DEBUG:
                cv2.waitKey(500)


    def disconnect_func(self):
        import time
        if self.start_grabbing_sign==1:
            self.report_label.setText('Disconnecting')
            self.wait=True
            self._running = False
            print('disconnect')
            self.connect_btn.setDisabled(True)
            # self.calibrate_btn.setDisabled(True)
            cv2.waitKey(3000)
            available_cams=self.obj.serialnumber()
            print(available_cams)
            for i in range(len(self.cams)):
                # if self.cameras[self.cams[i]].IsOpen:
                    print(self.cams[i])
                    if (self.cams[i]) in available_cams:
                        # if self.cameras[self.cams[i]].exitCode==0 :
                        try:
                            self.cameras[self.cams[i]].stop_grabbing()   
                        except:
                            continue  
                
            # self.thread_cameras.join()
            if self.capture_sign==False:
                self.func_stop_capture()
            self.start_grabbing_sign=0
            self.connect_btn.setDisabled(False)
            self.calibrate_btn.setDisabled(True)
            self.camera_panorama_cont=0
            self.report_label.setText('Disconnected')
            cv2.waitKey(1000)
            self.report_label.setText('')
            try:
                self.live_timer.stop()
            except:
                print('stop timer Eror')
        else:

            for i in range(len(self.cams)):
                # if self.cameras[self.cams[i]].IsOpen:
                    print(self.cams[i])
                    if (self.cams[i]) in available_cams:
                        if self.cameras[self.cams[i]].exitCode==0 :
                            try:
                                self.cameras[self.cams[i]].stop_grabbing()   
                            except:
                                continue  
                    
    def get_temps(self):

        self.serials=self.available_cams.check_serials()

    def show_available_cams(self):
        # return
        temp=[]
        
        self.cams_sign_list=[self.cam1_sign,self.cam2_sign,self.cam3_sign,self.cam4_sign]
        # print(len(self.available_cams.check_devices()))

        for i in range(len(self.cams_sign_list)):
            self.cams_sign_list[i].setStyleSheet("background-color:rgb(255,0,0)")
    


        t1 = threading.Timer(0.1,self.get_temps)
        t1.start()


        if '23961540' in self.serials:
            self.cams_sign_list[0].setStyleSheet("background-color:#8BDB81;border-radius:10px;")
            if self.start_grabbing_sign==1:
                self.show_temp('23961540',self.temp_cam1)

        if '23961515' in self.serials:
            self.cams_sign_list[1].setStyleSheet("background-color:#8BDB81;border-radius:10px;")
            if self.start_grabbing_sign==1:
                self.show_temp('23961515',self.temp_cam2)
        if '40150886' in self.serials:
            self.cams_sign_list[2].setStyleSheet("background-color:#8BDB81;border-radius:10px;")
            if self.start_grabbing_sign==1:
                self.show_temp('40150886',self.temp_cam3)
        if '23905933' in self.serials:
            self.cams_sign_list[3].setStyleSheet("background-color:#8BDB81;border-radius:10px;")
            if self.start_grabbing_sign==1:
                self.show_temp('23905933',self.temp_cam4)

        if self.start_grabbing_sign==0:
            for i in range (len(self.temp_list)):
                self.temp_list[i].setText('-')
    



    def show_temp(self,serial,label):
        try:

                if self.start_grabbing_sign==1:
                    # pass
                    
                    temp=self.cameras[serial].tempreture()
                    temp=round(temp,2)
                    label.setText(str(temp)[:4])
                    # print(self.timerwrite)
                    if self.timerwrite >=75:
                        # self.logger.create_new_log(message='serial : {} , temp : {}'.format(serial,temp))
                        pass
              
                    if self.timerwrite >=79:
                        self.timerwrite=0
                    else:
                        self.timerwrite+=1
        except:
            
            print('cant show tem')
            pass
        





    def play_cam_1(self):
        self.btn_cam1_sing='play'
        print('cam1:',self.btn_cam1_sing)
        self.cam_1_pause.setText('')
        self.D_cam_1_pausesign.setText('')
        self.live_cam_1_pause.setDisabled(False)
        self.D_cam_1_pause.setDisabled(False)
        self.live_cam_1_zoom.setText('x1')
        self.live_cam_1_zoom.setStyleSheet("QLabel { color: rgb(0,0,0); }")
      
 

    def pause_cam_1(self):
        self.btn_cam1_sing='pause'
        print('cam1:',self.btn_cam1_sing)
        self.cam_1_pause.setText('pause')
        self.D_cam_1_pausesign.setText('pause')
        self.live_cam_1_pause.setDisabled(True)
        self.D_cam_1_pause.setDisabled(True)
        self.image_cam1=self.image_1

    def play_cam_2(self):
        self.btn_cam2_sing='play'
        print('cam2:',self.btn_cam2_sing)
        self.cam_2_pause.setText('')
        self.D_cam_2_pausesign.setText('')
        self.live_cam_2_pause.setDisabled(False)
        self.D_cam_2_pause.setDisabled(False)
        self.live_cam_2_zoom.setText('x1')
        self.live_cam_2_zoom.setStyleSheet("QLabel { color: rgb(0,0,0); }")       

    def pause_cam_2(self):
        self.btn_cam2_sing='pause'
        print('cam2:',self.btn_cam2_sing)
        self.live_cam_2_pause.setDisabled(True)
        self.D_cam_2_pause.setDisabled(True)
        self.D_cam_2_pausesign.setText('pause')
        self.cam_2_pause.setText('pause')
        self.image_cam2=self.image_2

    def play_cam_3(self):
        self.btn_cam3_sing='play'
        print('cam3:',self.btn_cam3_sing)
        self.cam_3_pause.setText('')
        self.D_cam_3_pausesign.setText('')
        self.live_cam_3_pause.setDisabled(False)
        self.D_cam_3_pause.setDisabled(False)
        self.live_cam_3_zoom.setText('x1')
        self.live_cam_3_zoom.setStyleSheet("QLabel { color: rgb(0,0,0); }")

    def pause_cam_3(self):
        self.btn_cam3_sing='pause'
        self.live_cam_3_pause.setDisabled(True)
        self.D_cam_3_pause.setDisabled(True)
        print('cam3:',self.btn_cam3_sing)
        self.cam_3_pause.setText('pause')
        self.D_cam_3_pausesign.setText('pause')
        self.image_cam3=self.image_3

    def play_cam_4(self):
        self.btn_cam4_sing='play'
        print('cam4:',self.btn_cam4_sing)
        self.cam_4_pause.setText('')
        self.D_cam_4_pausesign.setText('')
        self.live_cam_4_pause.setDisabled(False)
        self.D_cam_4_pause.setDisabled(False)
        self.live_cam_4_zoom.setText('x1')
        self.live_cam_4_zoom.setStyleSheet("QLabel { color: rgb(0,0,0); }")

    def pause_cam_4(self):
        self.btn_cam4_sing='pause'
        print('cam4:',self.btn_cam4_sing)
        self.cam_4_pause.setText('pause')
        self.D_cam_4_pausesign.setText('pause')
        self.live_cam_4_pause.setDisabled(True)
        self.D_cam_4_pause.setDisabled(True)
        self.image_cam4=self.image_4


#blur and brighness-------------------------------


    def zoom_live_2(self,value):
        self.scale_live_1 = value
        print('zoom levele live cam 2: ',value)
        self.update()


    def cam_names(self):
        conn=self.create_connection('settings.db')
        cur = conn.cursor()
        cur.execute('select * from camera_names')
        records = cur.fetchall()
        for row in records:
            cam_1_name=str(row[0])
            cam_2_name=str(row[1])
            cam_3_name=str(row[2])
            cam_4_name=str(row[3])
        cur.execute('select * from cameras_serial')
        records = cur.fetchall()
        for row in records:
            cam_1_serial=str(row[0])
            cam_2_serial=str(row[1])
            cam_3_serial=str(row[2])
            cam_4_serial=str(row[3])
        
        try:

            self.dataset_cam_1_name.setText(str(cam_1_name)+' '+str(self.cam_1))
            self.dataset_cam_2_name.setText(str(cam_2_name)+' '+str(self.cam_2))
            self.dataset_cam_3_name.setText(str(cam_3_name)+' '+str(self.cam_3))
            self.dataset_cam_4_name.setText(str(cam_4_name)+' '+str(self.cam_4))
            self.live_cam_1_name.setText(str(cam_1_name)+' '+str(self.cam_1))
            self.live_cam_2_name.setText(str(cam_2_name)+' '+str(self.cam_2))
            self.live_cam_3_name.setText(str(cam_3_name)+' '+str(self.cam_3))
            self.live_cam_4_name.setText(str(cam_4_name)+' '+str(self.cam_4))
            # print('try',self.cam_1)
            # print('try',self.cam_2)
        except:
            pass


#table dataset_page-----------------
    def table(self):
        conn=self.create_connection('settings.db')
        cur = conn.cursor()
        cur.execute('select * from defect')
        self.records = cur.fetchall()

        self.defect_table.resizeColumnsToContents()
        self.defect_table.setColumnCount(1)
        self.hh_Labels=['Defects List']
        
        self.defect_table.setHorizontalHeaderLabels(self.hh_Labels)
        self.defect_table.setRowCount(99)
        self.defect_table.verticalHeader().setVisible(True)
        self.defect_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
      #  headers = ['defect', 'count', 'des']

        table_item = QTableWidgetItem()
        str1=[]
        for i in self.records:
            str1.append(i[0])  

        for row, string in enumerate(str1):
          #  print (row,string)
            table_item = QTableWidgetItem(str(string))
            #table_item.setData(Qt.DisplayRole, str(string))
            table_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            table_item.setCheckState(Qt.CheckState.Unchecked)
            self.defect_table.setItem(row,0,table_item)

        self.defect_table.setRowCount(row+1)

    
    def read_data_table(self):
        row_count=self.defect_table.rowCount()
        col_count=self.defect_table.columnCount()


        checked_list = []
        list=[]
        for i in range(self.defect_table.rowCount()):    
            if self.defect_table.item(i, 0).checkState() == QtCore.Qt.Checked:

                list.append(i)

        checked_list = []

        if len(list)!=0:
            for i in range (len(list)):
                checked_list.append(self.records[list[i]][0])
        else:
            checked_list.append('No Defect')

        return checked_list


    def uncked_defect_table(self,table_name):
        for i in range(table_name.rowCount()):    
            # table_item.setCheckState(Qt.CheckState.Unchecked)
                table_name.item(i, 0).setCheckState(Qt.CheckState.Unchecked)

        


    def clickBox(self, state):

        if state == QtCore.Qt.Checked:
            print('Checked')
        else:
            print('Unchecked')
#saving-------------------------------------

 
    def save(self):
        print('save')


    def save_imed_img(self,cam,label,name,notif):

        x =datetime.now()
        x=x.strftime("%Y%m%d%H%M%S")
        image = ImageQt.fromqpixmap(label.pixmap())


        

        image.save('{}/{}_cam_{}.{}'.format(self.parent_dir_imed,x,cam,self.format_image_imed))

        label_text=name

        notif.setText('Image Svaed ')
        cv2.waitKey(2000)
        notif.setText('')
        # self.L_notif_cam_3.setText('')
  
    def save_img_panorama(self,image,cam,slab_id):

        melting_id = self.melting_id.text()

        # if self.capture_sign:

        slab_id = self.folder_slab_id


        x =datetime.now()
        x=x.strftime("%Y%m%d%H%M%S")

        # self.parent_dir = "img_path"
        if not os.path.exists(self.parent_dir):
            os.mkdir(self.parent_dir)

        directory = str(slab_id)
        # directory =str(melting_id)+'/'+str(slab_id)
        path = os.path.join(self.parent_dir, 'temp')

        try:
            

            print('first_path',path)

            if self.create_path==True:
                print('create_path')
                if not os.path.exists(path):
                    
                    os.mkdir(path)
                    self.path=path
                    self.create_path=False
                    print("Directory '% s' created" % directory)
                    try:
                        
                        print("Directory '% s' created" % directory)
                    except:
                        print('eror')
                        # notif.setText('Eror : {}/cam_{}_*.tiff '.format(directory,cam))
                        
                elif os.path.exists(path):
                    directory = str(slab_id) +'_'+ '{}'.format(x)
                    if os.path.split(path)[1] == 'temp':
                        pass
                        # os.rename(path,os.path.join(self.parent_dir, directory))

                    # print(directory)


                    # edit version for get plc data

                    # path = os.path.join(self.parent_dir, directory)
                    # print('path',path)
                    # os.mkdir(path)

                    self.create_path=False

                    self.path=path
        except:
            print('eror in create path')
            # self.path=path
            # os.mkdir(path)
                # notif.setText('Image Svaed : {}/cam_{}_*.{} '.format(directory,cam,self.format_image))
        print('final_path',self.path)

        scale=50
        width = int(image.shape[1]*scale/100)
        height = int(image.shape[0]*scale/100)
        dim = (width,height)
        image = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)

        cv2.imwrite('{}/cam_{}_{}.png'.format(self.path,cam,x),image)




    def create_connection(self,db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)
            self.eror_window(msg=' NO connection to database {}'.format(db_file),level=3)

#report_page--------------------
    def report_page(self):
        self.stackedWidget.setCurrentWidget(self.page_report)


    def table_report_page_setup(self):
        self.hh_Labels=['Slab ID', 'Date', 'Time','Line','Slab Defects', 'Thickness','Weight','Width','Length','Image Path']
        self.table_report.setHorizontalHeaderLabels(self.hh_Labels)

        header = self.table_report.horizontalHeader()       
        header = self.table_report.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)


    def table_report_request(self):
        self.clear_table()
        
        tedad=self.spinBox_tedad.text()
        records=database.report_last(tedad)
        
        self.table_report.setRowCount(len(records))

        self.set_data(records)


    def clear_table(self):

        for i in range(self.table_report.rowCount()):
            self.table_report.removeRow(0)

    def set_data(self,records):

        self.records_table_report=records
        table_item = QTableWidgetItem()
        for row,string in enumerate(records):
            for i in range(10):

                table_item = QTableWidgetItem(str(string))
                if i ==0:
                    table_item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    table_item.setCheckState(Qt.CheckState.Unchecked)
                table_item.setData(Qt.DisplayRole, str(string[i+1]))
                self.table_report.setItem(row,i,table_item)
            # print(row)
            # if row<100:
            #     self.progressBar.setValue(row)
        self.progressBar.setValue(100)
        cv2.waitKey(5000)
        self.progressBar.setValue(0)
    

    def clear_check_box_table(self):
        self.uncked_defect_table(self.table_report)
        # clear_checkboxes_btn

    def edit_table(self):

        row_count=self.table_report.rowCount()
        col_count=self.table_report.columnCount()


        checked_list = []
        list=[]
        for i in range(self.table_report.rowCount()):    
            if self.table_report.item(i, 0).checkState().value == 2:
                list.append(i)

        checked_list = []

        if len(list)==1:
            for i in range (len(list)):
                checked_list.append(self.records[list[i]][0])
        elif len(list)>1:
            self.eror_window(texts.MESSAGES['only_one_raw'][self.language],2)
            return
        
        elif len(list)==0:
            self.eror_window(texts.MESSAGES['more_than_one'][self.language],2)
            return
        
        return checked_list

    def search_id(self):

        self.clear_table()
        
        id=self.lineEdit_id.text()
        print(id)
        records=database.search_id(id)
        self.table_report.setRowCount(len(records))

        self.set_data(records)
        # time.sleep(5)


    def search_line(self):

        self.clear_table()
        
        line=self.lineEdit_line.text()
        print(line)
        records=database.search_line(line)
        self.table_report.setRowCount(len(records))

        self.set_data(records)  
        
             



    def func_search_date(self):
        self.clear_table()
        # try:
        start_date=self.lineEdit_date_start.text()
        end_date=self.lineEdit_date_end.text()
        print(start_date  , end_date)
        # records=database.search_date('1400-02-02','1400-02-02')
        records=database.search_date('date',start_date,end_date)
        self.table_report.setRowCount(len(records))

        self.set_data(records)

        # time.sleep(5)
        # except:
        #     print('eror')


    def func_search_time(self):
        self.clear_table()
        # try:
        start_time=self.lineEdit_time_start.text()
        end_time=self.lineEdit_time_end.text()

        records=database.search_time(start_time,end_time)
        self.table_report.setRowCount(len(records))

        self.set_data(records)




    def func_search_weight(self):
        self.clear_table()
        try:
            start_date=self.start_weight_text.text()
            end_date=self.end_weight_text.text()
            # records=database.search_date('1400-02-02','1400-02-02')
            records=database.between('weight',start_date,end_date)
            self.table_report.setRowCount(len(records))

            self.set_data(records)

            # time.sleep(5)
        except:
            print('eror')


    def func_search_width(self):

        self.clear_table()
        try:
            start_date=self.start_width_text.text()
            end_date=self.end_width_text.text()
            # records=database.search_date('1400-02-02','1400-02-02')
            records=database.between('width',start_date,end_date)
            self.table_report.setRowCount(len(records))

            self.set_data(records)

            # time.sleep(5)
        except:
            print('eror')



    def full_search_func(self):
        self.clear_table()
        query = 'WHERE '


        if self.checkBox_line_report.isChecked():
            line=self.lineEdit_line.text()
            query+=" line= '{}' AND".format(line)

        if self.checkBox_id_report.isChecked():
            id=self.lineEdit_id.text()
            query+=" slab_id= '{}' AND".format(id)

        if self.checkBox_date_report.isChecked():
            start_date=self.lineEdit_date_start.text()
            end_date=self.lineEdit_date_end.text()
            query+=" date>='{}' AND date<='{}' AND".format(start_date,end_date)

        if self.checkBox_time_report.isChecked():
            if not self.checkBox_date_report.isChecked():
                current_date =str(jdatetime.date.today())
                self.lineEdit_date_start.setText(current_date)
                self.lineEdit_date_end.setText(current_date)
                query+=" date>='{}' AND date<='{}' AND".format(current_date,current_date)
            start_time=self.lineEdit_time_start.text()
            end_time=self.lineEdit_time_end.text()
            query+=" time>='{}' AND time<='{}' AND".format(start_time,end_time)

        if self.checkBox_width_report.isChecked():
            start_width=self.start_width_text.text()
            end_width=self.end_width_text.text()
            query+=" width>={} AND width<={} AND".format(start_width,end_width)

        if self.checkBox_weight_report.isChecked():
            start_weight=self.start_weight_text.text()
            end_weight_weight=self.end_weight_text.text()
            query+=" weight>={} AND weight<={} AND".format(start_weight,end_weight_weight)




        if query[-3:]=='AND':
            query=query[:-3]




        if self.checkBox_last_report.isChecked():
            tedad=self.spinBox_tedad.text()
            if query=='WHERE ':
                query=''
            query+='ORDER BY id DESC LIMIT {}'.format(tedad)





        print(query)
        records = database.full_search(query)
        if records:
            self.table_report.setRowCount(len(records))

            self.set_data(records)
        
        else:
            self.records_table_report=False
            self.show_mesagges(self.search_message,text='داده ای یافت نشد')


    def time_now(self):
        currentTime = QTime.currentTime()
        self.lineEdit_time_end.setText(currentTime.toString('hh:mm:ss'))





    def savefile(self):

        if not self.records_table_report:
            self.eror_window(texts.MESSAGES['take_report_first'][self.language],3)
            return
        filename,_ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        if _=='.xls(*.xls)':
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
            style = xlwt.XFStyle()
            font = xlwt.Font()
            font.bold = True
            style.font = font
            model = self.table_report.model()
            style = xlwt.easyxf('font: bold 1, color red;')

            lista=[]
            listb=[]
            row=self.table_report.rowCount()
            col=self.table_report.columnCount()
            # self.hh_Labels=['Slab ID', 'Date', 'Time','Line','Slab Defects', 'Thickness','Weight','Width','Length','Image Path']
            hh_Labels=['ID','Slab ID', 'Date', 'Time','Line','Slab Defects', 'Thickness','Weight','Width','Length','Image Path']

            for j in range(col):

                sheet.write(0,j+1,hh_Labels[j],style)
            for i in range(1,row+1):
                sheet.write(i,0,i,style)
            for i in range(row):
                # j is always the length of the unique values list of a field of a qgis layer,
                # selected by the user on a previous step
                for j in range(col):
                    a_item = self.table_report.item(i, j)
                    a_name = str(a_item.text())
                    sheet.write(i+1,j+1,a_name)
                    lista.append(a_item)
                    listb.append(a_name)

            
            wbk.save(filename)



    def add_database(self):


        print('add'*50)
        try:
            last_id=database.get_last_id()
            id=last_id+1
        except:
            id=0

        defects=self.read_data_table()

        defects=self.listToString(defects)

        # print('defects',defects)

        
        # if self.slab_id.text() !=self.fault_slab_id:
        new_path = os.path.join(self.parent_dir,self.slab_id.text())
                # self.path=new_path
                # self.path.split('/')
                
        # print('path change')
        

        data=(id,self.slab_id.text(),self.current_date,self.displayTxt_time,self.slab_line.value(),defects,self.slab_thickness.text()\
            ,self.slab_weight.text(),self.slab_width.text(),self.slab_lenght.text(),new_path)

        report=database.add_data(data)
        self.change_folder_name(new_path=new_path)
        self.report_label.setText(str(report))
        # cv2.waitKey(2000)
        self.report_label.setText("")

        # print('report',report)
        # threading.Timer(5,self.change_folder_name,args=(new_path,)).start()
        
        
    def change_folder_name(self,new_path):
        # try:
        import shutil

        if  os.path.split(new_path)[1] not in os.listdir(self.parent_dir):
            os.rename(self.path,new_path)
        else:
            file_names = os.listdir(self.path)
            for file_name in file_names:
                
                shutil.move(os.path.join(self.path, file_name), new_path)
            print('aaaaa')
        # except:
        #     print('Error change name')


    


    def listToString(self,s): 
        
        # initialize an empty string
        str1 = "" 
        
        # traverse in the string  
        for ele in s: 
            str1 += ele  
            str1 +='-'
        
        str1=str1[:-1]
        # return string  
        return str1        

#full_screen_page------------------

    def full_screen_page(self):
    
        self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)




    def show_full_screen(self):

        try:
            if self.last_btn=='fs1_btn':
                imgs=self.image_1
                # imgs=self.image_live_cam_1
            if self.last_btn=='fs2_btn':
                imgs=self.image_2
                # imgs=self.image_live_cam_2
            if self.last_btn=='fs3_btn':
                imgs=self.image_3

                h,w,_ = imgs.shape
                w_label=self.fullscreen_label.width()
                h_label=self.fullscreen_label.height()
                max_=max(h,w)
                x_center = (max_ - w) // 2
                y_center = (max_ - h) // 2
                color = (0,0,0)
                mask = np.full((max_,max_, 3), color, dtype=np.uint8)
                mask[y_center:y_center+h, 
                    x_center:x_center+w] = imgs
                imgs=mask


            if self.last_btn=='fs4_btn':
                imgs=self.image_4
                h,w,_ = imgs.shape
                w_label=self.fullscreen_label.width()
                h_label=self.fullscreen_label.height()
                max_=max(h,w)
                x_center = (max_ - w) // 2
                y_center = (max_ - h) // 2
                color = (0,0,0)
                mask = np.full((max_,max_, 3), color, dtype=np.uint8)
                print('a')
                mask[y_center:y_center+h, 
                    x_center:x_center+w] = imgs
                imgs=mask




            imgs=self.rotate_image(imgs,int(self.rotate_fulll_screen)%4)
            imgs_10 = QImage(imgs,imgs.shape[1],imgs.shape[0],imgs.strides[0], QImage.Format_BGR888 )
            self.fullscreen_label.setPixmap(QPixmap.fromImage(imgs_10))
        
        except:
            
            imgs=cv2.imread('images\error.png')
            imgs_10 = QImage(imgs,imgs.shape[1],imgs.shape[0],imgs.strides[0], QImage.Format_BGR888 )
            self.fullscreen_label.setPixmap(QPixmap.fromImage(imgs_10))


    def rotate_fullscreen(self):
        self.rotate_fulll_screen+=1
        # print(self.rotate_fulll_screen)



    def fs_1(self):
        self.fs_pause_sign.setText('')
        # print(self.cam_1)
        self.last_btn='fs1_btn'
        print( self.last_btn)
        self.fs_cam_name.setText(self.dataset_cam_1_name.text())
        # self.must_full=self.cam_1
        self.full_screen_page()
        self.show_full_screen()

        if self.btn_cam1_sing=='play':
            self.timer_fullscreen.start(100)
    
        else:   
            self.fs_pause_sign.setText('pause')

            self.timer_fullscreen.stop()
    def fs_2(self):
        self.fs_pause_sign.setText('')
        self.last_btn='fs2_btn'
        print(self.last_btn)
        self.fs_cam_name.setText(self.dataset_cam_2_name.text())

        # self.must_full=self.cam_2
        self.full_screen_page()
        self.show_full_screen()

        if self.btn_cam2_sing=='play':

            self.timer_fullscreen.start(100)
    
        else:   

            self.fs_pause_sign.setText('pause')
            self.timer_fullscreen.stop()

    def fs_3(self):
        self.fs_pause_sign.setText('')
        self.last_btn='fs3_btn'
        self.fs_cam_name.setText(self.dataset_cam_3_name.text())
        print(self.last_btn)
        # self.must_full=self.cam_3
        self.full_screen_page()
        self.show_full_screen()

        if self.btn_cam3_sing=='play':

            self.timer_fullscreen.start(100)
    
        else:   

            self.fs_pause_sign.setText('pause')
            self.timer_fullscreen.stop()
    def fs_4(self):
        self.fs_pause_sign.setText('')
        self.last_btn='fs4_btn'
        print(self.last_btn)
        self.fs_cam_name.setText(self.dataset_cam_4_name.text())
        # self.must_full=self.cam_4
        self.full_screen_page()
        self.show_full_screen()

        if self.btn_cam4_sing=='play':

            self.timer_fullscreen.start(100)
    
        else:   

            self.fs_pause_sign.setText('pause')
            self.timer_fullscreen.stop()



#camera_panorama
    def func_start_capture(self):
        

        if self.capturing_mode=='manual':
            if self.start_grabbing_sign==1:
                # self.capture_sign=True

                # while self.capture_sign:
                # time.sleep(0.5)

                if self.create_path:
                    print('start_capture')
                    self.capture_status_btn.setText('Capturing ...')
                self.stop_capture.setDisabled(False)
                self.start_capture.setDisabled(True)
                
                self.save_img_panorama(self.image_1,1,str(self.slab_id.text()))
                self.save_img_panorama(self.image_2,2,str(self.slab_id.text()))
                self.save_img_panorama(self.image_3,3,str(self.slab_id.text()))
                self.save_img_panorama(self.image_4,4,str(self.slab_id.text()))
                



                if self.capture_sign:
                    self.thread_capturing=threading.Timer(self.capturing_time,self.func_start_capture)
                    self.capture_sign=True
                    self.thread_capturing.start()

                    # self.capture_sign=False
            else :
                self.eror_window(texts.MESSAGES['No_Camera_Connection'][self.language],3)
            

        elif self.capturing_mode=='auto':

            if self.start_grabbing_sign==1:
                if self.mode:
                    # self.capture_sign=True

                    # while self.capture_sign:
                    # time.sleep(0.5)
                    if self.create_path:
                        print('start_capture')
                        self.capture_status_btn.setText('Capturing ...')
                    # self.stop_capture.setDisabled(False)
                    # self.start_capture.setDisabled(True)
                    
                    self.save_img_panorama(self.image_1,1,str(self.slab_id.text()))
                    self.save_img_panorama(self.image_2,2,str(self.slab_id.text()))
                    self.save_img_panorama(self.image_3,3,str(self.slab_id.text()))
                    self.save_img_panorama(self.image_4,4,str(self.slab_id.text()))
                    

                    if self.mode:
                        self.thread_capturing=threading.Timer(self.capturing_time,self.func_start_capture)
                    #     # self.capture_sign=False
                        self.capture_sign=True
                    
                        self.thread_capturing.start()

                        # self.capture_sign=False
            else :
                self.eror_window(texts.MESSAGES['No_Camera_Connection'][self.language],3)


    def func_stop_capture(self):

        print('*'*100)
        if self.capture_sign:
            # print('stop capturing')
            if self.thread_capturing.is_alive():

                self.thread_capturing.cancel()
                self.capture_status_btn.setText('')


            self.capture_sign=False
            if self.capturing_mode=='manual':
                self.stop_capture.setDisabled(True)
                self.start_capture.setDisabled(False)
            self.create_path=True
            cv2.waitKey(1000)
            self.add_database()

            self.uncked_defect_table(self.defect_table)


        if self.capturing_mode=='auto':
            self.capture_status_btn.setText('Waiting For Slab ...')
        else:
            self.capture_status_btn.setText('')

            


    def camera_panorama(self):
    
        print('ok')

        if self.camera_panorama_cont==0: 

            self.surf_img_last_cam_1=0
            self.surf_img_last_cam_2=0
            self.surf_img_last_cam_3=0
            self.surf_img_last_cam_4=0

            self.len=self.panorama_lenght
            print(self.len)

            self.list_last=[self.surf_img_last_cam_2,self.surf_img_last_cam_3,self.surf_img_last_cam_4]
            self.images=[self.image_2,self.image_3,self.image_4]
            self.pan_labels=[self.pan_image_label_2,self.pan_image_label_3,self.pan_image_label_4]

            for i in range(len(self.list_last)):

                self.list_last[i]=0
                self.start = True

                x=self.images[i]
                x=cv2.resize(x, (1200, 720))

                self.img=x

                w, h = self.img.shape[:2]
                self.list_last[i] = np.zeros((w,h*self.len,3)).astype('uint8') 


            self.thread_panorama = threading.Timer(0.5,self.pan_capture)

            self.thread_panorama.start()
            self.camera_panorama_cont=1


    def pan_capture(self):
        
        
        if self.start_grabbing_sign==1:

            for i in range((len(self.list_last))):

                # print(i)
                
                x=self.images[i]
                
                # x=cv2.rotate(x, cv2.ROTATE_180)
                # x=x[:,150:-330]
                
                if i==0:
                    x=cv2.resize(x, (720, 720))
                    x= cv2.rotate(x,rotateCode=ROTATE_90_COUNTERCLOCKWISE)
                else:
                    x=cv2.resize(x, (1200, 720))
                x=np.ascontiguousarray(x)
                
                self.img_pan=x
                # image = ImageQt.fromqpixmap(self.pan_image_label_1.pixmap())
                self.list_last[i] = get_pano.get_surf_img(self.img_pan,
                                            surf_img_last=self.list_last[i],
                                            surf_len=self.len,
                                            dim=0)
                width = int(self.list_last[i].shape[1] / 2)
                height = int(self.list_last[i].shape[0] /2)
                dim = (width, height)
                resized = cv2.resize(self.list_last[i], dim, interpolation=cv2.INTER_AREA)

                self.image_live_cam_1_p = QImage(resized,resized.shape[1], resized.shape[0],resized.strides[0], QImage.Format_BGR888 )
                
                self.pan_labels[i].setPixmap(QPixmap.fromImage(self.image_live_cam_1_p)) 

                self.start=False

                self.images=[self.image_2,self.image_3,self.image_4]

            self.thread_panorama = threading.Timer(1,self.pan_capture)

            self.thread_panorama.start()

    def fullscreen_panorama_cam_1(self):
        image = ImageQt.fromqpixmap(self.pan_image_label_1.pixmap())
        image=np.ascontiguousarray(image)
        self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)
        self.fs_cam_name.setText(self.dataset_cam_1_name.text())
        self.fs_pause_sign.setText('')
        self.fs = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
        
        self.fullscreen_label.setPixmap(QPixmap.fromImage(self.fs)) 
 
    def fullscreen_panorama_cam_2(self):
        image = ImageQt.fromqpixmap(self.pan_image_label_2.pixmap())
        image=np.ascontiguousarray(image)
        self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)
        self.fs_cam_name.setText(self.dataset_cam_2_name.text())
        self.fs_pause_sign.setText('')
        self.fs = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
        
        self.fullscreen_label.setPixmap(QPixmap.fromImage(self.fs)) 
 
    def fullscreen_panorama_cam_3(self):
        image = ImageQt.fromqpixmap(self.pan_image_label_3.pixmap())
        image=np.ascontiguousarray(image)
        self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)
        self.fs_cam_name.setText(self.dataset_cam_3_name.text())
        self.fs_pause_sign.setText('')
        self.fs = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
        
        self.fullscreen_label.setPixmap(QPixmap.fromImage(self.fs)) 
 
    def fullscreen_panorama_cam_4(self):
        image = ImageQt.fromqpixmap(self.pan_image_label_4.pixmap())
        image=np.ascontiguousarray(image)
        self.stackedWidget.setCurrentWidget(self.page_fullscreen_2)
        self.fs_cam_name.setText(self.dataset_cam_4_name.text())
        self.fs_pause_sign.setText('')
        self.fs = QImage(image,image.shape[1], image.shape[0],image.strides[0], QImage.Format_BGR888 )
        
        self.fullscreen_label.setPixmap(QPixmap.fromImage(self.fs)) 


#about_slab -----------------------------
    def slab_rate_fun(self):
        a=np.random.randint(5, high=10)
        self.slab_rate.setText(str(a))
        
    def func_default_parametrs(self):
        self.slab_id.setText('0')
        self.melting_id.setText('0')
        self.slab_width.setText('0')
        self.slab_weight.setText('0')
        self.slab_lenght.setText('0')
        self.slab_thickness.setText('0')




    def defect_list(self):
        entries = ['Is-suit']
        self.listWidget.addItems(entries)
        self.func_default_parametrs()
        self.slab_rate.setText('-')


    def set_plc_values(self):
        flag,dict_plc = plc_connection.get_plc_values()
        self.dict_plc = dict_plc
        # parms = ['slab_id','meltting_id','slab_length','slab_width','line_speed']
        if not flag:
            print('error in get plc data')

        dict_plc['slab_id'] = dict_plc['slab_id'].replace('\n','')
        dict_plc['slab_id'] = dict_plc['slab_id'].replace(' ','_')
        dict_plc['meltting_id'] = dict_plc['meltting_id'].replace('\n','')
        dict_plc['meltting_id'] = dict_plc['meltting_id'].replace(' ','_')


        if DEBUG and int(dict_plc['slab_id'])<=-1:
            dict_plc['slab_id'] =str(int(self.slab_id.text())-1)


        self.slab_id.setText(dict_plc['slab_id'])
        self.melting_id.setText(dict_plc['meltting_id'])
        self.slab_width.setText(dict_plc['slab_width'])
        # self.slab_weight.setText(dict_plc['slab_id'])
        self.slab_lenght.setText(dict_plc['slab_length'])
        # self.slab_thickness.setText(dict_plc['slab_id'])

        # if self.last_str_slab_id !=self.str_slab_id:
        #     self.label_sizing





        threading.Timer(1,self.set_plc_values).start()

        if self.capture_sign:
            self.folder_slab_id = self.dict_plc['slab_id']



# capturing --------------------------



    def fun_automatic_capture(self):
    
        self.capturing_mode='auto'
        self.start_capture.setDisabled(True)
        self.set_slab_details(True)
        # self.stop_capture.setDisable
        
        

    def fun_manual_capture(self):

        self.capturing_mode='manual'
        self.start_capture.setDisabled(False)
        self.stop_capture.setDisabled(False)
        self.set_slab_details(False)


    def set_slab_details(self,enable):
        list1=[self.slab_lenght,self.slab_weight,self.slab_width,self.slab_line,self.slab_thickness]
        #self.slab_id,
        for i in range(len(list1)):
            list1[i].setDisabled(enable)






#backup -------------------------------

    def create_backup(self):
        try:
            if self.Is_login:
                self.window_backup.set_data(self.records_table_report)
                self.window_backup.show()
            else:
                self.eror_window(msg=texts.MESSAGES['Please_Login'][self.language],level=2)
        except:
            self.eror_window(msg=texts.MESSAGES['take_report_first'][self.language],level=2)

        

        print('ok')

#click--------------------------

    def buttonClick(self,x=True):

            # cv2.waitKey(2000)
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
       # SHOW HOME PAGE
        if btnName == "capture_btn":
            print('asdqwewqe')
        if btnName =='connect_btn':

            print(self.start_grabbing_sign)
            if self.start_grabbing_sign==0:
                # try:
            # qwe        
                    self.obj=camera_get_len.Collector()
                    
                    if len(self.obj.check_devices()) >0 or DEBUG:

                        self.report_label.setText('Connecting')

                        self.initialize_cams()
                        self._running = True
                        self.wait=False
                        self.connect_btn.setDisabled(True)
                        self.calibrate_btn.setDisabled(False)

                        self.setup_camera()

                        QTimer.singleShot(300000, lambda: self.check_and_eror_calibrate())




                    else:
                        self.eror_window(texts.MESSAGES['No_Camera_Connection'][self.language],3)
 

                        
                # except:
                #     print('no camera connecte d')

            else:
                print('already connected')

        if btnName =='disconnect_btn':
            
            self.disconnect_func()

        if btnName == "save_btn":
            self.save()
        if btnName == 'setting_btn':
            print('setting')

            self.setting_window()
        if btnName =='user_btn':
            self.login_window()
             
        if btnName =='toggleButton':
            self.open_close_menu()


        if btnName =='right_box_btn':
            self.right_box_func()

        if btnName =='login_btn':
            self.login()
        if btnName == 'logout_btn':
            self.confirm_window(def_name='logout')
        if btnName == "live_btn":
            # time.sleep(2)
            self.timer_fullscreen.stop()
            try:
                self.thread_panorama.stop()
            except:
                pass
            self.stackedWidget.setCurrentWidget(self.page_live)
            self.last_btn='live_btn'
            # self.timer_fullscreen.stop()
            #self.page_layout1()
        if btnName == "page_live_dataset_btn":
            self.timer_fullscreen.stop()
            self.stackedWidget.setCurrentWidget(self.page_live_dataset)
            self.last_btn='page_live_dataset_btn'
            print(self.last_btn)
        if btnName == 'page_aboutus_btn':
            self.stackedWidget.setCurrentWidget(self.page_aboutus)
      
        if btnName == 'panorama_btn':
            self.stackedWidget.setCurrentWidget(self.page_panorama)
            if self.start_grabbing_sign==1:
                self.camera_panorama()

     

            
        if btnName == 'save_close_btn':
            print('yes')
            self.refresh()
        if btnName == 'fs1_btn':
            print('asdw')
            self.full_screen_page()

        if btnName == 'live_cam_1_capture':
            print('asdw')
            self.save_imed_img(self.cam_1,self.live_image_label_1,self.live_cam_1_name,self.L_notif_cam_1)

        if btnName == 'live_cam_2_capture':
            print('asdw')
            self.save_imed_img(self.cam_2,self.live_image_label_2,self.live_cam_2_name,self.L_notif_cam_2)
        
        if btnName == 'live_cam_3_capture':
            print('asdw')
            self.save_imed_img(self.cam_3,self.live_image_label_3,self.live_cam_3_name,self.L_notif_cam_3)
        
        if btnName == 'live_cam_4_capture':
            print('asdw')
            self.save_imed_img(self.cam_4,self.live_image_label_4,self.live_cam_4_name,self.L_notif_cam_4)    
        
        if btnName == 'fs_cam__capture':
            print('asdw')
            self.save_imed_img('cam',self.fullscreen_label,self.fs_cam_name,self.L_notif_cam_4)
        if btnName == 'D_cam_1_capture':
            print('asdw')
            self.save_imed_img(self.cam_1,self.datalive_image_label_1,self.live_cam_1_name,self.D_notif_cam_1)

        if btnName == 'D_cam_2_capture':
            print('asdw')
            self.save_imed_img(self.cam_2,self.datalive_image_label_2,self.live_cam_2_name,self.D_notif_cam_2)
        
        if btnName == 'D_cam_3_capture':
            print('asdw')
            self.save_imed_img(self.cam_3,self.datalive_image_label_3,self.live_cam_3_name,self.D_notif_cam_3)
        
        if btnName == 'D_cam_4_capture':
            print('asdw')
            self.save_imed_img(self.cam_4,self.datalive_image_label_4,self.live_cam_4_name,self.D_notif_cam_4)    

        if btnName == 'start_capture':
            self.capture_sign=True
    
            # self.save_img_panorama(self.image_head,1,str(self.slab_id.text()))  # save head image

            self.func_start_capture()
        
        if btnName == 'stop_capture':

            self.func_stop_capture()
        
        if btnName == 'automatic_btn':

            self.fun_automatic_capture()
        
        if btnName == 'manual_btn':

            self.fun_manual_capture()
        
        
        if btnName == 'slab_rate_manual':

            self.get_data('slab_rate')
        
        
        if btnName == 'slab_id_manual':

            self.get_data('slab_id')
        
        
        if btnName == 'slab_line_manual':

            self.get_data('slab_line')
        
        
        if btnName == 'slab_width_manual':

            self.get_data('slab_width')
        
        
        if btnName == 'slab_lenght_manual':

            self.get_data('slab_lenght')
        
        
        if btnName == 'slab_thickness_manual':
      
            self.get_data('slab_thickness')
        
        
        if btnName == 'manual_btn':
  
            self.fun_manual_capture()
        
        
        
        if btnName == 'backup_btn':
 
            self.create_backup()
        
        
        
        if btnName == 'toogle_cam_1':
   
            self.open_close_camera_bar(1)
        
        if btnName == 'toogle_cam_2':
  
            self.open_close_camera_bar(2)
        
        if btnName == 'toogle_cam_3':

            self.open_close_camera_bar(3)
        
        if btnName == 'toogle_cam_4':

            self.open_close_camera_bar(4)
        

            

    def set_image_label(self,label_name, img):
        h, w, ch = img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = sQImage(img.data, w, h, bytes_per_line, sQImage.Format_BGR888)


        label_name.setPixmap(sQPixmap.fromImage(convert_to_Qt_format))

    def set_pixmap(self,label_name,img_path):
        pixmap = sQPixmap(img_path)
        label_name.setPixmap(pixmap)




    def get_table_value(self,item):
        # http://www.python-forum.org/viewtopic.php?f=11&t=16817
        cellContent = item.data()
        sf = "You clicked on {}".format(cellContent)
        print(sf)
        if item.column()==9:
            self.open_images(cellContent)

    
    def open_images(self,folder_path):
        try:
            path = os.path.realpath(folder_path)
            os.startfile(path)
        except:
            self.eror_window(msg='Path not Exist',level=2)


    def do_calibrate(self):
        ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['calibrate_message'][self.language])
        if ret:
            self.calibration()

    def calibration(self):
            print('calibrated')
            #calibrate edge camera //////////////
            frame =self.image_1
            # frame= frame[500:-800, 200:]
            frame= frame[self.camera_1_calibration_parms[2]:self.camera_1_calibration_parms[4],self.camera_1_calibration_parms[1]:self.camera_1_calibration_parms[3]]
            # cv2.imshow('a',frame)
            # cv2.waitKey(0)
            # frame= frame[500:-800, 200:]
            self.slab_detection_obj.update_refrence_frame(refrence_frame=frame)
            #////////////////////////////////////
            #calibrate side camera //////////////
            frame=self.image_4
            frame = frame[0:200, 200:600]

            self.slab_detection_obj_side.update_refrence_frame(refrence_frame=frame)
            #////////////////////////////////////
            self.flag_calibration = True
    def show_question(self, title, message,question=True):
        """Show question window with specefic message
        Args:
            title (str) : set Title of window
            message (str) : set message of window
        Return (bool) : True/False
        """
        if question:
            msg = QMessageBox.question(
                self, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if msg == QMessageBox.Yes:
                return True
            if msg == QMessageBox.No:
                return False
        else:
            msg = QMessageBox.question(
                self, title, message, QMessageBox.Ok
            )
            if msg == QMessageBox.Ok:
                return True

    def manage_space_main(self):
        if not DEBUG:
            storage_manament.create_thread(self.parent_dir,time=5,threshold=0.88)

    def show_time(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'tool_start_time':
            self.set_field_time = 'start'
        
        elif btnName == 'tool_end_time':
            self.set_field_time = 'end'

        self.obj_clock.show()
    
    def set_time(self):

        self.obj_clock.close()
        if self.set_field_time == 'start':
            self.lineEdit_time_start.setText(self.obj_clock.time)
        elif self.set_field_time == 'end':
            self.lineEdit_time_end.setText(self.obj_clock.time)


    def show_calender(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'tool_start_calender':
            self.set_field_date = 'start'
        
        elif btnName == 'tool_end_calender':
            self.set_field_date = 'end'

        self.obj_calender.show()

    def set_date(self):
    
        self.obj_calender.close()
        if self.set_field_date == 'start':
            self.lineEdit_date_start.setText(self.obj_calender.selectd_date)
        elif self.set_field_date == 'end':
            self.lineEdit_date_end.setText(self.obj_calender.selectd_date)


   

    def adjust_contrast_brightness(self,img, contrast:float=1.0, brightness:int=1,sharpness:int = 1, saturation : int = 1,gama:float = 1.0,r=0,g=0,b=0,hsv = True):
        """
        Adjusts contrast and brightness of an uint8 image.
        contrast:   (0.0,  inf) with 1.0 leaving the contrast as is
        brightness: [-255, 255] with 0 leaving the brightness as is
        """
        brightness += int(round(255*(1-contrast)/2))
        img = cv2.addWeighted(img, contrast, img, 0, brightness)
        #
        img = self.gammaCorrection(img , gama)

        #hsv
        # cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img[:,:,0] += b
        img[:,:,1] += g
        img[:,:,2] += r




        if hsv:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        return img

    


    def gammaCorrection(self,src, gamma):
        invGamma = 1 / gamma

        table = [((i / 255) ** invGamma) * 255 for i in range(256)]
        table = np.array(table, np.uint8)

        return cv2.LUT(src, table)


    def set_big_label(self,e):


        btn = self.sender()
        btnName = btn.objectName()

        if btnName == 'checkBox_top':
            self.big_label = 'top'
            # self.checkBox_head.clicked()
            self.checkBox_head.setChecked(False)
        else:
            self.big_label ='head'
            self.checkBox_top.setChecked(False)




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



    def check_and_eror_calibrate(self):
        if self._running:
            if not self.flag_calibration:
                ret = self.show_question(texts.MESSAGES['message'][self.language],texts.MESSAGES['do_calibrate'][self.language],question=False)
                QTimer.singleShot(300000, lambda: self.check_and_eror_calibrate())




    def open_user_manual_file(self):
        import webbrowser
        path = "salb_user_manual.pdf"
        os.system(path)



if __name__ == "__main__":
    app = QApplication()
    app.setAttribute(sQtCore.Qt.AA_EnableHighDpiScaling)
    win = UI_main_window()
    win.show()
    sys.exit(app.exec())
    




