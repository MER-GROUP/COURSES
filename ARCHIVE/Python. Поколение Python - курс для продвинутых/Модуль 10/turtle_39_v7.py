import turtle
turtle.Screen().setup(1000, 200)
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def planet(t, x=0, y=0, r=50, color='yellow', name='Planet', ring=False):
  y = y-r
  x = x-400
  t.up(); t.goto(x, y); t.down()
  t.fillcolor(color)
  t.begin_fill()
  t.circle(r)
  t.end_fill()
  if ring:
    t.up(); t.goto(x, y+r); t.seth(-20)
    t.forward(1.2*r)
    t.seth(30)
    t.down()
    for _ in range(2):
      t.circle(r/4.5, 90)
      t.circle(r*1.7, 90)
    t.seth(0)
  t.up(); t.goto(x, y - 20)
  t.fillcolor('black')
  t.write(name, align='center', font=('arial', 10, 'normal'))
  

params = [
  dict(name='Солнце', x=-10, y=0, r=50, color='yellow'),
  dict(name='Меркурий', x=80, y=10, r=10, color='gold'),
  dict(name='Венера', x=130, y=0, r=20, color='goldenrod'),
  dict(name='Земля', x=180, y=0, r=15, color='limegreen'),
  dict(name='Марс', x=220, y=0, r=11, color='tomato'),
  dict(name='Юпитер', x=280, y=0, r=40, color='orange'),
  dict(name='Сатурн', x=390, y=0, r=40, color='chocolate', ring=True),
  dict(name='Уран', x=490, y=0, r=30, color='skyblue'),
  dict(name='Нептун', x=570, y=0, r=30, color='blue'),
  dict(name='Плутон', x=640, y=0, r=8, color='khaki')
]

for param in params:
  planet(t, **param)

turtle.done()