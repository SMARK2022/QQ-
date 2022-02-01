#coding=utf-8
import winreg
import re
import msvcrt
import time
from random import randint
import os


DICT_KEYCODE = {"KEYCODE_UNKNOWN": 0, "KEYCODE_MENU": 1, "KEYCODE_SOFT_RIGHT": 2, "KEYCODE_HOME": 3, "KEYCODE_BACK": 4, "KEYCODE_CALL": 5, "KEYCODE_ENDCALL": 6, "KEYCODE_0": 7, "KEYCODE_1": 8, "KEYCODE_2": 9, "KEYCODE_3": 10, "KEYCODE_4": 11, "KEYCODE_5": 12, "KEYCODE_6": 13, "KEYCODE_7": 14, "KEYCODE_8": 15, "KEYCODE_9": 16, "KEYCODE_STAR": 17, "KEYCODE_POUND": 18, "KEYCODE_DPAD_UP": 19, "KEYCODE_DPAD_DOWN": 20, "KEYCODE_DPAD_LEFT": 21, "KEYCODE_DPAD_RIGHT": 22, "KEYCODE_DPAD_CENTER": 23, "KEYCODE_VOLUME_UP": 24, "KEYCODE_VOLUME_DOWN": 25, "KEYCODE_POWER": 26, "KEYCODE_CAMERA": 27, "KEYCODE_CLEAR": 28, "KEYCODE_A": 29, "KEYCODE_B": 30, "KEYCODE_C": 31, "KEYCODE_D": 32, "KEYCODE_E": 33, "KEYCODE_F": 34, "KEYCODE_G": 35, "KEYCODE_H": 36, "KEYCODE_I": 37, "KEYCODE_J": 38, "KEYCODE_K": 39, "KEYCODE_L": 40, "KEYCODE_M": 41, "KEYCODE_N": 42, "KEYCODE_O": 43, "KEYCODE_P": 44,
                "KEYCODE_Q": 45, "KEYCODE_R": 46, "KEYCODE_S": 47, "KEYCODE_T": 48, "KEYCODE_U": 49, "KEYCODE_V": 50, "KEYCODE_W": 51, "KEYCODE_X": 52, "KEYCODE_Y": 53, "KEYCODE_Z": 54, "KEYCODE_COMMA": 55, "KEYCODE_PERIOD": 56, "KEYCODE_ALT_LEFT": 57, "KEYCODE_ALT_RIGHT": 58, "KEYCODE_SHIFT_LEFT": 59, "KEYCODE_SHIFT_RIGHT": 60, "KEYCODE_TAB": 61, "KEYCODE_SPACE": 62, "KEYCODE_SYM": 63, "KEYCODE_EXPLORER": 64, "KEYCODE_ENVELOPE": 65, "KEYCODE_ENTER": 66, "KEYCODE_DEL": 67, "KEYCODE_GRAVE": 68, "KEYCODE_MINUS": 69, "KEYCODE_EQUALS": 70, "KEYCODE_LEFT_BRACKET": 71, "KEYCODE_RIGHT_BRACKET": 72, "KEYCODE_BACKSLASH": 73, "KEYCODE_SEMICOLON": 74, "KEYCODE_APOSTROPHE": 75, "KEYCODE_SLASH": 76, "KEYCODE_AT": 77, "KEYCODE_NUM": 78, "KEYCODE_HEADSETHOOK": 79, "KEYCODE_FOCUS": 80, "KEYCODE_PLUS": 81, "KEYCODE_MENU": 82, "KEYCODE_NOTIFICATION": 83, "KEYCODE_SEARCH": 84, "TAG_LAST_KEYCODE": 85}


def get_desktop():
  key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                        r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
  return winreg.QueryValueEx(key, "Desktop")[0]

def Command(In_command):  # 支持返回的command执行
    tmp_r = os.popen(In_command)
    tmp_text = tmp_r.read()
    tmp_r.close()
    return tmp_text


def ADB_screen_size():
    '获取手机屏幕大小'
    size_str = Command('adb shell wm size')
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return (m.group(2), m.group(1))
    return (0,0)

def ADB_devices_re():  # 显示ADBdevices（非列表）re后缀为有返回值
    return Command("adb devices")


def ADB_tap(In_x: int, In_y: int):  # 模拟点击操作 无返回值
    os.system("adb shell input tap "+str(In_x)+" "+str(In_y))


def ADB_key(In_keycode: int):  # 模拟按键
    os.system("adb shell input keyevent "+str(In_keycode))


def ADB_swipe(In_startX: int, In_startY: int, In_endX: int, In_endY: int, In_timems: int):  # 模拟滑动
    os.system("adb shell input swipe "+str(In_startX)+" " +
              str(In_startY)+" "+str(In_endX)+" "+str(In_endY)+" "+str(In_timems))


# from Output_Basic import *  # 本操作可注释掉 (不需要显示的话，以下均可注释)
# import threading
# # 本函数可注释掉
# def ADB_tap_re(In_x: int, In_y: int):  # 模拟点击操作 re为有返回值
#     return Command("adb shell input tap "+str(In_x)+" "+str(In_y))

# # 本函数可注释掉


# def ADB_key_re(In_keycode: int):  # 模拟按键
#     return Command("adb shell input keyevent "+str(In_keycode))

# # 本函数可注释掉


# def ADB_swipe_re(In_startX: int, In_startY: int, In_endX: int, In_endY: int, In_timems: int):  # 模拟滑动
#     return Command("adb shell input swipe "+str(In_startX)+" " +
#                    str(In_startY)+" "+str(In_endX)+" "+str(In_endY)+" "+str(In_timems))

# # 本函数可注释掉


# def ADB_text(In_text: str):  # 发送文本
#     return Command("adb shell input "+In_text)

# # 本函数可注释掉
# TMP_flash = False  # 是否刷新
# def Img_cv2_monitor(In_imgpath: str, In_delayms: int = 1000, In_Windowtitle: str = "ADB_Img"):  # 必须已经有图像进行初始化
#     cv2.namedWindow(In_Windowtitle, 0)  # 此处有别于使用Output库的方式（因为需要持续输出显示）
#     global TMP_flash
#     try:
#         while True:
#             if TMP_flash:
#                 img = cv2.imread(In_imgpath)
#                 cv2.imshow(In_Windowtitle, img)
#                 TMP_flash = False
#             cv2.waitKey(In_delayms)
#     except KeyboardInterrupt:
#         return "Stop Now..."

# # 本函数可注释掉


# def ADB_screen_show(In_phonepath: str = "/sdcard/ADB01.png", In_pcpath: str = "D:\\ADB01.png"):  # 显示屏幕
#     Command("adb shell screencap -p "+In_phonepath)
#     tmp = Command("adb pull \""+In_phonepath+"\" \""+In_pcpath+"\"")
#     Out_img_cv2(In_pcpath)
#     return tmp


# # 本函数可注释掉
# # 监视屏幕，因长时间显示图片，所以用了threading+opencv显示，但是还是速度一般。。希望有大佬指教
# def ADB_screen_monitor(In_phonepath: str = "/sdcard/ADB01.png", In_pcpath: str = "D:\\ADB01.png", In_delayms: int = 1000):
#     tmp_cv2 = threading.Thread(
#         target=Img_cv2_monitor, args=(In_pcpath, In_delayms))
#     tmp_cv2.start()
#     global TMP_flash
#     try:
#         while True:
#             if TMP_flash == False:
#                 Command("adb shell screencap -p "+In_phonepath)
#                 Command("adb pull \""+In_phonepath+"\" \""+In_pcpath+"\"")
#                 TMP_flash = True
#                 time.sleep(In_delayms/1000)
#     except KeyboardInterrupt:
#         return "Stop Now..."


# if __name__ == '__main__':
#     # 连接设备的话直接在cmd里面敲吧。。懒得直接写了（一般自动连上手机）
#     print(ADB_screen_monitor("/sdcard/ADB01.png",
#                              "D:\\LENOVO\\Desktop\\tmp\ADB\\ADB01.png", 500))

#     # for i in range(100):
#     #     ADB_tap(40+randint(-30,10),1200+randint(-200,200))
#     #     time.sleep(0.1+0.01*randint(-5, 10))
#     #     ADB_tap(1050+randint(-5, 10), 1200+randint(-200, 200))
#     #     time.sleep(0.1+0.01*randint(-5, 10))
