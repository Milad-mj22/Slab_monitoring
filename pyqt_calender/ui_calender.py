# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calender.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(444, 440)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(100,100,100);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_year = QLabel(self.frame)
        self.label_year.setObjectName(u"label_year")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_year.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_year)

        self.comboBox_year = QComboBox(self.frame)
        self.comboBox_year.setObjectName(u"comboBox_year")
        self.comboBox_year.setMinimumSize(QSize(0, 27))

        self.horizontalLayout_5.addWidget(self.comboBox_year)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_2 = QSpacerItem(59, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_month = QLabel(self.frame)
        self.label_month.setObjectName(u"label_month")
        self.label_month.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_month)

        self.comboBox_month = QComboBox(self.frame)
        self.comboBox_month.setObjectName(u"comboBox_month")
        self.comboBox_month.setMinimumSize(QSize(0, 28))

        self.horizontalLayout_3.addWidget(self.comboBox_month)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_prev = QPushButton(self.centralwidget)
        self.pushButton_prev.setObjectName(u"pushButton_prev")
        self.pushButton_prev.setStyleSheet(u"background-color: Transparent;")
        icon = QIcon()
        icon.addFile(u"../images/chevron.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_prev.setIcon(icon)
        self.pushButton_prev.setIconSize(QSize(38, 57))

        self.horizontalLayout.addWidget(self.pushButton_prev)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setMinimumSize(QSize(40, 40))
        self.pushButton_5.setMaximumSize(QSize(40, 40))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_5, 0, 4, 1, 1, Qt.AlignHCenter)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setMinimumSize(QSize(40, 40))
        self.pushButton_12.setMaximumSize(QSize(40, 40))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_12, 1, 4, 1, 1, Qt.AlignHCenter)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setMinimumSize(QSize(40, 40))
        self.pushButton_7.setMaximumSize(QSize(40, 40))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_7, 0, 6, 1, 1, Qt.AlignHCenter)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setMinimumSize(QSize(40, 40))
        self.pushButton_10.setMaximumSize(QSize(40, 40))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_10, 1, 2, 1, 1, Qt.AlignHCenter)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(True)
        self.pushButton_13.setMinimumSize(QSize(40, 40))
        self.pushButton_13.setMaximumSize(QSize(40, 40))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_13, 1, 5, 1, 1, Qt.AlignHCenter)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(40, 40))
        self.pushButton_11.setMaximumSize(QSize(40, 40))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1, Qt.AlignHCenter)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setEnabled(True)
        self.pushButton_15.setMinimumSize(QSize(40, 40))
        self.pushButton_15.setMaximumSize(QSize(40, 40))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_15, 2, 0, 1, 1, Qt.AlignHCenter)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setEnabled(True)
        self.pushButton_17.setMinimumSize(QSize(40, 40))
        self.pushButton_17.setMaximumSize(QSize(40, 40))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_17, 2, 2, 1, 1, Qt.AlignHCenter)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QSize(40, 40))
        self.pushButton_1.setMaximumSize(QSize(40, 40))
        self.pushButton_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1, Qt.AlignHCenter)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(40, 40))
        self.pushButton_6.setMaximumSize(QSize(40, 40))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_6, 0, 5, 1, 1, Qt.AlignHCenter)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMinimumSize(QSize(40, 40))
        self.pushButton_8.setMaximumSize(QSize(40, 40))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1, Qt.AlignHCenter)

        self.pushButton_19 = QPushButton(self.centralwidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setEnabled(True)
        self.pushButton_19.setMinimumSize(QSize(40, 40))
        self.pushButton_19.setMaximumSize(QSize(40, 40))
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_19, 2, 4, 1, 1, Qt.AlignHCenter)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QSize(40, 40))
        self.pushButton_18.setMaximumSize(QSize(40, 40))
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_18, 2, 3, 1, 1, Qt.AlignHCenter)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 16777215))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setBold(False)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setToolTipDuration(0)

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(40)
        sizePolicy2.setVerticalStretch(40)
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setMaximumSize(QSize(40, 40))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1, Qt.AlignHCenter)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setEnabled(True)
        self.pushButton_14.setMinimumSize(QSize(40, 40))
        self.pushButton_14.setMaximumSize(QSize(40, 40))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_14, 1, 6, 1, 1, Qt.AlignHCenter)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(40, 40))
        self.pushButton_16.setMaximumSize(QSize(40, 40))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_16, 2, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(40, 40))
        self.pushButton_9.setMaximumSize(QSize(40, 40))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setEnabled(True)
        self.pushButton_20.setMinimumSize(QSize(40, 40))
        self.pushButton_20.setMaximumSize(QSize(40, 40))
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_20, 2, 5, 1, 1, Qt.AlignHCenter)

        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setEnabled(True)
        self.pushButton_24.setMinimumSize(QSize(40, 40))
        self.pushButton_24.setMaximumSize(QSize(40, 40))
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_24, 3, 2, 1, 1, Qt.AlignHCenter)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setMinimumSize(QSize(40, 40))
        self.pushButton_25.setMaximumSize(QSize(40, 40))
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_25, 3, 3, 1, 1, Qt.AlignHCenter)

        self.pushButton_26 = QPushButton(self.centralwidget)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setEnabled(True)
        self.pushButton_26.setMinimumSize(QSize(40, 40))
        self.pushButton_26.setMaximumSize(QSize(40, 40))
        self.pushButton_26.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_26, 3, 4, 1, 1, Qt.AlignHCenter)

        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setEnabled(True)
        self.pushButton_22.setMinimumSize(QSize(40, 40))
        self.pushButton_22.setMaximumSize(QSize(40, 40))
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_22, 3, 0, 1, 1, Qt.AlignHCenter)

        self.pushButton_28 = QPushButton(self.centralwidget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setEnabled(True)
        self.pushButton_28.setMinimumSize(QSize(40, 40))
        self.pushButton_28.setMaximumSize(QSize(40, 40))
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_28, 3, 6, 1, 1, Qt.AlignHCenter)

        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMinimumSize(QSize(40, 40))
        self.pushButton_23.setMaximumSize(QSize(40, 40))
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_23, 3, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setEnabled(True)
        self.pushButton_21.setMinimumSize(QSize(40, 40))
        self.pushButton_21.setMaximumSize(QSize(40, 40))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_21, 2, 6, 1, 1, Qt.AlignHCenter)

        self.pushButton_27 = QPushButton(self.centralwidget)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setEnabled(True)
        self.pushButton_27.setMinimumSize(QSize(40, 40))
        self.pushButton_27.setMaximumSize(QSize(40, 40))
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_27, 3, 5, 1, 1, Qt.AlignHCenter)

        self.pushButton_29 = QPushButton(self.centralwidget)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMinimumSize(QSize(40, 40))
        self.pushButton_29.setMaximumSize(QSize(40, 40))
        self.pushButton_29.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_29, 4, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(40, 40))
        self.pushButton_30.setMaximumSize(QSize(40, 40))
        self.pushButton_30.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_30, 4, 1, 1, 1)

        self.pushButton_31 = QPushButton(self.centralwidget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setEnabled(False)
        self.pushButton_31.setMinimumSize(QSize(40, 40))
        self.pushButton_31.setMaximumSize(QSize(40, 40))
        self.pushButton_31.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pushButton_31, 4, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setStyleSheet(u"background-color: Transparent;")
        icon1 = QIcon()
        icon1.addFile(u"next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_next.setIcon(icon1)
        self.pushButton_next.setIconSize(QSize(38, 57))

        self.horizontalLayout.addWidget(self.pushButton_next)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 17))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_10.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_selected_date = QLabel(self.frame_3)
        self.label_selected_date.setObjectName(u"label_selected_date")

        self.horizontalLayout_7.addWidget(self.label_selected_date)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.today_btn = QPushButton(self.frame_3)
        self.today_btn.setObjectName(u"today_btn")

        self.horizontalLayout_7.addWidget(self.today_btn)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 22))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.select_btn = QPushButton(self.frame_2)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setMaximumSize(QSize(75, 16777215))
        self.select_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.select_btn)

        self.close_btn = QPushButton(self.frame_2)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(75, 16777215))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Calender", None))
        self.label_year.setText(QCoreApplication.translate("MainWindow", u"Year  :", None))
        self.label_month.setText(QCoreApplication.translate("MainWindow", u"Month  :", None))
        self.pushButton_prev.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"13", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"18", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"14", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"24", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"26", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"22", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"28", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"23", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"21", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"27", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"29", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"31", None))
        self.pushButton_next.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"selected date is: ", None))
        self.label_selected_date.setText("")
        self.today_btn.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.close_btn.setText(QCoreApplication.translate("MainWindow", u"Close", None))
    # retranslateUi

