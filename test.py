'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''

import camera_panorama_trigger_2
import cv2

import numpy as np



cont=0



def check_image(img):
    print(np.average(img[0]))
    if np.average(img[0])<15:
        print('yes')






if __name__=='__main__':



    collector = camera_panorama_trigger_2.Collector('40150887',exposure=3000, gain=10, trigger=False, delay_packet=8310,\
        packet_size=8192,frame_transmission_delay=230000,manual=False)
        # collector.start_grabbing()
    cameras=collector

    cameras.start_grabbing()
    cameras.getPictures()


    # Assigning our static_back to None
    static_back = 0
    
    # List when any moving object appear
    motion_list = [ None, None ]
    
    # Time of movement
    time = []


    while True:
        
    #     # for cam in cameras:
    #     #         cam.trigg_exec()
                
    #     # for cam in cameras:
    #     #print(cam.camera.GetQueuedBufferCount())
        img = cameras.getPictures()

        img=cv2.resize(img,dsize=(480,300))

        # img=img[0]

        cv2.imshow('img',img)

        # check_image(img)
        #print(cam.camera.GetQueuedBufferCount())
        cv2.imshow('img1', cv2.resize( img, None, fx=0.5, fy=0.5 ))

        # cv2.waitKey(50)







        # Initializing motion = 0(no motion)
        motion = 0
    
        # Converting color image to gray_scale image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray=img
    
        # Converting gray scale image to GaussianBlur
        # so that change can be find easily
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
        # In first iteration we assign the value
        # of static_back to our first frame
        # if static_back is None:
        # static_back = gray
        # continue
    
        # Difference between static background
        # and current frame(which is GaussianBlur)
        diff_frame = cv2.absdiff(static_back, gray)
    
        # If change in between static background and
        # current frame is greater than 30 it will show white color(255)
        thresh_frame = cv2.threshold(diff_frame, 15, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    
        # Finding contour of moving object
        # cnts,_ = cv2.findContours(thresh_frame.copy(),
        #                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
        # for contour in cnts:
        #     if cv2.contourArea(contour) < 10000:
        #         continue
        #     motion = 1
    
        #     (x, y, w, h) = cv2.boundingRect(contour)
        #     # making green rectangle around the moving object
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    
        # # Appending status of motion
        # motion_list.append(motion)
    
        # motion_list = motion_list[-2:]

    # Displaying image in gray_scale
        # cv2.imshow("Gray Frame", gray)
    
        # Displaying the difference in currentframe to
        # the staticframe(very first_frame)
        # cv2.imshow("Difference Frame", diff_frame)
    
        # Displaying the black and white image in which if
        # intensity difference greater than 30 it will appear white
        cv2.imshow("Threshold Frame", thresh_frame)
    
        # Displaying color frame with contour of motion of object
        # cv2.imshow("Color Frame", img)

        cv2.waitKey(1)

        # print(thresh_frame)
        if np.count_nonzero(thresh_frame)>= 10000:
            print(np.count_nonzero(thresh_frame))
            print('cont',cont)
            cont+=1



        static_back = gray

 