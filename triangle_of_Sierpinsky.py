import turtle

def line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def sierpinski_triangle(age, x1, y1, x2, y2, x3, y3, final_age):
    if age == final_age:
        line(x1, y1, x2, y2)
        line(x2, y2, x3, y3)
        line(x3, y3, x1, y1)
    else:
        xd = (x1 + x2) / 2
        yd = (y1 + y2) / 2
        xe = (x2 + x3) / 2
        ye = (y2 + y3) / 2
        xf = (x1 + x3) / 2
        yf = (y1 + y3) / 2

        sierpinski_triangle(age + 1, x1, y1, xd, yd, xf, yf, final_age)
        sierpinski_triangle(age + 1, xd, yd, x2, y2, xe, ye, final_age)
        sierpinski_triangle(age + 1, xf, yf, xe, ye, x3, y3, final_age)

final_age = int(input("Enter the Fractal Generation: "))

x1, y1 = 10 / 2, 10 / 2
x2, y2 = 320 / 2, 470 / 2
x3, y3 = 630 / 2, 10 / 2

turtle.speed(0)
turtle.bgcolor("white")
turtle.pensize(1)

sierpinski_triangle(0, x1, y1, x2, y2, x3, y3, final_age)

turtle.done()
