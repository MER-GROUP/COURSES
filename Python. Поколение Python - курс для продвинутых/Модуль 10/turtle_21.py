import turtle as t
		
def spiral(n, s):
	size = s
	size_pen = int(1)
	color = dict(zip([1, 2, 3, 4, 5, 6], ['yellow', 'blue', 'red', 'orange', 'purple', 'green']))
	j = int(1)
	for i in range(n):
		t.color(color[j])
		j = j + 1 if 6 > j else 1
		t.forward(size)
		t.left(45)
		size += 5
		size_pen += 1
		t.pensize(size_pen)
	
if __name__ == '__main__':
	t.showturtle()
	t.shape('turtle')
	t.speed(10)
	spiral(45, 10)
	t.hideturtle()
	t.done()