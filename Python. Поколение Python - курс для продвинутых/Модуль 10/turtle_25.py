import turtle as t
		
def luch(r):
	color = ['lightblue', 'yellow', 'black', 'lightgreen', 'red']
	t.penup()
	size = 5
	t.pensize(size)
	x = (-2 * r) - (1 * size)
	y = 0
	t.goto(x, y)
	t.pendown()
	for i in range(5):
		t.color(color[i])
		t.circle(r)
		# x += (2 * r) + (1 * size)
		# x += (1 * r) + (1 * size)
		x += r + size // 2
		y = 0 if i % 2 else -60
		t.penup()
		t.goto(x, y)
		t.pendown()
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(10)
	luch(50)
	t.hideturtle()
	t.done()