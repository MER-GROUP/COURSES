'''
iter и next
Вам доступен список numbers, содержащий целые числа. Дополните приведенный ниже 
код с использованием функций iter() и next(), чтобы он вывел четвертый элемент 
данного списка.

numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
'''
numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
nums = iter(numbers)
[next(nums) for _ in range(3)]
print(next(nums))

# print(numbers)
# iter_numbers = iter(numbers)
# [numbers.remove(next(iter_numbers)) for _ in range(3)]
# print(numbers)  # [70, 45, 83, 12, ...]