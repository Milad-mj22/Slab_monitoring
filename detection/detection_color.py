import cv2
import os
import numpy as np
import time
t_all=[]
def show(name, img):
    cv2.imshow(name, cv2.resize(img, None, fx=0.3, fy=0.3))
    # print(img)
path = 'detection/images2'


l=(10,80,10)
h=(10,255,10)

def slab_detection(img,l=(10,80,90),h=(190,100,100),threshold=50000,name='None'):

    # mask = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    # mask = mask [:,:,0]
    # mask = cv2.threshold(mask , 170,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    # print(np.average(mask))
    # mask
    # mask = cv2.inRange( hsv, l, h)
    # mask= cv2.bitwise_and(img,img,mask =mask) 
    # mask = cv2.erode(mask, np.ones((1,1 )) , iterations=10)
    # mask = cv2.dilate(mask, np.ones(( 3,3 )) , iterations=15)

    # pixelpoints = cv2.findNonZero(mask) 
    # pixelpoints=len(pixelpoints)

    mask=img[150:400,100:350 ]
    mean_g = np.average(mask[:,:,1])
    mean_b = np.average(mask[:,:,0])
    mean_r = np.average(mask[:,:,2])
    print('mean_g',mean_g,'mean_b',mean_b,'mean_r',mean_r,name)
    # mask = mask[:,:,1]
    # print(np.average(mask),np.average(mask))
    # cv2.imshow('mask',mask) 
    # cv2.waitKey(0)

    # # print(pixelpoints)
    if np.average(mask)>150 :
        print("{} Detect {}".format(name,150))
        return True
    
    # else:
    #     print('{} noslab {}'.format(name,pixelpoints))
#     #     return False




for file in os.listdir(path):
    # t1=time.time()
    img = cv2.imread(os.path.join( path, file))
    ret=slab_detection(img, l, h,488999)
    print(ret)

  
# print(t_all,sum(t_all)/len(t_all))

# for file in os.listdir(path):
    # t1=time.time()
    # img = cv2.imread(os.path.join( path, file))
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange( hsv, l, h)
#     mask = cv2.erode(mask, np.ones((1,1 )) , iterations=1)
#     # show('mask1',mask)
#     mask = cv2.dilate(mask, np.ones(( 3,3 )) , iterations=15)
#     # b,g,r = cv2.split(img)
#     # show('img',img)
#     # show('b',b)
#     # show('g',g)
#     # show('r',r)
#     # show('mask',mask)
        
#     # thresh = 127
#     # im_bw = cv2.threshold(mask, thresh, 255, cv2.THRESH_BINARY)[1]
#     pixelpoints = cv2.findNonZero(mask)
#     print('pixelpoints',len(pixelpoints))
#     t2=time.time()

#     t_all.append(t2-t1)


#     cv2.waitKey(0)
  
# print(t_all,sum(t_all)/len(t_all))

