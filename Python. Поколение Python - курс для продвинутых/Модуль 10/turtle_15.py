import turtle as t

def linedot(n, size):
	t.pensize(size)
	for _ in range(n):
		t.dot()
		t.penup()
		t.forward(15)
		t.pendown()
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	linedot(10, 3)
	t.hideturtle()
	t.done()