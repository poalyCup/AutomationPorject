import os
import time
import pyautogui as pag
import win32api
import win32con
import win32gui

#为什么要在用之前定义函数啊，奇怪唉
def setWindowToTop():
    # 百度来的，没看懂。。
    # 置顶打开的画图工具，还是永久的那种
    hwnd = win32gui.FindWindow(None, "无标题 - 画图")
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)

def closeExe():
    time.sleep(1)
    os.system("taskkill /F /IM mspaint.exe")

def drawRectangle(position):
    # 暴力写法。。。。
    pag.mouseDown(x=position['x1'], y=position['y1'])
    pag.mouseUp(x=position['x1'], y=position['y2'], duration=0.5)
    pag.mouseDown(x=position['x1'], y=position['y2'])
    pag.mouseUp(x=position['x2'], y=position['y2'], duration=0.5)
    pag.mouseDown(x=position['x2'], y=position['y2'])
    pag.mouseUp(x=position['x2'], y=position['y1'], duration=0.5)
    pag.mouseDown(x=position['x2'], y=position['y1'])
    pag.mouseUp(x=position['x1'], y=position['y1'], duration=0.5)
    time.sleep(1)

# 简单粗暴，直接启动应用
os.startfile(r'C:\WINDOWS\system32\mspaint.exe')
time.sleep(1)
setWindowToTop()  ##不知道为什么打开之后会缩小
time.sleep(1)
# 双击标题栏，全屏
pag.doubleClick(x=1650, y=115, duration=0.5)
# 选中直线
# pag.click(x=404, y=115, duration=0.5) 不好用
# 选择size 8xp
pag.click(x=640, y=155, duration=0.5)
pag.click(x=657, y=322, duration=0.5)
# yellow
pag.click(x=888, y=110, duration=0.5)
position1 = {'x1': 500, 'y1': 500, 'x2': 600, 'y2': 600}
drawRectangle(position1)

# 选择size 3xp
pag.click(x=640, y=155, duration=0.5)
pag.click(x=680, y=240, duration=0.5)
# red
pag.click(x=844, y=110, duration=0.5)
drawRectangle(position1)



closeExe()























# def show(self):
#     # windows handlers<br/>
#     hwnd = self.window.handle
#     win32gui.SetForegroundWindow(hwnd)
#     win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)
#     X11LockScreenWindow.show(self)
# def hide(self):
#     X11LockScreenWindow.hide(self)<br/>
#     # windows handlers<br/>
#     hwnd = self.window.handle
#     win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,win32con.SWP_HIDEWINDOW|win32con.SWP_NOMOVE|win32con.SWP_NOSIZE|win32con.SWP_NOACTIVATE|win32con.SWP_NOOWNERZORDER)
