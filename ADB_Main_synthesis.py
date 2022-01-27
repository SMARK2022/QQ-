from ADB_Basic import *

# 连接设备的话直接在cmd里面敲吧。。懒得直接写了（一般自动连上手机）
print(ADB_devices())
# print(ADB_screen_monitor("/sdcard/ADB01.png",
#                          "D:\\LENOVO\\Desktop\\tmp\ADB\\ADB01.png", 500))

In_X, In_Y = 0, 0  # 也可以直接设置就不用输入了
if In_X == 0 or In_Y == 0:
    In_X = int(input("请输入屏幕宽度（像素）："))
    In_Y = int(input("请输入屏幕高度（像素）："))
In_times = int(input("请输入点击的循环次数："))
for i in range(In_times):  # 默认按100次
    ADB_tap(40+randint(-30, 10), In_Y/2+randint(-In_Y/4, In_Y/4))  # 左边界处按一下
    time.sleep(0.1+0.01*randint(-5, 10))  # 延时
    ADB_tap(1050+randint(-5, 10), In_Y/2+randint(-In_Y/4, In_Y/4))  # 右边界处按一下
    time.sleep(0.1+0.01*randint(-5, 10))
