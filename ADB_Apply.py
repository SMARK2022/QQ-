from xmlrpc.client import Boolean
from ADB_Basic import *
import msvcrt


def App_synthesis(In_X: int, In_Y: int):
    while True:
        try:
            tmp_random1 = randint(int(-In_Y/8), int(In_Y/8))
            tmp_in = int(input("请选择您的模式编号：(1=两侧放置, 2=中央放置, 3=左侧放置): "))
            print("【系统】循环点击正在运行中，如要终止请按 Ctrl+C")
            if(tmp_in == 1):
                while True:
                    ADB_tap(10, In_Y/2 + tmp_random1)  # 左边界处按一下
                    time.sleep(0.15)
                    ADB_tap(In_X-20, In_Y/2 + tmp_random1)  # 右边界处按一下
                    time.sleep(0.15)
            elif(tmp_in == 2):
                ADB_tap(In_X/2+5, In_Y/4 + tmp_random1)  # 中央处按一下
                time.sleep(0.15)
                while True:
                    ADB_tap(In_X/2, In_Y/4 + tmp_random1)  # 中央处按一下
                    time.sleep(0.15)
            elif(tmp_in == 3):
                while True:
                    ADB_tap(10, In_Y/2 + tmp_random1)  # 左边界处按一下
                    time.sleep(0.15)
        except KeyboardInterrupt:
            print("【等待】循环已执行停止，如要继续开始请按任意键(Esc键退出)...")
        if msvcrt.getch() == b'\x1b':  # 操作获取Esc
            return


def App_pull(In_X: int, In_Y: int):
    while True:  # 流星雨下拉（目前速度依然较慢。。）
        try:
            print("【系统】循环下拉正在运行中，如要终止请按 Ctrl+C")
            while True:  # 流星雨下拉（目前速度依然较慢。。）
                ADB_swipe(In_X/2, In_Y/4, In_X/2, In_Y/4*3, 100)
                time.sleep(0.1)
                # print("...")
        except KeyboardInterrupt:
            print("【等待】循环已停止，如要继续下拉请按任意键(Esc键退出)...")
            if msvcrt.getch() == b'\x1b':  # 操作获取Esc
                return


def App_open(In_X: int, In_Y: int):
    while True:
        tmp_in = int(input("请输入您要打开的次数: "))
        print("【系统】循环点击正在运行中，如要终止请按 Ctrl+C")
        try:
            for i in range(tmp_in):
                ADB_tap(In_X/2, In_Y/2)
                time.sleep(2)
                ADB_key(DICT_KEYCODE["KEYCODE_BACK"])
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("【终止】循环已强制停止")
        print("【等待】循环已执行停止，如要继续开始请按任意键(Esc键退出)...")
        if msvcrt.getch() == b'\x1b':  # 操作获取Esc
            return
    # 自动开星星


if __name__ == '__main__':
    App_synthesis(1050, 2400)
