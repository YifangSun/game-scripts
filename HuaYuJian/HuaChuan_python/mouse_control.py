import pyautogui
import time
import random

center_x = 238
center_y = 549

def from_drag_to(x1, y1, x2, y2, aduration=0.7):
    pyautogui.mouseDown(x1, y1)
    pyautogui.moveTo(x2, y2, 0.7)
    pyautogui.mouseUp(x2, y2) 

def move_direction(dx=0, dy=0, duration=0.7):
    from_drag_to(center_x, center_y, center_x + dx, center_y + dy, duration)

def press_shou_ji_bao_qi():
    pyautogui.click(1048,537,duration=0.2)
    time.sleep(5)
    
def press_likai():
    pyautogui.click(217,526,duration=0.2)
    time.sleep(0.2)
    pyautogui.click(805,514,duration=0.2)

def exception():
    dx = random.uniform(-1,1) * 100
    dy = random.uniform(-1,1) * 100
    move_direction(dx, dy, duration=2)

# 178,454  212,345
if __name__ == '__main__':
    # print(pyautogui.position())
    # move_direction(100,-100)
    # pyautogui.moveTo(238,549)
    # pyautogui.dragTo(383,448, 0.7)
    exception()