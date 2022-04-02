# Генераторы множеств
print('####################')
# digits = set(int(input()))
# TypeError: 'int' object is not iterable

# создание множества символов
print('####################')
digits = set(input())
print(digits)

# создание множества чисел
print('####################')
digits = set()
for c in input():
    digits.add(int(c))
print(digits)

# генератор множеств
# создание множества чисел
print('####################')
digits = {int(i) for i in input()}
print(digits)

# Создать множество, заполненное квадратами целых чисел от 0 до 9
print('####################')
squares = {i ** 2 for i in range(10)}
print(squares)

# Создать множество, заполненное кубами целых чисел от 10 до 20
print('####################')
cubes = {i ** 3 for i in range(10, 21)}
print(cubes)

# Создать множество, заполненное символами строки
print('####################')
chars = {c for c in 'abcdefg'}
print(chars)

# Условия в генераторе множеств
print('####################')
digits = {int(d) for d in 'abcd12ef78ghj90' if d.isdigit()}
print(digits)