from pymouse import PyMouse
import time

m = PyMouse()
m.click(100,100)
time.sleep(1)

m.press(178, 447)
m.press(228,497)
m.release(228,497)