
import sys
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
import sqlite3
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import PySide6.QtCore as sQtCore


ui2, _ = loadUiType("image_process.ui")
KEYS =['brightness','sharpness','contrast','gama','r','g','b','hsv']

class UI_image_processing(QMainWindow, ui2):
    global widgets
    widgets_eror = ui2
    image_glob=0
    close_sign=0


    

    def __init__(self):
        super(UI_image_processing, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        # self.set_selected_camera(1)
        self._old_pos = None

        self.apply_btn.clicked.connect(self.save_data)
        if __name__ == "__main__":
            self.connect_value_change()
            self.fetch_data()
        # self.save_data()

        # self.set_page(1)
        
        
    def set_page(self,num):
        num = int(num)
        if num ==1:
            self.stackedWidget.setCurrentWidget(self.page_cam_1)
        elif num ==2:
            self.stackedWidget.setCurrentWidget(self.page_cam_2)
        elif num ==3:
            self.stackedWidget.setCurrentWidget(self.page_cam_3)
        elif num ==4:
            self.stackedWidget.setCurrentWidget(self.page_cam_4)


    def mousePressEvent(self, event):
        btn = self.sender()
        # btnName = btn.objectName()
        if event.button() == sQtCore.Qt.LeftButton and not self.isMaximized():
            # accept event only on top and side bars
            if event.position().y()<=self.login_welcome_2.height() :#or event.position().x()<=self.login_welcome_2.width():
                self._old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        if event.button() == sQtCore.Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return
        delta = sQtCore.QPoint(event.globalPosition().toPoint() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPosition().toPoint()
        
    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)
        self.close_btn_2.clicked.connect(self.close_win)
    def close_win(self):
        self.close()
        
    def set_selected_camera(self,cam_num):
        self.label_selected_camera.setText('Camera '+str(cam_num))


    def set_ui_obj(self,ui_obj):
        self.ui_obj = ui_obj

    def connect_value_change(self):
        # cams = []
        for key in KEYS:
            for i in range(1,5):
                if key !='hsv':
                        exec('self.slider_{}_cam_{}.valueChanged.connect(self.change_value)'.format(key,i))
                else:
                    exec('self.checkBox_hsv_cam_{}.stateChanged.connect(self.set_checkbox)'.format(i))
                    exec('self.checkBox_default_cam_{}.stateChanged.connect(self.set_default)'.format(i))

        # self.slider_brightness_cam_1.valueChanged.connect(self.change_value)

    def change_value(self,e):
        btn = self.sender()
        btnName = btn.objectName()
        # print(btnName)
        name = btnName.split('_')[1]
        cam_num = btnName.split('_')[3]
        full_name = str(name)+'_cam_'+str(cam_num)
        # ui_btn = eval('self.ui_obj.{}'.format(full_name))
        exec('self.ui_obj.{} = btn.value()'.format(full_name))




    def set_checkbox(self,e):
        btn = self.sender()
        btnName = btn.objectName()
        # print(btnName)
        name = btnName.split('_')[1]
        cam_num = btnName.split('_')[3]
        full_name = str(name)+'_cam_'+str(cam_num)

        exec('self.ui_obj.{} = btn.isChecked()'.format(full_name))


    def set_default(self,e):
        btn = self.sender()
        btnName = btn.objectName()
        print('btnName',btnName)
        name = btnName.split('_')[1]
        cam_num = btnName.split('_')[3]     
        full_name = str(name)+'_cam_'+str(cam_num)

        # exec('self.ui_obj.{} = btn.isChecked()'.format(full_name))
        default_hsv = False
        default_values = 0

        if btn.isChecked():
            print('yes')
            # for i in range(0,4):
            #     cam = i+1
            for _,key in enumerate(KEYS):
                if key=='hsv':
                    s='self.checkBox_hsv_cam_{}.setChecked(False)'.format(cam_num,default_hsv)
                else:
                    s='self.slider_{}_cam_{}.setValue({})'.format(key,cam_num,default_values)
                exec(s)



    def fetch_data(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        cur.execute('select * from image_processing')
        parms = cur.fetchall()   
        # print('live_recfresh_rate  ',parms)
        for i in range(0,4):
            cam = i+1
            for _,key in enumerate(KEYS):
                if key=='hsv':
                    bool_ = (parms[i][_])
                    s='self.checkBox_hsv_cam_{}.setChecked({})'.format(cam,bool_)
                else:
                    s='self.slider_{}_cam_{}.setValue(parms[i][_])'.format(key,cam)

                try:
                    full_name = str(key)+'_cam_'+str(cam)
                    exec('self.ui_obj.{} = {}'.format(full_name,parms[i][_]))
                    # eval('self.ui_obj.{} = '.format(full_name))
                except:
                    print('eror')
                # print(cam , key)
                exec(s)



    def save_data(self):


        # sql = "UPDATE Theme SET color = '{}' WHERE id = 0".format(text)
        # cur.execute(sql)         
        # conn.commit()
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        # cur.execute('select * from image_processing')
        parms = cur.fetchall()   
        # print('live_recfresh_rate  ',parms)
        for i in range(0,4):
            cam = i+1
            for _,key in enumerate(KEYS):
                if key=='hsv':
                    # return
                    s='self.checkBox_hsv_cam_{}.isChecked()'.format(cam)
                    # print('ssssssssss',s)
                    # s=exec(s)
                else:
                    s='self.slider_{}_cam_{}.value()'.format(key,cam)
                s=eval(s)
                # print('ssssssssss',s)
                sql = "UPDATE image_processing SET '{}' = '{}' WHERE id = '{}'".format(key,s,cam)
                cur.execute(sql) 
                conn.commit()
   

        
        self.close()
                





if __name__ == "__main__":
    app = QApplication()
    win = UI_image_processing()
    win.show()
    sys.exit(app.exec())
