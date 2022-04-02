import random

arr = [i for i in range(1, 11)]
print(arr)
for _ in range(10):
	random.shuffle(arr)
	print(arr)