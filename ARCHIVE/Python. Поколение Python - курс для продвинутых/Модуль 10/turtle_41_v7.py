import turtle as t
import random as r
t.hideturtle()
t.speed(10)
t.Screen().bgcolor('midnightblue')
t.penup()

def star(x, y, size):
  t.goto(x, y)
  t.pencolor('yellow')
  t.pensize(size)
  t.dot()

def window():
  t.fillcolor('yellow')
  t.begin_fill()
  for _ in range(4):
    t.forward(15)
    t.right(90)
  t.end_fill()
  
def bild(a, b):
  t.fillcolor('darkblue')
  t.begin_fill()
  for _ in range(2):
    t.forward(a)
    t.left(90)
    t.forward(b)
    t.left(90)
  t.end_fill()
  k=t.pos()
  l=r.randrange(6)
  if l>0:
    for _ in range(l):
      t.goto(r.randrange(int(k[0]+5), int(k[0]+a-20), 20), r.randrange(int(k[1]+30), int(k[1]+b-4), 20))
      window()
    t.goto(k)  
for _ in range(25):
  star(r.randrange(-200, 201), r.randrange(-200, 201), r.randrange(1, 4))
t.goto(-200, -200)
n=0
while n<400:
  a=r.randrange(60, 101)
  b=r.randrange(120, 350)
  bild(a, b)
  t.goto(t.pos()[0]+a, -200)
  n+=a

t.done()