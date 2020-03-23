# 介绍
## 用到的库
### 必需
	PIL - 读取图片、旋转
	numpy - 数据处理
	PyMouse - 模拟点击
	PyQt5 - 对指定窗口截图
	pywin32 - win32gui获取窗口句柄（handle）

### 非必需
	matplotlib - 编程时测试图片使用
	time - 测试运行时间

## 效果
<img src="https://github.com/YifangSun/my-script-tools/blob/master/HuaYuJian/XiuShanZi_python/example.png">
效果基本上就是这样，最左边的头发没办法区分出来，右边比较明显的图片还是很容易区分的。程序弄完还要手动再补充操作几下。
## 用法
2-3关都是10片扇形，所以都用`demo2.p`。3-4关都是16片扇形，所以都用`demo4.p`。
下面以第二关为例

### 第一，把第这关的原图保存下来

pyqt_jietu.py - line 9:
```
hwnd = win32gui.FindWindow(None, '1') #'1'修改为你的游戏窗口名
```
pyqt_jietu.py - line 26:
```
img.save("5.png") #"5.png" ，第二关修改为2.png，第三关3.png
```
然后执行pyqt_jietu.py，图片就存下来了。

### 第二，运行demo
因为我的模拟器窗口名叫“1”，所以的demo2的line 16:
demo2.py - line 16:
```
hwnd = win32gui.FindWindow(None, '1') #'1'修改为你的游戏窗口名
```
修改就运行`demo2.py`
4-5关对应的是`demo3.py`，记得修改对应的。
### 第三，运行点击程序
第二步执行完会最后输出一个向量，把它粘贴到`dianji_test_2.py`并赋值给move
dianji_test_2.py - line 22:
```
move = [-1, -1, 5, 6, 5, 7, 8, -1, -1, -1]
```
运行。
不要遮挡模拟器窗口！

## 总结
1. PyMouse.click()不管用，反而是PyMouse.press()有用，可能是因为click点击时间太短？
 其实click点游戏里按钮都是正常的，只有这种特殊交互方法才会失灵（还有划船）。
2. 为什么不放在一个文件里呢？试过了，把dianji_test_2写成函数、import dianji_test_2都试过了，只要和demo在同一个文件，点的位置就不对。可能是PyMouse的问题。
3. 准确率低有点低？确实。为了追求速度，比对图片的方法就是直接矩阵相减，再求和。如果对比直方图或者用哈希法可能要准确点，但是有点慢，毕竟图片数量太多，16×16=256个。明天可能再摸索摸索速度问题。毕竟这个脚本就写了两个下午。
