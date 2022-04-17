import turtle as t
		
def spiral(n):
	size = int()
	for i in range(n):
		t.forward(size)
		t.stamp()
		t.right(20)
		size += 2
	
if __name__ == '__main__':
	t.Screen().bgcolor('lightgreen')
	t.showturtle()
	t.shape('turtle')
	t.speed(10)
	t.pensize(5)
	t.penup()
	t.stamp()
	spiral(42)
	t.hideturtle()
	t.done()