# Тоже правильное решение
import turtle as tt
import math
from random import randrange as rd

tt.tracer(25)
tt.radians()
tt.hideturtle()
#tt.showturtle()
tt.Screen().colormode(255)
tt.bgcolor('black')

def star_beam(s,l):
    color = (rd(255), rd(255), rd(255))
    tt.color(color)
    n = rd(3, 8)
    a = math.pi - math.acos(s / l)
    b = math.pi - math.asin(s / l)*2
    g = math.pi / n * 2
    for _ in range(n):
        tt.fillcolor(color)
        tt.begin_fill()
        tt.lt(g)
        tt.fd(s)
        tt.lt(a)
        tt.fd(l)
        tt.lt(b)
        tt.fd(l)
        tt.lt(a)
        tt.fd(s)
        tt.end_fill()

def mause1(x,y):
    k = rd(1, 5)
    m = rd(10, 30)
    tt.penup()
    tt.goto(x,y)
    tt.pendown()
    star_beam(k, m)

tt.Screen().onclick(mause1)
tt.Screen().listen()
tt.done()