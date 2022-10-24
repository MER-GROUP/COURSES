import turtle as t
from random import *
t.Screen().setup(400,400)
t.colormode(255)
t.tracer(10)
  
def z():
  t.penup()
  t.goto(randint(-200,200),randint(-200,200))
  t.pendown()
  zw=(randint(1,255),randint(1,255),randint(1,255))
  r=randint(3,15)
  n=randint(0,360)
  t.left(n)
  t.pencolor(zw)
  t.begin_fill()
  t.fillcolor(zw)
  for i in range(5):
    t.forward(r)
    t.left(144)
    t.forward(r)
    t.right(72)
  t.end_fill()

for i in range(30):
  z()
  
t.done()