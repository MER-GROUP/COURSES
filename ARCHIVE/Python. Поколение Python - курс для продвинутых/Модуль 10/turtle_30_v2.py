import turtle

turtle.begin_fill()
for i in (60, 160, 60, 160):
  turtle.forward(i)
  turtle.right(90)
turtle.end_fill()

for i in range(3):
  turtle.penup()
  turtle.goto(30, -(i + 1) * 50)
  turtle.fillcolor(['red', 'yellow', 'green'][i])
  turtle.begin_fill()
  turtle.circle(20)
  turtle.end_fill()
  
turtle.done()