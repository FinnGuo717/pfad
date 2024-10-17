import turtle
import random
import time

width = 800
height = 600
n = 1
d_list = []
x_list = []
y_list = []
sx_list = []
sy_list = []
c_list = []

for i in range(n):
    d = random.randint(20, 180)
    d_list.append(d)
    x = random.randint(-width // 2, width // 2)
    y = random.randint(-height // 2, height // 2)
    x_list.append(x)
    y_list.append(y)
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    c = (r, g, b)
    c_list.append(c)

    sx = random.randint(-5, 5)
    sy = random.randint(-5, 5)
    sx_list.append(sx)
    sy_list.append(sy)

def add_ball(x, y):
    d = random.randint(20, 180)
    d_list.append(d)
    x_list.append(x)
    y_list.append(y)
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    c = (r, g, b)
    c_list.append(c)

    sx = random.randint(-5, 5)
    sy = random.randint(-5, 5)
    sx_list.append(sx)
    sy_list.append(sy)

turtle.setup(width, height)
turtle.tracer(0)
turtle.hideturtle()
turtle.up()
turtle.colormode(255)

turtle.onscreenclick(add_ball)

while True:
    turtle.clear()
    for i in range(len(x_list)):
        x_list[i] += sx_list[i]
        y_list[i] += sy_list[i]
        if x_list[i] <= -width // 2 or x_list[i] >= width // 2:
            sx_list[i] = -sx_list[i]
        if y_list[i] <= -height // 2 or y_list[i] >= height // 2:
            sy_list[i] = -sy_list[i]

    for i in range(len(x_list)):
        turtle.goto(x_list[i], y_list[i])
        turtle.dot(d_list[i], c_list[i])
    turtle.update()
    time.sleep(0.01)
