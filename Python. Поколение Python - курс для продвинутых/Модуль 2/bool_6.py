# преобразование к типу bool
print('##########')
print(bool('Beegeek'))
print(bool(17))
print(bool(['apple', 'cherry']))
print(bool())
print(bool(''))
print(bool(0))
print(bool([]))

# функция (предикат) возвращающая bool значение
print('##########')
def is_even(num):
    return 0 == num % 2

print(is_even(8))
print(is_even(7))

# isinstance() - проверка соответствия типа объекта какому либо типу данных
print('##########')
print(isinstance(3, int))
print(isinstance(3.5, float))
print(isinstance('Beegeek', str))
print(isinstance([1, 2, 3], list))
print(isinstance(True, bool))

print(isinstance(3.5, int))
print(isinstance('Beegeek', float))

# type() - получение типа в качестве аргумента объекта
print('##########')
print(type(3))
print(type(3.5))
print(type('Beegeek'))
print(type([1, 2, 3]))
print(type(True))