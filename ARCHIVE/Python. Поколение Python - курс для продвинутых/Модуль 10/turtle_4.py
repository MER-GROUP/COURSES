import turtle as t

def square(side):
	angle = int(0)
	for _ in range(3):
		angle += 20
		t.setheading(angle)
		t.heading()
		for _ in range(4):
			t.forward(side)
			t.left(90)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	square(150)
	t.hideturtle()
	t.done()