def pascal(n):
	arr = [[1]]
	for i in range(1, n):
		row = [1]
		for j in range(1, i):
			row += [sum(arr[i - 1][j - 1 : j + 1])]
		row += [1]
		arr.append(row.copy())
	for i in arr:
		print(*i)
	
if __name__ == '__main__':
	pascal(int(input()))