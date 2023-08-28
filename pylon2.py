

# from pypylon import pylon
# tl_factory = pylon.TlFactory.GetInstance()
# camera = pylon.InstantCamera()
# camera.Attach(tl_factory.CreateFirstDevice())
# camera.Open()
# camera.StartGrabbing(1)
# # grab = self.camera.RetrieveResult(2000, pylon.TimeoutHandling_Return)
# converter = pylon.ImageFormatConverter()

# import cv2
# def pylon_cam():
#     while camera.IsGrabbing():
#         grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

#         if grabResult.GrabSucceeded():
#             # Access the image data
#             image = converter.Convert(grabResult)
#             img = image.GetArray()
#             cv2.namedWindow('title', cv2.WINDOW_NORMAL)
#             cv2.imshow('title', img)
#             k = cv2.waitKey(1)
#             # return img
#             # if k == 27:
#             #     break
#         grabResult.Release()
        
#     # Releasing the resource    
#     camera.StopGrabbing()


# pylon_cam()



import os

os.environ["PYLON_CAMEMU"] = "3"

from pypylon import genicam
from pypylon import pylon
import sys

# Number of images to be grabbed.
countOfImagesToGrab = 10

# Limits the amount of cameras used for grabbing.
# It is important to manage the available bandwidth when grabbing with multiple cameras.
# This applies, for instance, if two GigE cameras are connected to the same network adapter via a switch.
# To manage the bandwidth, the GevSCPD interpacket delay parameter and the GevSCFTD transmission delay
# parameter can be set for each GigE camera device.
# The "Controlling Packet Transmission Timing with the Interpacket and Frame Transmission Delays on Basler GigE Vision Cameras"
# Application Notes (AW000649xx000)
# provide more information about this topic.
# The bandwidth used by a FireWire camera device can be limited by adjusting the packet size.
maxCamerasToUse = 2

# The exit code of the sample application.
exitCode = 0

def get_names():
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
    #Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
def connection(): 
    tlFactory = pylon.TlFactory.GetInstance()

    # Get all attached devices and exit application if no device is found.
    devices = tlFactory.EnumerateDevices()
    tl_factory = pylon.TlFactory.GetInstance()
    devices = tl_factory.EnumerateDevices()
    cameras = pylon.InstantCameraArray(min(len(devices), maxCamerasToUse))

    l = cameras.GetSize()

    # Create and attach all Pylon Devices.
    for i, cam in enumerate(cameras):
        cam.Attach(tlFactory.CreateDevice(devices[i]))

        # Print the model name of the camera.
    print("Using device ", cam.GetDeviceInfo().GetModelName())

    # Starts grabbing for all cameras starting with index 0. The grabbing
    # is started for one camera after the other. That's why the images of all
    # cameras are not taken at the same time.
    # However, a hardware trigger setup can be used to cause all cameras to grab images synchronously.
    # According to their default configuration, the cameras are
    # set up for free-running continuous acquisition.
    cameras.StartGrabbing()

    # Grab c_countOfImagesToGrab from the cameras.
    for i in range(countOfImagesToGrab):
        if not cameras.IsGrabbing():
            break

        grabResult = cameras.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # When the cameras in the array are created the camera context value
        # is set to the index of the camera in the array.
        # The camera context is a user settable value.
        # This value is attached to each grab result and can be used
        # to determine the camera that produced the grab result.
        cameraContextValue = grabResult.GetCameraContext()

        # Print the index and the model name of the camera.
      #  print("Camera ", cameraContextValue, ": ", cameras[cameraContextValue].GetDeviceInfo().GetModelName())

        # Now, the image data can be processed.
     #   print("GrabSucceeded: ", grabResult.GrabSucceeded())
        print("SizeX: ", grabResult.GetWidth())
        print("SizeY: ", grabResult.GetHeight())
        img = grabResult.GetArray()
        print('img;,',img)
    #    print("Gray value of first pixel: ", img[0, 0])
    
# # except genicam.GenericException as e:
# #     # Error handling
# #     print("An exception occurred.", e.GetDescription())
# #     exitCode = 1

# # Comment the following two lines to disable waiting on exit.
# sys.exit(exitCode)

# print(get_names())
# list=get_names()
# print('list',list)
# connection()


from pypylon import pylon 


import cv2
import numpy as np
def impro(img):
    cv2.namedWindow('1', cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
    cv2.resizeWindow('1', 1080, 720)
    cv2.imshow("1", np.hstack([img, (255-img)]))
    cv2.waitKey(0)





# Pypylon get camera by serial number
def get_camera_by_serial(serial_number):
    # serial_number = '23911196'
    info = None
    for i in pylon.TlFactory.GetInstance().EnumerateDevices():
        if i.GetSerialNumber() == serial_number:
            info = i
            break
    else:
        print('Camera with {} serial number not found'.format(serial_number))

    # VERY IMPORTANT STEP! To use Basler PyPylon OpenCV viewer you have to call .Open() method on you camera
    # print('info;,',info)
    converter = pylon.ImageFormatConverter()
    tl_factory = pylon.TlFactory.GetInstance()
    if info is not None:
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(info))
        camera.Open()
        #camera.Attach(tl_factory.CreateFirstDevice())
        camera.Open()
        camera.StartGrabbing(1)
        while camera.IsGrabbing():
            grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

            if grabResult.GrabSucceeded():
                # Access the image data
                image = converter.Convert(grabResult)
                img = image.GetArray()
                # cv2.namedWindow('title', cv2.WINDOW_NORMAL)
                # cv2.imshow('title', img)
                # k = cv2.waitKey(1)
                return img
                # if k == 27:
                #     break
            grabResult.Release()
        
        # Releasing the resource    
        camera.StopGrabbing()


    # from pypylon_opencv_viewer import BaslerOpenCVViewer
    # viewer = BaslerOpenCVViewer(camera)
    # print(viewer)
    # viewer.set_impro_function(impro, own_window=True)
    # img = viewer.get_image()
    # impro(img)
#viewer.set_configuration(VIEWER_CONFIG_RGB_MATRIX)


if __name__ == "__main__":
    print(get_names())
    get_camera_by_serial('23905934')