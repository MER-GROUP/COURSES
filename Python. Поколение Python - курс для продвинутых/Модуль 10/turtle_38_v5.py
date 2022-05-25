from turtle import *
hideturtle()
circle(30)
penup()
goto(xcor(), ycor() + 30)
setheading(90)
for p in ["Север", "Восток", "Юг", "Запад"]:
  pendown()
  forward(100)
  penup()
  forward(5)
  if p in 'СеверЮг':
    write(p, align='center', font=('Times New Roman', 12, 'normal'))
  elif p == 'Восток':
    write(p, font=('Times New Roman', 12, 'normal'))
  elif p == 'Запад':
    write(p, align='right', font=('Times New Roman', 12, 'normal'))
  backward(105)
  right(90)
done()