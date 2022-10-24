import turtle as t
import random as r

t.Screen().bgcolor('white')
t.colormode(255)
t.speed(1000)
t.hideturtle()
def star(a, b, x, y):
  t.setheading(b)
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.color(r.randrange(256), r.randrange(256), r.randrange(256))
  t.begin_fill()
  for _ in range(5):
   t.forward(a)
   t.right(144)
  t.end_fill()

count = r.randrange(200)
for _ in range(count):
  a = r.randrange(35)
  b = r.randrange(180)
  x = r.randint(-200, 200)
  y = r.randint(-200, 200)
  star(a, b, x, y)
t.done()