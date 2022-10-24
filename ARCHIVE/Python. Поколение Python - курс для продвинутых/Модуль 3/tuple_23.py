# упаковка кортежей - присваивание его какой-либо переменной
print('####################')
tuple1 = (1, 2, 3)
tuple2 = ('b',)
tuple3 = ('red', 'green', 'blue', 'cyan')
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

# упаковка кортежей
print('####################')
tuple1 = 1, 2, 3
tuple2 = 'b',
print(type(tuple1))
print(type(tuple2))

# распаковка кортежей - присвоение значения элементов кортежа отдельным переменным
print('####################')
colors = ('red', 'green', 'blue', 'cyan')
(a, b, c, d) = colors
print(a)
print(b)
print(c)
print(d)

# распаковка кортежей
print('####################')
colors = ('red', 'green', 'blue', 'cyan')
a, b, c, d = colors
print(a)
print(b)
print(c)
print(d)

# colors = ('red', 'green', 'blue', 'cyan')
# a, b = colors
# ValueError: too many values to unpack

# colors = ('red', 'green', 'blue')
# a, b, c, d = colors
# ValueError: not enough values to unpack (expected 4, got 3)

# распаковка кортежей
print('####################')
colors = ('red', 'green', 'blue')
a, b, _ = colors
print(a)
print(b)

# распаковка кортежей
print('####################')
a = 7
b = 17
a, b = b, a
print(a, b)

# распаковка кортежей
print('####################')
a, b, c = 3, 2, 1
b, a, c = c, a, b
print(b, c, a)

# сбор несколько значений в одну переменную
print('####################')
a, b, *tail = 1, 2, 3, 4, 5, 6
print(a)
print(b)
print(tail)

# сбор несколько значений в одну переменную
print('####################')
a, b, *tail = 1, 2, 3
print(a)
print(b)
print(tail)

# сбор несколько значений в одну переменную
print('####################')
a, b, *tail = 1, 2
print(a)
print(b)
print(tail)

# сбор несколько значений в одну переменную
print('####################')
*names, surname = ('Стефани', 'Джоанн', 'Анджелина', 'Джерманотта')
print(names)
print(surname)

# сбор несколько значений в одну переменную
print('####################')
singer = ('Freddie', 'Bohemian Rhapsody', 'Killer Queen', 'Love of my life', 'Mercury')
name, *songs, surname = singer
print(name)
print(songs)
print(surname)

# распаковка единственного значения в кортеже
print('####################')
# не распаковка, а просто присвоение
a = 1,
# распаковка
b, = 1,
print(a)
print(b)

# распаковка любой последовательности
print('####################')
info = ['timur', 'beegeek.org']
# распаковка списка
user, domain = info    
print(user)
print(domain)
# распаковка строки
a, b, c, d = 'math'
print(a)
print(b)
print(c)
print(d)

# строковый метод partition()
print('####################')
s1 = 'abc-de'.partition('-')
s2 = 'abc-de'.partition('.')
s3 = 'abc-de-fgh'.partition('-')
print(s1)
print(s2)
print(s3)

# числа фибоначи и кортежи
print('####################')
n = int(input())
f1, f2 = 1, 1
for i in range(n):
    print(f1)
    f1, f2 = f2, f1 + f2