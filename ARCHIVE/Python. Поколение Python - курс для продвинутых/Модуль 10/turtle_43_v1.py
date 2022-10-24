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

def random_color():
	return r.randrange(256), r.randrange(256), r.randrange(256) 

def draw_poly_star(pencolor, bgcolor, obj):
	import random as ra
	obj.pencolor(pencolor)
	obj.fillcolor(bgcolor)
	obj.begin_fill()
	obj.left(ra.randrange(360))
	R, r = ra.randint(30, 70), ra.randint(5, 20)
	x = int(obj.xcor())
	y = int(obj.ycor())
	pi = m.pi
	i = 1
	n = ra.randint(3, 10)
	while (i<=n*2):
		goto(x+m.cos(i*pi/n)*r, y+m.sin(i*pi/n)*r, obj)
		i=i+1
		goto(x+m.cos(i*pi/n)*R, y+m.sin(i*pi/n)*R, obj)
		i=i+1
	goto(x+m.cos(i*pi/n)*r, y+m.sin(i*pi/n)*r, obj)
	i=i+1
	obj.end_fill()
	obj.pencolor('black')

def left_mouse_click_for_star(x, y):
	goto(x, y, t)
	color = random_color()
	# draw_star(color, color, t)
	draw_poly_star(color, color, t)

if __name__ == '__main__':
	# settings turtle
	# settings(t, 'white', 'black')
	settings(t, 'black', 'white')
	speed(t)

	# over set
	# t.Screen().bgcolor('white')
	# set screen size
	t.Screen().setup(640, 480)

	# var
	pass

	# algorithm
	t.Screen().onclick(left_mouse_click_for_star)
	t.Screen().listen()

	# pause
	t.done()