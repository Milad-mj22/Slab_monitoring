import cv2
import numpy as np


#img = cv2.imread('G:\work\PySide-Responsive-ui-master\myqr.png')
#print(img.shape)


def zoomin(img,scale, pt ):
    h,w = img.shape[:2]

    roi_w = int(w/scale)
    roi_h = int(h/scale)

    x,y = pt
    x1,x2,y1,y2=0,0,0,0

    x1 = int(x - roi_w/2)
    x2 = int(x + roi_w/2)

    y1 = int(y - roi_h/2)
    y2 = int(y + roi_h/2)
    #print(roi_h,h, roi_w,w, scale, x,y)
    #print('asd222',x1,x2,y1,y2)
    if x1<0:
        
        x2 = abs(x1) + x2
        x1=0
        #print('if1',x1,x2)
    if x2>w:
        x1 = x1 - (x2-w)
        x2=w
        #print('if2',x1,x2)

    if y1<0:
        y2 = abs(y1) + y2
        y1=0
        #print('if3',y1,y2)
    if y2>h:
        y1 = y1 - (y2-h)
        y2=h
        #print('if4',y1,y2)

    #print('asd',x1,x2,y1,y2)
    roi = np.copy(img[y1:y2, x1:x2])
    roi = cv2.resize(roi,(w,h))
    return roi
        


# if __name__ == "__main__":

#     res = zoomin(img,2,(10,10))

#     img = cv2.resize(img, None, fx=0.5, fy=0.5)
#     res = cv2.resize(res, None, fx=0.5, fy=0.5)

#     cv2.imshow('img', img)
#     cv2.imshow('res', res)
#     cv2.waitKey(0)
