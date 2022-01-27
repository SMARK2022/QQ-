import cv2
import time
from functools import wraps
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
from PIL import Image


def timethis(func):  # 函数计时修饰器，暂未用上 用法在def上一行添加"@timethis"
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}ms'.format(func.__module__,
                                    func.__name__, (end - start)*1000))
        return r
    return wrapper


def Out_img_plt(In_imgpath: str):  # 利用matplotlib打开，里面有坐标显示，比较方便
    tmp_Img = mpimg.imread(In_imgpath)
    plt.imshow(tmp_Img)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
    plt.show()


def Out_img_cv2(In_imgpath):  # 利用opencv-python打开，打开速度更快，比较迅速
    start = time.clock()
    img = cv2.imread(In_imgpath)
    cv2.namedWindow("ADB_Img", 0)
    cv2.imshow('ADB_Img', img)
    elapsed = (time.clock() - start)
    key = cv2.waitKey(0)
    return elapsed


# @timethis
def Out_img_PIL(In_imgpath):  # 直接系统默认程序打开图片
    im = Image.open(In_imgpath)
    im.show()


if __name__ == '__main__':
    Out_img_PIL("D:\\LENOVO\\Desktop\\tmp\\ADB\\01.png")
    # cv2.namedWindow("ADB_Img", 0)
    # try:
    #     for i in range(50):
    #         img = cv2.imread("D:\\LENOVO\\Desktop\\tmp\\ADB\\01.png")
    #         cv2.imshow('ADB_Img', img)
    #         cv2.waitKey(200)
    # except KeyboardInterrupt:
    #     print("exit")
