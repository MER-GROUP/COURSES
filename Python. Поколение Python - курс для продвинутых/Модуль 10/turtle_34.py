import turtle as t

def goto_over(x, y):
	t.penup()
	t.goto(x, y)
	t.pendown()
	
def circle(r, color):
	t.fillcolor(color)
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	
if __name__ == '__main__':
	t.Screen().bgcolor('blue')
	t.pencolor('blue')
	t.showturtle()
	t.shape('classic')
	t.speed(0)
	color = ('orange', 'blue')
	r1 = 250
	r2 = 100
	d = 3
	x = 325
	y = 250
	circle(r1, color[0])
	goto_over(t.xcor() + x, t.ycor() + y)
	t.left(90)
	circle(r2, color[1])
	while True:
		# goto_over(t.xcor() - d, t.ycor())
		r2 +=5
		circle(r2, color[1])
		if 290 == r2:
			break
	goto_over(0, 0)
	circle(r1, color[0])
	circle(r2, color[1])
	while True:
		pass
	t.hideturtle()
	t.done()