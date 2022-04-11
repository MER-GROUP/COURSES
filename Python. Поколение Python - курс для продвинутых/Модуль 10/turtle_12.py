import turtle as t

def box(side):
	t.setheading(90)
	t.heading()
	for _ in range(30):
		for i in range(4):
			t.forward(side)
			t.left(90)
		side += 10
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	box(100)
	t.hideturtle()
	t.done()