import autopy
import time
# 178,454  212,345
if __name__ == '__main__':
    autopy.mouse.move(178,454)
    # autopy.mouse.click()
    autopy.mouse.toggle(down = True)
    autopy.mouse.smooth_move(212,345)
    autopy.mouse.toggle(down = False)