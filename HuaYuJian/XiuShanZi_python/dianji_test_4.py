from pymouse import PyMouse
import time

m = PyMouse()

pos_16 = [[210, 392],[243,340],[262,294],[297,250],[336,226],
[383,194],[434,170],[485,167],[531,167],[579,199],[630, 199],
[668, 235],[717, 254],[750, 298],[780, 345],[794, 390]]

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

move =[-1, 3, -1, -1, 10, 12, 13, 11, 13, 15, -1, 14, 14, -1, -1, -1]


change_all(move)