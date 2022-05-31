import turtle as t
from math import *
t.speed(0)
t.hideturtle()
d=-169
t.up()
t.goto(d,0)
t.down()
zw = ['#ffff66','#ad5a00','#fd5a0A', 'cyan',
'#FF6347','#ad5a00','#ad5a00','#20B2AA', '#4169E1','#ad5a00']
r=[60,20,25,21,17,35,34,29,28,14]
pl=['Солнце','Меркурий','Венера','Земля','Марс','Юпитер','Сатурн','Уран','Нептун','Плутон']
for i in range(10):
  if i==6:
    dx = t.xcor()
    dy = t.ycor()-8.5
    a = 24
    b = 8
  t.pencolor('black')
  t.dot(r[i]+1)
  t.pencolor(zw[i])
  t.dot(r[i])
  t.up()
  t.right(90)
  t.forward(r[i]/2+10)
  t.write(pl[i],align='center')
  d+=r[i]/2+25
  t.goto(d,0)
  t.setheading(0)
t.goto(dx,dy)
t.pencolor('black')
t.pendown()
for deg in range(361):
    rad = radians(deg)
    x = a * sin(rad) + dx
    y = -b * cos(rad) + b + dy
    t.goto(x, y)

t.done()