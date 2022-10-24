def pack(s):
	arr = s.split()
	res = list()
	for el in arr:
		if res and el in res[-1]:
			res[-1].append(el)
		else:
			res.append([el])
	return res
	
if __name__ == '__main__':
	print(pack(input()))