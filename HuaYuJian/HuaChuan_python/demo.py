# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from pymouse import PyMouse
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import time
from skimage import transform,data

############ capture windows ############
test_name = 'test4.png'

hwnd = win32gui.FindWindow(None, '2')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
im = screen.grabWindow(hwnd).toImage()

## Qimage type to numpy
size = im.size()
s = im.bits().asstring(size.width() * size.height() * im.depth() // 8)  # format 0xffRRGGBB
arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), im.depth() // 8))
arr = arr[36:756,1:1281,0:3]

# test_2 = arr
test_2 = Image.open(test_name)
# test_2 = test_2.crop((569,433,714,578))
test_2 = np.array(test_2)
test_2 = test_2[433:578,569:714,1] #(145*145)

############# 方法一 2ms #############
x_total = 0
y_total = 0
n_total = 0
dst=transform.resize(test_2, (49, 49))
for i in range(49): #第几列
    for j in range(49): #第几行
        if(dst[j,i]>0.8):
            x_total += i
            y_total += j
            n_total += 1
x = np.floor(x_total / n_total).astype(int)
y = np.floor(y_total / n_total).astype(int)
dst[y,x] = 1

############# 方法二  28ms #############
# x_total = 0
# y_total = 0
# n_total = 0
# for i in range(145): #第几列
#     for j in range(145): #第几行
#         if(test_2[j,i]>225):
#             x_total += i
#             y_total += j
#             n_total += 1
# x = np.floor(x_total / n_total).astype(int)
# y = np.floor(y_total / n_total).astype(int)
# test_2[y,x] = 255

# plt.figure()
# plt.imshow(test_2)
# plt.show()

