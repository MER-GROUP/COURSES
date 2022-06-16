import turtle as t
from random import randrange
t.Screen().colormode(255)
t.Screen().bgcolor(10, 10, 40)
t.hideturtle()
t.speed(10)
t.penup()
# рисуем звезды
for _ in range(randrange(100,150)):
  t.pencolor(randrange(0, 50), randrange(0, 100), randrange(100, 255))
  t.goto(randrange(-195, 195), randrange(-115, 195))
  t.dot(randrange(1, 5))
#рисуем дома
for x in range(-200, 200, 40):
  y = randrange(2, 7)
  for i in range(y):
    t.fillcolor('dark blue')
    t.goto(x, i * 40 - 200)
    t.begin_fill()
    for _ in range(4):
      t.forward(41)
      t.left(90)
    t.end_fill()
# рисуем окна
    if randrange(3) == 0: #загорается 1 из 3 окон
      t.fillcolor(randrange(200, 255), randrange(200, 255), randrange(100))
      t.goto(x + 10, i * 40 - 190)
      t.begin_fill()
      for _ in range(4):
        t.forward(20)
        t.left(90)
      t.end_fill()
t.done()