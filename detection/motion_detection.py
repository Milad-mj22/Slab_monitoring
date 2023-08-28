import cv2
import numpy as np
import time

import camera_connection

NOT_CALIBRATED = 'Not Calibrated.'
DETECTED_NOT_MOVING = 'Slab Detected, Not moving'
DETECTED_MOVING = 'Slab Detected, Moving'
NOT_DETECTED = 'Not detected.'



def get_camera_grabber_object():
    collector = camera_connection.Collector(serial_number='0', list_devices_mode=True)
    serials_list = collector.serialnumber()
    collector = camera_connection.Collector(serials_list[0], trigger=False, manual=False, list_devices_mode=False)
    return collector


class Slab_Detection():
    def __init__(self, diffrence_contour_min_area=5000, change_state_n_trys=3, auto_update_refrence_interval=7):
        self.refrence_frame = None
        self.slab_frame = None
        self.diffrence_contour_min_area = diffrence_contour_min_area
        self.change_state_itr = 0
        self.change_state_n_trys = change_state_n_trys
        self.current_state = False # False for not detect, True for detect
        self.auto_update_refrence_itr = time.time()
        self.auto_update_refrence_interval = auto_update_refrence_interval # in seconds

        # difference contours area filter
        self.cnts_filter_area = lambda x: cv2.contourArea(x) > self.diffrence_contour_min_area


    def update_refrence_frame(self, refrence_frame):
        # apply preprocessing on image
        refrence_frame = self.apply_preprocessing_on_frame(frame=refrence_frame)
        self.refrence_frame = refrence_frame

    
    def apply_preprocessing_on_frame(self, frame):
        # rgb to gray (if needed)
        if len(frame.shape)>2:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

         # apply gaussian blur
        frame = cv2.GaussianBlur(frame, ksize=(5,5), sigmaX=0)

        return frame
    

    def calc_difference(self, current_frame, refrence_frame,thresh):
        # calculate difference 
        diffrence = cv2.absdiff(src1=refrence_frame, src2=current_frame)
        diffrence = cv2.dilate(diffrence, np.ones((5, 5)), 2)
        # take different areas that are different enough
        _, diffrence = cv2.threshold(src=diffrence, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)

        # find contours of differences and filter by minimum area
        contours, _ = cv2.findContours(image=diffrence, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
        contours = list(filter(self.cnts_filter_area, contours))

        # cv2.imshow('asd', diffrence)

        # difference
        sum_areas = sum([cv2.contourArea(cnt) for cnt in contours])

        return contours, sum_areas


    def detect_slab(self, current_frame,thresh,mode=True):
        # apply preprocessing on image
        current_frame = self.apply_preprocessing_on_frame(frame=current_frame)

        # cv2.imshow('current',current_frame)
        # cv2.waitKey(10)

        # return flase if refrence frame is not available (not calibrated)
        if self.refrence_frame is None:
            return False, NOT_CALIBRATED, [], False
        
        # calclate diffrence between frames
        contours0, diff_value = self.calc_difference(current_frame=current_frame, refrence_frame=self.refrence_frame,thresh=thresh)
        # print(contours0)
        # slab not detected
        if len(contours0)==0:
            # slab not detected and state is not detected
            if not self.current_state:
                self.change_state_itr = 0
                if (time.time()-self.auto_update_refrence_itr >= self.auto_update_refrence_interval) and (mode==False):
                    self.update_refrence_frame(refrence_frame=current_frame)
                    self.auto_update_refrence_itr = time.time()
                    print('auto claibrated')

                return False, NOT_DETECTED, contours0, False

            if self.change_state_itr >= self.change_state_n_trys:
                self.current_state = False
                self.update_refrence_frame(refrence_frame=current_frame)
                return False, NOT_DETECTED, contours0, False
            
            self.change_state_itr+=1
            # cv2.imshow('c',current_frame)
            return True, DETECTED_MOVING, contours0, False
        
        # slab detected
        elif len(contours0)>0:
            self.auto_update_refrence_itr = time.time()

            if self.current_state:
                self.change_state_itr = 0
                return True, DETECTED_MOVING, contours0, False
            
            if self.change_state_itr >= self.change_state_n_trys:
                self.current_state = True
                self.slab_frame = current_frame
                return True, DETECTED_MOVING, contours0, True
            
            self.change_state_itr+=1
            return False, NOT_DETECTED, contours0, False




if __name__ == "__main__":
    
    # create camera collector object
    collector = get_camera_grabber_object()
    collector.start_grabbing()

    # create slab detection object
    slab_detection_obj = Slab_Detection()

    
    while True:
        # take frame
        frame = collector.getPictures()

        # make detection
        res, msg, contours = slab_detection_obj.detect_slab(current_frame=frame.copy())
        res_frame = frame.copy()

        # put detection results on image
        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)
            res_frame = cv2.rectangle(img=res_frame, pt1=(x, y), pt2=(x + w, y + h), color=(255,255,255), thickness=2)
        
        res_frame = cv2.putText(img=res_frame, text=msg, org=(10,40),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,255,255), thickness=2, lineType=cv2.LINE_AA)

        # show image
        cv2.imshow('Live', cv2.resize(res_frame, None, fx=0.5, fy=0.5))
        cv2.imshow('Slab', cv2.resize(slab_detection_obj.slab_frame if slab_detection_obj.slab_frame is not None else np.zeros((res_frame.shape)), None, fx=0.5, fy=0.5))

        k = cv2.waitKey(33)
        # Esc key to stop
        if k==27:
            cv2.destroyAllWindows()
            break
        # space key to calibrate
        elif k==32:
            slab_detection_obj.update_refrence_frame(refrence_frame=frame)
            
