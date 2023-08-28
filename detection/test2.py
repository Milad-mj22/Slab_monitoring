import os

import models

import numpy as np

import time
import tensorflow as tf
#import torch
#print(torch.cuda.is_available())

cpu = tf.config.experimental.list_physical_devices('CPU')[0]
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
  tf.config.experimental.set_memory_growth(gpu, True)


tf.config.experimental.set_visible_devices(cpu)


model=models.resnet_unet2((416,416,1))




t_all = []

image=np.random.rand(1,416,416,1)
t=time.time()
model.predict(image)


for i in range(100):
    image=np.random.rand(1,416,416,1)
    t=time.time()


    model.predict(image)
    image = 'img.png'
    #os.system("python detect.py --weights best.pt --img 416 --conf 0.6 --save-txt --device 1 --source %s " %image)

    #etect.run(






    t=time.time()-t
    print(t)
    t_all.append(t)
t_all=np.array(t_all)
print(t_all.mean())
#def run(image):

     #os.system("python detect.py --weights best.pt --img 416 --conf 0.6 --save-txt --source %s " %image)
