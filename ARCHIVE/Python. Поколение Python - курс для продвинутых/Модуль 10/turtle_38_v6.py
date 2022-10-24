import turtle as t
t.hideturtle()
t.speed(0)
l=['Восток','Север','Запад','Юг']
for i in range(4):
  t.forward(100)
  t.penup()
  t.forward(40-(i%2)*20)
  t.write(l[i],align='center',font=('Arial', 12, 'normal'))
  t.backward(140-(i%2)*20)
  t.pendown()
  t.left(90)
t.goto(0,-30)
t.circle(30)
t.done()