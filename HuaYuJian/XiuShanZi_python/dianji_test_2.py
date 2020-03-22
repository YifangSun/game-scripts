from pymouse import PyMouse
import time

m = PyMouse()

pos_10 = [[220, 371],[264, 304],[317, 241],[382, 190],[467, 165],
[545, 160],[629, 198],[694, 252],[750, 314],[790, 377]]

def change(num1, num2):
    m.press(pos_10[num1][0],pos_10[num1][1])
    time.sleep(0.01)
    m.press(pos_10[num2][0],pos_10[num2][1])
    time.sleep(0.77)

def change_all(move):
    m.click(100,100)
    time.sleep(0.009)
    for i in range(10):
        if(move[i]!=-1):
            change(i,move[i])

move = [-1, -1, 5, 6, 5, 7, 8, -1, -1, -1]




change_all(move)

