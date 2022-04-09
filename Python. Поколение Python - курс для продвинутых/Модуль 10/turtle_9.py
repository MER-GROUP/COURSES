import turtle as t

def hexagon(side):
	for _ in range(10):
		for i in range(4):
			t.forward(side)
			angle = 120 if i % 2 else 60
			t.left(angle)
		t.left(35)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	hexagon(100)
	t.hideturtle()
	t.done()