# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_clock.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(266, 227)
        MainWindow.setMaximumSize(QSize(266, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(66, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.up_hour = QPushButton(self.frame_2)
        self.up_hour.setObjectName(u"up_hour")
        self.up_hour.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_hour.setStyleSheet(u"background-color:Transparent;")
        icon = QIcon()
        icon.addFile(u"images/chevron - up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.up_hour.setIcon(icon)
        self.up_hour.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.up_hour)

        self.label_hour = QLineEdit(self.frame_2)
        self.label_hour.setObjectName(u"label_hour")
        self.label_hour.setMinimumSize(QSize(0, 57))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(29)
        font.setBold(False)
        self.label_hour.setFont(font)
        self.label_hour.setFrame(False)

        self.verticalLayout_2.addWidget(self.label_hour, 0, Qt.AlignHCenter)

        self.down_hour = QPushButton(self.frame_2)
        self.down_hour.setObjectName(u"down_hour")
        self.down_hour.setCursor(QCursor(Qt.PointingHandCursor))
        self.down_hour.setStyleSheet(u"background-color:Transparent;")
        icon1 = QIcon()
        icon1.addFile(u"images/chevron - down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.down_hour.setIcon(icon1)
        self.down_hour.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.down_hour)


        self.horizontalLayout.addWidget(self.frame_2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(9, 16777215))
        font1 = QFont()
        font1.setPointSize(22)
        self.label_4.setFont(font1)

        self.horizontalLayout.addWidget(self.label_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(66, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.up_min = QPushButton(self.frame_5)
        self.up_min.setObjectName(u"up_min")
        self.up_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_min.setStyleSheet(u"background-color:Transparent;")
        self.up_min.setIcon(icon)
        self.up_min.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.up_min)

        self.label_min = QLineEdit(self.frame_5)
        self.label_min.setObjectName(u"label_min")
        self.label_min.setMinimumSize(QSize(0, 57))
        self.label_min.setFont(font)
        self.label_min.setFrame(False)

        self.verticalLayout_3.addWidget(self.label_min, 0, Qt.AlignHCenter)

        self.down_min = QPushButton(self.frame_5)
        self.down_min.setObjectName(u"down_min")
        self.down_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.down_min.setStyleSheet(u"background-color:Transparent;")
        self.down_min.setIcon(icon1)
        self.down_min.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.down_min)


        self.horizontalLayout.addWidget(self.frame_5)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(9, 16777215))
        self.label_5.setFont(font1)

        self.horizontalLayout.addWidget(self.label_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(66, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.up_sec = QPushButton(self.frame_6)
        self.up_sec.setObjectName(u"up_sec")
        self.up_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.up_sec.setStyleSheet(u"background-color:Transparent;")
        self.up_sec.setIcon(icon)
        self.up_sec.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.up_sec)

        self.label_sec = QLineEdit(self.frame_6)
        self.label_sec.setObjectName(u"label_sec")
        self.label_sec.setMinimumSize(QSize(0, 57))
        self.label_sec.setFont(font)
        self.label_sec.setFrame(False)

        self.verticalLayout_4.addWidget(self.label_sec, 0, Qt.AlignHCenter)

        self.down_sec = QPushButton(self.frame_6)
        self.down_sec.setObjectName(u"down_sec")
        self.down_sec.setCursor(QCursor(Qt.PointingHandCursor))
        self.down_sec.setStyleSheet(u"background-color:Transparent;")
        self.down_sec.setIcon(icon1)
        self.down_sec.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.down_sec)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 24))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.select_btn = QPushButton(self.frame_3)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.select_btn)

        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"24 Hour Format", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hour", None))
        self.up_hour.setText("")
        self.label_hour.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.down_hour.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Minute", None))
        self.up_min.setText("")
        self.label_min.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.down_min.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Second", None))
        self.up_sec.setText("")
        self.label_sec.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.down_sec.setText("")
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

