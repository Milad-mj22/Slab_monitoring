from pickle import TRUE
import sys
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon as sQIcon
from PySide6.QtGui import QPixmap as sQPixmap
import jdatetime

ui, _ =  loadUiType("pyqt_calender/calender.ui")

class UI_calender_window(QMainWindow, ui):
    def __init__(self):
        super(UI_calender_window, self).__init__()
        ###### setup UI
        # self.setWindowIcon(sQIcon('PathToIcon/icon.png'))
        self.setupUi(self)
        self.pos_ = self.pos()
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        ###### flags and variables

        ###### working buttons and widjets
        
        ###### qcombbottoms
        ###### default months
        self.months = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
        ##### default years
        self.years = ["1396", "1397", "1398", "1399", "1400", "1401",
        "1402", "1403", "1404","1405", "1406", "1407"]

        self.comboBox_month.addItems(self.months)
        self.comboBox_year.addItems(self.years)

        

        # self.pushButton_prev.setIcon(QIcon('pyqt_calender\prev.png'))
        # self.pushButton_next.setIcon(QIcon('pyqt_calender/next.png'))

        icon = sQIcon()
        icon.addPixmap(sQPixmap("pyqt_calender\prev.png"), sQIcon.Normal)
        self.pushButton_prev.setIcon(icon)

        icon = sQIcon()
        icon.addPixmap(sQPixmap("pyqt_calender/next.png"), sQIcon.Normal)
        self.pushButton_next.setIcon(icon)


        self.month_index = self.comboBox_month.currentIndex()
        self.month_name = self.comboBox_month.currentText()
        
        self.year_index = self.comboBox_year.currentIndex()
        self.year_name = self.comboBox_year.currentText()

        self.comboBox_month.currentIndexChanged.connect(self.index_changed_month)
        self.comboBox_year.currentIndexChanged.connect(self.index_changed_year)

        ##### prev and next month buttoms
  
        self.pushButton_prev.clicked.connect(lambda:self.go_prev_month())

        self.pushButton_next.clicked.connect(lambda:self.go_next_month())
        self.is_it_a_31_day_month()


        ##### date buttoms
        self.day = 1  #### default
        self.pushButton_31.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 31))
        self.pushButton_30.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 30))
        self.pushButton_29.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 29))
        self.pushButton_28.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 28))
        self.pushButton_27.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 27))
        self.pushButton_26.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 26))
        self.pushButton_25.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 25))
        self.pushButton_24.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 24))
        self.pushButton_23.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 23))
        self.pushButton_22.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 22))
        self.pushButton_21.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 21))
        self.pushButton_20.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 20))
        self.pushButton_19.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 19))
        self.pushButton_18.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 18))
        self.pushButton_17.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 17))
        self.pushButton_16.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 16))
        self.pushButton_15.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 15))
        self.pushButton_14.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 14))
        self.pushButton_13.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 13))
        self.pushButton_12.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 12))
        self.pushButton_11.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 11))
        self.pushButton_10.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 10))
        self.pushButton_9.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 9))
        self.pushButton_8.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 8))
        self.pushButton_7.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 7))
        self.pushButton_6.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 6))
        self.pushButton_5.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 5))
        self.pushButton_4.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 4))
        self.pushButton_3.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 3))
        self.pushButton_2.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 2))
        self.pushButton_1.clicked.connect(lambda:self.show_selected_date(self.month_index, self.year_name, 1))

        self.today_btn.clicked.connect(self.today_date)

        self.select_btn.clicked.connect(self.select_date)

        self.close_btn.clicked.connect(self.close_)

    def close_(self):
        self.close()

    def select_date(self):
        self.selectd_date = self.label_selected_date.text()

    ##### 31 day months
    def is_it_a_31_day_month(self):
        if self.month_index in range(6):
            self.pushButton_31.setEnabled(True)
        else:
            self.pushButton_31.setEnabled(False)

    
    ##### go to previous month
    def go_prev_month(self):
        current_month = self.month_index  ##### going back one month
        if current_month != 0:
            self.month_index = current_month - 1
            self.month_name = self.months[current_month - 1]
            self.comboBox_month.setCurrentIndex(current_month - 1)
        else:
            self.month_index = 11   #### going to previos year
            self.month_name = self.months[11]
            self.comboBox_month.setCurrentIndex(11)
            #### year
            if self.year_index != 0:
                prev_year = self.year_index - 1
                self.year_index = prev_year
                self.year_name = self.year_name[prev_year]
                self.comboBox_year.setCurrentIndex(prev_year)
            else:
                print("no data available from previous year")
        self.is_it_a_31_day_month()
    ##### go to next month
    def go_next_month(self):
        current_month = self.month_index  ##### going forward one month
        if current_month != 11:
            self.month_index = current_month + 1
            self.month_name = self.months[current_month + 1]
            self.comboBox_month.setCurrentIndex(current_month + 1)
        else:
            self.month_index = 0   #### going to next year
            self.month_name = self.months[0]
            self.comboBox_month.setCurrentIndex(0)
            #### year
            if self.year_index != len(self.years):
                prev_year = self.year_index + 1
                self.year_index = prev_year
                self.year_name = self.year_name[prev_year]
                self.comboBox_year.setCurrentIndex(prev_year)
            else:
                print("no data available from next year")
        self.is_it_a_31_day_month()


    ##### show date in label  : label_selected_date
    def show_selected_date(self, month_index, year_name, day):

        if month_index<=8:
            month_index ='0'+ str(month_index+1)
        else:
            month_index = str(month_index+1)

        if day<=9:
            day ='0' + str(day)
        else:
            day = str(day)

        if month_index != None:
            self.label_selected_date.setText(year_name +"-" + month_index+ "-"+day)##### add day here      
        else:
            self.label_selected_date.setText('')
        
    ###### select month 
    def index_changed_month(self, index):
        self.month_index = index
        self.month_name = self.months[index]
        print("month Index changed", self.month_index)
        print("month name", self.month_name)
        self.is_it_a_31_day_month()

    ###### select year
    def index_changed_year(self, index):
        self.year_index = index
        self.year_name = self.years[index]
        print("year Index changed", self.year_index)
        print("year name", self.year_name)



    def today_date(self):
        date = str(jdatetime.date.today())
        self.label_selected_date.setText(date)


if __name__ == "__main__":
    app = QApplication()
    win = UI_calender_window()
    win.show()
    sys.exit(app.exec())
