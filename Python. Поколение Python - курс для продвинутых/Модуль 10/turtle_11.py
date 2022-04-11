import turtle as t

def hexagon(side):
	for i in range(5):
		t.forward(side)
		t.right(144)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	hexagon(100)
	t.hideturtle()
	t.done()