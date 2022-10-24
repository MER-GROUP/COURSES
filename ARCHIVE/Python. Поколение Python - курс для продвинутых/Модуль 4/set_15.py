# Добавление элементов
# Метод add()
print('####################')
# создаем множество
numbers = {1, 1, 2, 3, 5, 8, 3}
print(numbers)
# добавляем число 21 в множество
numbers.add(21)
# добавляем число 34 в множество
numbers.add(34)
print(numbers)

# Метод add()
print('####################')
# создаем пустое множество
numbers = set()
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(1)
print(numbers)

# Метод add()
print('####################')
# создаем пустое множество
numbers = set()
for i in range(10):
    numbers.add(i*i + 1)
print(numbers)

# Удаление элемента
# Метод remove()
# удаляет элемент с генерацией исключения
print('####################')
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.remove(3)
print(numbers)
# KeyError
# numbers.remove(10)
# print(numbers)

# Метод discard()
# удаляет элемент без генерации исключения
print('####################')
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.discard(3)
print(numbers)
# не сгенерирует исключение
numbers.discard(10)
print(numbers)

# Метод pop()
# удаляет и возвращает случайный элемент из множества с генерацией исключения
print('####################')
numbers = {1, 2, 3, 4, 5}
print('до удаления:', numbers)
# удаляет случайный элемент множества, возвращая его
num = numbers.pop()
print('удалённый элемент:', num)
print('после удаления:', numbers)

# Метод clear()
# удаляет все элементы
print('####################')
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.clear()
print(numbers)