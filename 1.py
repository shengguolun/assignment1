# 导入所需的模块
import turtle
import colorsys

# 创建窗口和画笔
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")  # 设置背景颜色
t.speed(0)  # 设置画笔速度

# 定义颜色变量
n = 36  # 控制颜色的渐变频率
h = 0  # 初始色调

# 开始绘制图案
for i in range(360):
    # 使用色相-饱和度-明度 (HSV) 色彩模式生成颜色
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1 / n
    t.color(c)

    # 旋转和前进以形成图案
    t.left(145)
    for j in range(5):
        t.forward(i * 2)  # 随着循环增加步长
        t.left(150)

# 完成图形保持窗口打开
turtle.done()


