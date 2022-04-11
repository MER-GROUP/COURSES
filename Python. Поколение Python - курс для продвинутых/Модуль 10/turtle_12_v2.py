from turtle import *
from random import randrange
# максимальная скорость прорисовки 0
speed(0)

def print_figure(i):
  left(180)
  n = 10
  for _ in range(i):
    for _ in range(4):
      forward(n)
      right(90)
    # color(randrange(256), randrange(256), randrange(256))
    n += 1

print_figure(10000)