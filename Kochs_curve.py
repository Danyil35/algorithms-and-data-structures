import turtle
from math import atan2, sqrt, sin, cos, pi

def recursion(i, x1, y1, x2, y2):
    if i == 0:
        turtle.penup()
        turtle.goto(x1, y1)
        turtle.pendown()
        turtle.goto(x2, y2)
        return

    alpha = atan2(y2 - y1, x2 - x1)
    r = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    xa = x1 + r * cos(alpha) / 3
    ya = y1 + r * sin(alpha) / 3

    xc = xa + r * cos(alpha - pi / 3) / 3
    yc = ya + r * sin(alpha - pi / 3) / 3

    xb = x1 + 2 * r * cos(alpha) / 3
    yb = y1 + 2 * r * sin(alpha) / 3

    recursion(i - 1, x1, y1, xa, ya)
    recursion(i - 1, xa, ya, xc, yc)
    recursion(i - 1, xc, yc, xb, yb)
    recursion(i - 1, xb, yb, x2, y2)

turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(2)

recursion(8, 200, 0, -200, 0)

turtle.done()
