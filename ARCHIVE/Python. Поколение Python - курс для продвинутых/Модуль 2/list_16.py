def chunke(s, n):
	arr = list()
	cnt = int(1)
	for i in s.split():
		if arr and n > cnt:
			cnt += 1
			arr[-1].append(i)
		else:
			arr.append([i])
			cnt = 1
	print(arr)
	
if __name__ == '__main__':
	chunke(input(), int(input()))