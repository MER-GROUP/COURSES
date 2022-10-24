def pack(s):
	arr = s.split()
	pkg = list()
	start, end = [int()] * 2
	while not end == len(arr):
		if arr[end : end + 1] == arr[end + 1 : end + 2]:
			end += 1
		else:
			end +=1
			pkg.append(arr[start : end])
			start = int(end)
	return pkg
			
	
if __name__ == '__main__':
	print(pack(input()))