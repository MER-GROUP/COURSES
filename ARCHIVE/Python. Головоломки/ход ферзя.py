x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if x1 == x2 and y1 == y2:
	print('NO')
elif dx == dy or x1 == x2 or y1 == y2:
	print('YES')
else:
	print('NO')