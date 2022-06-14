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
	
def polygon(length, count_sides, obj, bgcolor, pencolor):
	length = length
	count_sides = count_sides
	try:
		if 3 > count_sides:
			raise MyExeption
	except (MyExeption):
		count_sides = 3
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	angle_sum = (count_sides - 2) * 180
	angle = 180 - angle_sum / count_sides
	for _ in range(count_sides):
		obj.forward(length)
		obj.right(angle)
	obj.end_fill()
	obj.pencolor('black')

if __name__ == '__main__':
	# settings turtle
	settings(t, 'white', 'black')
	speed(t)

	# var
	pass

	# algorithm
	goto(-50, 100, t)
	polygon(100, 8, t, 'black', 'black')
	goto(int(t.xcor() + 3), int(t.ycor()) - 5, t)
	polygon(95, 8, t, 'white', 'white')
	goto(int(t.xcor() + 3), int(t.ycor()) - 5, t)
	polygon(90, 8, t, 'red', 'red')
	goto(-85, -60, t)
	t.color('white')
	t.write('STOP', move=False, align='left', font=('Time New Roman', 50, 'normal'))

	# pause
	t.done()