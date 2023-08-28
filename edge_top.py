from tkinter.tix import Tree
import cv2
import numpy as np


# itr = 1
# # while True:

# def check_slab(image):

#     # image = cv2.imread('cam 1/2/img (%s).tiff' % itr)

#     # image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2), interpolation = cv2.INTER_AREA)
#     # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     # cv2.imshow('full image', image)
#     # cv2.waitKey(50)


#     # croped = image[0:-800, 100:-10]


#     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('image side', image)
#     cv2.waitKey(20)

#     croped = image[0:-800, 100:-10]

#     cv2.imshow('cropped', croped)
#     cv2.waitKey(10)

#     ksize = 3
#     kernel = np.ones((ksize, ksize), np.uint8)
#     sobely = cv2.Sobel(src=croped, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=ksize, scale=2, delta=0, borderType=cv2.BORDER_DEFAULT) # Sobel Edge
#     sobely = cv2.convertScaleAbs(sobely)
#     _, sobely = cv2.threshold(sobely, 0, 255, cv2.THRESH_BINARY)
#     #
#     sobelx = cv2.Sobel(src=croped, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=ksize, scale=2, delta=0, borderType=cv2.BORDER_DEFAULT) # Sobel Edge
#     sobelx = cv2.convertScaleAbs(sobelx)
#     _, sobelx = cv2.threshold(sobelx, 150, 255, cv2.THRESH_BINARY)
#     cv2.imshow('edgesy', sobely)
#     cv2.waitKey(20)
#     cv2.imshow('edgesx', sobelx)
#     cv2.waitKey(20)



#     edges_f = sobely * np.invert(sobelx == sobely)
#     edges_f = cv2.dilate(edges_f, kernel, iterations=1)
# # 
#     cv2.imshow('edges side1', edges_f)
#     cv2.waitKey(20)


#     cnts, _ = cv2.findContours(edges_f, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     filter_area = lambda x: 500 < cv2.contourArea(x) < 50000
#     cnts = list(filter(filter_area, cnts))

#     # if len(cnts) == 0:
#     #     print('New folder\img (%s).tiff' % itr)

    
#     # try:
#     #     cnts.sort(key = lambda x:cv2.contourArea(x), reverse=True)
#     #     print(cv2.contourArea(cnts[0]))
#     # except:
#     #     pass
    
#     edges_f = cv2.drawContours(np.zeros((edges_f.shape), dtype=np.uint8), cnts, -1, color=(255,255,255), thickness=cv2.FILLED)
#     cv2.imshow('edges top', edges_f)
#     cv2.waitKey(20)
#     try:
#         cnts.sort(key = lambda x:cv2.contourArea(x), reverse=True)
#         cnts=cv2.contourArea(cnts[0])
#     except:
#         cnts=0
#     return cnts

#     # cv2.waitKey(250)
#     # itr+=1


#     # cv2.waitKey(100)

#     # itr+=1



from tkinter.tix import Tree
import cv2
import numpy as np


itr = 1
# while True:

def check_slab(image):

    # image = cv2.imread('cam 1/2/img (%s).tiff' % itr)

    # image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2), interpolation = cv2.INTER_AREA)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image', image)
    # cv2.waitKey(50)

    croped = image[500:-800, 200:-10]
    # cv2.imshow('cropedtop', croped)
    # cv2.waitKey(50)

    ksize = 5
    kernel = np.ones((ksize, ksize), np.uint8)
    sobely = cv2.Sobel(src=croped, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=ksize, scale=2, delta=0, borderType=cv2.BORDER_DEFAULT) # Sobel Edge
    sobely = cv2.convertScaleAbs(sobely)
    _, sobely = cv2.threshold(sobely, 150, 255, cv2.THRESH_BINARY)
    #
    sobelx = cv2.Sobel(src=croped, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=ksize, scale=2, delta=0, borderType=cv2.BORDER_DEFAULT) # Sobel Edge
    sobelx = cv2.convertScaleAbs(sobelx)
    _, sobelx = cv2.threshold(sobelx, 150, 255, cv2.THRESH_BINARY)



    edges_f = sobely * np.invert(sobelx == sobely)
    edges_f = cv2.dilate(edges_f, kernel, iterations=1)

    # cv2.imshow('edges_f1', edges_f)
    # cv2.waitKey(50)


    cnts, _ = cv2.findContours(edges_f, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filter_area = lambda x: 600 < cv2.contourArea(x) < 100000
    cnts = list(filter(filter_area, cnts))

    # if len(cnts) == 0:
    #     print('New folder\img (%s).tiff' % itr)

    #cnts.sort(key = lambda x:cv2.contourArea(x), reverse=True)
    
    edges_ff = cv2.drawContours(np.zeros((edges_f.shape), dtype=np.uint8), cnts, -1, color=(255,255,255), thickness=cv2.FILLED)
    # cv2.imshow('edges_f2', edges_ff)
    # cv2.waitKey(50)

    # if len(cnts)>0:
    #     cv2.imwrite('f_%s.jpg' % itr, edges_f)
    #     cv2.imwrite('ff_%s.jpg' % itr, edges_ff)
    #     itr+=1

    try:
        cnts.sort(key = lambda x:cv2.contourArea(x), reverse=True)
        cnts=cv2.contourArea(cnts[0])
        print
    except:
        cnts=0
    return cnts
    # cv2.imshow('edges2', edges_f)


    # cv2.waitKey(100)

    # itr+=1





if __name__=='__main__':
    for i in range(5,167):
        img = cv2.imread('detection\images2/1 ({}).tiff'.format(i))

        # cv2.imshow('img',img)
        # cv2.waitKey(10)
        check_slab(img)
  