# модуль random
# работа с последовательностями

# Метод shuffle()
# Метод shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом.
print('####################')
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

# Метод choice()
# Метод choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент.
print('####################')
import random
print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(('a', 'b', 'c', 'd')))

# Метод sample()
# Метод sample() принимает два обязательных аргумента: первый – список (строка, кортеж, множество), второй – количество случайных элементов. Возвращает список из указанного количества уникальных (имеющих разные индексы) случайных элементов.
print('####################')
import random
numbers = [2, 5, 8, 9, 12]
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))
# Количество случайных элементов не должно превышать длину исходного списка (строки). Следующий код:
print('####################')
import random
numbers = [2, 5, 8, 9, 12]
#print(random.sample(numbers, 6))
# приведет к ошибке:
# ValueError: Sample larger than population or is negative

# Модуль string
# На текущий момент все функции из модуля string переехали в методы строкового типа данных str, однако в модуле string остались удобные константные строки, которые можно использовать при решении задач.
print('####################')
import string
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)