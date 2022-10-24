import turtle as t

def square(side):
	angle = int(0)
	for i in range(8):
		angle += 90
		if 4 == i:
			angle += 45
		t.setheading(angle)
		t.heading()
		for _ in range(4):
			t.forward(side)
			t.left(90)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	square(150)
	t.hideturtle()
	t.done()