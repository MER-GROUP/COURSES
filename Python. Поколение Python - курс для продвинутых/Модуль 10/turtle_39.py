'''
Напишите программу, которая рисует солнечную систему по образцу.
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
	
def circle(r, bgcolor, pencolor, obj):
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	obj.circle(r)
	obj.end_fill()
	obj.pencolor('black')

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

	# var
	bg_color_arr = []
	x = -280
	y = 0
	delta = 30
	font_size = 10
	radius_arr = [50, 20, 30, 25, 15, 40, 45, 35, 33, 10]
	bg_colors_arr = ['yellow', 
					'orange', 
					'orange' , 
					'green', 
					'red', 
					'orange', 
					'orange', 
					'gray',
					'blue',
					'orange']
	planets = ['Солнце',
				'Меркурий',
				'Венера',
				'Земля',
				'Марс',
				'Юпитер',
				'Сатурн',
				'Уран',
				'Нептун',
				'Плутон']
	steps = list(range(1, 11))

	# algorithm
	goto(x, y, t)
	for radius, bg_color, planet, step in zip(radius_arr, bg_colors_arr, planets, steps):
		goto(int(t.xcor()), int(t.ycor()) - int(radius), t)
		print('x =', t.xcor()) ###
		print('y =', t.ycor()) ###
		circle(radius, bg_color, 'black', t)
		if 7 == step:
			t.stamp()
		goto(int(t.xcor()), int(t.ycor()) - 20, t)
		t.write(planet, move=False, align='center', font=('Time New Roman', font_size, 'normal'))
		goto(int(t.xcor()), int(t.ycor()) + 20, t)
		if delta > radius:
			goto(int(t.xcor()) + int(radius) + int(delta) + 15, y, t)
		else:
			goto(int(t.xcor()) + int(radius) + int(delta) + 25, y, t)

	# pause
	t.done()