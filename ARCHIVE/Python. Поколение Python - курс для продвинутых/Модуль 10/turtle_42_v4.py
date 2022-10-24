from turtle import *
from math import *

pencolor('red')
fillcolor('red')
begin_fill()
for t in range(630):
  t*=0.01
  x = 128*sin(t)**3
  y = 8*(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t) - 5)
  goto(x, y)
end_fill()
done()