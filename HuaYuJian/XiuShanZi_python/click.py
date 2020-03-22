#-*-coding:utf-8-*-

import win32api
import time

def click(num1, num2):
    win32api.SetCursorPos([num1,num2])    #为鼠标焦点设定一个位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    time.sleep(1)

click(221,390)
click(221,390)
click(221,390)