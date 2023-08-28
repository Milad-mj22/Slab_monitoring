import cv2
import os
import numpy as np
def show(name, img):
    cv2.imshow(name, cv2.resize(img, None, fx=0.3, fy=0.3))
path = 'images'
l=(110,80,90)
h=(190,400,400)

for file in os.listdir(path):
    img = cv2.imread(os.path.join( path, file))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    show('hsv1',img)

    hsv[:,:,2] -= 60
    hsv[ hsv<0]=0
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    show('hsv2',img)


    hsv[:,:,2] += 60
    hsv[ hsv>255]=255
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    show('hsv3',img)

    hsv[:,:,2] -= 70
    hsv[ hsv<0]=0
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    show('hsv4',hsv)
    
    cv2.waitKey(0)
