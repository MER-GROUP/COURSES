# Перебор элементов множества
print('####################')
numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
for num in numbers:
    print(num)
    
# распаковка множества
print('####################')
numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
print(*numbers, sep='\n')

# функция sorted()
print('####################')
numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
sorted_numbers = sorted(numbers)
print(type(sorted_numbers))
print(*sorted_numbers, sep='\n')

# функция sorted() с параметром reverse
print('####################')
numbers = {0, 1, 1, 2, 3, 3, 3, 5, 6, 7, 7}
sortnumbers = sorted(numbers, reverse=True)
print(*sortnumbers, sep='\n')

# Сравнение множеств
print('####################')
myset1 = {1, 2, 3, 3, 3, 3}
myset2 = {2, 1, 3}
myset3 = {1, 2, 3, 4}
print(myset1 == myset2)
print(myset1 == myset3)
print(myset1 != myset3)