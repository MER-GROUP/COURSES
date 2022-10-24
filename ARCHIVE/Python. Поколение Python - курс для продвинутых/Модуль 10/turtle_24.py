import turtle as t
		
def luch(n, x):
	t.color('green')
	y = x
	size = x
	t.penup()
	t.goto(0, y)
	t.pendown()
	t.color('red')
	t.stamp()
	for i in range(n):
		x -= (size * 2) / n if not 0 == i else ((size * 2) / n) / 2
		t.color('green')
		t.goto(x , 0)
		t.color('blue')
		t.stamp()
		t.color('green')
		t.goto(0, y)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('circle')
	t.speed(10)
	luch(10, 200)
	t.hideturtle()
	t.done()