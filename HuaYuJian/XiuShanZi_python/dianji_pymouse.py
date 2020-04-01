from pymouse import PyMouse
import time

m = PyMouse()


def change(num1, num2):
    m.press(pos_16[num1][0],pos_16[num1][1])
    time.sleep(0.01)
    m.press(pos_16[num2][0],pos_16[num2][1])
    time.sleep(0.77)

def change_all(move):
    m.click(100,100)
    time.sleep(0.009)
    for i in range(16):
        if(move[i]!=-1):
            change(i,move[i])

# 178,454  212,345
if __name__ == '__main__':
    m.move(178,454)
    m.press(178,454)
    
    m.move(212,345)
    m.release(212,345)







change_all(move)