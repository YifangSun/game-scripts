# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linear_sum_assignment
from pymouse import PyMouse
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import time

test_name = '4_test.png'

############ capture windows ############
hwnd = win32gui.FindWindow(None, '1')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
im = screen.grabWindow(hwnd).toImage()

## Qimage type to numpy
size = im.size()
s = im.bits().asstring(size.width() * size.height() * im.depth() // 8)  # format 0xffRRGGBB
arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), im.depth() // 8))
arr = arr[36:756,1:1281,0:3]

# imgs = Image.fromarray(arr)
# imgs.save("2_test.png")

data_temp = Image.open('3.png')
data_2 = np.array(data_temp)
data_2 = data_2[134:719,218:1059,1]
zeros = np.zeros((256,841))
data_2 =  np.concatenate((data_2,zeros),axis=0)

# test_temp = Image.open(test_name)
# test_2 = np.array(test_temp)
test_2 = arr
test_2 = test_2[134:719,218:1059,1]
zeros = np.zeros((256,841))
test_2 =  np.concatenate((test_2,zeros),axis=0)

## cut round area
masking_round = np.zeros((841,841))
# i->行 j->列
for i in range(841):
    for j in range(841):
        dis = np.sqrt(pow(i-419,2)+pow(j-419,2))
        if (dis>=142.8) and (dis<=420.5):
            masking_round[j,i] = 1
        else:
            masking_round[j,i] = 0
data_2 = data_2 * masking_round
test_2 = test_2 * masking_round

# plt.figure()
# show = Image.fromarray(test_2)
# plt.imshow(show)
# plt.show()
## rotate argument
N = 10
left_angle = 170
angle_space = 160 / N
show_range = [left_angle-2*angle_space+1, left_angle-angle_space-1]
tan_bigger = np.abs(np.tan(show_range[0]/180*np.pi))
tan_lower = np.abs(np.tan(show_range[1]/180*np.pi))

masking_sector = masking_round
for i in range(420):
    for j in range(420):
        tann = (420-j)/(420-i)
        if (tann>tan_bigger) or (tann<tan_lower):
            masking_sector[j,i] = 0

for i in range(420):
    masking_sector[i+420,:] = 0

for i in range(420):
    masking_sector[:,i+420] = 0

############ get sector slice ############
gray2white = 30

data_im = Image.fromarray(data_2)
data_slice = np.zeros((420,420,N))
for n in range(N):
    data_rotate = data_im.rotate(angle_space*(n-1))
    data_array = np.array(data_rotate)
    if(n%2==1):
        data_array = data_array + gray2white
    data_array = data_array * masking_sector
    data_slice[:,:,n] = data_array[0:420,0:420]

test_im = Image.fromarray(test_2)
test_slice = np.zeros((420,420,N))
for n in range(N): 
    test_rotate = test_im.rotate(angle_space*(n-1))
    test_array = np.array(test_rotate)
    test_array = test_array * masking_sector
    if(n%2==1):
        test_array = test_array + gray2white
    test_array = test_array * masking_sector
    test_slice[:,:,n] = test_array[0:420,0:420]

# plt.figure()
# show1 = np.concatenate((test_slice[:,:,3],data_slice[:,:,4]),axis=0)
# show = Image.fromarray(show1)
# plt.imshow(show)
# plt.show()

# im1 = Image.fromarray(test_slice[:,:,14])
# plt.hist(test_slice[:,:,14], 256, [0, 256])
# plt.show()


diff=np.zeros((N,N))

for n in range(N):
    for m in range(N):
        cha = data_slice[:,:,n] - test_slice[:,:,m]
        cha = np.abs(cha)
        cha = cha.sum()
        diff[m,n] = cha
    
r, c = linear_sum_assignment(diff)

# print(r,c)
# test_show = Image.fromarray(test_slice[:,:,9])
# plt.imshow(test_show)
# plt.show()

############ calculate move ############
move = [0,1,2,3,4,5,6,7,8,9]

for i in range(N):
    idx = np.argsort(c)
    if(c[i]!=i):
        t = c[i]
        c[i] = c[idx[i]]
        c[idx[i]] = t
        move[i] = idx[i]
    else:
        move[i] = -1
print(move)


############ start click ############
# m = PyMouse()

# pos_10 = [[220, 371],[264, 304],[317, 241],[382, 190],[467, 165],
# [545, 160],[629, 198],[694, 252],[750, 314],[790, 377]]

# m.click(pos_10[0][0], pos_10[0][1])
# time.sleep(1)

# def change(num1, num2):
#     m.press(pos_10[num1][0],pos_10[num1][1])
#     time.sleep(0.01)
#     m.press(pos_10[num2][0],pos_10[num2][1])
#     time.sleep(0.77)

# def change_all(move):
#     m.click(100,100)
#     time.sleep(0.009)
#     for i in range(10):
#         if(move[i]!=-1):
#             change(i,move[i])

# change_all(move)