from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
import sqlite3
from sqlite3 import Error

from PySide6.QtCore import *

from PySide6.QtWidgets import *
def color(self):
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()       
    cur.execute('select * from Theme')
    rec = cur.fetchall()
    conn.commit()
    conn.close()    
    if str(rec[0][0])=='Blue-White':
        set_color_main_blue(self)
    if str(rec[0][0])=='Green_Gray':
        set_color_main_green(self)
# self.refresh_btn.setStyleSheet("QPushButton { background-color: yellow }")
def set_color_main_blue(self):
    self.centralwidget.setStyleSheet("QWidget { background-color: rgb(0,36,115); }")
    self.page_live.setStyleSheet("QWidget { background-color: rgb(230,230,249); }")
    self.page_report.setStyleSheet("QWidget { background-color: rgb(230,230,249); }")
    self.page_fullscreen_2.setStyleSheet("QWidget { background-color: rgb(230,230,249); }")
    self.page_aboutus.setStyleSheet("QWidget { background-color: rgb(230,230,249); }")
    frame_list=[self.frame87,self.frame_4,self.frame_camera_1,self.framw_camera,\
        self.frame_3,self.frame\
            ,self.frame_17,self.frame_21,self.Body_2,self.Container_2,self.aframe_2]
    for i in range(len(frame_list)):
        frame_list[i].setStyleSheet("QFrame { background-color: rgb(230,230,249); }")
    btn_list=[self.live_btn,self.page_live_dataset_btn,self.panorama_btn,self.page_fullscreen,self.page_report_btn\
        ,self.logout_btn,self.page_aboutus_btn,self.cam_1_btn,self.cam_2_btn,self.cam_3_btn,self.cam_4_btn]
    for i in range(len(btn_list)):
        btn_list[i].setStyleSheet("QPushButton { background-color: rgb(249,249,249);text-align: left;padding-left: 10px; }")
    self.leftMenu.setStyleSheet("QFrame { background-color: rgb(0,36,115); }")
    self.leftMenu_2.setStyleSheet("QFrame { background-color: rgb(230,230,249); }")
    self.userFrame.setStyleSheet("QFrame { background-color: rgb(0,36,115); }")
    self.headerFrame.setStyleSheet("QFrame { background-color: rgb(0,36,115); }")
    self.label_3.setStyleSheet("QLabel { background-color: rgb(0,36,115); color :rgb(249,249,249) ; }")
    self.label.setStyleSheet("QLabel { background-color: rgb(0,36,115); }")
    self.label_5.setStyleSheet("QLabel { background-color: rgb(0,36,115); }")
    self.label_44.setStyleSheet("QLabel { background-color: rgb(0,36,115); }")
    self.label_23.setStyleSheet("QLabel { background-color: rgb(0,36,115); }")
    self.label_5.setStyleSheet("QLabel { background-color: rgb(0,36,115); }")
    self.toggleFrame.setStyleSheet("QFrame { background-color: rgb(0,36,115); }")
    self.closeButton.setStyleSheet("QPushButton { border: none;background-color: rgb(0,36,115); } QPushButton:hover {	background-color: rgb(255, 38, 0);}QPushButton:pressed {	background-color: rgb(255, 0, 0); }")
    self.maxiButton.setStyleSheet("QPushButton { border: none;background-color: rgb(0,36,115); } QPushButton:hover {	background-color: rgb(255, 38, 0);}QPushButton:pressed {	background-color: rgb(255, 0, 0); }")
    self.miniButton.setStyleSheet("QPushButton { border: none;background-color: rgb(0,36,115);} QPushButton:hover {	background-color: rgb(255, 38, 0);}QPushButton:pressed {	background-color: rgb(255, 0, 0); }")
    self.toggleButton_6.setStyleSheet("QPushButton {	border: none;	background-color: rgb(0,36,115);	border-left: 1px solid rgb(30, 30, 30);	border-right:1px solid rgb(30, 30, 30);	color: rgb(255, 85, 0);	border-radius: 13px; }QPushButton:hover {border: 1px solid rgb(0,0, 0); }QPushButton:pressed {	background-color: rgb(25, 25, 25); }")
    self.user_btn.setStyleSheet("QPushButton {	border: none;	background-color: rgb(0,36,115);	border-left: 1px solid rgb(30, 30, 30);	border-right:1px solid rgb(30, 30, 30);	color: rgb(255, 85, 0);	border-radius: 13px; } QPushButton:hover {border: 1px solid rgb(0,0, 0); } QPushButton:pressed {	background-color: rgb(25, 25, 25); }")
    self.setting_btn.setStyleSheet("QPushButton {	border: none;	background-color: rgb(0,36,115);	border-left: 1px solid rgb(30, 30, 30);	border-right:1px solid rgb(30, 30, 30);	color: rgb(255, 85, 0);	border-radius: 13px; } QPushButton:hover {border: 1px solid rgb(0,0, 0); } QPushButton:pressed {	background-color: rgb(25, 25, 25); }")
    self.toggleButton.setStyleSheet("QPushButton { border: none;background-color: rgb(0,36,115);}QPushButton:hover {background-color: rgb(255, 38, 0);}QPushButton:pressed {background-color: rgb(255, 0, 0);}")
    self.refresh_btn.setStyleSheet("QPushButton { background-color: rgb(249,249,249);}")
    self.save_btn.setStyleSheet("QPushButton { background-color: rgb(249,249,249);}")
    # self.start_btn.setStyleSheet("QPushButton { background-color: rgb(249,249,249);}")
    # self.start_btn_live.setStyleSheet("QPushButton { background-color: rgb(249,249,249);}")

def set_color_main_green(self):
    self.centralwidget.setStyleSheet("QWidget { background-color: rgb(1, 182, 54); }")
    self.page_live.setStyleSheet("QWidget { background-color: rgb(116, 227, 154); }")
    self.page_report.setStyleSheet("QWidget { background-color: rgb(116, 227, 154); }")
    self.page_fullscreen_2.setStyleSheet("QWidget { background-color: rgb(116, 227, 154); }")
    self.page_aboutus.setStyleSheet("QWidget { background-color: rgb(116, 227, 154); }")
    frame_list=[self.frame87,self.frame_4,self.frame_camera_1,self.framw_camera,\
        self.frame_3,self.frame\
            ,self.frame_17,self.frame_21,self.Body_2,self.Container_2,self.aframe_2]
    for i in range(len(frame_list)):
        frame_list[i].setStyleSheet("QFrame { background-color: rgb(116, 227, 154); }")
    btn_list=[self.live_btn,self.page_live_dataset_btn,self.panorama_btn,self.page_fullscreen,self.page_report_btn\
        ,self.logout_btn,self.page_aboutus_btn,self.cam_1_btn,self.cam_2_btn,self.cam_3_btn,self.cam_4_btn]
    for i in range(len(btn_list)):
        btn_list[i].setStyleSheet("QPushButton { background-color: rgb(116, 227, 154);text-align: left;padding-left: 10px; }")
    self.leftMenu.setStyleSheet("QFrame { background-color: rgb(1, 182, 54); }")
    self.leftMenu_2.setStyleSheet("QFrame { background-color: rgb(116, 227, 154); }")
    self.userFrame.setStyleSheet("QFrame { background-color: rgb(1, 182, 54); }")
    self.headerFrame.setStyleSheet("QFrame { background-color: rgb(1, 182, 54); }")
    self.label_3.setStyleSheet("QLabel { background-color: rgb(224,224,224); color :rgb(152, 152, 152) ; }")
    self.label.setStyleSheet("QLabel { background-color: rgb(1, 182, 54); }")
    self.label_5.setStyleSheet("QLabel { background-color: rgb(1, 182, 54); }")
    self.label_44.setStyleSheet("QLabel { background-color: rgb(1, 182, 54); }")
    self.label_23.setStyleSheet("QLabel { background-color: rgb(1, 182, 54); }")
    self.label_5.setStyleSheet("QLabel { background-color: rgb(1, 182, 54); }")
    self.toggleFrame.setStyleSheet("QFrame { background-color: rgb(1, 182, 54); }")
    self.closeButton.setStyleSheet("QPushButton { border: none;background-color: rgb(1, 182, 54); } QPushButton:hover {	background-color: rgb(255, 38, 0);}QPushButton:pressed {	background-color: rgb(255, 0, 0); }")
    self.maxiButton.setStyleSheet("QPushButton { border: none;background-color: rgb(1, 182, 54); } QPushButton:hover {	background-color: rgb(255, 38, 0);}QPushButton:pressed {	background-color: rgb(255, 0, 0); }")
    self.miniButton.setStyleSheet("QPushButton { border: none;background-color: rgb(1, 182, 54);} QPushButton:hover {	background-color: rgb(255, 38, 0);}QPushButton:pressed {	background-color: rgb(255, 0, 0); }")
    self.toggleButton_6.setStyleSheet("QPushButton {	border: none;	background-color: rgb(1, 182, 54);	border-left: 1px solid rgb(30, 30, 30);	border-right:1px solid rgb(30, 30, 30);	color: rgb(255, 85, 0);	border-radius: 13px; }QPushButton:hover {border: 1px solid rgb(0,0, 0); }QPushButton:pressed {	background-color: rgb(25, 25, 25); }")
    self.user_btn.setStyleSheet("QPushButton {	border: none;	background-color: rgb(1, 182, 54);	border-left: 1px solid rgb(30, 30, 30);	border-right:1px solid rgb(30, 30, 30);	color: rgb(255, 85, 0);	border-radius: 13px; } QPushButton:hover {border: 1px solid rgb(0,0, 0); } QPushButton:pressed {	background-color: rgb(25, 25, 25); }")
    self.setting_btn.setStyleSheet("QPushButton {	border: none;	background-color: rgb(1, 182, 54);	border-left: 1px solid rgb(30, 30, 30);	border-right:1px solid rgb(30, 30, 30);	color: rgb(255, 85, 0);	border-radius: 13px; } QPushButton:hover {border: 1px solid rgb(0,0, 0); } QPushButton:pressed {	background-color: rgb(25, 25, 25); }")
    self.toggleButton.setStyleSheet("QPushButton { border: none;background-color: rgb(1, 182, 54);}QPushButton:hover {background-color: rgb(255, 38, 0);}QPushButton:pressed {background-color: rgb(255, 0, 0);}")
    self.refresh_btn.setStyleSheet("QPushButton { background-color: rgb(152, 152, 152);}")
    self.save_btn.setStyleSheet("QPushButton { background-color: rgb(152, 152, 152);}")
    # self.start_btn.setStyleSheet("QPushButton { background-color: rgb(152, 152, 152);}")
    # self.start_btn_live.setStyleSheet("QPushButton { background-color: rgb(152, 152, 152);}")








    


