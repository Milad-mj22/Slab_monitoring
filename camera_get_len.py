

from pypylon import pylon
import cv2
import time
import numpy as np
import sqlite3

DEBUG = False

class Collector():

    def __init__(self, gain = 0 , exposure = 70000, max_buffer = 20 ):
        """Initializes the Collector

        Args:
            gain (int, optional): The gain of images. Defaults to 0.
            exposure (float, optional): The exposure of the images. Defaults to 3000.
            max_buffer (int, optional): Image buffer for cameras. Defaults to 5.
        """
        self.gain = gain
        self.exposure = exposure
        self.max_buffer = max_buffer
        self.cont_eror=0

        self.__tl_factory = pylon.TlFactory.GetInstance()
        devices = []

        for device in self.__tl_factory.EnumerateDevices():
            if (device.GetDeviceClass() == 'BaslerGigE'):                
                devices.append(device)

        # assert len(devices) > 0 , 'No Camera is Connected!'

        self.cameras = list()

        for device in devices:
            camera = pylon.InstantCamera(self.__tl_factory.CreateDevice(device))
            self.cameras.append(camera)


    def check_devices(self):
        return self.cameras


    def start_grabbing(self):

        for i in range( len( self.cameras)):
            self.cameras[i].Open()
            # continue
            #print(self.cameras[i].GevSCPD.GetValue())
            
            # print('fdtyftyf')

            self.cameras[i].TriggerSelector.SetValue('FrameStart')
            #time.sleep(1)
            self.cameras[i].TriggerMode.SetValue('On')
            self.cameras[i].TriggerSource.SetValue('Software')
            sn=self.cameras[i].GetDeviceInfo().GetSerialNumber()
     
            if sn == '40150886':

                # self.cameras[i].GevSCPD.SetValue(3500)
                # self.cameras[i].GevSCFTD.SetValue(0)
                # self.cameras[i].GevSCBWR.SetValue(10)
                # self.cameras[i].GevSCBWR.SetValue(3)

                self.cameras[i].Gain.Value=int(self.cam1_detail[0][0])
                if DEBUG:
                    print('expo',self.exposure)
                self.cameras[i].ExposureTime=int(self.cam1_detail[0][1])
                if DEBUG:
                    print(self.cameras[i].ExposureTime())
                    print(self.cameras[i].Width.Value)

                self.cameras[i].Width=int(self.cam1_detail[0][3])
               # print(self.cameras[i].Width.Value)# = int(1921)#self.cam1_detail[0][3])
                self.cameras[i].Height = int(self.cam1_detail[0][4])
                if DEBUG:
                    print('camera config ok')
            


            if sn == '40150887':


                # self.cameras[i].GevSCPD.SetValue(30000)
                # self.cameras[i].GevSCFTD.SetValue(0)
                # self.cameras[i].GevSCBWR.SetValue(10)
                # self.cameras[i].GevSCBWR.SetValue(3)

                self.cameras[i].Gain.Value=int(self.cam1_detail[0][0])
                if DEBUG:
                    print('expo',self.exposure)
                self.cameras[i].ExposureTime=int(self.cam1_detail[0][1])
                if DEBUG:
                    print(self.cameras[i].ExposureTime())
                    print(self.cameras[i].Width.Value)

                self.cameras[i].Width=int(self.cam1_detail[0][3])
               # print(self.cameras[i].Width.Value)# = int(1921)#self.cam1_detail[0][3])
                self.cameras[i].Height = int(self.cam1_detail[0][4])
                if DEBUG:
                    print('camera confi ok')
            
            else:
                self.cameras[i].GevSCPD.SetValue(35000)
                self.cameras[i].GevSCFTD.SetValue(0)
                


            self.cameras[i].StartGrabbing()


    def stop_grabbing(self):
        for i in range( len( self.cameras)):
            #grabResult.Release()

            self.cameras[i].Close()

            
        
    def listDevices(self):
        """Lists the available devices
        
        """
        serial_list=[]
        device_info=[]
        if self.cameras!=NULL:
            for i ,  camera in enumerate(self.cameras):
                device_info = camera.GetDeviceInfo()
                if DEBUG:
                    print(
                        "Camera #%d %s @ %s (%s) @ %s" % (
                        i,
                        device_info.GetModelName(),
                        device_info.GetIpAddress(),
                        device_info.GetMacAddress(),
                        device_info.GetSerialNumber(),
                        )
                    
                    )
                serial_list.append(device_info.GetSerialNumber())
                if DEBUG:
                    print(device_info)
        else:
            print('no device')
        return serial_list
    def serialnumber(self):
        serial_list=[]
        for i ,  camera in enumerate(self.cameras):
            device_info = camera.GetDeviceInfo()
            serial_list.append(device_info.GetSerialNumber())
        return serial_list         


    def setExposure(self , exposure):
        """Sets exposure of the images

        Args:
            exposure (float, optional)
        """
        self.exposure = exposure

    def setGain(self, gain):
        """Sets gain of the images

        Args:
            gain (int, optional)
        """
        self.gain = gain

    def setBufferNumber(self, max_buffer):
        """Set Maximum buffer number for the cameras.

        Args:
            max_buffer (int, optional): Maximum buffer number.
        """
        self.max_buffer = max_buffer
    def cameras2(self):
        print(self.cameras)


    def getPictures(self, time_out = 5000):
        x=time.time()
        # print(x)
        """Retrives pictures from cameras.

        Args:
            camera_number (int): Camera Number.
            num_grab_images (int, optional): How many images should be retrived from the camera. Defaults to 1.
            time_out (int, optional): Time-out of the grabber. Defaults to 5000.

        Returns:
           list: A list of np.arrays for each retrived image.
        """


 

        #print(f'Using camera #{camera_number + 1}, {camera.GetDeviceInfo().GetModelName()} , on {camera.GetDeviceInfo().GetIpAddress()}')
        
        converter = pylon.ImageFormatConverter()

        # converting to opencv bgr format
        converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        imgs = {}
        for camera in self.cameras:
            #continue
            time.sleep(0.1)
            camera.TriggerSoftware()
            # camera.AcquisitionFrameRate.SetValue(160)
        if DEBUG:
            print('TRIGE Done')
        for camera in self.cameras:
            if camera.IsGrabbing():
                if DEBUG:
                    print('Is grabbing')
                grabResult = camera.RetrieveResult(time_out, pylon.TimeoutHandling_ThrowException)
                
                if DEBUG:
                    print('RetrieveResult')


                if grabResult.GrabSucceeded():
                    
                    if DEBUG:
                        print('Grab Succed')

                    image = converter.Convert(grabResult)
                    # img = image.GetArray()
                    # image = converter.Convert(grabResult)
                    imgs[camera.GetDeviceInfo().GetSerialNumber()]=image.Array
                    # decompressed_image = self.decompressor.DecompressImage(grabResult)
                    # print(decompressed_image)
                    # decompressed_array = decompressed_image.Array
                    # print(decompressed_array)
                    

                else:
                    imgs[camera.GetDeviceInfo().GetSerialNumber()]=np.zeros([1200,1920,3],dtype=np.uint8)
                    # print(imgs[camera.GetDeviceInfo().GetSerialNumber()])
                    self.cont_eror+=1
                    print('eror',self.cont_eror)
                    print("Error: ", grabResult.ErrorCode, grabResult.ErrorDescription)
            else:
                    print('erpr')
                    imgs[camera.GetDeviceInfo().GetSerialNumber()]=np.zeros([1200,1920,3],dtype=np.uint8)

            grabResult.Release()

            #camera.Close()

        z=time.time()
        # print(z-x)
        return imgs

    def get_names(self):
        mylist=[]
        try:

            # Get the transport layer factory.
            tlFactory = pylon.TlFactory.GetInstance()

            # Get all attached devices and exit application if no device is found.
            devices = tlFactory.EnumerateDevices()
            
            tl_factory = pylon.TlFactory.GetInstance()
            devices = tl_factory.EnumerateDevices()
            for device in devices:
            #  print(device.GetFriendlyName())
                mylist.append(device.GetFriendlyName())
        #  print(mylist)
            mylist=[x for x in mylist if "Emulation" not in x]
            # print(len(mylist))
        # my_finallist = [i for j, i in enumerate(mylist) if i not in mylist[:j]] 
        #  print(mylist)
            
            if len(mylist) == 0:
                mylist.append('No camera present.')
                raise pylon.RuntimeException("No camera present.")
            return mylist   
        except:
        # print('problem')
            mylist.append('prblem')
            return mylist  


    def get_cam(self,i):
        return self.cameras[i]
    
    def set_size(self):
        for camera in self.cameras:
            print('camera')

    def extract_cmas_data(self):
        details_list=[]
        conn = sqlite3.connect('settings.db')
        cur = conn.cursor()       
        cur.execute('select * from camera1')
        self.cam1_detail = cur.fetchall()
        details_list.append(self.cam1_detail)
        print(self.cam1_detail[0][0])

        cur.execute('select * from camera2')
        self.cam2_detail = cur.fetchall()
        details_list.append(self.cam2_detail)
        print(self.cam2_detail)

        cur.execute('select * from camera3')
        self.cam3_detail = cur.fetchall()
        details_list.append(self.cam1_detail)
        print(self.cam3_detail)

        cur.execute('select * from camera4')
        self.cam4_detail = cur.fetchall()
        details_list.append(self.cam4_detail)
        
        print(self.cam4_detail)
        conn.commit()
        conn.close()    

        return 

if __name__ == '__main__':
    collector = Collector(exposure=10000 , gain=30)
    collector.extract_cmas_data()
    collector.start_grabbing()
    print(collector.get_names())
    # b = collector.get_cam(1)
    # c = collector.get_cam(2)
    # a = collector.get_cam(0)

    collector.listDevices()
    # print(collector.cameras[0].GetDeviceInfo().GetIpAddress())
    while True:
        t=time.time()
        imgs = collector.getPictures()
        t2=time.time()
        print(t2-t)        
        
        print('-'*100)
        # if len(imgs)<=1:
            # continue
        # imgs = next(camera_grabber)
        # cv2.imshow('window', imgs['40150886'])
        # cv2.waitKey(10)

