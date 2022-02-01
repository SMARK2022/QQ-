#coding=utf-8
import cv2
import numpy as np
import math
from ADB_Basic import *

lowy = 450  # 界定识别的屏幕区域的上边界low和下边界high
highy = 1650


class _pos:  # 定义的点的信息，遍历寻路用

    def __init__(self, circle_x, circle_y, key):
        self.id = key  # 该点的id
        self.posx = circle_x  # 圆心坐标
        self.posy = circle_y
        self.To = []  # 可到达圆心的id集合
        self.numTo = 0
        self.isvisit = False

        return

    def addTo(self, keyto):
        self.numTo += 1
        self.To.append(keyto)
        return


class _analyze:  # 主要类

    def __init__(self, xpath):
        self.path = xpath
        self.posnum = 0
        self.graph = []
        self.table = []  # 创建了表
        self.routine = []  # DFS栈
        self.be_id = 0
        return

    def check_new(self, In_y1: float, In_x1: float, In_y2: float, In_x2: float, In_R: float):#检查两点间是否存在连线
        tmp_distance = math.sqrt((In_x1-In_x2) * (In_x1-In_x2) +
                                 (In_y1-In_y2) * (In_y1-In_y2))  # 根据距离切分点
        m = 0
        # print(In_R, In_x1, In_y1, In_x2, In_y2)
        tmp_dx = (In_x2-In_x1)/tmp_distance
        tmp_dy = (In_y2-In_y1)/tmp_distance
        tmp_sx = In_x1+tmp_dx*In_R
        tmp_sy = In_y1+tmp_dy*In_R
        # print(tmp_dx, tmp_dy, tmp_sx, tmp_sy)
        for i in range(int(tmp_distance-2*In_R)):
            tx = int(tmp_sx+tmp_dx*i)
            ty = int(tmp_sy+tmp_dy*i)
            # print(tx,ty,self.res[tx,ty])
            if self.res[tx, ty] > 0:
                # cv2.circle(self.img, (ty, tx), 2, (255, 0, 255), 10)
                m += 1
        # print('result:'+str(m/(tmp_distance-2*In_R)))
        if m/(tmp_distance-2*In_R) > 0.93:
            # print("---------Find one!---------\n")
            return True
        else:
            # print('---------------------------\n')
            return False

    def load(self):  # 主要处理函数
        self.img = cv2.imread(self.path)  # 读取图像
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)  # 转灰度图用于圆检测
        rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)  # 转hsv图用于颜色提取

        # 霍夫圆查找圆
        circles1 = cv2.HoughCircles(
            gray, cv2.HOUGH_GRADIENT, 1, 60, param1=100, param2=30, minRadius=50, maxRadius=80)
        circles = circles1[0, :, :]
        circles = np.uint16(np.around(circles))
        for i in circles:  # 遍历每个圆心
            if i[1] < lowy or i[1] > highy:  # 不符合边界要求，删去
                continue
            # cv2.circle(self.img, (i[0], i[1]), i[2],
            #            (255, 255, 0), 5)  # 画出每个圆心和半径
            # cv2.circle(self.img, (i[0], i[1]), 2, (255, 0, 255), 10)
            vi = _pos(i[0], i[1], self.posnum)  # 记录到graph(pos集合)中
            radio = i[2] + 6
            self.graph.append(vi)
            self.posnum += 1
        # print(circles)
        # 提取颜色蒙版
        colorLow = np.array([20, 10, 20])  # rgb颜色边界
        colorHigh = np.array([140, 120, 115])
        mask = cv2.inRange(rgb, colorLow, colorHigh)  # 提取颜色区域
        self.res = mask  # 与原图位运算

        oddid = 0
        self.table = np.zeros((self.posnum, self.posnum))
        for vi in self.graph:  # 两两遍历顶点，判断是否有边
            for vj in self.graph:
                if vi.id == vj.id or vi.id in vj.To or vj.id in vi.To:
                    continue
                # print(vi.id, "<--->", vj.id)
                if self.check_new(float(vi.posx), float(vi.posy), float(vj.posx), float(vj.posy), float(radio)):
                    vi.addTo(vj.id)
                    vj.addTo(vi.id)
                    self.table[vi.id][vj.id] = 1
                    self.table[vj.id][vi.id] = 1
                    # cv2.line(self.img, (vi.posx, vi.posy),
                    #          (vj.posx, vj.posy), (255, 0, 0), 10)  # 若有边，画出这条线
        for vi in self.graph:
            if vi.numTo % 2 == 1:
                oddid = vi.id
            # cv2.putText(self.img, str(vi.id), (vi.posx, vi.posy),
            #             cv2.FONT_HERSHEY_COMPLEX, 2.0, (0, 0, 255), 5)
        # print(oddid)
        # print(ana.table)
        self.be_id = oddid
        # cv2.circle(self.img, (self.graph[oddid].posx,
        #   self.graph[oddid].posy), 20, (255, 0, 255), 10,)

        # plt.subplot('121')
        # plt.imshow(self.img[:, :, [2, 1, 0]])
        # plt.subplot('122')
        # plt.imshow(self.res[:, :])
        # # print(radio)
        # plt.show()
        # plt.xticks([]),plt.yticks([])
        # plt.show()

    def dfs(self, j):
        for i in range(self.posnum):  # 挨个寻找与 t 连接的边
            if self.table[i][j] or self.table[j][i]:  # 如果这里有边，while 防止多边连接两点相同
                self.table[i][j] -= 1  # 该边数量减一，代表该边走过了
                self.table[j][i] -= 1  # 无向图
                self.dfs(i)
        self.routine.append(j)  # 回溯时把 t 点放进栈里1


def Apply_draw(IN_tmpdir_with_splash: str = get_desktop()+"\\"):
    while True:
        print(u"【系统】循环点击正在运行中，如要终止请按 Ctrl+C")
        try:
            while True:
                Command("adb shell screencap -p /sdcard/ADB01.png")
                Command("adb pull /sdcard/ADB01.png \"" +
                        IN_tmpdir_with_splash+"ADB01.png\"")
                # 读取图像
                ana = _analyze("\""+IN_tmpdir_with_splash+"ADB01.png\"")
                ana.load()
                ana.dfs(ana.be_id)
                print("【系统】连接顺序: ",ana.routine)
                for i in range(len(ana.routine)-1):
                    # print(ana.graph[ana.routine[i]].id, "-->", ana.graph[ana.routine[i+1]].id, ana.graph[ana.routine[i]].posx, ana.graph[ana.routine[i]].posy,
                    #   ana.graph[ana.routine[i+1]].posx, ana.graph[ana.routine[i+1]].posy)
                    ADB_swipe(ana.graph[ana.routine[i]].posx, ana.graph[ana.routine[i]].posy,
                            ana.graph[ana.routine[i+1]].posx, ana.graph[ana.routine[i+1]].posy, 200)
                    time.sleep(0.15)
                time.sleep(2)
        except KeyboardInterrupt:
            print(u"【终止】循环已强制停止")
        print(u"【等待】循环已执行停止，如要继续开始请按任意键(Esc键退出)...")
        if msvcrt.getch() == b'\x1b':  # 操作获取Esc
            return


