import turtle as t
t.speed(8)
for _ in range(8):
  t.pensize(4)
  t.forward(50)
  t.left(45)
t.penup()
t.goto(2.5, 6)
t.pendown()
t.pensize(1)
t.fillcolor('red')
t.begin_fill()
for _ in range(8):
  t.pencolor('red')
  t.forward(45)
  t.left(45)
t.end_fill()
t.goto(25,45)
t.color('white')
t.write('STOP',align='center',font=('Arial',30,'normal'))
t.done()