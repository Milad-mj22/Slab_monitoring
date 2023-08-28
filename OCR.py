from PIL import Image
import pytesseract

image = '2.jpeg'

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'



import cv2
import numpy as np

img_cv = cv2.imread('2.jpeg',0)


#$img_cv=cv2.equalizeHist(img_cv)
clahe = cv2 .createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_cv = clahe.apply(img_cv)
cv2.imshow('asd',img_cv)
cv2.waitKey(0)

img_cv=cv2.adaptiveThreshold(img_cv,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,91,9)


img_cv=cv2.erode(img_cv,np.ones((3,3)),iterations=1)




# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
# img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img_rgb))
# OR
# img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_cv))


cv2.imshow('asd',img_cv)

cv2.waitKey(0)