d, s = int(input()), input()
for i in s:
	if 'a' <= i <= 'z':
		for j in range(d):
			if 'a' < i:
				i = chr(ord(i) - 1)
			else:
				i = 'z'
	else:
		for j in range(d):
			if 'A' < i:
				i = chr(ord(i) - 1)
			else:
				i = 'Z'
	print(i, end='')