words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

def ascii(s):
	arr = list()
	for c in s:
		arr.append(ord(c))
	return arr

result = {i: ascii(i) for i in words}
print(result)