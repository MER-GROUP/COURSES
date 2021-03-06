# Модуль random
# подключение модуля
import random

# Функция randint()
# Функция randint() принимает два обязательных аргумента a и b и возвращает псевдослучайное целое число из отрезка [a; b].
print('####################')
num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)
print(num1)
print(num2)
print('####################')
for _ in range(10):
    print(random.randint(1, 100))
    
# Функция randrange()
# функция randrange() не возвращает саму последовательность чисел. Вместо этого она возвращает случайно выбранное число из последовательности чисел
print('####################')
num = random.randrange(10)
print(num)
print('####################')
num = random.randrange(5, 10)
print(num)
print('####################')
num = random.randrange(0, 101, 10)
print(num)

# Функция random()
# Функция random() возвращает случайное число с плавающей точкой в диапазоне от 0.00.0 до 1.01.0 (исключая 1.01.0).
print('####################')
num = random.random()
print(num)

# Функция uniform()
# Функция uniform() тоже возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон для отбора значений от а до б включительно.
print('####################')
num = random.uniform(1.5, 17.3)
print(num)

# Функция seed()
# начальное значение для гегерации псевдослучайных чисел
print('####################')
# явно устанавливаем начальное значение для генератора случайных чисел
random.seed(17)
for _ in range(10):
    print(random.randint(1, 100))
# Если выполнить код еще раз, получим ту же самую последовательность псевдослучайных чисел

# Примечание 1. Пусть r – случайное число из интервала (0;1). Для того, чтобы перевести такое число в интервал (a;b) можно воспользоваться формулой a + (b-a)⋅r.