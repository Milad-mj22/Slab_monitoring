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
from PyQt5 import QtCore
import sqlite3

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
import detect_lenguage


ui2, _ = loadUiType("default_setting.ui")

conn = sqlite3.connect('settings.db')
cur = conn.cursor()


class UI_default_setting_window(QMainWindow, ui2):
    global widgets
    widgets_eror = ui2
    sign=0
    def __init__(self):
        super(UI_default_setting_window, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.save_btn.clicked.connect(self.get_text)
        self.save_close_btn.clicked.connect(self.save_close)
        self.def_style()
        self.cam_names()
        self.language()
        self.set_language()
        self.label_size()
        self.Theme()
        self.font()
        self.width()
        self.capturing_time()
        self.set_image_format()
        self.set_address_path()
        self.live_refresh_rate()
        
        

        #self.comboBox_23.itemClicked.connect(self.on_itemClicked)
        self.manual_capturing.clicked.connect(self.check)
        self.auto_capturing.clicked.connect(self.check)
        self.manual_spped_line.clicked.connect(self.check)
        self.auto_spped_line.clicked.connect(self.check)
        self.manual_panorama_lenght.clicked.connect(self.check)
        self.auto_panorama_lenght.clicked.connect(self.check)

        self.toolButton_image_folder.clicked.connect(self.open_folder_dialog)
        self.toolButton_image_folder_2.clicked.connect(self.open_folder_dialog_2)

        self._old_pos = None

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




    # method called by radio button

    def set_language(self):
        if detect_lenguage.language()=='Persian(فارسی)':
            detect_lenguage.default_setting(self)




    def open_folder_dialog(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_image_directory.setText(file)


    def open_folder_dialog_2(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_image_directory_2.setText(file)

    def check(self):
        # checking if it is checked

        #capturing --------------

        if self.manual_capturing.isChecked():

            # changing text of label
            self.label.setText("It is now checked")
            self.spinBox_capturing_time.setDisabled(False)

        if self.auto_capturing.isChecked():

            # changing text of label
            self.label.setText("It is now checked")
            self.spinBox_capturing_time.setDisabled(True)
        # ///////////////////
        #speed line-------------
        if self.manual_spped_line.isChecked():

            # changing text of label
            self.label.setText("It is now checked")
            self.lineEdit_speed_line.setDisabled(False)
        
        if self.auto_spped_line.isChecked():

            # changing text of label
            self.label.setText("It is now checked")
            self.lineEdit_speed_line.setDisabled(True)
        # /////////////////
        #panorama lenght ---------

        if self.manual_panorama_lenght.isChecked():

            # changing text of label
            self.label.setText("It is now checked")
            self.spinBox_panorama_lenght.setDisabled(False)
        
        if self.auto_panorama_lenght.isChecked():

            # changing text of label
            self.label.setText("It is now checked")
            self.spinBox_panorama_lenght.setDisabled(True)   
        # ////////////////    
        




    def width(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from table_width')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    

        self.table_width_left.setValue(int(rec[0][0]))
        self.table_width_right.setValue(int(rec[0][1]))




    def font(self):
        x=['Arial', 'Arial Black', 'Forte', 'Gigi', 'jokerman' ,'Times New Roman' , 'Zilla Slab']
        self.comboBox_font.addItems(x)
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from font')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    

        self.comboBox_font.setCurrentText(str(rec[0][0]))
        self.spinBox_2.setValue(int(rec[0][1]))


    def set_image_format(self):
        x=['JPG', 'TIFF', 'BMP', 'JPEG', 'PNG']
        self.comboBox_image_format.addItems(x)       
        self.comboBox_imed_image_format.addItems(x)       



    def set_address_path(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from path')
        rec = cur.fetchall()
        # print(rec)
        self.lineEdit_image_directory.setText(rec[0][0])
        self.lineEdit_image_directory_2.setText(rec[1][0])

        self.comboBox_image_format.setCurrentText(str(rec[0][3]))
        self.comboBox_imed_image_format.setCurrentText(str(rec[1][3]))

        self.spinbox_image_quality.setValue(int(rec[0][2]))
        self.spinbox_imed_image_quality.setValue(int(rec[1][2]))
        
        cur.execute('select * from refresh_rate')
        rec = cur.fetchall()
        self.spinBox_panorama_lenght.setValue(int(rec[0][3]))
        # rec = cur.fetchall()




    def def_style(self):
        x=['JPG', 'TIFF', 'BMP', 'JPEG', 'PNG']
        self.comboBox_22.addItems(x)
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from setstyle')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    
        self.comboBox_image_format.setCurrentText(str(rec[0][0]))
        # self.lineEdit_image_directory.setText

    def def_style(self):
        x=['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
        self.comboBox_22.addItems(x)
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from setstyle')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    
        self.comboBox_22.setCurrentText(str(rec[0][0]))


    def language(self):
        x=['English','Persian(فارسی)','Russian']
        self.comboBox_23.addItems(x)
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from language')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    
        self.comboBox_23.setCurrentText(str(rec[0][0]))

    def Theme(self):
        x=['Gray','Blue-White','Dark','Green_Gray']
        self.comboBox_24.addItems(x)
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from Theme')
        rec = cur.fetchall()
        conn.commit()
        conn.close()    
        self.comboBox_24.setCurrentText(str(rec[0][0]))

    def capturing_time(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from capturing_time')
        rec = cur.fetchall()
        self.spinBox_capturing_time.setValue(rec[0][1])


    def live_refresh_rate(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from live_refresh_rate')
        rec = cur.fetchall()
        self.lineEdit_refresh_rate.setText(str(rec[0][1]))



    def activate_(self):
        self.close_btn_2.clicked.connect(self.close_win)
        self.close_btn.clicked.connect(self.close_win)

        self.def_defect_list()
    def close_win(self):
        self.close()
    def def_defect_list(self):
        cur.execute('select * from defect')
        records = cur.fetchall()

        str1=''    
        for i in records:
            str1 = str1 + '\n'+ str(i[0])   

        self.textEdit_1.setText(str(str1))
    def get_text(self):
        text=self.textEdit_1.toPlainText()
      #  listRes = list(x.split(" "))
        text =text.split()
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()

        new_records=[]
        for i in range(1,(len(text)+1)):
            new_records.append((text[i-1],i))
        cur.execute('DELETE FROM defect;')
        print('We have deleted', cur.rowcount, 'records from the table.')
        # print(new_records)
        cur.executemany('INSERT INTO defect VALUES(?,?);',new_records)
        print('We have inserted', cur.rowcount, 'records to the table.')

        #commit the changes to db			
        conn.commit()
        #close the connection
        conn.close()
    def save_close(self):
        text=self.comboBox_22.currentText()
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()
        sql = "UPDATE setstyle SET style = '{}' WHERE id = 0".format(text)
        cur.execute(sql) 
        cur = conn.cursor()
        text=self.comboBox_23.currentText()
        sql = "UPDATE language SET lan = '{}' WHERE id = 0".format(text)
        cur.execute(sql) 
        text=self.comboBox_24.currentText()
        sql = "UPDATE Theme SET color = '{}' WHERE id = 0".format(text)
        cur.execute(sql)         
        conn.commit()

        #font
        text=self.comboBox_font.currentText()
        sql = "UPDATE font SET font_name = '{}' WHERE id = 0".format(text)
        cur.execute(sql)         
        conn.commit()
        text=self.spinBox_2.value()
        sql = "UPDATE font SET size = '{}' WHERE id = 0".format(text)
        cur.execute(sql)         
        conn.commit()

        #width
        text=self.table_width_left.value()
        sql = "UPDATE table_width SET left_size = '{}' WHERE id = 0".format(text)
        cur.execute(sql)         
        conn.commit()
        text=self.table_width_right.value()
        sql = "UPDATE table_width SET right_size = '{}' WHERE id = 0".format(text)
        cur.execute(sql)         
        conn.commit()

        #cpaturing_time
        value=self.spinBox_capturing_time.value()
        sql = "UPDATE capturing_time SET value = '{}' WHERE id = 0".format(value)
        cur.execute(sql)         
        conn.commit()      


        #image pathfile address saving
        value=self.lineEdit_image_directory.text()
        sql = "UPDATE path SET image_path = '{}' WHERE id = 0".format(value)
        cur.execute(sql)         
        conn.commit()  
     
        value=self.lineEdit_image_directory_2.text()
        sql = "UPDATE path SET image_path = '{}' WHERE id = 1".format(value)
        cur.execute(sql)         
        conn.commit()  
        
        # image format_quality
        value=self.comboBox_image_format.currentText()
        sql = "UPDATE path SET format = '{}' WHERE id = 0".format(value)
        cur.execute(sql)         
        conn.commit()  
        value=self.comboBox_imed_image_format.currentText()
        sql = "UPDATE path SET format = '{}' WHERE id = 1".format(value)
        cur.execute(sql)         
        conn.commit()  
        value=self.spinbox_image_quality.value()
        sql = "UPDATE path SET quality = '{}' WHERE id = 0".format(value)
        cur.execute(sql)         
        conn.commit()  
        value=self.spinbox_imed_image_quality.value()
        sql = "UPDATE path SET quality = '{}' WHERE id = 1".format(value)
        cur.execute(sql)         
        conn.commit()  

        #Refresh rate

        text=self.lineEdit_refresh_rate.text()
        sql = "UPDATE live_refresh_rate SET value_ = '{}' WHERE id = 0".format(text)
        cur.execute(sql)         
        conn.commit()



        #image panorama
        value=self.spinBox_panorama_lenght.value()
        sql = "UPDATE refresh_rate SET panorama_lenght = '{}' WHERE id = 0".format(value)
        cur.execute(sql)         
        conn.commit() 
        #  self.spinBox_panorama_lenght.

       
        self.save_cam_names()

        self.save_label_size()
        conn.commit()
        self.close()

    def cam_names(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from camera_names')
        records = cur.fetchall()

        for row in records:
            self.cam_1_name=str(row[0])
            self.cam_2_name=str(row[1])
            self.cam_3_name=str(row[2])
            self.cam_4_name=str(row[3])
            self.lineEdit_cam_1.setText( self.cam_1_name)
            self.lineEdit_cam_2.setText( self.cam_2_name)
            self.lineEdit_cam_3.setText( self.cam_3_name)
            self.lineEdit_cam_4.setText( self.cam_4_name)

    def save_cam_names(self):
        sql = "UPDATE camera_names SET cam_1 = '{}' WHERE cam_1 = '{}'".format(self.lineEdit_cam_1.text(),str(self.cam_1_name))
        cur.execute(sql) 
        sql = "UPDATE camera_names SET cam_2 = '{}' WHERE cam_2 = '{}'".format(self.lineEdit_cam_2.text(),str(self.cam_2_name))
        cur.execute(sql)
        sql = "UPDATE camera_names SET cam_3 = '{}' WHERE cam_3 = '{}'".format(self.lineEdit_cam_3.text(),str(self.cam_3_name))
        cur.execute(sql) 
        sql = "UPDATE camera_names SET cam_4 = '{}' WHERE cam_4 = '{}'".format(self.lineEdit_cam_4.text(),str(self.cam_4_name))
        cur.execute(sql) 
        conn.commit()

    def label_size(self):
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from labels_size')
        records = cur.fetchall()

        self.line_width=[self.line_width_cam_1,self.line_width_cam_2,self.line_width_cam_3,self.line_width_cam_4,self.line_width_cam_5,self.line_width_cam_6,self.line_width_cam_7,self.line_width_cam_8]
        self.line_Height=[self.line_height_cam_1,self.line_height_cam_2,self.line_height_cam_3,self.line_height_cam_4,self.line_height_cam_5,self.line_height_cam_6,self.line_height_cam_7,self.line_height_cam_8]
        
        i=0
        for row in  records:
            line_width_str=(row[0])
            line_Height_str=(row[1])
            self.line_width[i].setValue(line_width_str)
            self.line_Height[i].setValue(line_Height_str)
            i+=1

    def save_label_size(self):
        for i in range (len(self.line_width)):
            j=i+1

            sql = "UPDATE labels_size SET Width = '{}' WHERE id = {}".format(self.line_width[i].value(),j)
            cur.execute(sql) 
            sql = "UPDATE labels_size SET Height = '{}' WHERE id = {}".format(self.line_Height[i].value(),j)
            cur.execute(sql) 
        conn.commit()








            


if __name__ == "__main__":
    app = QApplication()
    win = UI_default_setting_window()
    win.show()
    sys.exit(app.exec())
