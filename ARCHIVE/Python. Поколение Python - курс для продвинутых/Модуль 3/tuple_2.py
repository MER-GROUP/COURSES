# конвертация кортежа в список
print('####################')
number_tuple = (1, 2, 3, 4, 5)
print(number_tuple)
number_list = list(number_tuple)
print(number_list)

# конвертация списка в кортеж
print('####################')
str_list = ['один', 'два', 'три']
print(str_list)
str_tuple = tuple(str_list)
print(str_tuple)

# создание кортежа на основании строки
print('####################')
text = 'hello python'
print(text)
str_tuple = tuple(text)
print(str_tuple)

# конвертация строки в список и наоборот
print('####################')
s = 'симпотичный'
print(s)
a = list(s)
print(a)
a[4] = 'а'
s = ''.join(a)
print(s)

# конвертация кортежа в список и наоборот
print('####################')
writer = ('Лев Толстой', 1827)
print(writer)
a = list(writer)
print(a)
a[1] = 1828
writer = tuple(a)
print(writer)

# функция len() - длина кортежа
print('####################')
numbers = (2, 4, 6, 8, 10)
languages = ('Python', 'C#', 'C++', 'Java')
# выводим длину кортежа numbers
print(len(numbers))
# выводим длину кортежа languages
print(len(languages))
# выводим длину кортежа, состоящего из 3 элементов
print(len(('apple', 'banana', 'cherry')))

# оператор принадлежности in
# оператор in позволяет проверить, содержит ли кортеж некоторый элемент.
print('####################')
numbers = (2, 4, 6, 8, 10)
if 2 in numbers:
    print('Кортеж numbers содержит число 2')
else:
    print('Кортеж numbers не содержит число 2')
    
# оператор принадлежности in и логический оператор not
print('####################')
numbers = (2, 4, 6, 8, 10)
if 0 not in numbers:
    print('Кортеж numbers не содержит нулей')
    
# индексация
print('####################')
numbers = (2, 4, 6, 8, 10)
print(numbers[0])
print(numbers[-1])

# срезы
print('####################')
numbers = (2, 4, 6, 8, 10)
print(numbers[1:3])
print(numbers[2:5])

# операция конкатенации + и умножения на число *
print('####################')
print((1, 2, 3, 4) + (5, 6, 7, 8))
print((7, 8) * 3)
print((0,) * 10)

# расширенные операторы += и *=
print('####################')
a = (1, 2, 3, 4)
b = (7, 8)
# добавляем к кортежу a кортеж b
a += b
# повторяем кортеж b 5 раз 
b *= 5
print(a)
print(b)

# встроенные функции sum()
print('####################')
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('Сумма всех элементов кортежа =', sum(numbers))

# встроенные функции min(), max()
print('####################')
numbers = (3, 4, 10, 3333, 12, -7, -5, 4)
print('Минимальный элемент кортежа =', min(numbers))
print('Максимальный элемент кортежа =', max(numbers))

# метод index()
print('####################')
names = ('Gvido', 'Roman' , 'Timur')
position = names.index('Timur')
print(position)
# обращение к несуществующему значению приводит к ошибке ValueError: tuple.index(x): x not in tuple
# position = names.index('Anders')
# print(position)

# метод index() вместе с оператором принадлежности in
print('####################')
names = ('Gvido', 'Roman' , 'Timur')
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в кортеже')
    
# метод count()
print('####################')
names = ('Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur')
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')
print(cnt1)
print(cnt2)
print(cnt3)

# вложенные кортежи
print('####################')
colors = ('red', ('green', 'blue'), 'yellow')
numbers = (1, 2, (4, (6, 7, 8, 9)), 10, 11)
print(colors[1][1])
print(numbers[2][1][3])