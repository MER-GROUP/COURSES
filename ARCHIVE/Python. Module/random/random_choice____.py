from random import choice
arr = [4, 6, 8]
for _ in range(5):
	a = choice(arr)
	print(a)
	
print(choice('red alert'))
