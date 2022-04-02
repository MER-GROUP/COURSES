def chunke(s, n):
	arr = list()
	for i in range(0, len(s), n):
		arr.append(s[i : i + n])
	print(arr)
	
if __name__ == '__main__':
	chunke(input().split(), int(input()))