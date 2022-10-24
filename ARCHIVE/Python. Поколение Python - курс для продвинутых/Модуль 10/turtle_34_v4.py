import turtle

turtle.Screen().bgcolor('DarkBlue')
turtle.hideturtle()
turtle.pencolor('orange')
turtle.dot(200)

while True:
  da = turtle.Turtle()
  da.hideturtle()
  da.pencolor('DarkBlue')
  for i in range(200, -201, -1):
    da.penup()
    da.goto(i, 0)
    da.dot(200)
    # da._tracer(8, 0)
    # da._tracer(6, 25)
    da._tracer(6, 0)
    da.clear()
    da.dot(200)