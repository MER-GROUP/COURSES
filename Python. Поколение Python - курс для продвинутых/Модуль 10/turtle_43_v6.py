# Тоже правильное решение
import turtle
from random import randrange
from math import sin, cos, pi, tan 

def rand_color():
  return randrange(256), randrange(256), randrange(256)

def draw_star(x, y, n, size, color, angle):
  gamma = (45*(n-2))/n
  alfa = 360/n
  r = size/2
  b = r*sin(pi*alfa/360)/cos(2*pi*gamma/360)
  turtle.goto(x, y)
  turtle.left(angle)
  turtle.forward(r)
  turtle.left(180 - gamma)
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.pencolor(color)
  for i in range(n):
    turtle.forward(b)
    turtle.right(2*gamma)
    turtle.forward(b)
    turtle.left(180-2*gamma)
  turtle.end_fill()

def star(x, y):
  color = rand_color()
  n = randrange(3, 10)
  size = randrange(10, 40)
  angle = randrange(360)
  draw_star(x, y, n, size, color, angle)

turtle.hideturtle()
turtle.colormode(255)
turtle.penup()
turtle.speed(0)
turtle.Screen().bgcolor('Black')

turtle.Screen().listen()
turtle.Screen().onclick(star)
turtle.done()