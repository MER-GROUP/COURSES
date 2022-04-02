x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
x1y1, x2y2 = str(), str()

if 0 != x1 % 2 and 0 != y1 % 2:
	x1y1 = 'white'
elif 0 == x1 % 2 and 0 == y1 % 2:
	x1y1 = 'white'
else:
	x1y1 = 'black'	
	
if 0 != x2 % 2 and 0 != y2 % 2:
	x2y2 = 'white'
elif 0 == x2 % 2 and 0 == y2 % 2:
	x2y2 = 'white'
else:
	x2y2 = 'black'	
	
if x1y1 == x2y2:
	print('YES')
else:
	print('NO')