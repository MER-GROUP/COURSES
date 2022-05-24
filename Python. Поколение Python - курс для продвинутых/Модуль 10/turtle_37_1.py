import turtle as t
import math as m
import random as r

class MyExeption(BaseException):
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
	
def box(length, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for i in range(4):
		obj.forward(length)
		obj.right(90)
	obj.end_fill()
	obj.pencolor('black')

if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# algorithm
	color = int()
	for y in range(250, -250, -100):
		for x in range(-250, 250, 100):
			goto(x, y, t)
			box(100, ['black', 'white'][color % 2], 'black', t)
			color += 1

	# pause
	t.done()