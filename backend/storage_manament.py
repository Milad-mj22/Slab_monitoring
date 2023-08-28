from pathlib import Path
import os
import shutil
import threading
def get_files_in_path(dir_path, reverse=False):
    """
    this function is used to get all files in a path, sorted by date (old to new)

    Args:
        dir_path (_type_): _description_
        reverse (bool, optional): a boolean to reverse sorting to new to old. Defaults to False.

    Returns:
        file_paths: list of file pathes
    """

    file_paths = sorted(Path(dir_path).iterdir(), key=os.path.getmtime, reverse=reverse)

    
    return file_paths





# show storage status summary on dashboard, need to bugfix
def get_storage_status(disk_path):
    """
    this function is used to get storage statues of one drive

    Args:
        disk_path (_type_): drive path (in string)

    Returns:
        drive_info: in dict
    """

    # try:
    # print(disk_path)
    # try:
    total, used, free = shutil.disk_usage(disk_path)
    # except :
    #     total, used, free =5,1,1
    # Get the current working directory
    current_working_directory = os.getcwd()[:2]
    # drivename = get_drivename(current_working_directory)
    #
    total = total//(2**30)
    free = free//(2**30)
    used = total - free
    drive_info = {'total': total, 'used': used, 'used_perc': used/total, 'free': free}
    
    # except:
    #     drive_info = {'total': 0, 'used': 0, 'used_perc': 0, 'free': 0}
    
    return drive_info


def manage_space(threshold=0.12,path='none'):
    # print('path',path)
    main_path = path
    drive = str(path).split(':')[0]+':'
    ret = get_storage_status(drive)
    if ret['used_perc']>threshold:
        try:
            path =get_files_in_path(path)
            path = path[0]
            remove_folder(path)
            print('path {} deleted '.format(path))
        except:
            print('eror in delete')
            pass
    
    remove_thread = threading.Timer(5, manage_space,args=(threshold,main_path))
    remove_thread.start()

def remove_folder(path):
    try:
        try:
            shutil.rmtree(path)
        except:
            os.rmdir(path)
    except:
        try:
            os.remove(path)
        except:
            pass



    # if get_storage_status



def create_thread(path,time=180,threshold=0.50):

    remove_thread = threading.Timer(time, manage_space,args=(threshold,path))
    remove_thread.start()



if '__main__'==__name__:

    # x=get_files_in_path('D:/images')
    # print(x[3])
    # ret = get_storage_status('D:')
    # print(ret)
    # manage_space(path='D:\images')
    remove_thread = threading.Timer(5, manage_space,args=(0.10,'D:\images'))
    remove_thread.start()

    # remove_thread = threading.Thread(target=manage_space,args=(0.10,'D:\images'))
    # remove_thread.start()
    