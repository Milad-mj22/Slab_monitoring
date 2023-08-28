# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_confirm_window(object):
    def setupUi(self, confirm_window):
        if not confirm_window.objectName():
            confirm_window.setObjectName(u"confirm_window")
        confirm_window.resize(396, 439)
        self.frame = QFrame(confirm_window)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-30, -10, 441, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.273, stop:0 rgba(100,100,100,200), stop:1 rgba(130,130,130, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 20, 374, 421))
        self.frame_2.setLayoutDirection(Qt.RightToLeft)
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(197 , 195,196);\n"
"	border-radius: 15px;\n"
"border: 1px solid rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 240, 351, 71))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"border: rgb(197 , 195,196);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.yes_btn = QPushButton(self.frame_2)
        self.yes_btn.setObjectName(u"yes_btn")
        self.yes_btn.setGeometry(QRect(40, 370, 93, 31))
        palette = QPalette()
        brush = QBrush(QColor(154, 154, 149, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(100, 100, 100, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(154, 154, 149, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(154, 154, 149, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(154, 154, 149, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.yes_btn.setPalette(palette)
        self.yes_btn.setLayoutDirection(Qt.LeftToRight)
        self.yes_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,100,100);\n"
"\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 15px;\n"
"	border-left: 1px solid rgb(30, 30, 30);\n"
"	border-right:1px solid rgb(30, 30, 30);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.no_btn = QPushButton(self.frame_2)
        self.no_btn.setObjectName(u"no_btn")
        self.no_btn.setGeometry(QRect(230, 370, 93, 31))
        self.no_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,100,100);\n"
"\n"
"	color: rgb(154, 154, 149);\n"
"	border: none;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	border-radius: 15px;\n"
"	border-left: 1px solid rgb(30, 30, 30);\n"
"	border-right:1px solid rgb(30, 30, 30);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(0,0, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 50, 251, 211))
        self.label_2.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(197 , 195,196);\n"
"	border-radius: 15px;\n"
"border: 1px solid rgb(197 , 195,196);\n"
"}\n"
"\n"
"")
        self.label_2.setPixmap(QPixmap(u"images/dorsa1.png"))
        self.label_2.setScaledContents(True)
        self.label_43 = QLabel(self.frame_2)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setEnabled(True)
        self.label_43.setGeometry(QRect(110, 20, 161, 81))
        self.label_43.setStyleSheet(u"border:None;")
        self.label_43.setPixmap(QPixmap(u"images/637288638132980756.png"))
        self.label_43.setScaledContents(True)
        self.yes_btn.raise_()
        self.no_btn.raise_()
        self.label_2.raise_()
        self.label_43.raise_()
        self.label.raise_()

        self.retranslateUi(confirm_window)

        QMetaObject.connectSlotsByName(confirm_window)
    # setupUi

    def retranslateUi(self, confirm_window):
        confirm_window.setWindowTitle(QCoreApplication.translate("confirm_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("confirm_window", u"TextLabel", None))
        self.yes_btn.setText(QCoreApplication.translate("confirm_window", u"      YES", None))
        self.no_btn.setText(QCoreApplication.translate("confirm_window", u"       NO", None))
        self.label_2.setText("")
        self.label_43.setText("")
    # retranslateUi

