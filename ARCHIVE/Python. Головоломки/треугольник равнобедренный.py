# объявление функции
def draw_triangle():
    s = str()
    z = int(1)
    for i in range(8):
    	for j in range(1, 16):
    		s +=' '
    		if 8 == j:
    			dlina = len('*' * z)
    			if 1 == dlina:
    				s = s[ : 8 - 1] + ('*' * z)
    			else:
    				start = 8 - (dlina // 2 + 1)
    				s = s[ : start] + ('*' * z)
    	print(s.rstrip())
    	z += 2
    	s = str()

# основная программа
draw_triangle()  # вызов функции