from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

hwnd = win32gui.FindWindow(None, '1')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
im = screen.grabWindow(hwnd).toImage()
# im.save('screenshot.png')
# im.load("screenshot.png")
# img = Image.open('screenshot.png')

############### 直接转array例程 ###############
size = im.size()
# print(size,im.depth())
s = im.bits().asstring(size.width() * size.height() * im.depth() // 8)  # format 0xffRRGGBB
arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), im.depth() // 8))
# print(arr.shape)
arr = arr[36:756,1:1281,0:3]

img = Image.fromarray(arr)
img.save("5.png")
# plt.imshow(img)
# plt.show()

# 存了再读大概350ms，直接转array 28-38ms,图片是红蓝反相
# mfc截图存了再读大概40ms
# 暂时弃用