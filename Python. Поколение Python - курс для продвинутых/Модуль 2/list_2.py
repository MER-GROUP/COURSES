# заполнение списка 10-ю нулями
print('##########')
zeros = [0] * 10
print(len(zeros))

# вывод элементов списка
print('##########')
numbers = [10, 20, 30, 40, 50]
print(numbers[-2])
print(numbers[-4:-1])

# вывод элементов списка
print('##########')
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:5])
print(numbers[:4])
print(numbers[3:])

# вывод элементов списка
print('##########')
numbers = [4, 8, 12, 16, 34, 56, 100]
numbers[1:4] = [20, 24, 28]
print(numbers)

# вывод элементов списка
print('##########')
numbers = [5, 10, 15, 25]
print(numbers[::-2])

# вывод элементов списка
print('##########')
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)

numbers.append(60)
print(numbers)

# вывод элементов списка
print('##########')
numbers = [10, 20, 30, 40, 50]
numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)

# создание копии списка
print('##########')
letters = ['a', 'b', 'c', 'd']

# print(letters.copy.__doc__)
new_list1 = list(letters)
print(new_list1)

new_list2 = letters.copy()
print(new_list2)

# срез возвращает копию
new_list3 = letters[:]
print(new_list3)

# преобразование списка в строку
print('##########')
words = ['Hello', 'Python']
print('-'.join(words))

# удаление элементов списка
print('##########')
numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers)

# вывод элементов списка
# максильный лексиграфически
print('##########')
words = ['xyz', 'zara', 'beegeek']
print(max(words))

# вывод элементов списка
print('##########')
numbers = [1, 2, 3, 4, 5, 6, 7]
new_numbers =  [2 * x for x in numbers]
print(new_numbers)