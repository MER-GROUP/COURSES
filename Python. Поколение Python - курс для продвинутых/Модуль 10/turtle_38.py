'''
Напишите программу, которая рисует изображение компаса по образцу.
'''
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
	
def circle(r, color, obj):
	obj.fillcolor(color)
	obj.begin_fill()
	obj.circle(r)
	obj.end_fill()

def star(length, angle, obj, bgcolor, pencolor):
	obj.left(angle)
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for i in range(10):
		if 0 == i % 2:
			obj.forward(length)
			obj.left(72)
		else:
			obj.forward(length)
			obj.right(144)
	obj.end_fill()
	obj.pencolor('black')

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
	# test
	# print('length =', length)
	# s = square_polygon(length, count_sides)
	# len_side_polygon(s, count_sides)

def square_polygon(length, count_sides):
	s = round((count_sides * length ** 2) / (4 * m.tan(m.radians(180 / count_sides)))) 
	# test
	# print('s =', s)
	return s

def len_side_polygon(s, count_sides):
	length = round(m.sqrt((s * 4 * m.tan(m.radians(180 / count_sides))) / count_sides))
	# test
	# print('length =', length)
	return length

def box(length, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	for i in range(4):
		obj.forward(length)
		obj.right(90)
	obj.end_fill()
	obj.pencolor('black')

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