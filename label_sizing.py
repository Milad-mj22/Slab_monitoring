
import sqlite3
from sqlite3 import Error

from PySide6.QtCore import *

from PySide6.QtWidgets import *

def size(self):
    conn = self.create_connection('settings.db')
    cur = conn.cursor() 
    cur.execute('select * from labels_size')
    rec = cur.fetchall()
    conn.commit()
    conn.close()    
    resizing12(self,rec)
    return str(rec[0][0])

def resizing12(self,rec):
    labels=[self.live_image_label_1,self.live_image_label_2,self.live_image_label_3,self.live_image_label_4,self.frame_camera_1,self.datalive_image_label_2,self.datalive_image_label_3,self.datalive_image_label_4]
    for i in range(len(labels)):
        labels[i].setMaximumWidth(rec[i][0])
      #  labels[i].setMinimumWidth(rec[i][0])
        labels[i].setMaximumHeight(rec[i][1])
      #  labels[i].setMinimumHeight(rec[i][0])
    # print('yes')
    # self.horizontalSlider_cam1.setMaximumWidth(rec[0][0])
    # self.verticalSlider_5.setMaximumHeight(rec[1][1])
    # self.verticalSlider_6.setMaximumHeight(rec[2][1])
    # self.verticalSlider_7.setMaximumHeight(rec[3][1])
    # self.frame_11.setMaximumWidth(rec[0][0]+20)
    # self.live_image_label_5.setMaximumWidth(rec[0][0])
    self.live_image_label_5.setMaximumWidth(600)
    # self.live_image_label_5.setMaximumHeight(rec[0][1])
    self.frame_camera_1.setMinimumWidth(rec[4][0])


