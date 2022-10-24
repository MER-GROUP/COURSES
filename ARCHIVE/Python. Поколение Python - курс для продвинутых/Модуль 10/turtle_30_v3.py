from turtle import *

speed(0)# убираем анимаию

#рисуем прямоугольник с закрашиванием
fillcolor('black')
begin_fill()
for _ in range(2):
  right(90)
  forward(110)
  right(90)
  forward(50)
end_fill()

y = -35 # расположение света на оси у

# рисуем света:)
for i in ['red', 'yellow', 'green']:
  penup()
  goto(-25, y)
  pendown()
  fillcolor(i)
  begin_fill()
  circle(14)
  end_fill()
  y -= 35
  
done()