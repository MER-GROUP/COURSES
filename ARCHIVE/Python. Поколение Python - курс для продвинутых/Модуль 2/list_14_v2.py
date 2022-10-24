def pascal(n):
	arr = [[1]]
	for i in range(n):
		tmp = [1]
		for j in range(1, len(arr[i])):
			tmp += [sum(arr[i][j - 1 : j + 1])]
		tmp += [1]
		arr.append(tmp.copy())
			
	return arr[n]
		
if __name__ == '__main__':
	for i in range(int(input())):
		print(pascal(i))