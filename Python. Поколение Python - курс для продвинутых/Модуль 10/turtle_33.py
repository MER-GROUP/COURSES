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
	r = 250
	d = 60
	for i in range(2):
		circle(r, color[i])
		goto_over(t.xcor() + d, t.ycor())
	t.hideturtle()
	t.done()