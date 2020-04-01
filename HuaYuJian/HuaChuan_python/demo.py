# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import time
from skimage import transform,data
import mouse_control as mc


############ capture windows ############
test_name = 'test4.png'

def capture_window_to_Qimage(winName = '1'):
    hwnd = win32gui.FindWindow(None, winName)
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    Qimage = screen.grabWindow(hwnd).toImage()
    return Qimage

def Qimage_to_numpy(im):
    # 'Color in output array maybe different from real image'
    size = im.size()
    s = im.bits().asstring(size.width() * size.height() * im.depth() // 8)  # format 0xffRRGGBB
    arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), im.depth() // 8))
    arr = arr[36:756,1:1281,0:3]
    temp = np.copy(arr[:,:,0])
    arr[:,:,0] = arr[:,:,2]
    arr[:,:,2] = temp
    return arr

def find_direction_1(array):
    x_total = 0
    y_total = 0
    n_total = 0
    dst=transform.resize(array, (49, 49))
    for i in range(49): #第几列
        for j in range(49): #第几行
            if(dst[j,i]>0.8):
                x_total += i
                y_total += j
                n_total += 1
    if n_total!=0:
        x = np.floor(x_total / n_total).astype(int)
        y = np.floor(y_total / n_total).astype(int)
        dx = (x - 24) / 24 * 100
        dy = (y - 24) / 24 * 100
        return dx,dy
    else:
        return 0,0

def find_direction_2(array):
    x_total = 0
    y_total = 0
    n_total = 0
    for i in range(array.shape[1]): #第几列
        for j in range(array.shape[0]): #第几行
            if(test_2[j,i]>225):
                x_total += i
                y_total += j
                n_total += 1
    if n_total!=0:
        x = np.floor(x_total / n_total).astype(int)
        y = np.floor(y_total / n_total).astype(int)
        dx = (x - (array.shape[1]/2)) / (array.shape[1]/2) * 100
        dy = (y - (array.shape[0]/2)) / (array.shape[0]/2) * 100
        return dx,dy
    else:
        return 0,0

def find_pictue_in(x, y, winName, filename, diff):
    _pattern = Image.open(filename)
    w = _pattern.size[0]
    h = _pattern.size[1]
    _pattern = np.array(_pattern)[:,:,0]

    picture = capture_window_to_Qimage(winName)
    game_window = Qimage_to_numpy(picture)
    button_area = game_window[y:y+h, x:x+w, 1]
    # plt.imshow(button_area)
    # plt.show()
    temp_diff = np.sum(np.abs(_pattern - button_area))
    if(temp_diff < diff):
        return True
    else:
        return False

def find_pictue_in_2(x, y, winName, filename, diff):
    _pattern = Image.open(filename)
    w = _pattern.size[0]
    h = _pattern.size[1]
    _pattern = np.array(_pattern)[:,:,0]

    picture = capture_window_to_Qimage(winName)
    game_window = Qimage_to_numpy(picture)
    button_area = game_window[y:y+h, x:x+w, 1]
    
    # plt.imshow(button_area)
    # plt.show()
    mid_x = np.floor(w/2).astype(int)
    mid_y = np.floor(h/2).astype(int)
    diff0 = diff_of_block(_pattern[0:mid_y, 0:mid_x], button_area[0:mid_y, 0:mid_x] )
    diff1 = diff_of_block(_pattern[0:mid_y, mid_x:x+w], button_area[0:mid_y, mid_x:x+w] )
    diff2 = diff_of_block(_pattern[mid_y:y+h, 0:mid_x], button_area[mid_y:y+h, 0:mid_x] )
    diff3 = diff_of_block(_pattern[mid_y:y+h, mid_x:x+w], button_area[mid_y:y+h, mid_x:x+w] )
    # print(diff0, diff1, diff2, diff3 )
    return diff0<diff[0] and diff1<diff[1] and diff2<diff[2] and diff3<diff[3]


def diff_of_block(arr1, arr2):
    return np.sum(np.abs(arr1 - arr2))


def could_shou_ji_bao_qi():
    # 66000, 100000, 98000, 44000
    return find_pictue_in_2(1018,475,'1','shou_ji_bao_qi.png',diff=[69000, 100000, 98000, 41500])

def coude_likai():
    return find_pictue_in(156,478,'1','146_478_likai.png',105000)
    # false 672474 677032 411146 341375 423418 313502
    # true 98944



# test_2 = Image.open(test_name)
# test_2 = test_2.crop((569,433,714,578))
# test_2 = np.array(test_2)

# 146_478_likai.png


if __name__ == '__main__':
    # print(could_shou_ji_bao_qi())
    beg = time.time()
    while coude_likai()==False:
        im = capture_window_to_Qimage('2')
        game_window = Qimage_to_numpy(im)
        compass = game_window[433:578,569:714,1] #(145*145)
        dx, dy = find_direction_1(compass)
        mc.move_direction(dx, dy)
        if could_shou_ji_bao_qi():
            mc.press_shou_ji_bao_qi()
        exption = np.random.randint(0,16)
        if exption == 0:
            mc.exception()
        now_time = time.time()
        if now_time-beg>600:
            break

    mc.press_likai()