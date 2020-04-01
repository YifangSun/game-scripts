from pymouse import PyMouse

m = PyMouse()
a = m.position()    #获取当前坐标的位置
print(a)

# m.move(31, 223)   #鼠标移动到(x,y)位置
# a = m.position()
# print(a)
# m.click(555, 555)  #移动并且在(x,y)位置左击
