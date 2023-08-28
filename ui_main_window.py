# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1386, 1030)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(2000, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.verticalLayout_31 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 2, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_6)

        self.toolBar = QFrame(self.centralwidget)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMinimumSize(QSize(0, 38))
        self.toolBar.setMaximumSize(QSize(16777215, 38))
        self.toolBar.setFrameShape(QFrame.NoFrame)
        self.toolBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.toolBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleFrame = QFrame(self.toolBar)
        self.toggleFrame.setObjectName(u"toggleFrame")
        self.toggleFrame.setMinimumSize(QSize(38, 33))
        self.toggleFrame.setMaximumSize(QSize(30, 30))
        self.toggleFrame.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.toggleFrame.setFrameShape(QFrame.NoFrame)
        self.toggleFrame.setFrameShadow(QFrame.Raised)
        self.toggleButton = QPushButton(self.toggleFrame)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setEnabled(True)
        self.toggleButton.setGeometry(QRect(0, 0, 40, 30))
        self.toggleButton.setMinimumSize(QSize(40, 30))
        self.toggleButton.setMaximumSize(QSize(30, 30))
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"images/menu_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton.setIcon(icon)
        self.toggleButton.setIconSize(QSize(28, 38))

        self.horizontalLayout_2.addWidget(self.toggleFrame)

        self.headerFrame = QFrame(self.toolBar)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 0))
        self.headerFrame.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.headerFrame.setFrameShape(QFrame.NoFrame)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.headerFrame)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_3.addWidget(self.label_23)

        self.label_44 = QLabel(self.headerFrame)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_3.addWidget(self.label_44)

        self.horizontalSpacer_17 = QSpacerItem(19, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_17)

        self.label_7 = QLabel(self.headerFrame)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Traditional Arabic"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_7.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(370, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalSpacer_22 = QSpacerItem(34, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_22)

        self.label_3 = QLabel(self.headerFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(0, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_3.setFont(font2)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"border:none;")
        self.label_3.setFrameShape(QFrame.StyledPanel)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setLineWidth(9)
        self.label_3.setMidLineWidth(0)
        self.label_3.setTextFormat(Qt.AutoText)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(58, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.headerFrame)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamilies([u"Traditional Arabic"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_6.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.label_49 = QLabel(self.headerFrame)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setEnabled(True)
        self.label_49.setMaximumSize(QSize(55, 16777215))
        self.label_49.setCursor(QCursor(Qt.ArrowCursor))
        self.label_49.setPixmap(QPixmap(u"images/637288638132980756.png"))
        self.label_49.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_49)

        self.horizontalSpacer_23 = QSpacerItem(12, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_23)

        self.label_61 = QLabel(self.headerFrame)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setEnabled(True)
        self.label_61.setMinimumSize(QSize(95, 0))
        self.label_61.setMaximumSize(QSize(89, 16777215))
        self.label_61.setCursor(QCursor(Qt.ArrowCursor))
        self.label_61.setPixmap(QPixmap(u"images/whitew.png"))
        self.label_61.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_61)

        self.login_welcome = QLabel(self.headerFrame)
        self.login_welcome.setObjectName(u"login_welcome")

        self.horizontalLayout_3.addWidget(self.login_welcome)

        self.label_5 = QLabel(self.headerFrame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.userFrame = QFrame(self.headerFrame)
        self.userFrame.setObjectName(u"userFrame")
        self.userFrame.setMinimumSize(QSize(200, 30))
        self.userFrame.setMaximumSize(QSize(200, 30))
        self.userFrame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(100,100,100);\n"
"}")
        self.userFrame.setFrameShape(QFrame.NoFrame)
        self.userFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.userFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.setting_btn = QPushButton(self.userFrame)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setMinimumSize(QSize(30, 30))
        self.setting_btn.setMaximumSize(QSize(30, 30))
        self.setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_btn.setToolTipDuration(-3)
        self.setting_btn.setStyleSheet(u"QPushButton {\n"
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
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"images/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_btn.setIcon(icon1)
        self.setting_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.setting_btn)

        self.user_btn = QPushButton(self.userFrame)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setMinimumSize(QSize(90, 26))
        self.user_btn.setMaximumSize(QSize(130, 26))
        font4 = QFont()
        font4.setBold(True)
        self.user_btn.setFont(font4)
        self.user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"	border-left: 1px solid rgb(30, 30, 30);\n"
"	border-right:1px solid rgb(30, 30, 30);\n"
"	color: rgb(46,202,254);\n"
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
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/milad/Downloads/21-avatar-outline.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon2)
        self.user_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.user_btn)

        self.toggleButton_6 = QPushButton(self.userFrame)
        self.toggleButton_6.setObjectName(u"toggleButton_6")
        self.toggleButton_6.setMinimumSize(QSize(50, 26))
        self.toggleButton_6.setMaximumSize(QSize(50, 26))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.toggleButton_6.setFont(font5)
        self.toggleButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton_6.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"	border-left: 1px solid rgb(30, 30, 30);\n"
"	border-right:1px solid rgb(30, 30, 30);\n"
"	color: rgb(46,202,254);\n"
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
        icon3 = QIcon()
        icon3.addFile(u"images/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toggleButton_6.setIcon(icon3)
        self.toggleButton_6.setIconSize(QSize(16, 18))

        self.horizontalLayout_4.addWidget(self.toggleButton_6)


        self.horizontalLayout_3.addWidget(self.userFrame)


        self.horizontalLayout_2.addWidget(self.headerFrame)

        self.actionFrame = QFrame(self.toolBar)
        self.actionFrame.setObjectName(u"actionFrame")
        self.actionFrame.setMinimumSize(QSize(100, 0))
        self.actionFrame.setMaximumSize(QSize(125, 16777215))
        self.actionFrame.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"")
        self.actionFrame.setFrameShape(QFrame.NoFrame)
        self.actionFrame.setFrameShadow(QFrame.Raised)
        self.miniButton = QPushButton(self.actionFrame)
        self.miniButton.setObjectName(u"miniButton")
        self.miniButton.setGeometry(QRect(0, 0, 30, 30))
        self.miniButton.setMinimumSize(QSize(30, 30))
        self.miniButton.setMaximumSize(QSize(30, 30))
        self.miniButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.miniButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 0);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons8_minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miniButton.setIcon(icon4)
        self.miniButton.setIconSize(QSize(30, 30))
        self.maxiButton = QPushButton(self.actionFrame)
        self.maxiButton.setObjectName(u"maxiButton")
        self.maxiButton.setGeometry(QRect(30, 0, 30, 30))
        self.maxiButton.setMinimumSize(QSize(30, 30))
        self.maxiButton.setMaximumSize(QSize(30, 30))
        self.maxiButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.maxiButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 0);\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icons8_separate_document_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maxiButton.setIcon(icon5)
        self.maxiButton.setIconSize(QSize(30, 30))
        self.closeButton = QPushButton(self.actionFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(60, 0, 40, 30))
        self.closeButton.setMinimumSize(QSize(40, 30))
        self.closeButton.setMaximumSize(QSize(40, 30))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 0);\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icons8_multiply.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon6)
        self.closeButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.actionFrame)


        self.verticalLayout_31.addWidget(self.toolBar)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_7)

        self.Body = QFrame(self.centralwidget)
        self.Body.setObjectName(u"Body")
        self.Body.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"\n"
"")
        self.Body.setFrameShape(QFrame.NoFrame)
        self.Body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.Body)
        self.leftMenu.setObjectName(u"leftMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenu.sizePolicy().hasHeightForWidth())
        self.leftMenu.setSizePolicy(sizePolicy1)
        self.leftMenu.setMinimumSize(QSize(44, 0))
        self.leftMenu.setMaximumSize(QSize(44, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(120, 120,120);")
        self.leftMenu.setFrameShape(QFrame.NoFrame)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.aframe = QFrame(self.leftMenu)
        self.aframe.setObjectName(u"aframe")
        self.aframe.setMinimumSize(QSize(200, 225))
        self.aframe.setStyleSheet(u"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.273, stop:0 rgba(100,100,100,200), stop:1 rgba(130,130,130, 255));")
        self.aframe.setFrameShape(QFrame.NoFrame)
        self.aframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.aframe)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.live_btn = QPushButton(self.aframe)
        self.live_btn.setObjectName(u"live_btn")
        self.live_btn.setMinimumSize(QSize(200, 45))
        self.live_btn.setMaximumSize(QSize(1111111, 45))
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(12)
        font6.setBold(False)
        self.live_btn.setFont(font6)
        self.live_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: left;\n"
"	padding-left: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80,80,80);\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"images/layout (4) - Copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.live_btn.setIcon(icon7)
        self.live_btn.setIconSize(QSize(44, 46))
        self.live_btn.setCheckable(False)

        self.verticalLayout_3.addWidget(self.live_btn)

        self.page_live_dataset_btn = QPushButton(self.aframe)
        self.page_live_dataset_btn.setObjectName(u"page_live_dataset_btn")
        self.page_live_dataset_btn.setEnabled(False)
        self.page_live_dataset_btn.setMinimumSize(QSize(200, 45))
        self.page_live_dataset_btn.setMaximumSize(QSize(16777215, 45))
        self.page_live_dataset_btn.setFont(font6)
        self.page_live_dataset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.page_live_dataset_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: left;\n"
"	padding-left: 9px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80,80, 80);\n"
"}\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"images/right-panel-layout-interface-symbol.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_live_dataset_btn.setIcon(icon8)
        self.page_live_dataset_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.page_live_dataset_btn)

        self.panorama_btn = QPushButton(self.aframe)
        self.panorama_btn.setObjectName(u"panorama_btn")
        self.panorama_btn.setMinimumSize(QSize(200, 45))
        self.panorama_btn.setMaximumSize(QSize(16777215, 45))
        self.panorama_btn.setFont(font6)
        self.panorama_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.panorama_btn.setStyleSheet(u"QPushButton {\n"
"\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"icons/p.png", QSize(), QIcon.Normal, QIcon.Off)
        self.panorama_btn.setIcon(icon9)
        self.panorama_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.panorama_btn)

        self.page_fullscreen = QPushButton(self.aframe)
        self.page_fullscreen.setObjectName(u"page_fullscreen")
        self.page_fullscreen.setMinimumSize(QSize(200, 45))
        self.page_fullscreen.setMaximumSize(QSize(111111, 45))
        self.page_fullscreen.setFont(font6)
        self.page_fullscreen.setCursor(QCursor(Qt.PointingHandCursor))
        self.page_fullscreen.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_fullscreen.setIcon(icon10)
        self.page_fullscreen.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.page_fullscreen)

        self.page_report_btn = QPushButton(self.aframe)
        self.page_report_btn.setObjectName(u"page_report_btn")
        self.page_report_btn.setMinimumSize(QSize(200, 45))
        self.page_report_btn.setMaximumSize(QSize(16777215, 45))
        self.page_report_btn.setFont(font6)
        self.page_report_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.page_report_btn.setAutoFillBackground(False)
        self.page_report_btn.setStyleSheet(u"QPushButton {\n"
"	color:rgb(0,0,0);\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"icons/r.png", QSize(), QIcon.Normal, QIcon.Off)
        self.page_report_btn.setIcon(icon11)
        self.page_report_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.page_report_btn)

        self.page_aboutus_btn = QPushButton(self.aframe)
        self.page_aboutus_btn.setObjectName(u"page_aboutus_btn")
        self.page_aboutus_btn.setMinimumSize(QSize(200, 45))
        self.page_aboutus_btn.setMaximumSize(QSize(16777215, 45))
        self.page_aboutus_btn.setFont(font6)
        self.page_aboutus_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.page_aboutus_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color:  rgb(197 , 195,196);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/icons8_secured_letter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.page_aboutus_btn.setIcon(icon12)
        self.page_aboutus_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.page_aboutus_btn)


        self.verticalLayout_4.addWidget(self.aframe)

        self.bt = QSpacerItem(20, 271, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.bt)

        self.frame_2 = QFrame(self.leftMenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 50))
        self.frame_2.setMaximumSize(QSize(200, 50))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logout_btn = QPushButton(self.frame_2)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setEnabled(False)
        self.logout_btn.setMinimumSize(QSize(200, 52))
        self.logout_btn.setMaximumSize(QSize(200, 45))
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(10)
        self.logout_btn.setFont(font7)
        self.logout_btn.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(120,120,120);\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(120,120,120);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/icons8_logout_rounded_down.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon13)
        self.logout_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.logout_btn)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.leftMenu)

        self.Container = QFrame(self.Body)
        self.Container.setObjectName(u"Container")
        self.Container.setMaximumSize(QSize(16777215, 16777215))
        self.Container.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"")
        self.Container.setFrameShape(QFrame.NoFrame)
        self.Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.Container)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setFamilies([u"MT Extra"])
        self.stackedWidget.setFont(font8)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(197 , 195,196);\n"
"")
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page_live_dataset = QWidget()
        self.page_live_dataset.setObjectName(u"page_live_dataset")
        self.page_live_dataset.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.verticalLayout_6 = QVBoxLayout(self.page_live_dataset)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame87 = QFrame(self.page_live_dataset)
        self.frame87.setObjectName(u"frame87")
        self.frame87.setStyleSheet(u"background-color: rgb(197 , 195,196);")
        self.frame87.setFrameShape(QFrame.NoFrame)
        self.frame87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame87)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(2, 3, 6, 0)
        self.frame_camera_1 = QFrame(self.frame87)
        self.frame_camera_1.setObjectName(u"frame_camera_1")
        self.frame_camera_1.setMinimumSize(QSize(0, 0))
        self.frame_camera_1.setMaximumSize(QSize(16777215, 16777215))
        self.frame_camera_1.setStyleSheet(u"background-color: rgb(197 , 195,196);\n"
"")
        self.frame_camera_1.setFrameShape(QFrame.Box)
        self.frame_camera_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_camera_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.frame_30 = QFrame(self.frame_camera_1)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setEnabled(False)
        self.frame_30.setMaximumSize(QSize(16777215, 50))
        self.frame_30.setFrameShape(QFrame.Box)
        self.frame_30.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.dataset_cam_1_name = QLabel(self.frame_30)
        self.dataset_cam_1_name.setObjectName(u"dataset_cam_1_name")
        self.dataset_cam_1_name.setMaximumSize(QSize(500, 20))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(197, 195, 196, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.dataset_cam_1_name.setPalette(palette)
        font9 = QFont()
        font9.setFamilies([u"Times New Roman"])
        font9.setPointSize(11)
        self.dataset_cam_1_name.setFont(font9)
        self.dataset_cam_1_name.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.horizontalLayout_44.addWidget(self.dataset_cam_1_name)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_19)

        self.D_notif_cam_5 = QLabel(self.frame_30)
        self.D_notif_cam_5.setObjectName(u"D_notif_cam_5")
        palette1 = QPalette()
        brush6 = QBrush(QColor(255, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_notif_cam_5.setPalette(palette1)

        self.horizontalLayout_44.addWidget(self.D_notif_cam_5)

        self.D_cam_1_pausesign = QLabel(self.frame_30)
        self.D_cam_1_pausesign.setObjectName(u"D_cam_1_pausesign")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_cam_1_pausesign.setPalette(palette2)
        font10 = QFont()
        font10.setPointSize(10)
        self.D_cam_1_pausesign.setFont(font10)

        self.horizontalLayout_44.addWidget(self.D_cam_1_pausesign)

        self.D_cam_1_rotate = QPushButton(self.frame_30)
        self.D_cam_1_rotate.setObjectName(u"D_cam_1_rotate")
        self.D_cam_1_rotate.setMaximumSize(QSize(23, 30))
        font11 = QFont()
        font11.setBold(False)
        self.D_cam_1_rotate.setFont(font11)
        self.D_cam_1_rotate.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_1_rotate.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u"images/icons8-rotate-left-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.D_cam_1_rotate.setIcon(icon14)
        self.D_cam_1_rotate.setIconSize(QSize(14, 14))
        self.D_cam_1_rotate.setCheckable(False)
        self.D_cam_1_rotate.setAutoRepeatDelay(295)
        self.D_cam_1_rotate.setAutoRepeatInterval(101)

        self.horizontalLayout_44.addWidget(self.D_cam_1_rotate)

        self.D_cam_1_capture = QPushButton(self.frame_30)
        self.D_cam_1_capture.setObjectName(u"D_cam_1_capture")
        self.D_cam_1_capture.setMaximumSize(QSize(23, 30))
        self.D_cam_1_capture.setFont(font11)
        self.D_cam_1_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_1_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u"images/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.D_cam_1_capture.setIcon(icon15)
        self.D_cam_1_capture.setIconSize(QSize(20, 20))
        self.D_cam_1_capture.setCheckable(False)
        self.D_cam_1_capture.setAutoRepeatDelay(295)
        self.D_cam_1_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_44.addWidget(self.D_cam_1_capture)

        self.D_cam_1_play = QPushButton(self.frame_30)
        self.D_cam_1_play.setObjectName(u"D_cam_1_play")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.D_cam_1_play.sizePolicy().hasHeightForWidth())
        self.D_cam_1_play.setSizePolicy(sizePolicy2)
        self.D_cam_1_play.setMinimumSize(QSize(0, 0))
        self.D_cam_1_play.setMaximumSize(QSize(30, 30))
        self.D_cam_1_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_1_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u"images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.D_cam_1_play.setIcon(icon16)

        self.horizontalLayout_44.addWidget(self.D_cam_1_play)

        self.D_cam_1_pause = QPushButton(self.frame_30)
        self.D_cam_1_pause.setObjectName(u"D_cam_1_pause")
        sizePolicy2.setHeightForWidth(self.D_cam_1_pause.sizePolicy().hasHeightForWidth())
        self.D_cam_1_pause.setSizePolicy(sizePolicy2)
        self.D_cam_1_pause.setMinimumSize(QSize(0, 0))
        self.D_cam_1_pause.setMaximumSize(QSize(30, 30))
        self.D_cam_1_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_1_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        icon17 = QIcon()
        icon17.addFile(u"images/pause-button (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.D_cam_1_pause.setIcon(icon17)

        self.horizontalLayout_44.addWidget(self.D_cam_1_pause)

        self.D_cam_1_zoom = QLabel(self.frame_30)
        self.D_cam_1_zoom.setObjectName(u"D_cam_1_zoom")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush7 = QBrush(QColor(85, 170, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush8 = QBrush(QColor(85, 170, 0, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.D_cam_1_zoom.setPalette(palette3)

        self.horizontalLayout_44.addWidget(self.D_cam_1_zoom)

        self.D_fs1_btn = QPushButton(self.frame_30)
        self.D_fs1_btn.setObjectName(u"D_fs1_btn")
        self.D_fs1_btn.setMaximumSize(QSize(30, 30))
        self.D_fs1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_fs1_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        icon18 = QIcon()
        icon18.addFile(u"icons/full-screen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.D_fs1_btn.setIcon(icon18)

        self.horizontalLayout_44.addWidget(self.D_fs1_btn)


        self.verticalLayout_8.addWidget(self.frame_30)

        self.datalive_image_label_1 = QLabel(self.frame_camera_1)
        self.datalive_image_label_1.setObjectName(u"datalive_image_label_1")
        self.datalive_image_label_1.setMinimumSize(QSize(0, 0))
        self.datalive_image_label_1.setMaximumSize(QSize(16777215, 16777215))
        self.datalive_image_label_1.setFocusPolicy(Qt.StrongFocus)
        self.datalive_image_label_1.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.datalive_image_label_1.setPixmap(QPixmap(u"C:/Users/milad/.designer/backup/icons/change.png"))
        self.datalive_image_label_1.setScaledContents(True)
        self.datalive_image_label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.datalive_image_label_1.setMargin(2)

        self.verticalLayout_8.addWidget(self.datalive_image_label_1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_18.addWidget(self.frame_camera_1, 0, Qt.AlignTop)

        self.framw_camera = QFrame(self.frame87)
        self.framw_camera.setObjectName(u"framw_camera")
        self.framw_camera.setMaximumSize(QSize(16777215, 16777215))
        self.framw_camera.setStyleSheet(u"background-color: rgb(197 , 195,196);\n"
"")
        self.framw_camera.setFrameShape(QFrame.Box)
        self.framw_camera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.framw_camera)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_27 = QFrame(self.framw_camera)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setEnabled(False)
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setFrameShape(QFrame.Box)
        self.frame_27.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.dataset_cam_2_name = QLabel(self.frame_27)
        self.dataset_cam_2_name.setObjectName(u"dataset_cam_2_name")
        self.dataset_cam_2_name.setMaximumSize(QSize(500, 20))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.dataset_cam_2_name.setPalette(palette4)
        self.dataset_cam_2_name.setFont(font9)
        self.dataset_cam_2_name.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.horizontalLayout_40.addWidget(self.dataset_cam_2_name)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_11)

        self.D_notif_cam_2 = QLabel(self.frame_27)
        self.D_notif_cam_2.setObjectName(u"D_notif_cam_2")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_notif_cam_2.setPalette(palette5)

        self.horizontalLayout_40.addWidget(self.D_notif_cam_2)

        self.D_cam_2_pausesign = QLabel(self.frame_27)
        self.D_cam_2_pausesign.setObjectName(u"D_cam_2_pausesign")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_cam_2_pausesign.setPalette(palette6)
        self.D_cam_2_pausesign.setFont(font10)

        self.horizontalLayout_40.addWidget(self.D_cam_2_pausesign)

        self.D_cam_2_zoom = QLabel(self.frame_27)
        self.D_cam_2_zoom.setObjectName(u"D_cam_2_zoom")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.D_cam_2_zoom.setPalette(palette7)

        self.horizontalLayout_40.addWidget(self.D_cam_2_zoom)

        self.D_cam_2_play = QPushButton(self.frame_27)
        self.D_cam_2_play.setObjectName(u"D_cam_2_play")
        sizePolicy2.setHeightForWidth(self.D_cam_2_play.sizePolicy().hasHeightForWidth())
        self.D_cam_2_play.setSizePolicy(sizePolicy2)
        self.D_cam_2_play.setMinimumSize(QSize(0, 0))
        self.D_cam_2_play.setMaximumSize(QSize(30, 30))
        self.D_cam_2_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_2_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_2_play.setIcon(icon16)

        self.horizontalLayout_40.addWidget(self.D_cam_2_play)

        self.D_cam_2_pause = QPushButton(self.frame_27)
        self.D_cam_2_pause.setObjectName(u"D_cam_2_pause")
        sizePolicy2.setHeightForWidth(self.D_cam_2_pause.sizePolicy().hasHeightForWidth())
        self.D_cam_2_pause.setSizePolicy(sizePolicy2)
        self.D_cam_2_pause.setMinimumSize(QSize(0, 0))
        self.D_cam_2_pause.setMaximumSize(QSize(30, 30))
        self.D_cam_2_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_2_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_2_pause.setIcon(icon17)

        self.horizontalLayout_40.addWidget(self.D_cam_2_pause)

        self.D_cam_2_capture = QPushButton(self.frame_27)
        self.D_cam_2_capture.setObjectName(u"D_cam_2_capture")
        self.D_cam_2_capture.setMaximumSize(QSize(23, 30))
        self.D_cam_2_capture.setFont(font11)
        self.D_cam_2_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_2_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_2_capture.setIcon(icon15)
        self.D_cam_2_capture.setIconSize(QSize(20, 20))
        self.D_cam_2_capture.setCheckable(False)
        self.D_cam_2_capture.setAutoRepeatDelay(295)
        self.D_cam_2_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_40.addWidget(self.D_cam_2_capture)

        self.D_fs2_btn = QPushButton(self.frame_27)
        self.D_fs2_btn.setObjectName(u"D_fs2_btn")
        self.D_fs2_btn.setMaximumSize(QSize(30, 30))
        self.D_fs2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_fs2_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_fs2_btn.setIcon(icon18)

        self.horizontalLayout_40.addWidget(self.D_fs2_btn)


        self.verticalLayout_7.addWidget(self.frame_27)

        self.datalive_image_label_2 = QLabel(self.framw_camera)
        self.datalive_image_label_2.setObjectName(u"datalive_image_label_2")
        self.datalive_image_label_2.setMaximumSize(QSize(16777215, 16777215))
        self.datalive_image_label_2.setAcceptDrops(False)
        self.datalive_image_label_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.datalive_image_label_2.setFrameShape(QFrame.WinPanel)
        self.datalive_image_label_2.setPixmap(QPixmap(u"C:/Users/milad/.designer/backup/images/8387315901543238865-512.png"))
        self.datalive_image_label_2.setScaledContents(True)
        self.datalive_image_label_2.setAlignment(Qt.AlignCenter)
        self.datalive_image_label_2.setMargin(2)

        self.verticalLayout_7.addWidget(self.datalive_image_label_2)

        self.frame_28 = QFrame(self.framw_camera)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(False)
        self.frame_28.setMaximumSize(QSize(16777215, 50))
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.dataset_cam_3_name = QLabel(self.frame_28)
        self.dataset_cam_3_name.setObjectName(u"dataset_cam_3_name")
        self.dataset_cam_3_name.setMaximumSize(QSize(500, 20))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.dataset_cam_3_name.setPalette(palette8)
        self.dataset_cam_3_name.setFont(font9)
        self.dataset_cam_3_name.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.horizontalLayout_41.addWidget(self.dataset_cam_3_name)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_14)

        self.D_notif_cam_3 = QLabel(self.frame_28)
        self.D_notif_cam_3.setObjectName(u"D_notif_cam_3")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_notif_cam_3.setPalette(palette9)

        self.horizontalLayout_41.addWidget(self.D_notif_cam_3)

        self.D_cam_3_pausesign = QLabel(self.frame_28)
        self.D_cam_3_pausesign.setObjectName(u"D_cam_3_pausesign")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_cam_3_pausesign.setPalette(palette10)
        self.D_cam_3_pausesign.setFont(font10)

        self.horizontalLayout_41.addWidget(self.D_cam_3_pausesign)

        self.D_cam_3_zoom = QLabel(self.frame_28)
        self.D_cam_3_zoom.setObjectName(u"D_cam_3_zoom")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.D_cam_3_zoom.setPalette(palette11)

        self.horizontalLayout_41.addWidget(self.D_cam_3_zoom)

        self.D_cam_3_play = QPushButton(self.frame_28)
        self.D_cam_3_play.setObjectName(u"D_cam_3_play")
        sizePolicy2.setHeightForWidth(self.D_cam_3_play.sizePolicy().hasHeightForWidth())
        self.D_cam_3_play.setSizePolicy(sizePolicy2)
        self.D_cam_3_play.setMinimumSize(QSize(0, 0))
        self.D_cam_3_play.setMaximumSize(QSize(30, 30))
        self.D_cam_3_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_3_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_3_play.setIcon(icon16)

        self.horizontalLayout_41.addWidget(self.D_cam_3_play)

        self.D_cam_3_pause = QPushButton(self.frame_28)
        self.D_cam_3_pause.setObjectName(u"D_cam_3_pause")
        sizePolicy2.setHeightForWidth(self.D_cam_3_pause.sizePolicy().hasHeightForWidth())
        self.D_cam_3_pause.setSizePolicy(sizePolicy2)
        self.D_cam_3_pause.setMinimumSize(QSize(0, 0))
        self.D_cam_3_pause.setMaximumSize(QSize(30, 30))
        self.D_cam_3_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_3_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_3_pause.setIcon(icon17)

        self.horizontalLayout_41.addWidget(self.D_cam_3_pause)

        self.D_cam_3_capture = QPushButton(self.frame_28)
        self.D_cam_3_capture.setObjectName(u"D_cam_3_capture")
        self.D_cam_3_capture.setMaximumSize(QSize(23, 30))
        self.D_cam_3_capture.setFont(font11)
        self.D_cam_3_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_3_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_3_capture.setIcon(icon15)
        self.D_cam_3_capture.setIconSize(QSize(20, 20))
        self.D_cam_3_capture.setCheckable(False)
        self.D_cam_3_capture.setAutoRepeatDelay(295)
        self.D_cam_3_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_41.addWidget(self.D_cam_3_capture)

        self.D_fs3_btn = QPushButton(self.frame_28)
        self.D_fs3_btn.setObjectName(u"D_fs3_btn")
        self.D_fs3_btn.setMaximumSize(QSize(30, 30))
        self.D_fs3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_fs3_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_fs3_btn.setIcon(icon18)

        self.horizontalLayout_41.addWidget(self.D_fs3_btn)


        self.verticalLayout_7.addWidget(self.frame_28)

        self.datalive_image_label_3 = QLabel(self.framw_camera)
        self.datalive_image_label_3.setObjectName(u"datalive_image_label_3")
        self.datalive_image_label_3.setMaximumSize(QSize(16777215, 16777215))
        self.datalive_image_label_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.datalive_image_label_3.setPixmap(QPixmap(u"C:/Users/milad/.designer/backup/icons/change.png"))
        self.datalive_image_label_3.setScaledContents(True)
        self.datalive_image_label_3.setWordWrap(False)
        self.datalive_image_label_3.setMargin(2)
        self.datalive_image_label_3.setIndent(-1)

        self.verticalLayout_7.addWidget(self.datalive_image_label_3)

        self.frame_29 = QFrame(self.framw_camera)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setEnabled(False)
        self.frame_29.setMaximumSize(QSize(16777215, 50))
        self.frame_29.setFrameShape(QFrame.Box)
        self.frame_29.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.dataset_cam_4_name = QLabel(self.frame_29)
        self.dataset_cam_4_name.setObjectName(u"dataset_cam_4_name")
        self.dataset_cam_4_name.setMaximumSize(QSize(500, 20))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.dataset_cam_4_name.setPalette(palette12)
        self.dataset_cam_4_name.setFont(font9)
        self.dataset_cam_4_name.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.horizontalLayout_42.addWidget(self.dataset_cam_4_name)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_15)

        self.D_notif_cam_4 = QLabel(self.frame_29)
        self.D_notif_cam_4.setObjectName(u"D_notif_cam_4")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_notif_cam_4.setPalette(palette13)

        self.horizontalLayout_42.addWidget(self.D_notif_cam_4)

        self.D_cam_4_pausesign = QLabel(self.frame_29)
        self.D_cam_4_pausesign.setObjectName(u"D_cam_4_pausesign")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.D_cam_4_pausesign.setPalette(palette14)
        self.D_cam_4_pausesign.setFont(font10)

        self.horizontalLayout_42.addWidget(self.D_cam_4_pausesign)

        self.D_cam_4_zoom = QLabel(self.frame_29)
        self.D_cam_4_zoom.setObjectName(u"D_cam_4_zoom")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.D_cam_4_zoom.setPalette(palette15)

        self.horizontalLayout_42.addWidget(self.D_cam_4_zoom)

        self.D_cam_4_play = QPushButton(self.frame_29)
        self.D_cam_4_play.setObjectName(u"D_cam_4_play")
        sizePolicy2.setHeightForWidth(self.D_cam_4_play.sizePolicy().hasHeightForWidth())
        self.D_cam_4_play.setSizePolicy(sizePolicy2)
        self.D_cam_4_play.setMinimumSize(QSize(0, 0))
        self.D_cam_4_play.setMaximumSize(QSize(30, 30))
        self.D_cam_4_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_4_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_4_play.setIcon(icon16)

        self.horizontalLayout_42.addWidget(self.D_cam_4_play)

        self.D_cam_4_pause = QPushButton(self.frame_29)
        self.D_cam_4_pause.setObjectName(u"D_cam_4_pause")
        sizePolicy2.setHeightForWidth(self.D_cam_4_pause.sizePolicy().hasHeightForWidth())
        self.D_cam_4_pause.setSizePolicy(sizePolicy2)
        self.D_cam_4_pause.setMinimumSize(QSize(0, 0))
        self.D_cam_4_pause.setMaximumSize(QSize(30, 30))
        self.D_cam_4_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_4_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_4_pause.setIcon(icon17)

        self.horizontalLayout_42.addWidget(self.D_cam_4_pause)

        self.D_cam_4_capture = QPushButton(self.frame_29)
        self.D_cam_4_capture.setObjectName(u"D_cam_4_capture")
        self.D_cam_4_capture.setMaximumSize(QSize(23, 30))
        self.D_cam_4_capture.setFont(font11)
        self.D_cam_4_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_cam_4_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_cam_4_capture.setIcon(icon15)
        self.D_cam_4_capture.setIconSize(QSize(20, 20))
        self.D_cam_4_capture.setCheckable(False)
        self.D_cam_4_capture.setAutoRepeatDelay(295)
        self.D_cam_4_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_42.addWidget(self.D_cam_4_capture)

        self.D_fs4_btn = QPushButton(self.frame_29)
        self.D_fs4_btn.setObjectName(u"D_fs4_btn")
        self.D_fs4_btn.setMaximumSize(QSize(30, 30))
        self.D_fs4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.D_fs4_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.D_fs4_btn.setIcon(icon18)

        self.horizontalLayout_42.addWidget(self.D_fs4_btn)


        self.verticalLayout_7.addWidget(self.frame_29)

        self.datalive_image_label_4 = QLabel(self.framw_camera)
        self.datalive_image_label_4.setObjectName(u"datalive_image_label_4")
        self.datalive_image_label_4.setMaximumSize(QSize(16777215, 16777215))
        self.datalive_image_label_4.setAcceptDrops(True)
        self.datalive_image_label_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.datalive_image_label_4.setScaledContents(True)
        self.datalive_image_label_4.setAlignment(Qt.AlignCenter)
        self.datalive_image_label_4.setMargin(2)

        self.verticalLayout_7.addWidget(self.datalive_image_label_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.horizontalLayout_18.addWidget(self.framw_camera)


        self.verticalLayout_6.addWidget(self.frame87)

        self.frame_3 = QFrame(self.page_live_dataset)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(197 , 195,196);\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(197 , 195,196);\n"
"border:rgb(197 , 195,196);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 0, 10, 0)

        self.horizontalLayout_7.addWidget(self.frame_6)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_live_dataset)
        self.page_fullscreen_2 = QWidget()
        self.page_fullscreen_2.setObjectName(u"page_fullscreen_2")
        self.horizontalLayout_11 = QHBoxLayout(self.page_fullscreen_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 2, 3, 3)
        self.Body_2 = QFrame(self.page_fullscreen_2)
        self.Body_2.setObjectName(u"Body_2")
        self.Body_2.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"\n"
"")
        self.Body_2.setFrameShape(QFrame.NoFrame)
        self.Body_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.Body_2)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.leftMenu_2 = QFrame(self.Body_2)
        self.leftMenu_2.setObjectName(u"leftMenu_2")
        sizePolicy1.setHeightForWidth(self.leftMenu_2.sizePolicy().hasHeightForWidth())
        self.leftMenu_2.setSizePolicy(sizePolicy1)
        self.leftMenu_2.setMinimumSize(QSize(43, 0))
        self.leftMenu_2.setMaximumSize(QSize(43, 16777215))
        self.leftMenu_2.setStyleSheet(u"background-color: rgb(100, 100,100);")
        self.leftMenu_2.setFrameShape(QFrame.NoFrame)
        self.leftMenu_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.leftMenu_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.aframe_2 = QFrame(self.leftMenu_2)
        self.aframe_2.setObjectName(u"aframe_2")
        self.aframe_2.setMinimumSize(QSize(46, 225))
        self.aframe_2.setStyleSheet(u"background-color: rgb(100,100,100);")
        self.aframe_2.setFrameShape(QFrame.NoFrame)
        self.aframe_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.aframe_2)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.cam_1_btn = QPushButton(self.aframe_2)
        self.cam_1_btn.setObjectName(u"cam_1_btn")
        self.cam_1_btn.setMinimumSize(QSize(40, 45))
        self.cam_1_btn.setMaximumSize(QSize(40, 45))
        self.cam_1_btn.setFont(font6)
        self.cam_1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam_1_btn.setLayoutDirection(Qt.LeftToRight)
        self.cam_1_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,100,100);\n"
"\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"    text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(120,120,120);\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"icons/1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cam_1_btn.setIcon(icon19)
        self.cam_1_btn.setIconSize(QSize(20, 25))

        self.verticalLayout_32.addWidget(self.cam_1_btn, 0, Qt.AlignHCenter)

        self.cam_2_btn = QPushButton(self.aframe_2)
        self.cam_2_btn.setObjectName(u"cam_2_btn")
        self.cam_2_btn.setMinimumSize(QSize(40, 45))
        self.cam_2_btn.setMaximumSize(QSize(40, 45))
        self.cam_2_btn.setFont(font6)
        self.cam_2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam_2_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,100,100);\n"
"\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"    text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(120,120,120);\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u"icons/2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cam_2_btn.setIcon(icon20)
        self.cam_2_btn.setIconSize(QSize(20, 25))

        self.verticalLayout_32.addWidget(self.cam_2_btn, 0, Qt.AlignHCenter)

        self.cam_3_btn = QPushButton(self.aframe_2)
        self.cam_3_btn.setObjectName(u"cam_3_btn")
        self.cam_3_btn.setMinimumSize(QSize(40, 45))
        self.cam_3_btn.setMaximumSize(QSize(40, 45))
        self.cam_3_btn.setFont(font6)
        self.cam_3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam_3_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,100,100);\n"
"\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"    text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(120,120,120);\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u"icons/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cam_3_btn.setIcon(icon21)
        self.cam_3_btn.setIconSize(QSize(21, 25))

        self.verticalLayout_32.addWidget(self.cam_3_btn, 0, Qt.AlignHCenter)

        self.cam_4_btn = QPushButton(self.aframe_2)
        self.cam_4_btn.setObjectName(u"cam_4_btn")
        self.cam_4_btn.setMinimumSize(QSize(40, 45))
        self.cam_4_btn.setMaximumSize(QSize(40, 45))
        self.cam_4_btn.setFont(font6)
        self.cam_4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cam_4_btn.setAutoFillBackground(False)
        self.cam_4_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,100,100);\n"
"\n"
"	color: rgb(0,0,0);\n"
"	border: none;\n"
"    text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 20px;\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(120,120,120);\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u"icons/4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cam_4_btn.setIcon(icon22)
        self.cam_4_btn.setIconSize(QSize(20, 25))

        self.verticalLayout_32.addWidget(self.cam_4_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.aframe_2, 0, Qt.AlignRight)

        self.bt_2 = QSpacerItem(20, 329, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.bt_2)

        self.frame_5 = QFrame(self.leftMenu_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 50))
        self.frame_5.setMaximumSize(QSize(200, 50))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_5)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_22.addWidget(self.frame_5)


        self.horizontalLayout_28.addWidget(self.leftMenu_2, 0, Qt.AlignRight)

        self.Container_2 = QFrame(self.Body_2)
        self.Container_2.setObjectName(u"Container_2")
        self.Container_2.setMaximumSize(QSize(16777215, 16777215))
        self.Container_2.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"")
        self.Container_2.setFrameShape(QFrame.NoFrame)
        self.Container_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.Container_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(5, 3, 3, 3)
        self.frame_32 = QFrame(self.Container_2)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 50))
        self.frame_32.setMaximumSize(QSize(16777215, 50))
        self.frame_32.setFrameShape(QFrame.Box)
        self.frame_32.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.fs_cam_name = QLabel(self.frame_32)
        self.fs_cam_name.setObjectName(u"fs_cam_name")
        self.fs_cam_name.setMaximumSize(QSize(500, 16))
        font12 = QFont()
        font12.setFamilies([u"Times New Roman"])
        font12.setPointSize(13)
        self.fs_cam_name.setFont(font12)

        self.horizontalLayout_37.addWidget(self.fs_cam_name)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_9)

        self.fs_pause_sign = QLabel(self.frame_32)
        self.fs_pause_sign.setObjectName(u"fs_pause_sign")
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush9 = QBrush(QColor(100, 100, 100, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        self.fs_pause_sign.setPalette(palette16)
        self.fs_pause_sign.setFont(font10)

        self.horizontalLayout_37.addWidget(self.fs_pause_sign)

        self.fs2_btn_11 = QPushButton(self.frame_32)
        self.fs2_btn_11.setObjectName(u"fs2_btn_11")
        self.fs2_btn_11.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.fs2_btn_11.sizePolicy().hasHeightForWidth())
        self.fs2_btn_11.setSizePolicy(sizePolicy2)
        self.fs2_btn_11.setMinimumSize(QSize(0, 0))
        self.fs2_btn_11.setMaximumSize(QSize(30, 30))
        self.fs2_btn_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs2_btn_11.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110);\n"
"}\n"
"")
        self.fs2_btn_11.setIcon(icon16)

        self.horizontalLayout_37.addWidget(self.fs2_btn_11)

        self.fs2_btn_12 = QPushButton(self.frame_32)
        self.fs2_btn_12.setObjectName(u"fs2_btn_12")
        self.fs2_btn_12.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.fs2_btn_12.sizePolicy().hasHeightForWidth())
        self.fs2_btn_12.setSizePolicy(sizePolicy2)
        self.fs2_btn_12.setMinimumSize(QSize(0, 0))
        self.fs2_btn_12.setMaximumSize(QSize(30, 30))
        self.fs2_btn_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs2_btn_12.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110);\n"
"}\n"
"")
        self.fs2_btn_12.setIcon(icon17)

        self.horizontalLayout_37.addWidget(self.fs2_btn_12)

        self.fs_cam__capture = QPushButton(self.frame_32)
        self.fs_cam__capture.setObjectName(u"fs_cam__capture")
        self.fs_cam__capture.setMaximumSize(QSize(23, 30))
        self.fs_cam__capture.setFont(font11)
        self.fs_cam__capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs_cam__capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.fs_cam__capture.setIcon(icon15)
        self.fs_cam__capture.setIconSize(QSize(20, 20))
        self.fs_cam__capture.setCheckable(False)
        self.fs_cam__capture.setAutoRepeatDelay(295)
        self.fs_cam__capture.setAutoRepeatInterval(101)

        self.horizontalLayout_37.addWidget(self.fs_cam__capture)

        self.fs_cam__rotate = QPushButton(self.frame_32)
        self.fs_cam__rotate.setObjectName(u"fs_cam__rotate")
        self.fs_cam__rotate.setMaximumSize(QSize(23, 30))
        self.fs_cam__rotate.setFont(font11)
        self.fs_cam__rotate.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs_cam__rotate.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.fs_cam__rotate.setIcon(icon14)
        self.fs_cam__rotate.setIconSize(QSize(14, 14))
        self.fs_cam__rotate.setCheckable(False)
        self.fs_cam__rotate.setAutoRepeatDelay(295)
        self.fs_cam__rotate.setAutoRepeatInterval(101)

        self.horizontalLayout_37.addWidget(self.fs_cam__rotate)


        self.verticalLayout_34.addWidget(self.frame_32)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.fullscreen_label = QLabel(self.Container_2)
        self.fullscreen_label.setObjectName(u"fullscreen_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fullscreen_label.sizePolicy().hasHeightForWidth())
        self.fullscreen_label.setSizePolicy(sizePolicy3)
        self.fullscreen_label.setMinimumSize(QSize(1, 1))
        self.fullscreen_label.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.fullscreen_label.setPixmap(QPixmap(u"C:/Users/milad/.designer/backup/images/8387315901543238865-512.png"))
        self.fullscreen_label.setScaledContents(True)
        self.fullscreen_label.setMargin(2)

        self.horizontalLayout_29.addWidget(self.fullscreen_label)


        self.verticalLayout_34.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_28.addWidget(self.Container_2)


        self.horizontalLayout_11.addWidget(self.Body_2)

        self.stackedWidget.addWidget(self.page_fullscreen_2)
        self.page_live = QWidget()
        self.page_live.setObjectName(u"page_live")
        self.verticalLayout_15 = QVBoxLayout(self.page_live)
        self.verticalLayout_15.setSpacing(3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(4, 3, 3, 3)
        self.frame_49 = QFrame(self.page_live)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_49)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_47)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_47)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setEnabled(False)
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setMaximumSize(QSize(16777215, 0))
        self.frame_23.setFrameShape(QFrame.Box)
        self.frame_23.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(11, 7, -1, -1)
        self.live_cam_2_name = QLabel(self.frame_23)
        self.live_cam_2_name.setObjectName(u"live_cam_2_name")
        self.live_cam_2_name.setMaximumSize(QSize(500, 16777215))
        self.live_cam_2_name.setFont(font9)

        self.horizontalLayout_32.addWidget(self.live_cam_2_name)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_3)

        self.L_notif_cam_2 = QLabel(self.frame_23)
        self.L_notif_cam_2.setObjectName(u"L_notif_cam_2")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.L_notif_cam_2.setPalette(palette17)

        self.horizontalLayout_32.addWidget(self.L_notif_cam_2)

        self.cam_2_pause = QLabel(self.frame_23)
        self.cam_2_pause.setObjectName(u"cam_2_pause")
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.cam_2_pause.setPalette(palette18)
        self.cam_2_pause.setFont(font10)

        self.horizontalLayout_32.addWidget(self.cam_2_pause)

        self.live_cam_2_zoom = QLabel(self.frame_23)
        self.live_cam_2_zoom.setObjectName(u"live_cam_2_zoom")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush7)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush10 = QBrush(QColor(120, 120, 120, 128))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush7)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.live_cam_2_zoom.setPalette(palette19)

        self.horizontalLayout_32.addWidget(self.live_cam_2_zoom)

        self.live_cam_2_play = QPushButton(self.frame_23)
        self.live_cam_2_play.setObjectName(u"live_cam_2_play")
        sizePolicy2.setHeightForWidth(self.live_cam_2_play.sizePolicy().hasHeightForWidth())
        self.live_cam_2_play.setSizePolicy(sizePolicy2)
        self.live_cam_2_play.setMinimumSize(QSize(0, 0))
        self.live_cam_2_play.setMaximumSize(QSize(30, 30))
        self.live_cam_2_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_2_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_2_play.setIcon(icon16)

        self.horizontalLayout_32.addWidget(self.live_cam_2_play)

        self.live_cam_2_pause = QPushButton(self.frame_23)
        self.live_cam_2_pause.setObjectName(u"live_cam_2_pause")
        sizePolicy2.setHeightForWidth(self.live_cam_2_pause.sizePolicy().hasHeightForWidth())
        self.live_cam_2_pause.setSizePolicy(sizePolicy2)
        self.live_cam_2_pause.setMinimumSize(QSize(0, 0))
        self.live_cam_2_pause.setMaximumSize(QSize(30, 30))
        self.live_cam_2_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_2_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_2_pause.setIcon(icon17)

        self.horizontalLayout_32.addWidget(self.live_cam_2_pause)

        self.checkBox_cam_2 = QCheckBox(self.frame_23)
        self.checkBox_cam_2.setObjectName(u"checkBox_cam_2")

        self.horizontalLayout_32.addWidget(self.checkBox_cam_2)

        self.live_cam_2_setting = QPushButton(self.frame_23)
        self.live_cam_2_setting.setObjectName(u"live_cam_2_setting")
        self.live_cam_2_setting.setMaximumSize(QSize(23, 30))
        self.live_cam_2_setting.setFont(font11)
        self.live_cam_2_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_2_setting.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        icon23 = QIcon()
        icon23.addFile(u"icons/tools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.live_cam_2_setting.setIcon(icon23)
        self.live_cam_2_setting.setIconSize(QSize(20, 20))
        self.live_cam_2_setting.setCheckable(False)
        self.live_cam_2_setting.setAutoRepeatDelay(295)
        self.live_cam_2_setting.setAutoRepeatInterval(101)

        self.horizontalLayout_32.addWidget(self.live_cam_2_setting)

        self.live_cam_2_capture = QPushButton(self.frame_23)
        self.live_cam_2_capture.setObjectName(u"live_cam_2_capture")
        self.live_cam_2_capture.setMaximumSize(QSize(23, 30))
        font13 = QFont()
        font13.setBold(False)
        font13.setUnderline(False)
        font13.setStrikeOut(False)
        self.live_cam_2_capture.setFont(font13)
        self.live_cam_2_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_2_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"            QPushButton{\n"
"                letter-spacing: 0.1px;\n"
"                font-size: 14px;\n"
"                font-weight: 400;\n"
"                line-height: 45px;\n"
"                text-decoration: none;\n"
"                color: #FFF;\n"
"            }\n"
"")
        self.live_cam_2_capture.setIcon(icon15)
        self.live_cam_2_capture.setIconSize(QSize(20, 20))
        self.live_cam_2_capture.setCheckable(False)
        self.live_cam_2_capture.setAutoRepeatDelay(295)
        self.live_cam_2_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_32.addWidget(self.live_cam_2_capture)

        self.fs2_btn = QPushButton(self.frame_23)
        self.fs2_btn.setObjectName(u"fs2_btn")
        self.fs2_btn.setMaximumSize(QSize(30, 30))
        self.fs2_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs2_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.fs2_btn.setIcon(icon18)

        self.horizontalLayout_32.addWidget(self.fs2_btn)


        self.verticalLayout_45.addWidget(self.frame_23)

        self.toogle_cam_2 = QPushButton(self.frame_47)
        self.toogle_cam_2.setObjectName(u"toogle_cam_2")
        self.toogle_cam_2.setMaximumSize(QSize(23, 11))
        icon24 = QIcon()
        icon24.addFile(u"images/chevron - down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toogle_cam_2.setIcon(icon24)

        self.verticalLayout_45.addWidget(self.toogle_cam_2)


        self.verticalLayout_9.addWidget(self.frame_47)

        self.live_image_label_2 = QLabel(self.frame)
        self.live_image_label_2.setObjectName(u"live_image_label_2")
        sizePolicy3.setHeightForWidth(self.live_image_label_2.sizePolicy().hasHeightForWidth())
        self.live_image_label_2.setSizePolicy(sizePolicy3)
        self.live_image_label_2.setMinimumSize(QSize(1, 1))
        self.live_image_label_2.setMaximumSize(QSize(16777215, 11111111))
        self.live_image_label_2.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.live_image_label_2.setPixmap(QPixmap(u"../Foolad-slab/images/8387315901543238865-512.png"))
        self.live_image_label_2.setScaledContents(True)
        self.live_image_label_2.setMargin(2)

        self.verticalLayout_9.addWidget(self.live_image_label_2)

        self.frame_41 = QFrame(self.frame)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_41)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_41)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setEnabled(True)
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setMaximumSize(QSize(16777215, 1))
        self.frame_51.setFrameShape(QFrame.Box)
        self.frame_51.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.live_cam_4_name = QLabel(self.frame_51)
        self.live_cam_4_name.setObjectName(u"live_cam_4_name")
        self.live_cam_4_name.setMaximumSize(QSize(500, 16777215))
        self.live_cam_4_name.setFont(font9)

        self.horizontalLayout_36.addWidget(self.live_cam_4_name)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_10)

        self.L_notif_cam_4 = QLabel(self.frame_51)
        self.L_notif_cam_4.setObjectName(u"L_notif_cam_4")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.L_notif_cam_4.setPalette(palette20)

        self.horizontalLayout_36.addWidget(self.L_notif_cam_4)

        self.cam_4_pause = QLabel(self.frame_51)
        self.cam_4_pause.setObjectName(u"cam_4_pause")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.cam_4_pause.setPalette(palette21)
        self.cam_4_pause.setFont(font10)

        self.horizontalLayout_36.addWidget(self.cam_4_pause)

        self.live_cam_4_zoom = QLabel(self.frame_51)
        self.live_cam_4_zoom.setObjectName(u"live_cam_4_zoom")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.live_cam_4_zoom.setPalette(palette22)

        self.horizontalLayout_36.addWidget(self.live_cam_4_zoom)

        self.live_cam_4_play = QPushButton(self.frame_51)
        self.live_cam_4_play.setObjectName(u"live_cam_4_play")
        sizePolicy2.setHeightForWidth(self.live_cam_4_play.sizePolicy().hasHeightForWidth())
        self.live_cam_4_play.setSizePolicy(sizePolicy2)
        self.live_cam_4_play.setMinimumSize(QSize(0, 0))
        self.live_cam_4_play.setMaximumSize(QSize(30, 30))
        self.live_cam_4_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_4_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_4_play.setIcon(icon16)

        self.horizontalLayout_36.addWidget(self.live_cam_4_play)

        self.live_cam_4_pause = QPushButton(self.frame_51)
        self.live_cam_4_pause.setObjectName(u"live_cam_4_pause")
        sizePolicy2.setHeightForWidth(self.live_cam_4_pause.sizePolicy().hasHeightForWidth())
        self.live_cam_4_pause.setSizePolicy(sizePolicy2)
        self.live_cam_4_pause.setMinimumSize(QSize(0, 0))
        self.live_cam_4_pause.setMaximumSize(QSize(30, 30))
        self.live_cam_4_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_4_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_4_pause.setIcon(icon17)

        self.horizontalLayout_36.addWidget(self.live_cam_4_pause)

        self.checkBox_cam_4 = QCheckBox(self.frame_51)
        self.checkBox_cam_4.setObjectName(u"checkBox_cam_4")

        self.horizontalLayout_36.addWidget(self.checkBox_cam_4)

        self.live_cam_4_setting = QPushButton(self.frame_51)
        self.live_cam_4_setting.setObjectName(u"live_cam_4_setting")
        self.live_cam_4_setting.setMaximumSize(QSize(23, 30))
        self.live_cam_4_setting.setFont(font11)
        self.live_cam_4_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_4_setting.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_4_setting.setIcon(icon23)
        self.live_cam_4_setting.setIconSize(QSize(20, 20))
        self.live_cam_4_setting.setCheckable(False)
        self.live_cam_4_setting.setAutoRepeatDelay(295)
        self.live_cam_4_setting.setAutoRepeatInterval(101)

        self.horizontalLayout_36.addWidget(self.live_cam_4_setting)

        self.live_cam_4_capture = QPushButton(self.frame_51)
        self.live_cam_4_capture.setObjectName(u"live_cam_4_capture")
        self.live_cam_4_capture.setMaximumSize(QSize(23, 34))
        self.live_cam_4_capture.setFont(font11)
        self.live_cam_4_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_4_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_4_capture.setIcon(icon15)
        self.live_cam_4_capture.setIconSize(QSize(20, 20))
        self.live_cam_4_capture.setCheckable(False)
        self.live_cam_4_capture.setAutoRepeatDelay(295)
        self.live_cam_4_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_36.addWidget(self.live_cam_4_capture)

        self.fs4_btn = QPushButton(self.frame_51)
        self.fs4_btn.setObjectName(u"fs4_btn")
        self.fs4_btn.setMaximumSize(QSize(30, 30))
        self.fs4_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs4_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.fs4_btn.setIcon(icon18)

        self.horizontalLayout_36.addWidget(self.fs4_btn)


        self.verticalLayout_12.addWidget(self.frame_51)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_16)

        self.frame_24 = QFrame(self.frame_41)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_24)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setEnabled(False)
        self.frame_25.setMaximumSize(QSize(16777215, 1))
        self.frame_25.setFrameShape(QFrame.Box)
        self.frame_25.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.live_cam_3_name = QLabel(self.frame_25)
        self.live_cam_3_name.setObjectName(u"live_cam_3_name")
        self.live_cam_3_name.setMaximumSize(QSize(500, 16777215))
        self.live_cam_3_name.setFont(font9)

        self.horizontalLayout_34.addWidget(self.live_cam_3_name)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_8)

        self.L_notif_cam_3 = QLabel(self.frame_25)
        self.L_notif_cam_3.setObjectName(u"L_notif_cam_3")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.L_notif_cam_3.setPalette(palette23)

        self.horizontalLayout_34.addWidget(self.L_notif_cam_3)

        self.cam_3_pause = QLabel(self.frame_25)
        self.cam_3_pause.setObjectName(u"cam_3_pause")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.cam_3_pause.setPalette(palette24)
        self.cam_3_pause.setFont(font10)

        self.horizontalLayout_34.addWidget(self.cam_3_pause)

        self.live_cam_3_zoom = QLabel(self.frame_25)
        self.live_cam_3_zoom.setObjectName(u"live_cam_3_zoom")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.live_cam_3_zoom.setPalette(palette25)

        self.horizontalLayout_34.addWidget(self.live_cam_3_zoom)

        self.live_cam_3_play = QPushButton(self.frame_25)
        self.live_cam_3_play.setObjectName(u"live_cam_3_play")
        sizePolicy2.setHeightForWidth(self.live_cam_3_play.sizePolicy().hasHeightForWidth())
        self.live_cam_3_play.setSizePolicy(sizePolicy2)
        self.live_cam_3_play.setMinimumSize(QSize(0, 0))
        self.live_cam_3_play.setMaximumSize(QSize(30, 30))
        self.live_cam_3_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_3_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_3_play.setIcon(icon16)

        self.horizontalLayout_34.addWidget(self.live_cam_3_play)

        self.live_cam_3_pause = QPushButton(self.frame_25)
        self.live_cam_3_pause.setObjectName(u"live_cam_3_pause")
        sizePolicy2.setHeightForWidth(self.live_cam_3_pause.sizePolicy().hasHeightForWidth())
        self.live_cam_3_pause.setSizePolicy(sizePolicy2)
        self.live_cam_3_pause.setMinimumSize(QSize(0, 0))
        self.live_cam_3_pause.setMaximumSize(QSize(30, 30))
        self.live_cam_3_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_3_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_3_pause.setIcon(icon17)

        self.horizontalLayout_34.addWidget(self.live_cam_3_pause)

        self.checkBox_cam_3 = QCheckBox(self.frame_25)
        self.checkBox_cam_3.setObjectName(u"checkBox_cam_3")

        self.horizontalLayout_34.addWidget(self.checkBox_cam_3)

        self.live_cam_3_setting = QPushButton(self.frame_25)
        self.live_cam_3_setting.setObjectName(u"live_cam_3_setting")
        self.live_cam_3_setting.setMaximumSize(QSize(23, 30))
        self.live_cam_3_setting.setFont(font11)
        self.live_cam_3_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_3_setting.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_3_setting.setIcon(icon23)
        self.live_cam_3_setting.setIconSize(QSize(20, 20))
        self.live_cam_3_setting.setCheckable(False)
        self.live_cam_3_setting.setAutoRepeatDelay(295)
        self.live_cam_3_setting.setAutoRepeatInterval(101)

        self.horizontalLayout_34.addWidget(self.live_cam_3_setting)

        self.live_cam_3_capture = QPushButton(self.frame_25)
        self.live_cam_3_capture.setObjectName(u"live_cam_3_capture")
        self.live_cam_3_capture.setMaximumSize(QSize(23, 30))
        self.live_cam_3_capture.setFont(font11)
        self.live_cam_3_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_3_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_3_capture.setIcon(icon15)
        self.live_cam_3_capture.setIconSize(QSize(20, 20))
        self.live_cam_3_capture.setCheckable(False)
        self.live_cam_3_capture.setAutoRepeatDelay(295)
        self.live_cam_3_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_34.addWidget(self.live_cam_3_capture)

        self.fs3_btn = QPushButton(self.frame_25)
        self.fs3_btn.setObjectName(u"fs3_btn")
        self.fs3_btn.setMaximumSize(QSize(30, 30))
        self.fs3_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs3_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.fs3_btn.setIcon(icon18)

        self.horizontalLayout_34.addWidget(self.fs3_btn)


        self.verticalLayout_10.addWidget(self.frame_25)

        self.toogle_cam_3 = QPushButton(self.frame_24)
        self.toogle_cam_3.setObjectName(u"toogle_cam_3")
        self.toogle_cam_3.setMaximumSize(QSize(23, 11))
        self.toogle_cam_3.setIcon(icon24)

        self.verticalLayout_10.addWidget(self.toogle_cam_3, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_24)

        self.toogle_cam_4 = QPushButton(self.frame_41)
        self.toogle_cam_4.setObjectName(u"toogle_cam_4")
        self.toogle_cam_4.setMaximumSize(QSize(23, 11))
        self.toogle_cam_4.setIcon(icon24)

        self.verticalLayout_12.addWidget(self.toogle_cam_4)

        self.frame_55 = QFrame(self.frame_41)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.live_image_label_4 = QLabel(self.frame_55)
        self.live_image_label_4.setObjectName(u"live_image_label_4")
        sizePolicy3.setHeightForWidth(self.live_image_label_4.sizePolicy().hasHeightForWidth())
        self.live_image_label_4.setSizePolicy(sizePolicy3)
        self.live_image_label_4.setMinimumSize(QSize(1, 1))
        self.live_image_label_4.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.live_image_label_4.setPixmap(QPixmap(u"../Foolad-slab/images/8387315901543238865-512.png"))
        self.live_image_label_4.setScaledContents(True)
        self.live_image_label_4.setMargin(2)

        self.horizontalLayout_9.addWidget(self.live_image_label_4)

        self.live_image_label_3 = QLabel(self.frame_55)
        self.live_image_label_3.setObjectName(u"live_image_label_3")
        sizePolicy3.setHeightForWidth(self.live_image_label_3.sizePolicy().hasHeightForWidth())
        self.live_image_label_3.setSizePolicy(sizePolicy3)
        self.live_image_label_3.setMinimumSize(QSize(1, 1))
        self.live_image_label_3.setAutoFillBackground(False)
        self.live_image_label_3.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.live_image_label_3.setPixmap(QPixmap(u"../Foolad-slab/images/8387315901543238865-512.png"))
        self.live_image_label_3.setScaledContents(True)
        self.live_image_label_3.setMargin(2)

        self.horizontalLayout_9.addWidget(self.live_image_label_3)


        self.verticalLayout_12.addWidget(self.frame_55)


        self.verticalLayout_9.addWidget(self.frame_41)


        self.horizontalLayout_43.addWidget(self.frame)

        self.frame_15 = QFrame(self.frame_49)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(400, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_42 = QFrame(self.frame_15)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_42)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_42)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setEnabled(False)
        self.frame_26.setMinimumSize(QSize(0, 0))
        self.frame_26.setMaximumSize(QSize(16777215, 0))
        self.frame_26.setFrameShape(QFrame.Box)
        self.frame_26.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.live_cam_1_name = QLabel(self.frame_26)
        self.live_cam_1_name.setObjectName(u"live_cam_1_name")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.live_cam_1_name.sizePolicy().hasHeightForWidth())
        self.live_cam_1_name.setSizePolicy(sizePolicy4)
        self.live_cam_1_name.setMaximumSize(QSize(500, 16777215))
        self.live_cam_1_name.setFont(font9)

        self.horizontalLayout_38.addWidget(self.live_cam_1_name)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_13)

        self.L_notif_cam_1 = QLabel(self.frame_26)
        self.L_notif_cam_1.setObjectName(u"L_notif_cam_1")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.L_notif_cam_1.setPalette(palette26)

        self.horizontalLayout_38.addWidget(self.L_notif_cam_1)

        self.cam_1_pause = QLabel(self.frame_26)
        self.cam_1_pause.setObjectName(u"cam_1_pause")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.cam_1_pause.setPalette(palette27)
        self.cam_1_pause.setFont(font10)

        self.horizontalLayout_38.addWidget(self.cam_1_pause)

        self.live_cam_1_zoom = QLabel(self.frame_26)
        self.live_cam_1_zoom.setObjectName(u"live_cam_1_zoom")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush7)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush7)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush7)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush7)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush7)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush7)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.live_cam_1_zoom.setPalette(palette28)

        self.horizontalLayout_38.addWidget(self.live_cam_1_zoom)

        self.live_cam_1_play = QPushButton(self.frame_26)
        self.live_cam_1_play.setObjectName(u"live_cam_1_play")
        sizePolicy2.setHeightForWidth(self.live_cam_1_play.sizePolicy().hasHeightForWidth())
        self.live_cam_1_play.setSizePolicy(sizePolicy2)
        self.live_cam_1_play.setMinimumSize(QSize(0, 0))
        self.live_cam_1_play.setMaximumSize(QSize(30, 30))
        self.live_cam_1_play.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_1_play.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_1_play.setIcon(icon16)

        self.horizontalLayout_38.addWidget(self.live_cam_1_play)

        self.live_cam_1_pause = QPushButton(self.frame_26)
        self.live_cam_1_pause.setObjectName(u"live_cam_1_pause")
        sizePolicy2.setHeightForWidth(self.live_cam_1_pause.sizePolicy().hasHeightForWidth())
        self.live_cam_1_pause.setSizePolicy(sizePolicy2)
        self.live_cam_1_pause.setMinimumSize(QSize(0, 0))
        self.live_cam_1_pause.setMaximumSize(QSize(30, 30))
        self.live_cam_1_pause.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_1_pause.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_1_pause.setIcon(icon17)

        self.horizontalLayout_38.addWidget(self.live_cam_1_pause)

        self.checkBox_cam_1 = QCheckBox(self.frame_26)
        self.checkBox_cam_1.setObjectName(u"checkBox_cam_1")

        self.horizontalLayout_38.addWidget(self.checkBox_cam_1)

        self.live_cam_1_setting = QPushButton(self.frame_26)
        self.live_cam_1_setting.setObjectName(u"live_cam_1_setting")
        self.live_cam_1_setting.setEnabled(False)
        self.live_cam_1_setting.setMaximumSize(QSize(23, 30))
        self.live_cam_1_setting.setFont(font11)
        self.live_cam_1_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_1_setting.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_1_setting.setIcon(icon23)
        self.live_cam_1_setting.setIconSize(QSize(20, 20))
        self.live_cam_1_setting.setCheckable(False)
        self.live_cam_1_setting.setAutoRepeatDelay(295)
        self.live_cam_1_setting.setAutoRepeatInterval(101)

        self.horizontalLayout_38.addWidget(self.live_cam_1_setting)

        self.live_cam_1_capture = QPushButton(self.frame_26)
        self.live_cam_1_capture.setObjectName(u"live_cam_1_capture")
        self.live_cam_1_capture.setMaximumSize(QSize(23, 30))
        self.live_cam_1_capture.setFont(font11)
        self.live_cam_1_capture.setCursor(QCursor(Qt.PointingHandCursor))
        self.live_cam_1_capture.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.live_cam_1_capture.setIcon(icon15)
        self.live_cam_1_capture.setIconSize(QSize(20, 20))
        self.live_cam_1_capture.setCheckable(False)
        self.live_cam_1_capture.setAutoRepeatDelay(295)
        self.live_cam_1_capture.setAutoRepeatInterval(101)

        self.horizontalLayout_38.addWidget(self.live_cam_1_capture)

        self.fs1_btn = QPushButton(self.frame_26)
        self.fs1_btn.setObjectName(u"fs1_btn")
        self.fs1_btn.setMaximumSize(QSize(30, 30))
        self.fs1_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fs1_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(197 , 195,196);\n"
"}\n"
"")
        self.fs1_btn.setIcon(icon18)

        self.horizontalLayout_38.addWidget(self.fs1_btn)


        self.verticalLayout_47.addWidget(self.frame_26)

        self.toogle_cam_1 = QPushButton(self.frame_42)
        self.toogle_cam_1.setObjectName(u"toogle_cam_1")
        self.toogle_cam_1.setMaximumSize(QSize(23, 11))
        self.toogle_cam_1.setIcon(icon24)

        self.verticalLayout_47.addWidget(self.toogle_cam_1)

        self.label = QLabel(self.frame_42)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 38))
        font14 = QFont()
        font14.setPointSize(12)
        self.label.setFont(font14)

        self.verticalLayout_47.addWidget(self.label, 0, Qt.AlignHCenter)

        self.live_image_label_5 = QLabel(self.frame_42)
        self.live_image_label_5.setObjectName(u"live_image_label_5")
        self.live_image_label_5.setMinimumSize(QSize(1, 200))
        self.live_image_label_5.setMaximumSize(QSize(16777215, 11111111))
        self.live_image_label_5.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.live_image_label_5.setAcceptDrops(False)
        self.live_image_label_5.setStyleSheet(u"QLabel{\n"
"	background-color:rgb(197 , 195,196);\n"
"	border: 2px solid rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.live_image_label_5.setPixmap(QPixmap(u"../Foolad-slab/images/camera.png"))
        self.live_image_label_5.setScaledContents(True)
        self.live_image_label_5.setMargin(2)

        self.verticalLayout_47.addWidget(self.live_image_label_5, 0, Qt.AlignHCenter)

        self.live_image_label_1 = QLabel(self.frame_42)
        self.live_image_label_1.setObjectName(u"live_image_label_1")
        self.live_image_label_1.setFrameShape(QFrame.Box)
        self.live_image_label_1.setScaledContents(True)

        self.verticalLayout_47.addWidget(self.live_image_label_1)


        self.verticalLayout.addWidget(self.frame_42)


        self.horizontalLayout_43.addWidget(self.frame_15)


        self.verticalLayout_15.addWidget(self.frame_49)

        self.stackedWidget.addWidget(self.page_live)
        self.page_aboutus = QWidget()
        self.page_aboutus.setObjectName(u"page_aboutus")
        self.gridLayout_3 = QGridLayout(self.page_aboutus)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(4)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_14 = QFrame(self.page_aboutus)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(3, 65))
        self.frame_14.setMaximumSize(QSize(16777215, 900))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(197 , 195,196);\n"
"\n"
"	border-radius: 15px;\n"
"	border: 1px solid rgb(0,0, 0);\n"
"}\n"
"\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.textEdit_2 = QTextEdit(self.frame_14)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 16777215))
        font15 = QFont()
        font15.setFamilies([u"Britannic Bold"])
        self.textEdit_2.setFont(font15)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_8.addWidget(self.textEdit_2)

        self.textEdit = QTextEdit(self.frame_14)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 16777215))
        self.textEdit.setFont(font15)

        self.horizontalLayout_8.addWidget(self.textEdit)


        self.gridLayout_2.addWidget(self.frame_14, 1, 0, 1, 2)

        self.horizontalFrame_3 = QFrame(self.page_aboutus)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalFrame_3.setMinimumSize(QSize(0, 329))
        self.layoutWidget = QWidget(self.horizontalFrame_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 544, 302))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.layoutWidget)
        self.label_33.setObjectName(u"label_33")
        font16 = QFont()
        font16.setPointSize(21)
        self.label_33.setFont(font16)

        self.horizontalLayout_10.addWidget(self.label_33)

        self.user_manual_btn = QPushButton(self.layoutWidget)
        self.user_manual_btn.setObjectName(u"user_manual_btn")

        self.horizontalLayout_10.addWidget(self.user_manual_btn)

        self.label_34 = QLabel(self.layoutWidget)
        self.label_34.setObjectName(u"label_34")
        sizePolicy2.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy2)
        self.label_34.setMaximumSize(QSize(300, 300))
        self.label_34.setPixmap(QPixmap(u"C:/Users/milad/.designer/backup/topcoder.png"))
        self.label_34.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_34)


        self.gridLayout_2.addWidget(self.horizontalFrame_3, 2, 1, 1, 1)

        self.horizontalFrame_5 = QFrame(self.page_aboutus)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        sizePolicy2.setHeightForWidth(self.horizontalFrame_5.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_5.setSizePolicy(sizePolicy2)
        self.horizontalFrame_5.setMinimumSize(QSize(0, 72))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_32 = QLabel(self.horizontalFrame_5)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_14.addWidget(self.label_32)


        self.gridLayout_2.addWidget(self.horizontalFrame_5, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.horizontalFrame_2 = QFrame(self.page_aboutus)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setFrameShape(QFrame.Box)
        self.horizontalFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_45 = QLabel(self.horizontalFrame_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(500, 252))
        self.label_45.setFont(font8)
        self.label_45.setPixmap(QPixmap(u"images/dorsa2.png"))
        self.label_45.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_45, 0, Qt.AlignTop)

        self.label_46 = QLabel(self.horizontalFrame_2)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_6.addWidget(self.label_46)

        self.label_43 = QLabel(self.horizontalFrame_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setEnabled(True)
        self.label_43.setPixmap(QPixmap(u"images/637288638132980756.png"))

        self.horizontalLayout_6.addWidget(self.label_43)


        self.gridLayout_3.addWidget(self.horizontalFrame_2, 0, 0, 1, 1, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.page_aboutus)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.horizontalLayout_16 = QHBoxLayout(self.page_report)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(3, 3, 4, 4)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_17 = QFrame(self.page_report)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(3, 3, 3, 3)
        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(400, 0))
        self.frame_19.setMaximumSize(QSize(300, 16777215))
        self.frame_19.setFrameShape(QFrame.Panel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.checkBox_last_report = QCheckBox(self.frame_19)
        self.checkBox_last_report.setObjectName(u"checkBox_last_report")
        self.checkBox_last_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_19.addWidget(self.checkBox_last_report)

        self.label_29 = QLabel(self.frame_19)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 50))
        self.label_29.setFont(font12)

        self.horizontalLayout_19.addWidget(self.label_29, 0, Qt.AlignLeft)

        self.spinBox_tedad = QSpinBox(self.frame_19)
        self.spinBox_tedad.setObjectName(u"spinBox_tedad")
        self.spinBox_tedad.setMaximumSize(QSize(16777215, 16777212))
        font17 = QFont()
        font17.setFamilies([u"Times New Roman"])
        font17.setPointSize(12)
        self.spinBox_tedad.setFont(font17)
        self.spinBox_tedad.setMaximum(999)
        self.spinBox_tedad.setValue(10)

        self.horizontalLayout_19.addWidget(self.spinBox_tedad)


        self.verticalLayout_19.addLayout(self.horizontalLayout_19)

        self.line_11 = QFrame(self.frame_19)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_11)

        self.verticalSpacer_10 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_10)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.checkBox_id_report = QCheckBox(self.frame_19)
        self.checkBox_id_report.setObjectName(u"checkBox_id_report")
        self.checkBox_id_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_20.addWidget(self.checkBox_id_report)

        self.label_37 = QLabel(self.frame_19)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 50))
        self.label_37.setFont(font12)

        self.horizontalLayout_20.addWidget(self.label_37)

        self.lineEdit_id = QLineEdit(self.frame_19)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_id.setFont(font17)

        self.horizontalLayout_20.addWidget(self.lineEdit_id)


        self.verticalLayout_23.addLayout(self.horizontalLayout_20)


        self.verticalLayout_19.addLayout(self.verticalLayout_23)

        self.line_12 = QFrame(self.frame_19)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_12)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_13)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.checkBox_line_report = QCheckBox(self.frame_19)
        self.checkBox_line_report.setObjectName(u"checkBox_line_report")
        self.checkBox_line_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_26.addWidget(self.checkBox_line_report)

        self.label_30 = QLabel(self.frame_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 50))
        self.label_30.setFont(font12)

        self.horizontalLayout_26.addWidget(self.label_30)

        self.lineEdit_line = QLineEdit(self.frame_19)
        self.lineEdit_line.setObjectName(u"lineEdit_line")
        self.lineEdit_line.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_line.setFont(font17)

        self.horizontalLayout_26.addWidget(self.lineEdit_line)


        self.verticalLayout_19.addLayout(self.horizontalLayout_26)

        self.line_13 = QFrame(self.frame_19)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_13)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_11)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.checkBox_date_report = QCheckBox(self.frame_19)
        self.checkBox_date_report.setObjectName(u"checkBox_date_report")
        self.checkBox_date_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_21.addWidget(self.checkBox_date_report, 0, Qt.AlignBottom)

        self.label_47 = QLabel(self.frame_19)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font12)

        self.horizontalLayout_21.addWidget(self.label_47, 0, Qt.AlignBottom)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_11 = QFrame(self.frame_19)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 7))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 30))
        font18 = QFont()
        font18.setFamilies([u"Times New Roman"])
        font18.setPointSize(9)
        self.label_48.setFont(font18)

        self.horizontalLayout_24.addWidget(self.label_48)

        self.tool_start_calender = QToolButton(self.frame_11)
        self.tool_start_calender.setObjectName(u"tool_start_calender")
        self.tool_start_calender.setEnabled(True)
        self.tool_start_calender.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_24.addWidget(self.tool_start_calender)


        self.verticalLayout_25.addWidget(self.frame_11)

        self.lineEdit_date_start = QLineEdit(self.frame_19)
        self.lineEdit_date_start.setObjectName(u"lineEdit_date_start")
        self.lineEdit_date_start.setFont(font17)

        self.verticalLayout_25.addWidget(self.lineEdit_date_start)


        self.horizontalLayout_21.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_12 = QFrame(self.frame_19)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 7))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.frame_12)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(16777215, 30))
        self.label_56.setFont(font18)

        self.horizontalLayout_25.addWidget(self.label_56)

        self.tool_end_calender = QToolButton(self.frame_12)
        self.tool_end_calender.setObjectName(u"tool_end_calender")
        self.tool_end_calender.setEnabled(True)
        self.tool_end_calender.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_25.addWidget(self.tool_end_calender)


        self.verticalLayout_26.addWidget(self.frame_12)

        self.lineEdit_date_end = QLineEdit(self.frame_19)
        self.lineEdit_date_end.setObjectName(u"lineEdit_date_end")
        self.lineEdit_date_end.setFont(font17)

        self.verticalLayout_26.addWidget(self.lineEdit_date_end)


        self.horizontalLayout_21.addLayout(self.verticalLayout_26)


        self.verticalLayout_27.addLayout(self.horizontalLayout_21)


        self.verticalLayout_19.addLayout(self.verticalLayout_27)

        self.line_18 = QFrame(self.frame_19)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_18)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_12)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.checkBox_time_report = QCheckBox(self.frame_19)
        self.checkBox_time_report.setObjectName(u"checkBox_time_report")
        self.checkBox_time_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_22.addWidget(self.checkBox_time_report, 0, Qt.AlignBottom)

        self.label_53 = QLabel(self.frame_19)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font12)

        self.horizontalLayout_22.addWidget(self.label_53, 0, Qt.AlignBottom)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_50 = QFrame(self.frame_19)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 18))
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_50)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font18)

        self.horizontalLayout_51.addWidget(self.label_54)

        self.tool_start_time = QToolButton(self.frame_50)
        self.tool_start_time.setObjectName(u"tool_start_time")
        self.tool_start_time.setEnabled(True)
        self.tool_start_time.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_51.addWidget(self.tool_start_time)


        self.verticalLayout_29.addWidget(self.frame_50)

        self.lineEdit_time_start = QLineEdit(self.frame_19)
        self.lineEdit_time_start.setObjectName(u"lineEdit_time_start")
        self.lineEdit_time_start.setFont(font17)

        self.verticalLayout_29.addWidget(self.lineEdit_time_start)


        self.horizontalLayout_22.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_54 = QFrame(self.frame_19)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 18))
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_54)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font18)

        self.horizontalLayout_52.addWidget(self.label_55)

        self.btn_now_time = QPushButton(self.frame_54)
        self.btn_now_time.setObjectName(u"btn_now_time")
        self.btn_now_time.setMaximumSize(QSize(66, 16777215))

        self.horizontalLayout_52.addWidget(self.btn_now_time)

        self.tool_end_time = QToolButton(self.frame_54)
        self.tool_end_time.setObjectName(u"tool_end_time")
        self.tool_end_time.setEnabled(True)
        self.tool_end_time.setMaximumSize(QSize(15, 15))

        self.horizontalLayout_52.addWidget(self.tool_end_time)


        self.verticalLayout_30.addWidget(self.frame_54)

        self.lineEdit_time_end = QLineEdit(self.frame_19)
        self.lineEdit_time_end.setObjectName(u"lineEdit_time_end")
        self.lineEdit_time_end.setFont(font17)

        self.verticalLayout_30.addWidget(self.lineEdit_time_end)


        self.horizontalLayout_22.addLayout(self.verticalLayout_30)


        self.verticalLayout_28.addLayout(self.horizontalLayout_22)


        self.verticalLayout_19.addLayout(self.verticalLayout_28)

        self.line_19 = QFrame(self.frame_19)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_19)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.checkBox_width_report = QCheckBox(self.frame_19)
        self.checkBox_width_report.setObjectName(u"checkBox_width_report")
        self.checkBox_width_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_64.addWidget(self.checkBox_width_report, 0, Qt.AlignBottom)

        self.label_71 = QLabel(self.frame_19)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font12)

        self.horizontalLayout_64.addWidget(self.label_71, 0, Qt.AlignBottom)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.label_72 = QLabel(self.frame_19)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font18)

        self.verticalLayout_54.addWidget(self.label_72)

        self.start_width_text = QLineEdit(self.frame_19)
        self.start_width_text.setObjectName(u"start_width_text")
        self.start_width_text.setFont(font17)

        self.verticalLayout_54.addWidget(self.start_width_text)


        self.horizontalLayout_64.addLayout(self.verticalLayout_54)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_73 = QLabel(self.frame_19)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font18)

        self.verticalLayout_55.addWidget(self.label_73)

        self.end_width_text = QLineEdit(self.frame_19)
        self.end_width_text.setObjectName(u"end_width_text")
        self.end_width_text.setFont(font17)

        self.verticalLayout_55.addWidget(self.end_width_text)


        self.horizontalLayout_64.addLayout(self.verticalLayout_55)


        self.verticalLayout_53.addLayout(self.horizontalLayout_64)


        self.verticalLayout_19.addLayout(self.verticalLayout_53)

        self.line_20 = QFrame(self.frame_19)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_20)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.checkBox_weight_report = QCheckBox(self.frame_19)
        self.checkBox_weight_report.setObjectName(u"checkBox_weight_report")
        self.checkBox_weight_report.setMaximumSize(QSize(17, 16777215))

        self.horizontalLayout_65.addWidget(self.checkBox_weight_report, 0, Qt.AlignBottom)

        self.label_74 = QLabel(self.frame_19)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font12)

        self.horizontalLayout_65.addWidget(self.label_74, 0, Qt.AlignBottom)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_75 = QLabel(self.frame_19)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font18)

        self.verticalLayout_57.addWidget(self.label_75)

        self.start_weight_text = QLineEdit(self.frame_19)
        self.start_weight_text.setObjectName(u"start_weight_text")
        self.start_weight_text.setFont(font17)

        self.verticalLayout_57.addWidget(self.start_weight_text)


        self.horizontalLayout_65.addLayout(self.verticalLayout_57)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_76 = QLabel(self.frame_19)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font18)

        self.verticalLayout_58.addWidget(self.label_76)

        self.end_weight_text = QLineEdit(self.frame_19)
        self.end_weight_text.setObjectName(u"end_weight_text")
        self.end_weight_text.setFont(font17)

        self.verticalLayout_58.addWidget(self.end_weight_text)


        self.horizontalLayout_65.addLayout(self.verticalLayout_58)


        self.verticalLayout_56.addLayout(self.horizontalLayout_65)


        self.verticalLayout_19.addLayout(self.verticalLayout_56)

        self.line_21 = QFrame(self.frame_19)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_21)

        self.verticalSpacer_17 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_19.addItem(self.verticalSpacer_17)

        self.full_search = QPushButton(self.frame_19)
        self.full_search.setObjectName(u"full_search")
        self.full_search.setFont(font12)

        self.verticalLayout_19.addWidget(self.full_search)

        self.search_message = QLabel(self.frame_19)
        self.search_message.setObjectName(u"search_message")

        self.verticalLayout_19.addWidget(self.search_message, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_9)

        self.backup_btn = QPushButton(self.frame_19)
        self.backup_btn.setObjectName(u"backup_btn")
        self.backup_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_19.addWidget(self.backup_btn, 0, Qt.AlignLeft)

        self.progressBar = QProgressBar(self.frame_19)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_19.addWidget(self.progressBar)


        self.horizontalLayout_17.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_21)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.table_report = QTableWidget(self.frame_21)
        if (self.table_report.columnCount() < 10):
            self.table_report.setColumnCount(10)
        if (self.table_report.rowCount() < 10):
            self.table_report.setRowCount(10)
        self.table_report.setObjectName(u"table_report")
        font19 = QFont()
        font19.setFamilies([u"Times New Roman"])
        font19.setPointSize(14)
        self.table_report.setFont(font19)
        self.table_report.setFrameShape(QFrame.Box)
        self.table_report.setFrameShadow(QFrame.Plain)
        self.table_report.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_report.setDragEnabled(True)
        self.table_report.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_report.setTextElideMode(Qt.ElideMiddle)
        self.table_report.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_report.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_report.setRowCount(10)
        self.table_report.setColumnCount(10)

        self.verticalLayout_11.addWidget(self.table_report)

        self.frame_10 = QFrame(self.frame_21)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 32))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.clear_checkboxes_btn = QPushButton(self.frame_10)
        self.clear_checkboxes_btn.setObjectName(u"clear_checkboxes_btn")
        self.clear_checkboxes_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_27.addWidget(self.clear_checkboxes_btn)

        self.edit_btn = QPushButton(self.frame_10)
        self.edit_btn.setObjectName(u"edit_btn")
        self.edit_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_27.addWidget(self.edit_btn)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_12)

        self.export_btn = QPushButton(self.frame_10)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_27.addWidget(self.export_btn)


        self.verticalLayout_11.addWidget(self.frame_10)


        self.horizontalLayout_17.addWidget(self.frame_21)


        self.horizontalLayout_12.addWidget(self.frame_17)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.page_report)
        self.page_panorama = QWidget()
        self.page_panorama.setObjectName(u"page_panorama")
        self.horizontalLayout_39 = QHBoxLayout(self.page_panorama)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(3, 2, 3, 3)
        self.frame_38 = QFrame(self.page_panorama)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.Box)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_38)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 1)
        self.frame_33 = QFrame(self.frame_38)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 338))
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(4, 2, 2, 0)
        self.frame_camera_pan_1 = QFrame(self.frame_33)
        self.frame_camera_pan_1.setObjectName(u"frame_camera_pan_1")
        self.frame_camera_pan_1.setMinimumSize(QSize(0, 147))
        self.frame_camera_pan_1.setMaximumSize(QSize(16777215, 16777215))
        self.frame_camera_pan_1.setStyleSheet(u"background-color: rgb(197 , 195,196);\n"
"")
        self.frame_camera_pan_1.setFrameShape(QFrame.NoFrame)
        self.frame_camera_pan_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_camera_pan_1)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_camera_pan_1)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(60, 60))
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_22)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 10, 0, 0)
        self.dataset_cam_1_name_8 = QLabel(self.frame_22)
        self.dataset_cam_1_name_8.setObjectName(u"dataset_cam_1_name_8")
        self.dataset_cam_1_name_8.setMaximumSize(QSize(500, 20))
        self.dataset_cam_1_name_8.setFont(font9)
        self.dataset_cam_1_name_8.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.verticalLayout_36.addWidget(self.dataset_cam_1_name_8)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_15)


        self.verticalLayout_37.addWidget(self.frame_22)


        self.horizontalLayout_31.addWidget(self.frame_camera_pan_1)

        self.scrollArea = QScrollArea(self.frame_33)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 938, 595))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 0)
        self.pan_image_label_2 = QLabel(self.scrollAreaWidgetContents)
        self.pan_image_label_2.setObjectName(u"pan_image_label_2")
        self.pan_image_label_2.setMaximumSize(QSize(16777215, 16777215))
        self.pan_image_label_2.setFrameShape(QFrame.Box)
        self.pan_image_label_2.setLineWidth(2)
        self.pan_image_label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.pan_image_label_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_31.addWidget(self.scrollArea)


        self.verticalLayout_14.addWidget(self.frame_33)

        self.line_4 = QFrame(self.frame_38)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(1000, 0))
        self.line_4.setMaximumSize(QSize(1000, 16777215))
        self.line_4.setSizeIncrement(QSize(5, 0))
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_14.addWidget(self.line_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_34 = QFrame(self.frame_38)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 300))
        self.frame_34.setMaximumSize(QSize(16777215, 350))
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(9, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_34)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(60, 0))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 6, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.dataset_cam_1_name_6 = QLabel(self.frame_18)
        self.dataset_cam_1_name_6.setObjectName(u"dataset_cam_1_name_6")
        self.dataset_cam_1_name_6.setMaximumSize(QSize(500, 20))
        self.dataset_cam_1_name_6.setFont(font9)
        self.dataset_cam_1_name_6.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.verticalLayout_24.addWidget(self.dataset_cam_1_name_6)


        self.verticalLayout_20.addWidget(self.frame_18, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_20)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.dataset_cam_1_name_9 = QLabel(self.frame_20)
        self.dataset_cam_1_name_9.setObjectName(u"dataset_cam_1_name_9")
        self.dataset_cam_1_name_9.setMaximumSize(QSize(500, 20))
        self.dataset_cam_1_name_9.setFont(font9)
        self.dataset_cam_1_name_9.setStyleSheet(u"border: rgb(197 , 195,196);")

        self.verticalLayout_35.addWidget(self.dataset_cam_1_name_9)


        self.verticalLayout_20.addWidget(self.frame_20, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_45.addWidget(self.frame_16)

        self.scrollArea_3 = QScrollArea(self.frame_34)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 937, 348))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(2, 3, 2, 3)
        self.pan_image_label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.pan_image_label_3.setObjectName(u"pan_image_label_3")
        self.pan_image_label_3.setMaximumSize(QSize(16777215, 170))
        self.pan_image_label_3.setFrameShape(QFrame.Box)
        self.pan_image_label_3.setLineWidth(2)
        self.pan_image_label_3.setScaledContents(True)
        self.pan_image_label_3.setMargin(2)

        self.verticalLayout_40.addWidget(self.pan_image_label_3)

        self.pan_image_label_4 = QLabel(self.scrollAreaWidgetContents_3)
        self.pan_image_label_4.setObjectName(u"pan_image_label_4")
        self.pan_image_label_4.setMaximumSize(QSize(16777215, 170))
        self.pan_image_label_4.setFrameShape(QFrame.Box)
        self.pan_image_label_4.setLineWidth(2)
        self.pan_image_label_4.setScaledContents(True)
        self.pan_image_label_4.setMargin(2)

        self.verticalLayout_40.addWidget(self.pan_image_label_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_45.addWidget(self.scrollArea_3)


        self.verticalLayout_14.addWidget(self.frame_34)


        self.horizontalLayout_39.addWidget(self.frame_38)

        self.stackedWidget.addWidget(self.page_panorama)

        self.verticalLayout_18.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.Container)

        self.frame_36 = QFrame(self.Body)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(20, 0))
        self.frame_36.setMaximumSize(QSize(20, 16777215))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_36)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.right_box_btn = QPushButton(self.frame_36)
        self.right_box_btn.setObjectName(u"right_box_btn")
        self.right_box_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.right_box_btn.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);;\n"
"	color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"\n"
"")
        icon25 = QIcon()
        icon25.addFile(u"images/chevron.png", QSize(), QIcon.Normal, QIcon.Off)
        self.right_box_btn.setIcon(icon25)

        self.verticalLayout_43.addWidget(self.right_box_btn)

        self.verticalSpacer_5 = QSpacerItem(20, 1999999999, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_5)

        self.right_box_btn_3 = QPushButton(self.frame_36)
        self.right_box_btn_3.setObjectName(u"right_box_btn_3")
        self.right_box_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.right_box_btn_3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,100,100);;\n"
"	color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"")
        self.right_box_btn_3.setIcon(icon25)

        self.verticalLayout_43.addWidget(self.right_box_btn_3)


        self.horizontalLayout.addWidget(self.frame_36, 0, Qt.AlignTop)

        self.right_frame = QFrame(self.Body)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(300, 0))
        self.right_frame.setMaximumSize(QSize(0, 16777215))
        self.right_frame.setStyleSheet(u"")
        self.right_frame.setFrameShape(QFrame.WinPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.right_frame.setLineWidth(3)
        self.verticalLayout_38 = QVBoxLayout(self.right_frame)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(6, 0, 4, 0)
        self.verticalSpacer_14 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_14)

        self.frame_13 = QFrame(self.right_frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 65))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_30.setSpacing(2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_13)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_31)
        self.verticalLayout_44.setSpacing(2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 1, 0, 0)
        self.frame_35 = QFrame(self.frame_31)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 52))
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_35)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line)

        self.frame_44 = QFrame(self.frame_35)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_44)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_44)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_49.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.cam2_sign = QPushButton(self.frame_44)
        self.cam2_sign.setObjectName(u"cam2_sign")
        self.cam2_sign.setMinimumSize(QSize(0, 24))
        self.cam2_sign.setStyleSheet(u"background-color:#8BDB81;\n"
"border-radius:10px;")
        icon26 = QIcon()
        icon26.addFile(u"images/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cam2_sign.setIcon(icon26)

        self.verticalLayout_49.addWidget(self.cam2_sign)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.temp_cam2 = QLabel(self.frame_45)
        self.temp_cam2.setObjectName(u"temp_cam2")
        self.temp_cam2.setFont(font14)

        self.horizontalLayout_48.addWidget(self.temp_cam2, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.frame_45)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(20, 15))
        self.label_10.setFrameShape(QFrame.NoFrame)
        self.label_10.setPixmap(QPixmap(u"images/icons8-celsius-32.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_48.addWidget(self.label_10, 0, Qt.AlignVCenter)


        self.verticalLayout_49.addWidget(self.frame_45)


        self.horizontalLayout_13.addWidget(self.frame_44)

        self.line_10 = QFrame(self.frame_35)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_10)

        self.frame_43 = QFrame(self.frame_35)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_43)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_43)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_46.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.cam1_sign = QPushButton(self.frame_43)
        self.cam1_sign.setObjectName(u"cam1_sign")
        self.cam1_sign.setMinimumSize(QSize(0, 24))
        self.cam1_sign.setStyleSheet(u"background-color:#8BDB81;\n"
"border-radius:10px;")
        self.cam1_sign.setIcon(icon26)

        self.verticalLayout_46.addWidget(self.cam1_sign)

        self.frame_40 = QFrame(self.frame_43)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.temp_cam1 = QLabel(self.frame_40)
        self.temp_cam1.setObjectName(u"temp_cam1")
        self.temp_cam1.setFont(font14)

        self.horizontalLayout_33.addWidget(self.temp_cam1, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_40)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(20, 15))
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_4.setPixmap(QPixmap(u"images/icons8-celsius-32.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.label_4, 0, Qt.AlignVCenter)


        self.verticalLayout_46.addWidget(self.frame_40)


        self.horizontalLayout_13.addWidget(self.frame_43)

        self.line_6 = QFrame(self.frame_35)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_6)

        self.frame_46 = QFrame(self.frame_35)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_46)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_46)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_50.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.cam3_sign = QPushButton(self.frame_46)
        self.cam3_sign.setObjectName(u"cam3_sign")
        self.cam3_sign.setMinimumSize(QSize(0, 24))
        self.cam3_sign.setStyleSheet(u"background-color:#8BDB81;\n"
"border-radius:10px;")
        self.cam3_sign.setIcon(icon26)

        self.verticalLayout_50.addWidget(self.cam3_sign)

        self.frame_52 = QFrame(self.frame_46)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.NoFrame)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.temp_cam3 = QLabel(self.frame_52)
        self.temp_cam3.setObjectName(u"temp_cam3")
        self.temp_cam3.setFont(font14)

        self.horizontalLayout_53.addWidget(self.temp_cam3, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_52)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(20, 15))
        self.label_22.setFrameShape(QFrame.NoFrame)
        self.label_22.setPixmap(QPixmap(u"images/icons8-celsius-32.png"))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_53.addWidget(self.label_22, 0, Qt.AlignVCenter)


        self.verticalLayout_50.addWidget(self.frame_52)


        self.horizontalLayout_13.addWidget(self.frame_46)

        self.line_7 = QFrame(self.frame_35)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_7)

        self.frame_48 = QFrame(self.frame_35)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_48)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_48)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_52.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.cam4_sign = QPushButton(self.frame_48)
        self.cam4_sign.setObjectName(u"cam4_sign")
        self.cam4_sign.setMinimumSize(QSize(0, 24))
        self.cam4_sign.setStyleSheet(u"background-color:#8BDB81;\n"
"border-radius:10px;")
        self.cam4_sign.setIcon(icon26)

        self.verticalLayout_52.addWidget(self.cam4_sign)

        self.frame_53 = QFrame(self.frame_48)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.temp_cam4 = QLabel(self.frame_53)
        self.temp_cam4.setObjectName(u"temp_cam4")
        self.temp_cam4.setFont(font14)

        self.horizontalLayout_59.addWidget(self.temp_cam4, 0, Qt.AlignHCenter)

        self.label_25 = QLabel(self.frame_53)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(20, 15))
        self.label_25.setFrameShape(QFrame.NoFrame)
        self.label_25.setPixmap(QPixmap(u"images/icons8-celsius-32.png"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_59.addWidget(self.label_25, 0, Qt.AlignVCenter)


        self.verticalLayout_52.addWidget(self.frame_53)


        self.horizontalLayout_13.addWidget(self.frame_48)


        self.verticalLayout_44.addWidget(self.frame_35)


        self.horizontalLayout_30.addWidget(self.frame_31)


        self.verticalLayout_38.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.line_2 = QFrame(self.right_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_38.addWidget(self.line_2)

        self.frame_4 = QFrame(self.right_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 40))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.cam1_sign_detect = QLabel(self.frame_4)
        self.cam1_sign_detect.setObjectName(u"cam1_sign_detect")
        self.cam1_sign_detect.setMinimumSize(QSize(35, 35))
        self.cam1_sign_detect.setMaximumSize(QSize(35, 35))
        self.cam1_sign_detect.setPixmap(QPixmap(u"images/circle.png"))
        self.cam1_sign_detect.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.cam1_sign_detect)

        self.line_15 = QFrame(self.frame_4)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_15)

        self.cam2_sign_detect = QLabel(self.frame_4)
        self.cam2_sign_detect.setObjectName(u"cam2_sign_detect")
        self.cam2_sign_detect.setMinimumSize(QSize(35, 35))
        self.cam2_sign_detect.setMaximumSize(QSize(35, 35))
        self.cam2_sign_detect.setPixmap(QPixmap(u"images/circle.png"))
        self.cam2_sign_detect.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.cam2_sign_detect)

        self.line_16 = QFrame(self.frame_4)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_16)

        self.cam3_sign_detect = QLabel(self.frame_4)
        self.cam3_sign_detect.setObjectName(u"cam3_sign_detect")
        self.cam3_sign_detect.setMinimumSize(QSize(35, 35))
        self.cam3_sign_detect.setMaximumSize(QSize(35, 35))
        self.cam3_sign_detect.setPixmap(QPixmap(u"images/circle.png"))
        self.cam3_sign_detect.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.cam3_sign_detect)

        self.line_17 = QFrame(self.frame_4)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_17)

        self.cam4_sign_detect = QLabel(self.frame_4)
        self.cam4_sign_detect.setObjectName(u"cam4_sign_detect")
        self.cam4_sign_detect.setMinimumSize(QSize(35, 35))
        self.cam4_sign_detect.setMaximumSize(QSize(35, 35))
        self.cam4_sign_detect.setPixmap(QPixmap(u"images/circle.png"))
        self.cam4_sign_detect.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.cam4_sign_detect)


        self.verticalLayout_38.addWidget(self.frame_4)

        self.groupBox = QGroupBox(self.right_frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setTitle(u"About Slab ")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_42 = QVBoxLayout(self.groupBox)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.frame_37 = QFrame(self.groupBox)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_37)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 11, -1, -1)
        self.frame_9 = QFrame(self.frame_37)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(50, 213))
        self.frame_9.setMaximumSize(QSize(382, 16777215))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(7, 0, 0, 0)
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(150, 16777215))
        self.label_26.setFont(font17)

        self.horizontalLayout_46.addWidget(self.label_26, 0, Qt.AlignLeft)

        self.slab_rate = QLabel(self.frame_9)
        self.slab_rate.setObjectName(u"slab_rate")
        self.slab_rate.setEnabled(False)
        self.slab_rate.setFont(font9)

        self.horizontalLayout_46.addWidget(self.slab_rate)

        self.label_60 = QLabel(self.frame_9)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(32, 0))
        self.label_60.setMaximumSize(QSize(28, 16777215))
        self.label_60.setFont(font9)

        self.horizontalLayout_46.addWidget(self.label_60)

        self.horizontalSpacer_7 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_7)

        self.slab_rate_manual = QPushButton(self.frame_9)
        self.slab_rate_manual.setObjectName(u"slab_rate_manual")
        self.slab_rate_manual.setMaximumSize(QSize(20, 16777215))
        icon27 = QIcon()
        icon27.addFile(u"images/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.slab_rate_manual.setIcon(icon27)

        self.horizontalLayout_46.addWidget(self.slab_rate_manual)


        self.verticalLayout_39.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_35 = QLabel(self.frame_9)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(150, 16777215))
        self.label_35.setFont(font17)

        self.horizontalLayout_61.addWidget(self.label_35, 0, Qt.AlignLeft)

        self.melting_id = QLineEdit(self.frame_9)
        self.melting_id.setObjectName(u"melting_id")
        self.melting_id.setEnabled(True)
        self.melting_id.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_61.addWidget(self.melting_id, 0, Qt.AlignRight)

        self.slab_id_manual_2 = QPushButton(self.frame_9)
        self.slab_id_manual_2.setObjectName(u"slab_id_manual_2")
        self.slab_id_manual_2.setMaximumSize(QSize(20, 16777215))
        self.slab_id_manual_2.setIcon(icon27)

        self.horizontalLayout_61.addWidget(self.slab_id_manual_2)


        self.verticalLayout_39.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(150, 16777215))
        self.label_28.setFont(font17)

        self.horizontalLayout_47.addWidget(self.label_28, 0, Qt.AlignLeft)

        self.slab_id = QLineEdit(self.frame_9)
        self.slab_id.setObjectName(u"slab_id")
        self.slab_id.setEnabled(True)
        self.slab_id.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_47.addWidget(self.slab_id, 0, Qt.AlignRight)

        self.slab_id_manual = QPushButton(self.frame_9)
        self.slab_id_manual.setObjectName(u"slab_id_manual")
        self.slab_id_manual.setMaximumSize(QSize(20, 16777215))
        self.slab_id_manual.setIcon(icon27)

        self.horizontalLayout_47.addWidget(self.slab_id_manual)


        self.verticalLayout_39.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(150, 16777215))
        self.label_31.setFont(font17)

        self.horizontalLayout_50.addWidget(self.label_31, 0, Qt.AlignLeft)

        self.slab_line = QSpinBox(self.frame_9)
        self.slab_line.setObjectName(u"slab_line")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.slab_line.sizePolicy().hasHeightForWidth())
        self.slab_line.setSizePolicy(sizePolicy5)
        self.slab_line.setMinimumSize(QSize(110, 0))

        self.horizontalLayout_50.addWidget(self.slab_line)

        self.slab_line_manual = QPushButton(self.frame_9)
        self.slab_line_manual.setObjectName(u"slab_line_manual")
        self.slab_line_manual.setMaximumSize(QSize(20, 16777215))
        self.slab_line_manual.setIcon(icon27)

        self.horizontalLayout_50.addWidget(self.slab_line_manual)


        self.verticalLayout_39.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(150, 16777215))
        self.label_50.setFont(font17)

        self.horizontalLayout_54.addWidget(self.label_50, 0, Qt.AlignLeft)

        self.slab_width = QLineEdit(self.frame_9)
        self.slab_width.setObjectName(u"slab_width")
        self.slab_width.setEnabled(False)
        self.slab_width.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_54.addWidget(self.slab_width, 0, Qt.AlignRight)

        self.label_17 = QLabel(self.frame_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_54.addWidget(self.label_17)

        self.slab_width_manual = QPushButton(self.frame_9)
        self.slab_width_manual.setObjectName(u"slab_width_manual")
        self.slab_width_manual.setMaximumSize(QSize(20, 16777215))
        self.slab_width_manual.setIcon(icon27)

        self.horizontalLayout_54.addWidget(self.slab_width_manual)


        self.verticalLayout_39.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_51 = QLabel(self.frame_9)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(150, 16777215))
        self.label_51.setFont(font17)

        self.horizontalLayout_58.addWidget(self.label_51, 0, Qt.AlignLeft)

        self.slab_weight = QLineEdit(self.frame_9)
        self.slab_weight.setObjectName(u"slab_weight")
        self.slab_weight.setEnabled(False)
        self.slab_weight.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_58.addWidget(self.slab_weight, 0, Qt.AlignRight)

        self.label_18 = QLabel(self.frame_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_58.addWidget(self.label_18)

        self.slab_width_manual_2 = QPushButton(self.frame_9)
        self.slab_width_manual_2.setObjectName(u"slab_width_manual_2")
        self.slab_width_manual_2.setMaximumSize(QSize(20, 16777215))
        self.slab_width_manual_2.setIcon(icon27)

        self.horizontalLayout_58.addWidget(self.slab_width_manual_2)


        self.verticalLayout_39.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_57 = QLabel(self.frame_9)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(150, 16777215))
        self.label_57.setFont(font17)

        self.horizontalLayout_56.addWidget(self.label_57, 0, Qt.AlignLeft)

        self.slab_lenght = QLineEdit(self.frame_9)
        self.slab_lenght.setObjectName(u"slab_lenght")
        self.slab_lenght.setEnabled(False)
        self.slab_lenght.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_56.addWidget(self.slab_lenght, 0, Qt.AlignRight)

        self.label_19 = QLabel(self.frame_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_56.addWidget(self.label_19)

        self.slab_lenght_manual = QPushButton(self.frame_9)
        self.slab_lenght_manual.setObjectName(u"slab_lenght_manual")
        self.slab_lenght_manual.setMaximumSize(QSize(20, 16777215))
        self.slab_lenght_manual.setIcon(icon27)

        self.horizontalLayout_56.addWidget(self.slab_lenght_manual)


        self.verticalLayout_39.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_52 = QLabel(self.frame_9)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(150, 16777215))
        self.label_52.setFont(font17)

        self.horizontalLayout_55.addWidget(self.label_52, 0, Qt.AlignLeft)

        self.slab_thickness = QLineEdit(self.frame_9)
        self.slab_thickness.setObjectName(u"slab_thickness")
        self.slab_thickness.setEnabled(False)
        self.slab_thickness.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_55.addWidget(self.slab_thickness, 0, Qt.AlignRight)

        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(22, 16777215))

        self.horizontalLayout_55.addWidget(self.label_20)

        self.slab_thickness_manual = QPushButton(self.frame_9)
        self.slab_thickness_manual.setObjectName(u"slab_thickness_manual")
        self.slab_thickness_manual.setMaximumSize(QSize(20, 16777215))
        self.slab_thickness_manual.setIcon(icon27)

        self.horizontalLayout_55.addWidget(self.slab_thickness_manual)


        self.verticalLayout_39.addLayout(self.horizontalLayout_55)


        self.verticalLayout_17.addLayout(self.verticalLayout_39)


        self.verticalLayout_41.addWidget(self.frame_9)

        self.line_5 = QFrame(self.frame_37)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_41.addWidget(self.line_5)

        self.label_2 = QLabel(self.frame_37)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font9)
        self.label_2.setStyleSheet(u"text-align: center;")

        self.verticalLayout_41.addWidget(self.label_2)

        self.listWidget = QListWidget(self.frame_37)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 30))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_41.addWidget(self.listWidget)


        self.verticalLayout_42.addWidget(self.frame_37)


        self.verticalLayout_38.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.right_frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 154))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.defect_table = QTableWidget(self.groupBox_2)
        if (self.defect_table.columnCount() < 1):
            self.defect_table.setColumnCount(1)
        self.defect_table.setObjectName(u"defect_table")
        self.defect_table.setMinimumSize(QSize(50, 0))
        self.defect_table.setFrameShape(QFrame.WinPanel)
        self.defect_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.defect_table.setDragDropMode(QAbstractItemView.DragOnly)
        self.defect_table.setRowCount(0)
        self.defect_table.setColumnCount(1)

        self.verticalLayout_5.addWidget(self.defect_table)


        self.verticalLayout_38.addWidget(self.groupBox_2, 0, Qt.AlignBottom)

        self.frame_56 = QFrame(self.right_frame)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(10, 40))
        self.frame_56.setFrameShape(QFrame.Box)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.checkBox_top = QCheckBox(self.frame_56)
        self.checkBox_top.setObjectName(u"checkBox_top")

        self.horizontalLayout_60.addWidget(self.checkBox_top)

        self.checkBox_head = QCheckBox(self.frame_56)
        self.checkBox_head.setObjectName(u"checkBox_head")

        self.horizontalLayout_60.addWidget(self.checkBox_head)

        self.checkBox_mesh = QCheckBox(self.frame_56)
        self.checkBox_mesh.setObjectName(u"checkBox_mesh")
        self.checkBox_mesh.setChecked(False)

        self.horizontalLayout_60.addWidget(self.checkBox_mesh)


        self.verticalLayout_38.addWidget(self.frame_56)

        self.frame_39 = QFrame(self.right_frame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(10, 40))
        self.frame_39.setFrameShape(QFrame.Box)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_59 = QLabel(self.frame_39)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(100, 16777215))
        self.label_59.setFont(font17)

        self.horizontalLayout_57.addWidget(self.label_59)

        self.fps_val = QLabel(self.frame_39)
        self.fps_val.setObjectName(u"fps_val")
        self.fps_val.setFont(font9)

        self.horizontalLayout_57.addWidget(self.fps_val)


        self.verticalLayout_38.addWidget(self.frame_39)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_3)

        self.frame_8 = QFrame(self.right_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 51))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_8)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_9 = QFrame(self.frame_8)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_9, 0, 3, 1, 1)

        self.frame_57 = QFrame(self.frame_8)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_57)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.connect_btn = QPushButton(self.frame_57)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setMinimumSize(QSize(0, 30))
        self.connect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.connect_btn.setStyleSheet(u"border:none;")
        icon28 = QIcon()
        icon28.addFile(u"images/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.connect_btn.setIcon(icon28)
        self.connect_btn.setIconSize(QSize(27, 32))

        self.verticalLayout_21.addWidget(self.connect_btn)

        self.label_13 = QLabel(self.frame_57)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_21.addWidget(self.label_13, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.frame_57, 0, 0, 1, 1)

        self.frame_60 = QFrame(self.frame_8)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_60)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.calibrate_btn = QPushButton(self.frame_60)
        self.calibrate_btn.setObjectName(u"calibrate_btn")
        self.calibrate_btn.setEnabled(False)
        self.calibrate_btn.setMinimumSize(QSize(0, 30))
        self.calibrate_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.calibrate_btn.setStyleSheet(u"border:none;")
        icon29 = QIcon()
        icon29.addFile(u"images/target.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calibrate_btn.setIcon(icon29)
        self.calibrate_btn.setIconSize(QSize(26, 24))

        self.verticalLayout_48.addWidget(self.calibrate_btn)

        self.label_16 = QLabel(self.frame_60)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_48.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.frame_60, 0, 6, 1, 1)

        self.frame_58 = QFrame(self.frame_8)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_58)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.disconnect_btn = QPushButton(self.frame_58)
        self.disconnect_btn.setObjectName(u"disconnect_btn")
        self.disconnect_btn.setMinimumSize(QSize(6, 30))
        self.disconnect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.disconnect_btn.setStyleSheet(u"border:none;")
        icon30 = QIcon()
        icon30.addFile(u"images/disconnected-chains.png", QSize(), QIcon.Normal, QIcon.Off)
        self.disconnect_btn.setIcon(icon30)
        self.disconnect_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_59.addWidget(self.disconnect_btn)

        self.label_14 = QLabel(self.frame_58)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_59.addWidget(self.label_14, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.frame_58, 0, 2, 1, 1)

        self.line_14 = QFrame(self.frame_8)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_14, 0, 5, 1, 1)

        self.line_8 = QFrame(self.frame_8)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_8, 0, 1, 1, 1)

        self.frame_59 = QFrame(self.frame_8)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_59)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.refresh_btn = QPushButton(self.frame_59)
        self.refresh_btn.setObjectName(u"refresh_btn")
        self.refresh_btn.setMinimumSize(QSize(0, 30))
        self.refresh_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refresh_btn.setStyleSheet(u"border:none;")
        icon31 = QIcon()
        icon31.addFile(u"images/refresh(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_btn.setIcon(icon31)

        self.verticalLayout_51.addWidget(self.refresh_btn)

        self.label_15 = QLabel(self.frame_59)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_51.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.gridLayout_4.addWidget(self.frame_59, 0, 4, 1, 1)


        self.verticalLayout_38.addWidget(self.frame_8)

        self.line_3 = QFrame(self.right_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_38.addWidget(self.line_3)

        self.frame_7 = QFrame(self.right_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 83))
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_16 = QVBoxLayout(self.frame_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(8, 2, 8, 2)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_4)

        self.automatic_btn = QRadioButton(self.frame_7)
        self.automatic_btn.setObjectName(u"automatic_btn")
        self.automatic_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.automatic_btn.setStyleSheet(u"QRadioButton {\n"
"    background-color:       Transparent;\n"
"    color:                  Black;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(46,202,254);\n"
"    border:                 2px solid green;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")

        self.horizontalLayout_15.addWidget(self.automatic_btn)

        self.horizontalSpacer_6 = QSpacerItem(15, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_6)

        self.manual_btn = QRadioButton(self.frame_7)
        self.manual_btn.setObjectName(u"manual_btn")
        self.manual_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.manual_btn.setStyleSheet(u"QRadioButton {\n"
"    background-color:       Transparent;\n"
"    color:                  Black;\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       rgb(0,252,130);\n"
"    border:                 2px solid green;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:      White;\n"
"    border:                 2px solid white;\n"
"}")
        self.manual_btn.setChecked(True)

        self.horizontalLayout_15.addWidget(self.manual_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.start_capture = QPushButton(self.frame_7)
        self.start_capture.setObjectName(u"start_capture")
        self.start_capture.setMinimumSize(QSize(0, 28))
        self.start_capture.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.start_capture)

        self.stop_capture = QPushButton(self.frame_7)
        self.stop_capture.setObjectName(u"stop_capture")
        self.stop_capture.setEnabled(True)
        self.stop_capture.setMinimumSize(QSize(0, 28))
        self.stop_capture.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.stop_capture)


        self.verticalLayout_16.addLayout(self.horizontalLayout_23)

        self.capture_status_btn = QLabel(self.frame_7)
        self.capture_status_btn.setObjectName(u"capture_status_btn")

        self.verticalLayout_16.addWidget(self.capture_status_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_38.addWidget(self.frame_7)

        self.verticalSpacer = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer)

        self.report_label = QLabel(self.right_frame)
        self.report_label.setObjectName(u"report_label")
        self.report_label.setStyleSheet(u"padding-left: 5px;")

        self.verticalLayout_38.addWidget(self.report_label)

        self.verticalSpacer_8 = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_8)

        self.label_time = QLabel(self.right_frame)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setMaximumSize(QSize(200, 16777215))
        self.label_time.setStyleSheet(u"border: rgb(197 , 195,196);\n"
"color:rgb(150,150,150);")

        self.verticalLayout_38.addWidget(self.label_time, 0, Qt.AlignHCenter)

        self.label_date = QLabel(self.right_frame)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMaximumSize(QSize(200, 16777215))
        self.label_date.setStyleSheet(u"border: rgb(197 , 195,196);\n"
"color:rgb(150,150,150);")

        self.verticalLayout_38.addWidget(self.label_date, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.right_frame)


        self.verticalLayout_31.addWidget(self.Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText("")
        self.label_23.setText("")
        self.label_44.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0633\u06cc\u0633\u062a\u0645 \u0628\u0627\u0632\u0631\u0633\u06cc \u0633\u0637\u062d \u062a\u062e\u062a\u0627\u0644 CCM 5", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DORSA Slab Monitoring System ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0646\u062a\u0631\u0644 \u06a9\u06cc\u0641\u06cc \u0646\u0627\u062d\u06cc\u0647 \u0641\u0648\u0644\u0627\u062f \u0633\u0627\u0632\u06cc", None))
        self.label_49.setText("")
        self.label_61.setText("")
        self.login_welcome.setText("")
        self.label_5.setText("")
#if QT_CONFIG(tooltip)
        self.setting_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.user_btn.setToolTip(QCoreApplication.translate("MainWindow", u"User", None))
#endif // QT_CONFIG(tooltip)
        self.user_btn.setText(QCoreApplication.translate("MainWindow", u"Guest", None))
#if QT_CONFIG(tooltip)
        self.toggleButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Notification", None))
#endif // QT_CONFIG(tooltip)
        self.toggleButton_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.miniButton.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.miniButton.setText("")
#if QT_CONFIG(tooltip)
        self.maxiButton.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxiButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeButton.setText("")
        self.live_btn.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.page_live_dataset_btn.setText(QCoreApplication.translate("MainWindow", u"  Page 2", None))
        self.panorama_btn.setText(QCoreApplication.translate("MainWindow", u"  Panorama ", None))
        self.page_fullscreen.setText(QCoreApplication.translate("MainWindow", u"  FullScreen", None))
        self.page_report_btn.setText(QCoreApplication.translate("MainWindow", u"  Report", None))
        self.page_aboutus_btn.setText(QCoreApplication.translate("MainWindow", u"  About us", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"  Signout", None))
        self.dataset_cam_1_name.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.D_notif_cam_5.setText("")
        self.D_cam_1_pausesign.setText("")
        self.D_cam_1_rotate.setText("")
        self.D_cam_1_capture.setText("")
        self.D_cam_1_play.setText("")
        self.D_cam_1_pause.setText("")
        self.D_cam_1_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.D_fs1_btn.setText("")
        self.datalive_image_label_1.setText("")
        self.dataset_cam_2_name.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.D_notif_cam_2.setText("")
        self.D_cam_2_pausesign.setText("")
        self.D_cam_2_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.D_cam_2_play.setText("")
        self.D_cam_2_pause.setText("")
        self.D_cam_2_capture.setText("")
        self.D_fs2_btn.setText("")
        self.datalive_image_label_2.setText("")
        self.dataset_cam_3_name.setText(QCoreApplication.translate("MainWindow", u"Camera 3", None))
        self.D_notif_cam_3.setText("")
        self.D_cam_3_pausesign.setText("")
        self.D_cam_3_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.D_cam_3_play.setText("")
        self.D_cam_3_pause.setText("")
        self.D_cam_3_capture.setText("")
        self.D_fs3_btn.setText("")
        self.datalive_image_label_3.setText("")
        self.dataset_cam_4_name.setText(QCoreApplication.translate("MainWindow", u"Camera 4", None))
        self.D_notif_cam_4.setText("")
        self.D_cam_4_pausesign.setText("")
        self.D_cam_4_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.D_cam_4_play.setText("")
        self.D_cam_4_pause.setText("")
        self.D_cam_4_capture.setText("")
        self.D_fs4_btn.setText("")
        self.datalive_image_label_4.setText("")
        self.cam_1_btn.setText("")
        self.cam_2_btn.setText("")
        self.cam_3_btn.setText("")
        self.cam_4_btn.setText("")
        self.fs_cam_name.setText("")
        self.fs_pause_sign.setText("")
        self.fs2_btn_11.setText("")
        self.fs2_btn_12.setText("")
        self.fs_cam__capture.setText("")
        self.fs_cam__rotate.setText("")
        self.fullscreen_label.setText("")
        self.live_cam_2_name.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.L_notif_cam_2.setText("")
        self.cam_2_pause.setText("")
        self.live_cam_2_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.live_cam_2_play.setText("")
        self.live_cam_2_pause.setText("")
        self.checkBox_cam_2.setText("")
        self.live_cam_2_setting.setText("")
        self.live_cam_2_capture.setText("")
        self.fs2_btn.setText("")
        self.toogle_cam_2.setText("")
        self.live_image_label_2.setText("")
        self.live_cam_4_name.setText(QCoreApplication.translate("MainWindow", u"Camera 4", None))
        self.L_notif_cam_4.setText("")
        self.cam_4_pause.setText("")
        self.live_cam_4_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.live_cam_4_play.setText("")
        self.live_cam_4_pause.setText("")
        self.checkBox_cam_4.setText("")
        self.live_cam_4_setting.setText("")
        self.live_cam_4_capture.setText("")
        self.fs4_btn.setText("")
        self.live_cam_3_name.setText(QCoreApplication.translate("MainWindow", u"Camera 3", None))
        self.L_notif_cam_3.setText("")
        self.cam_3_pause.setText("")
        self.live_cam_3_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.live_cam_3_play.setText("")
        self.live_cam_3_pause.setText("")
        self.checkBox_cam_3.setText("")
        self.live_cam_3_setting.setText("")
        self.live_cam_3_capture.setText("")
        self.fs3_btn.setText("")
        self.toogle_cam_3.setText("")
        self.toogle_cam_4.setText("")
        self.live_image_label_4.setText("")
        self.live_image_label_3.setText("")
        self.live_cam_1_name.setText(QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.L_notif_cam_1.setText("")
        self.cam_1_pause.setText("")
        self.live_cam_1_zoom.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.live_cam_1_play.setText("")
        self.live_cam_1_pause.setText("")
        self.checkBox_cam_1.setText("")
        self.live_cam_1_setting.setText("")
        self.live_cam_1_capture.setText("")
        self.fs1_btn.setText("")
        self.toogle_cam_1.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0635\u0648\u06cc\u0631 \u062b\u0627\u0628\u062a \u062c\u0647\u062a \u0628\u0627\u0632\u0631\u0633\u06cc \u0633\u0631\u200c\u0627\u0633\u0644\u0628", None))
        self.live_image_label_5.setText("")
        self.live_image_label_1.setText("")
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Britannic Bold'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#484844;\">\u062a\u0645\u0627\u0633 \u0628\u0627 \u0645\u0627</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-famil"
                        "y:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0634\u0645\u0627\u0631\u0647 \u062a\u0645\u0627\u0633: 33931171(031)</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0627\u06cc\u0645\u06cc\u0644: info@dorsa-co.ir</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0648\u0628\u0633\u0627\u06cc\u062a: dorsa-co.ir </span></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0622\u062f\u0631\u0633"
                        ": \u0627\u0635\u0641\u0647\u0627\u0646 - \u0634\u0647\u0631\u06a9 \u0639\u0644\u0645\u06cc \u062a\u062d\u0642\u06cc\u0642\u0627\u062a\u06cc \u0627\u0635\u0641\u0647\u0627\u0646 - \u0633\u0627\u062e\u062a\u0645\u0627\u0646 \u0641\u0646 \u0627\u0641\u0631\u06cc\u0646\u06cc 1 - \u0648\u0627\u062d\u062f 108</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"justify\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Britannic Bold'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; color:#484844;\"> \u062f\u0631\u0628\u0627\u0631\u0647 \u0645\u0627</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:"
                        "0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'IranSansNum','Arial','Helvetica','sans-serif'; font-size:16pt; color:#000000;\">\u06af\u0631\u0648\u0647 \u062a\u062d\u0642\u06cc\u0642\u0627\u062a\u06cc \u062f\u0631\u0635\u0627 (\u062f\u06cc\u062f\u0647 \u0631\u0627\u06cc\u0627\u0646 \u0635\u0646\u0639\u062a\u06cc \u0627\u0635\u0641\u0647\u0627\u0646) \u060c \u0628\u0627 \u0647\u062f\u0641 \u0646\u0638\u0627\u0631\u062a\u060c \u0639\u06cc\u0628 \u06cc\u0627\u0628\u06cc \u0648 \u0628\u0647\u0628\u0648\u062f \u0641\u0631\u0622\u06cc\u0646\u062f\u0647\u0627\u06cc \u062a\u0648\u0644\u06cc\u062f \u062f\u0631 \u0635\u0646\u0627\u06cc\u0639 \u0645\u062e\u062a\u0644\u0641 \u0628\u0627 \u0628\u0647\u0631\u0647 \u06af\u06cc\u0631\u06cc \u0627\u0632 \u0627\u0628\u0632\u0627\u0631 \u067e\u0631\u062f\u0627\u0632\u0634"
                        " \u062a\u0635\u0648\u06cc\u0631 \u0648 \u0628\u06cc\u0646\u0627\u06cc\u06cc \u0645\u0627\u0634\u06cc\u0646 \u062f\u0631 \u0633\u0627\u0644 \u06f1\u06f3\u06f9\u06f6 \u0622\u063a\u0627\u0632 \u0628\u0647 \u06a9\u0627\u0631 \u06a9\u0631\u062f. \u0647\u0633\u062a\u0647 \u0627\u0648\u0644\u06cc\u0647 \u0627\u06cc\u0646 \u06af\u0631\u0648\u0647 \u062a\u0648\u0633\u0637 \u0686\u0646\u062f \u062a\u0646 \u0627\u0632 \u0627\u0633\u0627\u062a\u06cc\u062f\u060c \u0641\u0627\u0631\u063a \u0627\u0644\u062a\u062d\u0635\u06cc\u0644\u0627\u0646 \u0648 \u062f\u0627\u0646\u0634\u062c\u0648\u06cc\u0627\u0646 \u062f\u0627\u0646\u0634\u06af\u0627\u0647 \u0635\u0646\u0639\u062a\u06cc \u0627\u0635\u0641\u0647\u0627\u0646\u060c \u062f\u0631 \u0631\u0627\u0633\u062a\u0627\u06cc \u0627\u0646\u062c\u0627\u0645 \u067e\u0631\u0648\u0698\u0647\u00ad\u0647\u0627\u06cc \u062a\u062d\u0642\u06cc\u0642 \u0648 \u062a\u0648\u0633\u0639\u0647 \u062f\u0631 \u0635\u0646\u0639\u062a \u0641\u0648\u0644\u0627\u062f \u0627\u0632 \u0633\u0627\u0644 \u06f1"
                        "\u06f3\u06f8\u06f6 \u062a\u0634\u06a9\u06cc\u0644 \u0634\u062f. \u0627\u06cc\u0646 \u0645\u062c\u0645\u0648\u0639\u0647 \u0628\u0639\u062f \u0627\u0632 \u06a9\u0633\u0628 \u062a\u062c\u0627\u0631\u0628 \u0627\u0631\u0632\u0634\u0645\u0646\u062f \u062f\u0631 \u0628\u0647 \u0627\u0646\u062c\u0627\u0645 \u0631\u0633\u0627\u0646\u062f\u0646 \u067e\u0631\u0648\u0698\u0647\u00ad\u0647\u0627\u06cc \u0645\u062e\u062a\u0644\u0641 \u067e\u0631\u062f\u0627\u0632\u0634 \u062a\u0635\u0648\u06cc\u0631 \u062f\u0631 \u0645\u062c\u062a\u0645\u0639 \u0641\u0648\u0644\u0627\u062f \u0645\u0628\u0627\u0631\u06a9\u0647 \u0627\u0635\u0641\u0647\u0627\u0646\u060c \u0628\u0631 \u0622\u0646 \u0634\u062f \u062a\u0627 \u0628\u0627 \u0627\u0633\u062a\u0641\u0627\u062f\u0647 \u0627\u0632 \u0627\u0645\u06a9\u0627\u0646\u0627\u062a \u0645\u0648\u062c\u0648\u062f \u062f\u0631 \u062f\u0627\u0646\u0634\u06af\u0627\u0647 \u0635\u0646\u0639\u062a\u06cc \u0627\u0635\u0641\u0647\u0627\u0646 \u0648 \u0634\u0647\u0631\u06a9 \u0639\u0644\u0645\u06cc \u0648"
                        " \u062a\u062d\u0642\u06cc\u0642\u0627\u062a\u06cc \u0622\u0646\u060c \u0628\u0647 \u0635\u0648\u0631\u062a \u0631\u0633\u0645\u06cc \u0648 \u062d\u0631\u0641\u0647 \u0627\u06cc \u0641\u0639\u0627\u0644\u06cc\u062a \u0647\u0627\u06cc \u062e\u0648\u062f \u0631\u0627 \u0622\u063a\u0627\u0632 \u06a9\u0646\u062f. \u06af\u0631\u0648\u0647 \u062a\u062d\u0642\u06cc\u0642\u06cc \u062f\u0631\u0635\u0627 \u062f\u0631 \u067e\u06cc \u0622\u0646 \u0627\u0633\u062a \u06a9\u0647 \u0628\u0627 \u0627\u062a\u06a9\u0627 \u0648 \u0628\u0627\u0648\u0631 \u0628\u0647 \u062a\u0648\u0627\u0646 \u0648 \u062f\u0627\u0646\u0634 \u062c\u0648\u0627\u0646\u0627\u0646 \u0645\u062a\u062e\u0635\u0635 \u0648 \u0628\u0627 \u0627\u0646\u06af\u06cc\u0632\u0647 \u06a9\u0634\u0648\u0631\u0645\u0627\u0646 \u0628\u062a\u0648\u0627\u0646\u062f\u060c \u06af\u0631\u0647 \u0647\u0627 \u0648 \u06af\u0644\u0648\u06af\u0627\u0647\u00ad\u0647\u0627\u06cc \u062a\u0646\u06af \u0635\u0646\u0639\u062a \u06a9\u0634\u0648\u0631 \u0631\u0627 \u0634\u0646\u0627\u0633"
                        "\u0627\u06cc\u06cc \u0648 \u0628\u0631\u0627\u06cc \u062d\u0644 \u0622\u0646\u00ad\u0647\u0627 \u0627\u0642\u062f\u0627\u0645 \u06a9\u0646\u062f.</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'IranSansNum','Arial','Helvetica','sans-serif'; font-size:16pt; color:#000000;\">\u0634\u0631\u06a9\u062a \u062f\u06cc\u062f\u0647 \u0631\u0627\u06cc\u0627\u0646 \u0635\u0646\u0639\u062a\u06cc \u0627\u0635\u0641\u0647\u0627\u0646 \u0628\u0647 \u0639\u0646\u0648\u0627\u0646 \u0634\u0631\u06a9\u062a\u06cc \u062f\u0627\u0646\u0634 \u0628\u0646\u06cc\u0627\u0646 \u0648 \u067e\u06cc\u0634\u0631\u0648 \u062f\u0631 \u0639\u0631\u0635\u0647 \u062e\u062f\u0645\u0627\u062a \u0631\u0633\u0627\u0646\u06cc \u062f\u0631 \u062d\u0648\u0632\u0647 \u0628\u06cc\u0646\u0627\u06cc\u06cc \u0645\u0627\u0634\u06cc\u0646 \u0647\u0627\u06cc \u0635\u0646\u0639\u062a\u06cc \u0648 \u0628\u0627 \u0627\u062a"
                        "\u06a9\u0627 \u0628\u0647 \u0646\u06cc\u0631\u0648\u0647\u0627\u06cc \u0645\u062a\u062e\u0635\u0635 \u0648 \u0647\u0645\u06a9\u0627\u0631\u0627\u0646 \u062f\u0627\u062e\u0644\u06cc \u062e\u0648\u062f\u060c \u06af\u0627\u0645\u06cc \u0646\u0648\u06cc\u0646 \u062f\u0631 \u0639\u0631\u0635\u0647 \u0627\u0631\u0627\u0626\u0647 \u062a\u06a9\u0646\u0648\u0644\u0648\u0698\u06cc \u0647\u0627\u06cc \u0646\u0648\u06cc\u0646 \u00a0\u067e\u0631\u062f\u0627\u0632\u0634 \u062a\u0635\u0627\u0648\u06cc\u0631 \u0635\u0646\u0639\u062a\u06cc \u062f\u0631 \u06a9\u0634\u0648\u0631 \u0628\u0631\u062f\u0627\u0634\u062a\u0647 \u0627\u0633\u062a \u0648 \u062f\u0633\u062a\u0627\u0648\u0631\u062f\u0647\u0627 \u0648 \u062a\u0644\u0627\u0634 \u0647\u0627\u06cc \u0632\u06cc\u0627\u062f \u0634\u0631\u06a9\u062a \u0646\u06cc\u0632 \u0646\u0634\u0627\u0646 \u062f\u0647\u0646\u062f\u0647 \u0627\u06cc\u0646 \u0645\u0648\u0636\u0648\u0639 \u0645\u06cc \u0628\u0627\u0634\u062f.</span></p>\n"
"<p align=\"justify\" dir='rtl' style=\" margin-top:0px"
                        "; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'IranSansNum','Arial','Helvetica','sans-serif'; font-size:16pt; color:#000000;\">\u062f\u06cc\u062f\u06af\u0627\u0647 \u0648 \u0647\u062f\u0641 \u0634\u0631\u06a9\u062a \u0633\u0631\u0648\u06cc\u0633 \u062f\u0647\u06cc \u0628\u0647 \u0645\u0634\u062a\u0631\u06cc\u0627\u0646 \u062f\u0631 \u0641\u0636\u0627\u06cc\u06cc \u0627\u0645\u0646\u060c \u0642\u0627\u0628\u0644 \u0627\u0637\u0645\u06cc\u0646\u0627\u0646 \u0648 \u062f\u0631 \u062f\u0633\u062a\u0631\u0633 \u0648 \u06a9\u0645\u06a9 \u0628\u0647 \u062a\u0648\u0633\u0639\u0647 \u0648 \u0628\u06a9\u0627\u0631\u06af\u06cc\u0631\u06cc \u0641\u0646\u0627\u0648\u0631\u06cc \u0647\u0627\u06cc \u0631\u0648\u0632 \u062f\u0646\u06cc\u0627 \u0647\u0645\u06af\u0627\u0645 \u0628\u0627 \u0628\u0648\u0645\u06cc \u0633\u0627\u0632\u06cc \u0641\u0646 \u0622\u0648\u0631\u06cc\u060c \u062e\u062f\u0645\u0627\u062a \u0648 \u062f\u0627\u0646\u0634 \u062f\u0631"
                        " \u0633\u0637\u062d \u0645\u0644\u06cc \u062f\u0631 \u06a9\u0646\u0627\u0631 \u0627\u06cc\u062c\u0627\u062f \u0641\u0636\u0627\u06cc \u06a9\u0633\u0628 \u0648 \u06a9\u0627\u0631 \u0627\u0645\u0646\u060c \u0645\u0637\u0645\u0626\u0646 \u0648 \u067e\u0648\u06cc\u0627 \u0645\u06cc \u0628\u0627\u0634\u062f \u0648 \u062f\u0631 \u0646\u0647\u0627\u06cc\u062a \u0628\u0627 \u062d\u0631\u06a9\u062a \u062f\u0631 \u06a9\u0646\u0627\u0631 \u0645\u0634\u062a\u0631\u06cc\u0627\u0646 \u062f\u0631 \u0627\u0628\u0639\u0627\u062f \u0641\u0646\u06cc \u0648 \u0645\u062f\u06cc\u0631\u06cc\u062a\u06cc\u060c \u0634\u0631\u06a9\u062a \u062f\u06cc\u062f\u0647 \u0631\u0627\u06cc\u0627\u0646 \u0635\u0646\u0639\u062a\u06cc \u0627\u0635\u0641\u0647\u0627\u0646 \u062a\u0628\u062f\u06cc\u0644 \u0628\u0647 \u062f\u0633\u062a \u062a\u0648\u0627\u0646\u0627\u06cc \u0645\u0634\u062a\u0631\u06cc \u062f\u0631 \u0627\u0631\u0627\u0626\u0647 \u0627\u0646\u0648\u0627\u0639 \u0633\u0631\u0648\u06cc\u0633 \u0647\u0627 \u0648 \u062e\u062f\u0645\u0627\u062a"
                        " \u06af\u0631\u062f\u06cc\u062f\u0647 \u0648 \u0622\u0633\u0648\u062f\u06af\u06cc \u062e\u06cc\u0627\u0644\u060c \u0622\u0631\u0627\u0645\u0634 \u0648 \u0627\u0637\u0645\u06cc\u0646\u0627\u0646 \u0631\u0627 \u0628\u0631\u0627\u06cc \u0645\u0634\u062a\u0631\u06cc\u0627\u0646 \u0628\u0647 \u0627\u0631\u0645\u063a\u0627\u0646 \u0645\u06cc \u0622\u0648\u0631\u062f. \u0631\u0627\u0647\u06a9\u0627\u0631 \u0645\u062d\u0648\u0631\u06cc\u060c \u062d\u0641\u0638 \u062d\u0642\u0648\u0642 \u0645\u0634\u062a\u0631\u06cc\u0627\u0646 \u0648 \u06a9\u0627\u0631\u0645\u0646\u062f\u0627\u0646\u060c \u0631\u0642\u0627\u0628\u062a \u0633\u0627\u0644\u0645\u060c \u0647\u0645 \u0627\u0641\u0632\u0627\u06cc\u06cc \u062a\u062c\u0627\u0631\u06cc \u0648 \u0627\u06cc\u062c\u0627\u062f \u0627\u0631\u0632\u0634 \u0627\u0641\u0632\u0648\u062f\u0647 \u0628\u0647 \u0639\u0646\u0648\u0627\u0646 \u0627\u0635\u0648\u0644 \u062f\u0631 \u062a\u0645\u0627\u0645 \u0633\u0627\u062e\u062a\u0627\u0631 \u0634\u0631\u06a9\u062a \u0645\u0648\u0631\u062f \u0642"
                        "\u0628\u0648\u0644 \u0648 \u062c\u0627\u0631\u06cc \u0628\u0648\u062f\u0647 \u0648 \u06a9\u0644\u06cc\u0647 \u0645\u062f\u06cc\u0631\u0627\u0646 \u0648 \u0633\u0647\u0627\u0645\u062f\u0627\u0631\u0627\u0646 \u0634\u0631\u06a9\u062a \u0646\u0647\u0627\u06cc\u062a \u062a\u0644\u0627\u0634 \u062e\u0648\u062f \u0631\u0627 \u062c\u0647\u062a \u0631\u0639\u0627\u06cc\u062a \u0627\u06cc\u0646 \u0627\u0635\u0648\u0644 \u062f\u0631 \u062a\u0645\u0627\u0645\u06cc \u0639\u0631\u0635\u0647 \u0647\u0627\u06cc \u0645\u062f\u06cc\u0631\u06cc\u062a\u06cc \u0648 \u062a\u062c\u0627\u0631\u06cc \u0628\u06a9\u0627\u0631 \u06af\u0631\u0641\u062a\u0647 \u0627\u0646\u062f.</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"User Guide:", None))
        self.user_manual_btn.setText(QCoreApplication.translate("MainWindow", u"User Manual File", None))
        self.label_34.setText("")
        self.label_32.setText("")
        self.label_45.setText("")
        self.label_46.setText("")
        self.label_43.setText("")
        self.checkBox_last_report.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"by Last :", None))
        self.spinBox_tedad.setPrefix("")
        self.checkBox_id_report.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"by ID :", None))
        self.checkBox_line_report.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"by Line :", None))
        self.checkBox_date_report.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"by DATE :", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Start Date:  1400-01-01  ", None))
        self.tool_start_calender.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Start Date:  1400-01-01  ", None))
        self.tool_end_calender.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_time_report.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"by TIME :", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Start Time: 24:59:59", None))
        self.tool_start_time.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.btn_now_time.setText(QCoreApplication.translate("MainWindow", u"Time to now", None))
        self.tool_end_time.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox_width_report.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"by Width :", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Start :", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"End :", None))
        self.checkBox_weight_report.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"by Weight :", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Start :", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"End :", None))
        self.full_search.setText(QCoreApplication.translate("MainWindow", u" Search", None))
        self.search_message.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.backup_btn.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.clear_checkboxes_btn.setText(QCoreApplication.translate("MainWindow", u"Clear Check boxes", None))
        self.edit_btn.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.export_btn.setText(QCoreApplication.translate("MainWindow", u"Export as EXCEL", None))
        self.dataset_cam_1_name_8.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.pan_image_label_2.setText("")
        self.dataset_cam_1_name_6.setText(QCoreApplication.translate("MainWindow", u"Camera 3", None))
        self.dataset_cam_1_name_9.setText(QCoreApplication.translate("MainWindow", u"Camera 4", None))
        self.pan_image_label_3.setText("")
        self.pan_image_label_4.setText("")
#if QT_CONFIG(tooltip)
        self.right_box_btn.setToolTip(QCoreApplication.translate("MainWindow", u"ToolBox", None))
#endif // QT_CONFIG(tooltip)
        self.right_box_btn.setText("")
        self.right_box_btn_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Head", None))
#if QT_CONFIG(tooltip)
        self.cam2_sign.setToolTip(QCoreApplication.translate("MainWindow", u"23961540", None))
#endif // QT_CONFIG(tooltip)
        self.cam2_sign.setText("")
        self.temp_cam2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Top", None))
#if QT_CONFIG(tooltip)
        self.cam1_sign.setToolTip(QCoreApplication.translate("MainWindow", u"23961515", None))
#endif // QT_CONFIG(tooltip)
        self.cam1_sign.setText("")
        self.temp_cam1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Right", None))
#if QT_CONFIG(tooltip)
        self.cam3_sign.setToolTip(QCoreApplication.translate("MainWindow", u"40150886", None))
#endif // QT_CONFIG(tooltip)
        self.cam3_sign.setText("")
        self.temp_cam3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_22.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Left", None))
#if QT_CONFIG(tooltip)
        self.cam4_sign.setToolTip(QCoreApplication.translate("MainWindow", u"23905933", None))
#endif // QT_CONFIG(tooltip)
        self.cam4_sign.setText("")
        self.temp_cam4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_25.setText("")
        self.cam1_sign_detect.setText("")
        self.cam2_sign_detect.setText("")
        self.cam3_sign_detect.setText("")
        self.cam4_sign_detect.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Slab Rate:", None))
        self.slab_rate.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.slab_rate_manual.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Melting ID :", None))
        self.slab_id_manual_2.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Slab ID:", None))
        self.slab_id_manual.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Slab Line :", None))
        self.slab_line_manual.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Width :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.slab_width_manual.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Weight :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.slab_width_manual_2.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Lenght :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.slab_lenght_manual.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Thickness :", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.slab_thickness_manual.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Defects List", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Add New Defect", None))
        self.checkBox_top.setText(QCoreApplication.translate("MainWindow", u"Head", None))
        self.checkBox_head.setText(QCoreApplication.translate("MainWindow", u"Top", None))
        self.checkBox_mesh.setText(QCoreApplication.translate("MainWindow", u"Mesh", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.fps_val.setText(QCoreApplication.translate("MainWindow", u"        --", None))
#if QT_CONFIG(tooltip)
        self.connect_btn.setToolTip(QCoreApplication.translate("MainWindow", u"connect", None))
#endif // QT_CONFIG(tooltip)
        self.connect_btn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(tooltip)
        self.calibrate_btn.setToolTip(QCoreApplication.translate("MainWindow", u"calibrate", None))
#endif // QT_CONFIG(tooltip)
        self.calibrate_btn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
#if QT_CONFIG(tooltip)
        self.disconnect_btn.setToolTip(QCoreApplication.translate("MainWindow", u"disconnect", None))
#endif // QT_CONFIG(tooltip)
        self.disconnect_btn.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.refresh_btn.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.automatic_btn.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.manual_btn.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.start_capture.setText(QCoreApplication.translate("MainWindow", u"START Capture", None))
        self.stop_capture.setText(QCoreApplication.translate("MainWindow", u"STOP Capture", None))
        self.capture_status_btn.setText("")
        self.report_label.setText("")
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
    # retranslateUi

