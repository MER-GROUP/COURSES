from turtle import *
for i in range(5):
    if 1 < i < 4:
        circle(-30)
    circle(100, 72)
for i in range(5):
    if 1 < i < 4:
        penup(), goto(xcor() + 10 *(-1)**(i%2), ycor() + 10)
        dot(20)
        goto(xcor() - 10 *(-1)**(i%2), ycor() - 10), pendown()
    circle(60, 72)
penup(), sety(ycor() + 25), pendown(), sety(ycor() + 60), circle(10)
done()