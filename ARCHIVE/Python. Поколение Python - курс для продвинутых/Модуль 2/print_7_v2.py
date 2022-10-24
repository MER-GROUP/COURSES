num = input()
for idx in range(len(num) - 3, 0, -3):
	#print(idx)
	num = num[:idx] + ',' + num[idx:]
print(num)