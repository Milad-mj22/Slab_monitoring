import cv2
import numpy as np


itr = 1
# while True:
def check_slab(image):


    # image = cv2.imread('New folder\img (%s).tiff' % itr)


    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image side', image)
    #cv2.waitKey(10)

    # croped = image[0:350, 600:1200]
    croped = image[0:200, 300:600]
    # cv2.imshow('cropped', croped)
    # cv2.waitKey(10)

    ksize = 3
    kernel = np.ones((ksize, ksize), np.uint8)
    sobely = cv2.Sobel(src=croped, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=ksize, scale=2, delta=0, borderType=cv2.BORDER_DEFAULT) # Sobel Edge
    sobely = cv2.convertScaleAbs(sobely)
    _, sobely = cv2.threshold(sobely, 100, 255, cv2.THRESH_BINARY)
    #
    sobelx = cv2.Sobel(src=croped, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=ksize, scale=2, delta=0, borderType=cv2.BORDER_DEFAULT) # Sobel Edge
    sobelx = cv2.convertScaleAbs(sobelx)
    _, sobelx = cv2.threshold(sobelx, 100, 255, cv2.THRESH_BINARY)
    # cv2.imshow('edgesy', sobely)
    #cv2.waitKey(0)
    # cv2.imshow('edgesx', sobelx)
    #cv2.waitKey(0)



    edges_f = sobely * np.invert(sobelx == sobely)
    edges_f = cv2.dilate(edges_f, kernel, iterations=1)
# 
    # cv2.imshow('edges side1', edges_f)
    #cv2.waitKey(0)


    cnts, _ = cv2.findContours(edges_f, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filter_area = lambda x: 500 < cv2.contourArea(x) < 50000
    cnts = list(filter(filter_area, cnts))

    # if len(cnts) == 0:
    #     print('New folder\img (%s).tiff' % itr)

    
    # try:
    #     cnts.sort(key = lambda x:cv2.contourArea(x), reverse=True)
    #     print(cv2.contourArea(cnts[0]))
    # except:
    #     pass
    
    edges_f = cv2.drawContours(np.zeros((edges_f.shape), dtype=np.uint8), cnts, -1, color=(255,255,255), thickness=cv2.FILLED)
    # cv2.imshow('edges side2', edges_f)
    # cv2.waitKey(20)
    try:
        cnts.sort(key = lambda x:cv2.contourArea(x), reverse=True)
        cnts=cv2.contourArea(cnts[0])
    except:
        cnts=0
    return cnts

    # cv2.waitKey(250)
    # itr+=1

