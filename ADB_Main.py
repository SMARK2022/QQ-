from ADBbasic import *

if __name__ == '__main__':
    # 连接设备的话直接在cmd里面敲吧。。懒得直接写了（一般自动连上手机）
    # print(ADB_screen_monitor("/sdcard/ADB01.png",
    #                          "D:\\LENOVO\\Desktop\\tmp\ADB\\ADB01.png", 500))

    for i in range(100):#默认按100次
        ADB_tap(40+randint(-30, 10), 1200+randint(-200, 200))#左边界处按一下
        time.sleep(0.1+0.01*randint(-5, 10))#延时
        ADB_tap(1050+randint(-5, 10), 1200+randint(-200, 200))#右边界处按一下
        time.sleep(0.1+0.01*randint(-5, 10))
