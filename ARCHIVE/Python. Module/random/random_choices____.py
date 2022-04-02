from random import choices, choice

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(choice(arr))
print(choices(arr))
print(choices(arr, k=4))
print(choices(arr, k=15))