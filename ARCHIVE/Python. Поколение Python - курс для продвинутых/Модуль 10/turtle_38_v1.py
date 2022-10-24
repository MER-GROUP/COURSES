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
	
def cross(side, pencolor, obj):
	obj.pencolor(pencolor)
	for _ in range(4):
		obj.forward(side)
		goto(0, 0, obj)
		obj.left(90)

def text(*arr, obj, side):
	font_size = 15
	font_size_part = font_size - 10
	side_part = side // 10
	goto(-side - side_part, -font_size + font_size_part, obj)
	obj.write(arr[0], move=False, align='right', font=('Time New Roman', font_size, 'normal'))
	goto(0, -side - side_part * 2, obj)
	obj.write(arr[1], move=False, align='center', font=('Time New Roman', font_size, 'normal'))
	goto(side + side_part, -font_size + font_size_part, obj)
	obj.write(arr[2], move=False, align='left', font=('Time New Roman', font_size, 'normal'))
	goto(0, side + side_part, obj)
	obj.write(arr[3], move=False, align='center', font=('Time New Roman', font_size, 'normal'))

if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# algorithm
	length = 200
	r = 75
	cross(length, 'black', t)
	goto(0, -r, t)
	t.circle(r)
	text('Запад', 'Юг', 'Восток', 'Север', obj=t, side=length)

	# pause
	t.done()