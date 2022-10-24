import turtle as t

def krug(r):
	for i in range(1, r + 1):
		t.circle(i)
		
if __name__ == '__main__':
	t.showturtle()
	t.shape('classic')
	t.speed(0)
	t.circle(85)
	t.circle(150)
	t.penup()
	t.left(90)
	t.forward(35)
	t.pendown()
	t.forward(85)
	t.right(90)
	t.circle(15)
	
	t.penup()
	t.goto(60, 160)
	t.pendown()
	
	# t.shape('circle')
	# t.stamp()
	
	krug(15)
	
	t.penup()
	t.goto(-60, 160)
	t.pendown()
	krug(15)
	
	t.penup()
	t.goto(-130, 250)
	t.pendown()
	t.circle(50)
	
	t.penup()
	t.goto(130, 250)
	t.pendown()
	t.circle(50)
	
	t.hideturtle()
	t.done()