# '''
# A simple Program for grabing video from basler camera and converting it to opencv img.
# Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
# '''
# from pypylon import pylon
# import cv2

# # conecting to the first available camera
# camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())

# # Grabing Continusely (video) with minimal delay
# camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
# converter = pylon.ImageFormatConverter()

# # converting to opencv bgr format
# converter.OutputPixelFormat = pylon.PixelType_BGR8packed
# converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

# while camera.IsGrabbing():
#     grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

#     if grabResult.GrabSucceeded():
#         # Access the image data
#         image = converter.Convert(grabResult)
#         img = image.GetArray()
#         cv2.namedWindow('title', cv2.WINDOW_NORMAL)
#         cv2.imshow('title', img)
#         k = cv2.waitKey(1)
#         if k == 27:
#             break
#     grabResult.Release()
    
# # Releasing the resource    
# camera.StopGrabbing()

# cv2.destroyAllWindows()


# import numpy as np
# import cv2

# image = cv2.imread('myqr.png')
# y=0
# x=0
# h=100
# w=200
# crop = image[y:y+h, x:x+w]
# cv2.imshow('Image', crop)
# cv2.waitKey(0) 

from PIL import Image
import cv2
 
from PIL import Image  

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height),color = (73, 109, 137) )
img.show()
# cv2.waitKey(0)