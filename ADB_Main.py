#coding=utf-8
from ADB_Apply import *
from ADB_Basic import *
from ADB_Apply_draw import *


# 连接设备的话直接自己在cmd里面敲吧。。懒得直接写了（一般自动连上手机）
print(u"【初始化】本函数文件是团圆饭ADB操作助手，正在运行中...")
print(u"【初始化】下方是您连接的设备列表，请确认列表中已经有您的设备...")
print(ADB_devices_re())
print(u"【初始化】如果未找到您的设备，请连接好ADB后重新运行...")
# print(ADB_screen_monitor(u"/sdcard/ADB01.png",
#                          "D:\\LENOVO\\Desktop\\tmp\ADB\\ADB01.png", 500))

In_X, In_Y = ADB_screen_size()  # 也可以直接设置就不用输入了
if In_X == 0 or In_Y == 0:  # 2340 1080
    In_X = int(input(u"【输入】请输入屏幕宽度（像素）: "))
    In_Y = int(input(u"【输入】请输入屏幕高度（像素）: "))

while True:

    tmp_in = int(input(u"请选择您的操作编号: (1=自动开星星, 2=自动红包雨下拉, 3=自动团圆饭, 4=自动一笔连): "))
    if(tmp_in == 1):
        App_open(In_X, In_Y)
    elif(tmp_in == 2):
        App_pull(In_X, In_Y)
    elif(tmp_in == 3):
        App_synthesis(In_X, In_Y)
    elif(tmp_in == 4):
        Apply_draw()
