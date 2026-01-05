import math
from turtle import *

# 定义心形的参数方程（k为弧度值）
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# 画布/画笔基础设置
speed(0)  # 最快绘制速度
bgcolor("black")  # 黑色背景
pensize(2)  # 画笔粗细（让点更明显）
color("#f73448")  # 修正后的红色（6位有效颜色码）
penup()  # 抬起画笔，避免移动时留痕

# 遍历弧度值绘制心形点集（核心修正：用弧度步长，去掉goto(0,0)）
for i in range(1000):
    # 将i转换为弧度（步长0.01，避免角度过大）
    k = i * 0.01
    # 计算心形坐标并缩放（*20放大尺寸）
    x = hearta(k) * 20
    y = heartb(k) * 20
    # 移动到目标坐标，绘制点
    goto(x, y)
    pendown()  # 放下画笔（绘制点）

hideturtle()  # 隐藏画笔箭头
done()  # 保持画布不关闭