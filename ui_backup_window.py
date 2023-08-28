# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backup_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_pause_btn(object):
    def setupUi(self, pause_btn):
        if not pause_btn.objectName():
            pause_btn.setObjectName(u"pause_btn")
        pause_btn.resize(753, 569)
        self.centralwidget = QWidget(pause_btn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(197 , 195,196);\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.frame_6)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 0))
        self.headerFrame.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.headerFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMaximumSize(QSize(150, 100))
        self.label_2.setPixmap(QPixmap(u"C:/Users/milad/Desktop/dorsa2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setMargin(-1)
        self.label_2.setIndent(4)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(370, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalSpacer_3 = QSpacerItem(326, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.userFrame = QFrame(self.headerFrame)
        self.userFrame.setObjectName(u"userFrame")
        self.userFrame.setMinimumSize(QSize(404, 30))
        self.userFrame.setMaximumSize(QSize(200, 30))
        self.userFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(100,100,100);\n"
"}")
        self.userFrame.setFrameShape(QFrame.NoFrame)
        self.userFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.userFrame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 20, 0)
        self.login_welcome = QLabel(self.userFrame)
        self.login_welcome.setObjectName(u"login_welcome")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        self.login_welcome.setFont(font)

        self.horizontalLayout_7.addWidget(self.login_welcome, 0, Qt.AlignRight)

        self.user_btn = QPushButton(self.userFrame)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setEnabled(False)
        self.user_btn.setMinimumSize(QSize(90, 26))
        self.user_btn.setMaximumSize(QSize(90, 26))
        font1 = QFont()
        font1.setBold(True)
        self.user_btn.setFont(font1)
        self.user_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"	border-left: 1px solid rgb(30, 30, 30);\n"
"	border-right:1px solid rgb(30, 30, 30);\n"
"	color: rgb(255, 85, 0);\n"
"	border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons8_account_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon)
        self.user_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.user_btn)

        self.toggleButton_6 = QPushButton(self.userFrame)
        self.toggleButton_6.setObjectName(u"toggleButton_6")
        self.toggleButton_6.setMinimumSize(QSize(50, 26))
        self.toggleButton_6.setMaximumSize(QSize(50, 26))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.toggleButton_6.setFont(font2)
        self.toggleButton_6.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"	border-left: 1px solid rgb(30, 30, 30);\n"
"	border-right:1px solid rgb(30, 30, 30);\n"
"	color: rgb(255, 85, 0);\n"
"	border-radius: 13px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(25, 25, 25);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icons8_alarm.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton_6.setIcon(icon1)
        self.toggleButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.toggleButton_6)


        self.horizontalLayout_6.addWidget(self.userFrame, 0, Qt.AlignRight)

        self.horizontalSpacer_2 = QSpacerItem(58, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.close_btn = QPushButton(self.headerFrame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(40, 30))
        self.close_btn.setMaximumSize(QSize(40, 30))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icons8_multiply.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.close_btn)


        self.horizontalLayout_9.addWidget(self.headerFrame)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 38))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_directory = QLineEdit(self.frame_2)
        self.lineEdit_directory.setObjectName(u"lineEdit_directory")
        self.lineEdit_directory.setStyleSheet(u"padding-left:5px;")

        self.horizontalLayout_2.addWidget(self.lineEdit_directory)

        self.toolButton_folder = QToolButton(self.frame_2)
        self.toolButton_folder.setObjectName(u"toolButton_folder")
        self.toolButton_folder.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.toolButton_folder)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_report = QTableWidget(self.frame_4)
        if (self.table_report.columnCount() < 11):
            self.table_report.setColumnCount(11)
        if (self.table_report.rowCount() < 50):
            self.table_report.setRowCount(50)
        self.table_report.setObjectName(u"table_report")
        self.table_report.setFont(font)
        self.table_report.setFrameShape(QFrame.Box)
        self.table_report.setFrameShadow(QFrame.Plain)
        self.table_report.setDragEnabled(True)
        self.table_report.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_report.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_report.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_report.setRowCount(50)
        self.table_report.setColumnCount(11)

        self.verticalLayout_2.addWidget(self.table_report)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 22))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 0, 0, 0)
        self.selectall_btn = QPushButton(self.frame_7)
        self.selectall_btn.setObjectName(u"selectall_btn")
        self.selectall_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.selectall_btn)

        self.selectavailable_btn = QPushButton(self.frame_7)
        self.selectavailable_btn.setObjectName(u"selectavailable_btn")
        self.selectavailable_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.selectavailable_btn)

        self.clearall_btn = QPushButton(self.frame_7)
        self.clearall_btn.setObjectName(u"clearall_btn")
        self.clearall_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.clearall_btn)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 45))
        self.frame_5.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.frame_5)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_4.addWidget(self.progressBar)

        self.start_btn = QPushButton(self.frame_5)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.start_btn)

        self.pause_btn_2 = QPushButton(self.frame_5)
        self.pause_btn_2.setObjectName(u"pause_btn_2")
        self.pause_btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pause_btn_2)

        self.cancel_btn = QPushButton(self.frame_5)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.cancel_btn)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_notif = QLabel(self.frame_3)
        self.label_notif.setObjectName(u"label_notif")

        self.horizontalLayout_3.addWidget(self.label_notif, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        pause_btn.setCentralWidget(self.centralwidget)

        self.retranslateUi(pause_btn)

        QMetaObject.connectSlotsByName(pause_btn)
    # setupUi

    def retranslateUi(self, pause_btn):
        pause_btn.setWindowTitle(QCoreApplication.translate("pause_btn", u"MainWindow", None))
        self.label_2.setText("")
        self.login_welcome.setText("")
        self.user_btn.setText(QCoreApplication.translate("pause_btn", u"Guest", None))
        self.toggleButton_6.setText(QCoreApplication.translate("pause_btn", u"0", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("pause_btn", u"Backup Address :", None))
        self.toolButton_folder.setText(QCoreApplication.translate("pause_btn", u"...", None))
        self.selectall_btn.setText(QCoreApplication.translate("pause_btn", u"Select All", None))
        self.selectavailable_btn.setText(QCoreApplication.translate("pause_btn", u"Select Availables", None))
        self.clearall_btn.setText(QCoreApplication.translate("pause_btn", u"Clear All", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.start_btn.setText(QCoreApplication.translate("pause_btn", u"Start", None))
        self.pause_btn_2.setText(QCoreApplication.translate("pause_btn", u"Pause", None))
        self.cancel_btn.setText(QCoreApplication.translate("pause_btn", u"Cancel", None))
        self.label_notif.setText("")
    # retranslateUi

