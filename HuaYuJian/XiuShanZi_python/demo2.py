# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import linear_sum_assignment

test_name = '2_test.png'

# img = Image.open('2.png')
# img = img.rotate(16) 

data_temp = Image.open('2.png')
data_2 = np.array(data_temp)
data_2 = data_2[134:719,218:1059,1]
zeros = np.zeros((256,841))
data_2 =  np.concatenate((data_2,zeros),axis=0)
print(data_2.shape)

test_temp = Image.open(test_name)
test_2 = np.array(test_temp)
test_2 = test_2[134:719,218:1059,1]
zeros = np.zeros((256,841))
test_2 =  np.concatenate((test_2,zeros),axis=0)
print(test_2.shape)

# data_temp = imread(path)
# test_2 = data_temp(135:719,219:1059,1)
# test_2 = [test_2; zeros(256,841)]

# i->行 j->列
for i in range(841):
    for j in range(841):
        dis = np.sqrt(pow(i-420,2)+pow(j-420,2))
        if (dis<142.8) or (dis>420.5):
            test_2[i,j] = 0
            data_2[j,i] = 0

## 开始旋转
N = 10
left_angle = 170
angle_space = 160 / N
show_range = [left_angle-angle_space+4.5, left_angle-4.5]
tan_bigger = np.abs(np.tan(show_range[0]/180*np.pi))
tan_lower = np.abs(np.tan(show_range[1]/180*np.pi))

data_slice = np.zeros((420,420,N))
for n in range(N):
    data_im = Image.fromarray(data_2)
    data_rotate = data_im.rotate(angle_space*n)
    data_array = np.array(data_rotate)
    for i in range(420):
        for j in range(420):
            tann = (420-j)/(420-i)
            if (tann>tan_bigger) or (tann<tan_lower):
                data_array[j,i] = 0
    data_slice[:,:,n] = data_array[0:420,0:420]

test_slice = np.zeros((420,420,N))
for n in range(N):
    test_im = Image.fromarray(test_2)
    test_rotate = test_im.rotate(angle_space*n)
    test_array = np.array(test_rotate)
    for i in range(420):
        for j in range(420):
            tann = (420-j)/(420-i)
            if (tann>tan_bigger) or (tann<tan_lower):
                test_array[j,i] = 0
    test_slice[:,:,n] = test_array[0:420,0:420]

# show_a = data_slice[:,:,1] - test_slice[:,:,1]
# print(show_a)
# plt.imshow(show_a)
# plt.show()

diff = np.zeros((N,N))
for n in range(N):
    for m in range(N):
        cha = data_slice[:,:,n] - test_slice[:,:,m]
        cha = np.abs(cha)
        cha = cha.sum()
        diff[n,m] = cha
    
print(diff)
r, c = linear_sum_assignment(diff)
print(r,c)
# test_show = Image.fromarray(test_slice[:,:,9])
# plt.imshow(test_show)
# plt.show()
