# import cv2
# import time

# frame_id = 0
# starting_time = time.time()
# elapsed_time_pause = 0
# cap = cv2.VideoCapture(0)
# while True:
#     _, frame = cap.read()
#     frame_id += 1

#     #...some processing...

#     elapsed_time = time.time() - starting_time - elapsed_time_pause
#     fps = frame_id / elapsed_time

#     cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2) #print del FPS
#     cv2.putText(frame, "frame id: " + str(frame_id), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
#     elapsed_time_pause = 0

#     cv2.imshow('frame', frame)
#     key = cv2.waitKey(1)
#     if key == ord('p'):
#         starting_time_pause = time.time()
#         cv2.waitKey(0)
#         elapsed_time_pause = time.time() - starting_time_pause
#     elif key == ord('q'):
#          break
# cap.release()
# cv2.destroyAllWindows()
# import cv2
# cap = cv2.VideoCapture(0) # getting video from webcam
# while cap.isOpened():
#     ret, img = cap.read()

#     cv2.imshow("Frame",img)

#     key = cv2.waitKey(1)
#     if key == ord('q'):
#         break
#     if key == ord('p'):
#         cv2.waitKey(-1) #wait until any key is pressed
# cap.release()
# cv2.destroyAllWindows()

# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

# class MyApp(QWidget):

#     def __init__(self, *args):
#         super().__init__(*args)

#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)

#         self.button_zoom_in = QPushButton('Zoom IN', self)
#         self.button_zoom_in.clicked.connect(self.on_zoom_in)
#         self.layout.addWidget(self.button_zoom_in)

#         self.button_zoom_out = QPushButton('Zoom OUT', self) 
#         self.button_zoom_out.clicked.connect(self.on_zoom_out)
#         self.layout.addWidget(self.button_zoom_out)

#         self.pixmap = QPixmap('images/637288638132980756.png')
#         self.height = self.pixmap.height()

#         self.label = QLabel(self)
#         self.label.setPixmap(self.pixmap)
#         self.layout.addWidget(self.label)

#         self.show()

#     def on_zoom_in(self, event):
#         self.height += 100
#         self.resize_image()

#     def on_zoom_out(self, event):
#         self.height -= 100
#         self.resize_image()

#     def resize_image(self):
#         scaled_pixmap = self.pixmap.scaledToHeight(self.height)
#         self.label.setPixmap(scaled_pixmap)

# # --- main ---

# app = QApplication([])
# win = MyApp()
# app.exec()

list1=['1',1,'14','wdas']

list2=[1,'wdas']


for i in range(len(list2)):
    if list2[i] in list1:
        print('yes')