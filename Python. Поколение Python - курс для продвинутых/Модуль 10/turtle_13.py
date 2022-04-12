import turtle as t

def box(side):
	t.setheading(90)
	t.heading()
	for _ in range(24):
		for i in range(2):
			t.forward(side)
			t.left(90)
		side += 10
	t.forward(side)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	box(10)
	t.hideturtle()
	t.done()