'''
Напишите программу, которая рисует изображение сердца по образцу.
'''
import turtle as t
import math as m
import random as r

class MyExeption(Exception):
	pass

def check(obj):
	try:
		obj.Screen()
		obj.colormode()
		return True
	except (AttributeError):
		return False

def settings(obj, bgcolor, pencolor):
	if check(obj):
		obj.Screen().bgcolor(bgcolor)
		obj.colormode(255)
	obj.pencolor(pencolor)
	obj.showturtle()
	obj.shape('classic')
	obj.speed(0)
	obj.hideturtle()

def speed(obj):
	try:
		obj.tracer(8)
	except (AttributeError):
		obj._tracer(8)

def goto(x, y, obj):
	obj.penup()
	obj.goto(x, y)
	obj.pendown()

def heart(obj, bgcolor, pencolor):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for deg in range(360):
		rad = m.radians(deg)
		x = 128*m.sin(rad)**3
		y = 8*(13*m.cos(rad)-5*m.cos(2*rad)-2*m.cos(3*rad)-m.cos(4*rad) - 5)
		obj.goto(x, y)
	obj.end_fill()
	obj.pencolor('black')

if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# over set
	t.Screen().bgcolor('white')
	# set screen size
	t.Screen().setup(640, 480)

	# var
	pass

	# algorithm
	heart(t, 'red', 'red')

	# pause
	t.done()