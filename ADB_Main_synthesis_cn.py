from ADB_Basic import *

# 连接设备的话直接在cmd里面敲吧。。懒得直接写了（一般自动连上手机）
print("【初始化】本函数文件是团圆饭ADB操作助手，正在运行中...")
print("【初始化】下方是您连接的设备列表，请确认列表中已经有您的设备...")
print(ADB_devices())
print("【初始化】如果未找到您的设备，请连接好ADB后重新运行...")
# print(ADB_screen_monitor("/sdcard/ADB01.png",
#                          "D:\\LENOVO\\Desktop\\tmp\ADB\\ADB01.png", 500))

In_X, In_Y = 0, 0  # 也可以直接设置就不用输入了
if In_X == 0 or In_Y == 0:
    In_X = int(input("【输入】请输入屏幕宽度（像素）："))
    In_Y = int(input("【输入】请输入屏幕高度（像素）："))
In_times = int(input("【输入】请输入点击的循环次数："))
while True:
    print("【系统】循环"+str(In_times)+"次正在运行中，如要终止请按 Ctrl+C")
    try:
        for i in range(In_times):  # 默认按In_times次
            ADB_tap(0+randint(4, 25), int(In_Y/2) +
                    randint(int(-In_Y/4), int(In_Y/4)))  # 左边界处按一下
            time.sleep(0.1+0.01*randint(-5, 10))  # 延时
            ADB_tap(In_X+randint(-25, 4), int(In_Y/2) +
                    randint(int(-In_Y/4), int(In_Y/4)))  # 右边界处按一下
            time.sleep(0.1+0.01*randint(-5, 10))
    except KeyboardInterrupt:
        print("【系统】操作循环已中断...")
    print("【等待】本次循环已执行完毕，如要再来一轮请按任意键...")
    os.system('pause>nul')
