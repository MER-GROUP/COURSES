import turtle as t
t.speed(0)
t.ht()
t.up()
t.goto(160, 0)
t.write('Восток', align='center', font=('Arial', 12, 'normal'))
t.goto(0, -140)
t.write('Юг', align='center', font=('Arial', 12, 'normal'))
t.goto(-160, 0)
t.write('Запад', align='center', font=('Arial', 12, 'normal'))
t.goto(0, 140)
t.write('Север', align='center', font=('Arial', 12, 'normal'))
t.goto(0, 4)
t.pendown()
for i in range(4):
  t.forward(115)
  t.backward(115)
  t.right(90)
t.up()
t.goto(0, -31)
t.pendown()
t.circle(35)  
t.done()