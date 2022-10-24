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
	
def oval_line(r, obj):
	a = r + int(r / 2)
	b = r - int(r / 4)
	dx = obj.xcor()
	dy = obj.ycor()
	for deg in range(361):
		rad = m.radians(deg)
		x = a * m.sin(rad) + dx
		y = -b * m.cos(rad) + b + dy
		obj.goto(x, y)

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
		circle(radius, bg_color, 'black', t)
		if 7 == step:
			# oval(radius + int(radius * 1 / 4), 'white', 'black', t)
			goto(int(t.xcor()), int(t.ycor() + int(radius/ 4)), t)
			oval_line(radius, t)
			goto(int(t.xcor()), int(t.ycor() - int(radius/ 4)), t)
		goto(int(t.xcor()), int(t.ycor()) - 20, t)
		t.write(planet, move=False, align='center', font=('Time New Roman', font_size, 'normal'))
		goto(int(t.xcor()), int(t.ycor()) + 20, t)
		if delta > radius:
			goto(int(t.xcor()) + int(radius) + int(delta) + 15, y, t)
		else:
			goto(int(t.xcor()) + int(radius) + int(delta) + 25, y, t)

	# pause
	t.done()