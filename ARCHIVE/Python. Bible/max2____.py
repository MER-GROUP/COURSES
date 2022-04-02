from random import randint
arr = [randint(-10, 10) for i in range(10)]
print(arr)
largest = max(i for i in arr)
print(largest)