# список - изменяемый тип данных
print('###################')
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list[0] = 9
my_list[4] = 7
print(my_list)

# кортеж - не изменяемый тип данных
print('###################')
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 9
# my_tuple[4] = 7
print(my_tuple)

# пустой кортеж
print('###################')
empty_tuple = ()
# кортеж из двух чисел
point = (1.5, 6.0)
# кортеж из трех строк
names = ('Timur', 'Ruslan', 'Roman')             # кортеж из 6 элементов разных типов
info = ('Timur', 'Guev', 28, 170, 60, False)
# кортеж из кортежа и списка в переменной
nested_tuple = (('one', 'two'), ['three', 'four'])

# кортеж с одним элементом
print('###################')
my_tuple = (1,)
# <class 'tuple'>
print(type(my_tuple))
# если запятую пропустить, то кортеж создан не будет
my_tuple = (1)
# <class 'int'>
print(type(my_tuple))

# функции всегда возвращают кортеж
print('###################')
def get_powers(num):
    return num**2, num**3, num**4
result = get_powers(5)
print(type(result))
print(result)

# изменять список в кортеже можно
print('###################')
my_tuple = (1, 'python', [1, 2, 3])
print(my_tuple)
my_tuple[2][0] = 100
my_tuple[2].append(17)
print(my_tuple)