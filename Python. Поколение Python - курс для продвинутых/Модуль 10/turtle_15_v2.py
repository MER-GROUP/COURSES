import turtle

def circle_stamp():
  turtle.shape('circle')
  for _ in range(5):
    turtle.stamp()
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()
    
circle_stamp()
turtle.done()