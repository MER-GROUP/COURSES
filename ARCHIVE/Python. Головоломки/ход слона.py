x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 == x2 and y1 == y2:
	print('NO')
elif abs(x1 - x2) == abs(y1 - y2):
	print('YES')
else:
	print('NO')