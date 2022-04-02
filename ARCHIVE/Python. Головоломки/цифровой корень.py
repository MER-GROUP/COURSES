d = int(input())
d = str(d)
sum = int()
while 1 < len(d):
	for i in d:
		sum += int(i)
	d = str(sum)
	sum = 0
print(d)