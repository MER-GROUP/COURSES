import turtle

turtle.pensize(4)
for i in range(5):
  turtle.penup()
  turtle.goto(i * 30, (1 - i % 2) * 25)
  turtle.pencolor(['cyan', 'yellow', 'black', 'light green', 'red'][i])
  turtle.pendown()
  turtle.circle(30)