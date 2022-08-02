import turtle as t
from random import randrange as r

def beam(side):               # рисуем один лучик звезды
   for i in range(3):
      t.left(120)
      t.forward(side)
      
def draw_star(x, y, side):      # рисуем звезду
    t.penup()
    t.goto(x, y)
    t.fillcolor(r(0, 256), r(0, 256), r(0, 256))   # выбор цвета звезды
    t.begin_fill()
    t.left(r(0, 91))            # поворот звезды (чтобы не все смотрели строго вверх)
    n = r(5, 9)                 # выбор количества лучей звезды
    for i in range(n):
        beam(side)
        t.right(360 / n)
        t.forward(side)
    t.end_fill()
    
def left_mouse_click(x, y):  
    draw_star(x, y, r(2, 12))     # 3 аргумент функции - размер одного луча

t.Screen().colormode(255)
t.Screen().bgcolor(2, 13, 44)
t.hideturtle()
t.speed(0)
t.Screen().onclick(left_mouse_click)
t.Screen().listen()
t.done()