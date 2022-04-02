from random import sample

arr = [i for i in range(10)]
print(sample(arr, 1))
print(sample(arr, 10))
#print(sample(arr, 11)) #error
print(sample(arr, 3))
print(type(sample(arr, 3)))