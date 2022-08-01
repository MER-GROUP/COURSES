from turtle import *
from math import *

Screen().setup(500, 500), speed(0), pencolor('red'), fillcolor('red')
t = 0
begin_fill()
while t < pi * 2:
    t += 1/100
    x = 128 * sin(t) ** 3
    y = 8 * (13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t) - 5)
    goto(x, y)
end_fill()
done()