x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if 1 == dx and  2 == dy or 1 == dy and  2 == dx:
	print('YES')
else:
	print('NO')