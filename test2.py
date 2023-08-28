
# # import sys
# # from PyQt5 import QtCore, QtGui, QtWidgets
# # from PyQt5.QtGui import QMovie
# # from PyQt5.QtCore import Qt

# # class LoadingGif(object):
  
# #     def mainUI(self, FrontWindow):
# #         FrontWindow.setObjectName("FTwindow")
# #         FrontWindow.resize(320, 300)
# #         self.centralwidget = QtWidgets.QWidget(FrontWindow)
# #         self.centralwidget.setObjectName("main-widget")
  
# #         # Label Create
# #         self.label = QtWidgets.QLabel(self.centralwidget)
# #         self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
# #         self.label.setMinimumSize(QtCore.QSize(250, 250))
# #         self.label.setMaximumSize(QtCore.QSize(250, 250))
# #         self.label.setObjectName("lb1")
# #         FrontWindow.setCentralWidget(self.centralwidget)
  
# #         # Loading the GIF
# #         self.movie = QMovie("21-avatar-outline.gif")
# #         self.label.setMovie(self.movie)
  
# #         self.startAnimation()
  
# #     # Start Animation
  
# #     def startAnimation(self):
# #         self.movie.start()
  
# #     # Stop Animation(According to need)
# #     def stopAnimation(self):
# #         self.movie.stop()
  
  
# # app = QtWidgets.QApplication(sys.argv)
# # window = QtWidgets.QMainWindow()
# # demo = LoadingGif()
# # demo.mainUI(window)
# # window.show()
# # sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)


# class MouseTracker(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.setMouseTracking(True)

#     def initUI(self):
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Mouse Tracker')
#         self.label = QLabel(self)
#         self.label.resize(200, 40)
#         self.show()

#     def mouseMoveEvent(self, event):
#         self.label.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MouseTracker()
#     sys.exit(app.exec_())


def hello():
    print("hello, world")

from threading import Timer

t = Timer(2.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed