import cv2
from os import listdir
from os.path import splitext
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse


# input arguments
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--imgroot", type=str, default='./data/', help='directory to images')
    parser.add_argument("--surflen", type=int, default=6, help='legth of the surface image')
    parser.add_argument("--dim", type=int, default=0, help='which dim to concate images along')
    
    return parser.parse_args()


def get_surf_img(img, surf_img_last, surf_len, dim=0):
    w, h = img.shape[:2]
            
    if dim == 0:
        surf_img_last = shift_img(surf_img_last, h, dim=0)
        surf_img_last[:,:h] = img
    else:
        surf_img_last = shift_img(surf_img_last, w, dim=1)
        surf_img_last[:w,:] = img
    
    return surf_img_last


def shift_img(surf_img, shift_value, dim=0):
    if dim == 0:
        shift = np.float32([[1, 0, shift_value], [0, 1, 0]])
    else:
        shift = np.float32([[1, 0, 0], [0, 1, shift_value]])
    
    shifted = cv2.warpAffine(surf_img, shift, (surf_img.shape[1], surf_img.shape[0]))
    
    return shifted


if __name__ == '__main__':
    args = get_args()
    
    # get image ids
    ids = [splitext(file)[0] for file in listdir(args.imgroot) if not file.startswith('.')]
    
    # this is for the begining of the program, that no image is yet available
    start = True
    
    for idx in ids:
        # get new image
        img = cv2.imread(os.path.join(args.imgroot, idx+'.tiff'))
        if start:
            start = False
            w, h = img.shape[:2]
            if args.dim == 0:
                surf_img_last = np.zeros((w,h*args.surflen,3)).astype('uint8')           
            else:
                surf_img_last = np.zeros((w*args.surflen,h,3)).astype('uint8')
        
        surf_img_last = get_surf_img(img,
                                     surf_img_last=surf_img_last,
                                     surf_len=args.surflen,
                                     dim=args.dim)
        
        # show surface image
        width = int(surf_img_last.shape[1] / args.surflen)
        height = int(surf_img_last.shape[0] / args.surflen)
        dim = (width, height)
        resized = cv2.resize(surf_img_last, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow('surface image', resized)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        