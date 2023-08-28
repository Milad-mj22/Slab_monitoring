import argparse
import torch



print(torch.cuda.is_available())

import sys
print(sys.path)
import torch
import os
import time
import numpy as np
t_all=[]
os.system("python detect.py --weights best.pt --img 416 --conf 0.6 --save-txt --source img.png " )

