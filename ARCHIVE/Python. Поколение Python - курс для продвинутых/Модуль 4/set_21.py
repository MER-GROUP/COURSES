# Операции над множествами
# Объединение множеств: метод union()
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.union(myset2)
print(myset3)

# Объединение множеств: оператор |
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 | myset2
print(myset3)

# Пересечение множеств: метод intersection()
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.intersection(myset2)
print(myset3)

# Пересечение множеств: оператор &
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 & myset2
print(myset3)

# Разность множеств: метод difference()
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.difference(myset2)
print(myset3)

# Разность множеств: оператор -
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 - myset2
print(myset3)

# Разность множеств: метод difference()
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset2.difference(myset1)
print(myset3)

# Симметрическая разность: метод symmetric_difference()
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1.symmetric_difference(myset2)
print(myset3)

# Симметрическая разность: оператор ^
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset3 = myset1 ^ myset2
print(myset3)
#myset1 ^ myset2 == myset2 ^ myset1

# Метод update()
# Метод update() изменяет исходное множество по объединению
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
# изменяем множество myset1
myset1.update(myset2)
print(myset1)

# Метод update(): оператор |=
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1 |= myset2
print(myset1)

# Метод intersection_update()
# Метод intersection_update() изменяет исходное множество по пересечению
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
# изменяем множество myset1
myset1.intersection_update(myset2)
print(myset1)

# Метод intersection_update(): оператор &=
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1 &= myset2
print(myset1)

# Метод difference_update()
# Метод difference_update() изменяет исходное множество по разности
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
# изменяем множество myset1
myset1.difference_update(myset2)
print(myset1)

# Метод difference_update(): оператор -=
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1 -= myset2
print(myset1)

# Метод symmetric_difference_update()
# Метод symmetric_difference_update() изменяет исходное множество по симметрической разности
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
# изменяем множество myset1
myset1.symmetric_difference_update(myset2)
print(myset1)

# Метод symmetric_difference_update(): оператор ^=
print('###################')
myset1 = {1, 2, 3, 4, 5}
myset2 = {3, 4, 6, 7, 8}
myset1 ^= myset2
print(myset1)

# методы принимают не только тип set но и другие итерируемые типы
print('###################')
mylist = [2021, 2020, 2019, 2018, 2017, 2016]
mytuple = (2021, 2020, 2016)
mystr = 'abcd'
myset = {2009, 2010, 2016}
# объединяем со строкой
print(myset.union(mystr))
# пересекаем со списком
print(myset.intersection(mylist))
# находим разность с кортежем
print(myset.difference(mytuple))

# операторы не работают с итерируемыми типами
print('###################')
mylist = [2021, 2020, 2019, 2018, 2017, 2016]
mytuple = (2021, 2020, 2016)
mystr = 'abcd'
myset = {2009, 2010, 2016}
# print(myset | mystr)
# print(myset & mylist)
# print(myset - mytuple)
# TypeError: unsupported operand type(s) for |: 'set' and 'str'
# TypeError: unsupported operand type(s) for &: 'set' and 'list'
# TypeError: unsupported operand type(s) for -: 'set' and 'tuple'

# методы и операторы позволяют совершать операции над несколькими множествами сразу
print('###################')
myset1 = {1, 2, 3, 4, 5, 6}
myset2 = {2, 3, 4, 5}
myset3 = {5, 6, 7, 8}

union1 = myset1.union(myset2, myset3)
union2 = myset1 | myset2 | myset3

difference1 = myset1.difference(myset2, myset3)
# порядок выполнения слева-направо
difference2 = myset1 - myset2 - myset3

print(union1 == union2)
print(difference1 == difference2)

# Оператор ^ симметрической разности позволяет использовать несколько множеств, а метод symmetric_difference() – нет
print('###################')
myset1 = {1, 2, 3, 4, 5, 6}
myset2 = {2, 3, 4, 7}
myset3 = {6, 20, 30}
# порядок выполнения слева-направо
symdifference = myset1 ^ myset2 ^ myset3
print(symdifference)

# Оператор ^ симметрической разности позволяет использовать несколько множеств, а метод symmetric_difference() – нет
myset1 = {1, 2, 3, 4, 5, 6}
myset2 = {2, 3, 4, 7}
myset3 = {6, 20, 30}
# symdifference = myset1.symmetric_difference(myset2, myset3)
# print(symdifference)
# TypeError: symmetric_difference() takes exactly one argument (2 given)