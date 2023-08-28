
import sys


from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *

from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from camera_setting_window import *
from default_setting_window import *
from manage_user_window import *

from head_calibration import UI_calibration_window


import detect_lenguage
ui2, _ = loadUiType("setting_window.ui")


class UI_setting_window(QMainWindow, ui2):
    global widgets
    widgets_eror = ui2
    sign=0
    def __init__(self):
        super(UI_setting_window, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.window_defult = UI_default_setting_window()
        self.window_defult.save_close_btn.clicked.connect(self.print)
        

        self.window_manage_user = UI_manage_user_window()
        self.set_language()

    def print(self):
        print('asdwqqwrqfsddc')
    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)
        self.software_settings.clicked.connect(self.sofware_win)
        self.pop_settings.clicked.connect(self.pop_win)
        self.report_settings.clicked.connect(self.report_win)

        self.camera_settings.clicked.connect(self.camera_win)
        self.manage_user_btn.clicked.connect(self.manage_user_win)
        self.calibration_settings.clicked.connect(self.close_win)

        



    def close_win(self):
        self.close()

    def set_language(self):
        if detect_lenguage.language()=='Persian(فارسی)':
            detect_lenguage.setting_window(self)



    def camera_win(self):
        self.window = UI_camera_setting_window()
       # self.ui2= UI_eror_window()
        self.window.show()
        self.close()
    def sofware_win(self):
        self.window_defult.user_btn.setText(self.user_btn.text())
        self.window_defult.login_welcome.setText(self.login_welcome.text())
        self.window_defult.show()
        self.close()
    def pop_win(self):
        self.close()
    def report_win(self):
        self.close()
    def default_win(self):
        self.window_defult.user_btn.setText(self.user_btn.text())
        self.window_defult.login_welcome.setText(self.login_welcome.text())
        self.window_defult.show()

        self.close()
    def manage_user_win(self):
        self.window_manage_user.user_btn.setText(self.user_btn.text())
        self.window_manage_user.login_welcome.setText(self.login_welcome.text())
        self.window_manage_user.show()
        self.close()
            








if __name__ == "__main__":
    app = QApplication()
    win = UI_setting_window()
    win.show()
    sys.exit(app.exec())
