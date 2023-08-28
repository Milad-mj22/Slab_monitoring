from PIL import Image, ImageFilter
import cv2
  
# Opening the image (R prefixed to string
# in order to deal with '\' in paths)
# image = Image.open(r"G:/DORSA/Slab-Images/Basler_acA1920-40gc__23911196__20211031_104527263_0981.tiff")
  
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
  
# defining the canny detector function
  
# here weak_th and strong_th are thresholds for
# double thresholding step
def Canny_detector(img_ori, weak_th = None, strong_th = None):
     
    # conversion of image to grayscale
    img = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)
      
    # Noise reduction step
    img=cv2.resize(img,(640,480))
    img = cv2.GaussianBlur(img, (5, 5), 1.4)
    cv2.imshow('GaussianBlur',img)
    cv2.waitKey(0)
    # Calculating the gradients
    gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)
    cv2.imshow('gx',gx)
    cv2.waitKey(0)       
    cv2.imshow('gy',gy)
    cv2.waitKey(0)       
    # Conversion of Cartesian coordinates to polar
    mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees = True)
    cv2.imshow('Sobel',mag)
    cv2.waitKey(0)     
    # setting the minimum and maximum thresholds
    # for double thresholding
    from scipy import ndimage
    roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
    roberts_cross_h = np.array( [[ 0, 1 ],
                                [ -1, 0 ]] )
#     Advantages:

#     Detection of edges and orientation are easy.
#     Diagonal direction points are preserved.

    # Disadvantages:

    #     Very sensitive to noise.
    #     not very accurate in edge detection.
    img2 = cv2.imread("cam_2_20221108151114.tiff",0).astype('float64')
    img2/=255.0
    vertical = ndimage.convolve( img2, roberts_cross_v )
    horizontal = ndimage.convolve( img2, roberts_cross_h )
    
    edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
    edged_img*=255
    cv2.imshow('edged_img',edged_img)
    cv2.waitKey(0)   


    hsv = cv2.cvtColor(img_ori, cv2.COLOR_BGR2HSV)
      
    # define range of red color in HSV
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
      
    # create a red HSV colour boundary and 
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)
  
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('res',res)
    cv2.waitKey(0)
    # Display an original image
    # cv2.imshow('Original',frame)
  
    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame,100,200)
    cv2.imshow('edges',edges)
    cv2.waitKey(0)

    image = cv2.resize(img_ori, (500, 600))
    
    # The initial processing of the image
    # image = cv2.medianBlur(image, 3)
    image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # The declaration of CLAHE
    # clipLimit -> Threshold for contrast limiting
    clahe = cv2.createCLAHE(clipLimit = 5)
    final_img = clahe.apply(image_bw) + 30
    
    # Ordinary thresholding the same image
    _, ordinary_img = cv2.threshold(image_bw, 155, 255, cv2.THRESH_BINARY)
    
    # Showing all the three images
    cv2.imshow("ordinary threshold", ordinary_img)
    cv2.imshow("CLAHE image", final_img)
    
frame = cv2.imread("cam_2_20221108151114.tiff")

 
# calling the designed function for
# finding edges
canny_img = Canny_detector(frame)

# Displaying the input and output image 




