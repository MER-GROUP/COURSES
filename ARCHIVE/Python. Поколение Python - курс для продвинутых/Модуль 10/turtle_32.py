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
	t.showturtle()
	t.shape('classic')
	t.speed(0)
	color = ('red', 'orange', 'yellow', 'green', 'lime', 'aqua', 'blue', 'navy', 'purple', 'red')
	r = 250
	d = 25
	for i in range(10):
		circle(r, color[i])
		r -= 50
		goto_over(t.xcor(), t.ycor() + d)
		r += d
	t.hideturtle()
	t.done()