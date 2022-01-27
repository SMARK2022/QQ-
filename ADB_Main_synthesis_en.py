from ADB_Basic import *

# 连接设备的话直接在cmd里面敲吧。。懒得直接写了（一般自动连上手机）
print("[Info]The program is an ADB assistant in QQ game: Synthetic reunion dinner")
print("[Info]Here comes the list of the devices connected ,please ensure that your phone is in it...")
print(ADB_devices())
print("[Info]If it's not in the list above, please restart the program after connecting it...")
# print(ADB_screen_monitor("/sdcard/ADB01.png",
#                          "D:\\LENOVO\\Desktop\\tmp\ADB\\ADB01.png", 500))

In_X, In_Y = 0, 0  # 也可以直接设置就不用输入了
if In_X == 0 or In_Y == 0:
    In_X = int(
        input("[Input]Please input the width of your phone screen(pixel): "))
    In_Y = int(
        input("[Input]Please input the height of your phone screen(pixel): "))
In_times = int(input("[Input]Please input the cycle of clicking: "))
while True:
    print("[Info]We'll run "+str(In_times)+" cycles,press Ctrl+C to STOP")
    try:
        for i in range(In_times):  # 默认按In_times次
            ADB_tap(0+randint(4, 25), int(In_Y/2) +
                    randint(int(-In_Y/4), int(In_Y/4)))  # 左边界处按一下
            time.sleep(0.1+0.01*randint(-5, 10))  # 延时
            ADB_tap(In_X+randint(-25, 4), int(In_Y/2) +
                    randint(int(-In_Y/4), int(In_Y/4)))  # 右边界处按一下
            time.sleep(0.1+0.01*randint(-5, 10))
    except KeyboardInterrupt:
        print("[Info]Interrupt now...")
    print("[Input]Finished! If another cycle, press any key to continue...")
    os.system('pause>nul')
