x, y = input()
n = 8
board = [['.'] * 8 for _ in range(n)]
x = ord(x) - 97
y = n - int(y)
board[y][x] = 'N'

for i in range(n):
	for j in range(n):
		if 2 == abs(y - i) * abs(x - j):
			board[i][j] = '*'
			
for i in board:
	print(*i)