'''
Всякие примеры
'''
print('##################################')
a = b = c = 0
print(a, b, c)
print(id(a), id(b), id(c))

a, b, c = 0, 0, 0
print(a, b, c)
print(id(a), id(b), id(c))

a = b = c = 999999999
print(a, b, c)
print(id(a), id(b), id(c))

a, b, c = 999999999, 999999999, 999999999
print(a, b, c)
print(id(a), id(b), id(c))

print('##################################')

print('9 % 5 =', 9 % 5)
print('-9 % 5 =', -9 % 5)
print('9 % -5 =', 9 % -5)
print('-9 % -5 =', -9 % -5)
print('-9 % 4 =', -9 % 4)
print('9 % -4 =', 9 % -4)
print('-9 % -4 =', -9 % -4)

print('2 ** 4 =', 2 ** 4)

print('##################################')

# # ввод целого числа
# d = int(input())

# # здесь продолжите программу
# print(abs(d))

print('##################################')

# # ввод целого числа
# d1, d2, d3, d4, d5 = map(int, input().split())

# # здесь продолжите программу
# print(min(d1, d2, d3, d4, d5))

print('##################################')

# # ввод целого числа
# d1, d2, d3, d4, d5 = map(int, input().split())

# # здесь продолжите программу
# print(max(d1, d2, d3, d4, d5))

print('##################################')

# # ввод данных
# a, b = map(int, input().split())

# # здесь продолжите программу
# print(round((a**2 + b**2)**0.5, 2))

print('##################################')

# # ввод данных
# n, k = map(int, input().split())

# # здесь продолжите программу
# import math as mt
# print(int(mt.factorial(n) / (mt.factorial(k) * mt.factorial(n - k))))

print('##################################')

# # ввод данных
# n, m = map(int, input().split())

# # здесь продолжите программу
# print((n + m) // 20 + bool((n + m) % 20))

print('##################################')

# # ввод данных
# x = int(input())

# # здесь продолжите программу
# print(int(500 // (x - (x * 0.1))))

print('##################################')

# a = 7
# b = -4
# c = 3
# print(f'{a} {b} {c}')

print('##################################')

# a = 7
# b = -4
# c = 3
# print(a, b, c, sep='\n')

print('##################################')

# s1 = "Hello"
# s2 = "Balakirev"

# print(s1, end=' ')
# print(s2)

print('##################################')

# # ввод данных
# s1, s2 = map(str.strip, input().split())

# # здесь продолжите программу
# print(f'Word 1: {s1} | Word 2: {s2}')

print('##################################')

# a, b = map(int, input().split())
# print(a**b)

print('##################################')

# a, b = map(float, input().split())
# print(a + b)

print('##################################')

# X, Y = map(int, input().split())
# print(X + Y + 2*X + 4*Y)

print('##################################')

# print(2 * (float(input()) + float(input())))

print('##################################')

# print(round(__import__('math').pi, 3))

print('##################################')

# print(f'Вы ввели число {input()}')
# print(input('Вы ввели число '))
# print( float(input("Вы ввели число ")))

print('##################################')

# print(bool())

print('##################################')

# print(not(int(float(input())) % 3))

print('##################################')

# print(float(input()) * 100 % 100 > 50)

print('##################################')

# a, b = map(int, input().split())
# print(not(a % b))

print('##################################')

# a, b, c = map(int, input().split())
# print(a+b>c and b+c>a and c+a>b)

print('##################################')

# print(
#     0 <= (n:=float(input())) <= 2 
#     or 10 <= n <= 20
# )

print('##################################')

# print(input() + ' ' + input())

print('##################################')

# a, b = map(str, input().split())
# a += ' '
# b += ' '
# print(a*2 + b*3)

print('##################################')

# a, b = map(int, input().split())
# print('Переменная a = ' + str(a) + ', переменная b = ' + str(b))

print('##################################')

# a = input()
# print('Строка: ' + a + '. Длина: ' + str(len(a)))

print('##################################')

# a, b = input().split()
# print(str(a in b), str(a == b), str(a > b), str(a < b))

print('##################################')

# a, b = input().split()
# print('Коды: ' + a + ' = ' + str(ord(a)) +', ' + b + ' = ' + str(ord(b)))

print('##################################')

# s = input()
# print(s[0]+s[-1])

print('##################################')

# s = input()
# print(s[:4])

print('##################################')

# s = input()
# print(s[-3:])

print('##################################')

# s1, s2 = input(), input()
# print(s1[::2], s2[1::2])

print('##################################')

# s = input()
# # print(s[:5][::-1])
# print(input()[4::-1])

print('##################################')

# s1, s2 = input().split()
# print(s1[:len(s2)][1::2] == s2[1::2])

print('##################################')

# print(input().capitalize())

print('##################################')

# print(input().count('-'))

print('##################################')

# print(input().find('ra'))

print('##################################')

# print(input().replace('---', '-').replace('--', '-'))

print('##################################')

# print(*map(lambda x: x.rjust(3, '0'), input().split()), sep='\n')

print('##################################')

# print(len(input().split()))

print('##################################')

# print(input().replace(' ', ';'))

print('##################################')

# print('Тема занятия "спецсимволы"')

print('##################################')

# print('\\'.join(input().split()))

print('##################################')

# print(input().replace(' ', '\'', 1).replace(' ', '\"'))

print('##################################')

# print(r'C:\WINDOWS\System32\drivers\etc\hosts')

print('##################################')

# print('"' + input() + '"')

print('##################################')

# print("Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(input(), input(), input()))

print('##################################')

# print("Габариты: {0} x {1} x {2}".format(*input().split()))

print('##################################')

# print(f'{min(arr:=input().split())} {max(arr)}')

print('##################################')

# print(f'г. {input()}, ул. {input()}, д. {input()}, кв. {input()}')

print('##################################')

# a, b = (float(input()) for _ in range(2))
# print(f'Вы можете получить {int(b // a)}$ за {int(b)} рублей по курсу {a}')

print('##################################')

# print(list(map(int, input().split())))

print('##################################')

# cities = input().split()
# print()

print('##################################')

# cities = input().split()
# print("Москва" in cities)

print('##################################')

# cities = input().split()
# print(cities[-1])
# print((lambda cities=input().split(): cities[~0])())

print('##################################')

# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks), 1))

print('##################################')

# book = [input() for _ in range(4)]
# del book[1]
# book[1] = 'Пушкин'
# book[2] = float(book[2]) * 2
# print(book)

print('##################################')

# print(max(arr:=list(map(int, input().split()))), min(arr), sum(arr))

print('##################################')

# print(*sorted(arr:=list(map(int, input().split())), reverse=True))

print('##################################')

# cities = ["Москва", "Тверь", "Вологда"] + input().split()
# print(*cities)

print('##################################')

# cities = input().split() + ["Москва", "Тверь", "Вологда"]
# print(*cities)

print('##################################')

# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[:3])

print('##################################')

# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[-4:])

print('##################################')

# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[::2])

print('##################################')

# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1::2])

print('##################################')

# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[6:1:-1])

print('##################################')

# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[::-2])

print('##################################')

# arr = list(map(int, input().split()))
# arr.append(arr[0] != arr[-1])
# print(*arr)

print('##################################')

# cities = ["Москва", "Казань", "Ярославль"]
# # cities.insert(1, "Ульяновск")
# # cities[1:1] = str('Ульяновск')
# cities[1:1] = ['Ульяновск']
# print(len(cities))
# print(*cities)

print('##################################')

# arr = list(input())
# arr.remove('+')
# arr.insert(0, '8')
# arr.remove('7')
# arr.remove('-')
# arr.remove('-')
# print(*arr, sep='')

print('##################################')

# arr = input().split()
# print(arr[2], arr[0][0] + '.' + arr[1][0] + '.')

print('##################################')

# arr = list(map(int, input().split()))
# arr.sort()
# print(*arr[:3])

print('##################################')

# arr = list(map(int, input().split()))
# # arr[-1] = 1 == arr[-1] % 2
# arr[-1] = not not arr[-1] % 2
# print(*arr)

print('##################################')

# arr = list(map(int, input().split()))
# print(arr.count(2))

print('##################################')

# arr = list(map(str, input().split()))
# arr.sort()
# arr.pop(0)
# print(*arr)

print('##################################')

# a = [5.4, 6.7, 10.4]
# a.append(list(map(int, input().split())))
# print(a)

print('##################################')

# a = [5.4, 6.7, 10.4]
# a.append(list(map(int, input().split())))
# print(a)

print('##################################')

# a = []
# a.append(input().split())
# a.append(input().split())
# a.append(input().split())
# print(a)

print('##################################')

# a = []
# a.append(list(map(int, input().split())))
# a.append(list(map(int, input().split())))
# a.append(list(map(int, input().split())))
# print(a[0][-1], a[1][-1], a[2][-1])

print('##################################')

# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#     ["Я", "Python", "выучил", "с", "каналом"],
#     ["Балакирев", "что", "раздавал?"]]

# print(input() in sum(t, []))

print('##################################')

# a, b = map(float, input().split())
# print(a if a > b else b)

print('##################################')

# print(
#     'ДА' 
#     if (s:=input().lower()) == s[::-1] 
#     else 
#     'НЕТ'
# )

print('##################################')

# m, n = map(int, input().split())
# if not m % n:
#     print(m // n)
# else:
#     print(f'{m} на {n} нацело не делится')

print('##################################')

# a, b, c = map(int, input().split())
# print('ДА' if c**2 == a**2 + b**2 else 'НЕТ')

print('##################################')

# a = input()[-1]
# if '7' == a:
#     print('ДА')
# else:
#     print('НЕТ')

print('##################################')

# a = input()
# if 't' in a and 'h' in a and 'o' in a:
#     print('ДА')
# else:
#     print('НЕТ')

print('##################################')

# a = input().split()
# if 'Москва' in a:
#     a.remove('Москва')
# print(*a)

print('##################################')

# a, b, c, d = map(int, input().split())

# if (a-2 >= c and b-2 >= d) or (a-2 >= d and b-2 >= c):
#     print('ДА')
# else:
#     print('НЕТ')

print('##################################')

# a = input()

# if sum(map(int, a[:3])) == sum(map(int, a[3:])):
#     print('ДА')
# else:
#     print('НЕТ')

print('##################################')

# a = float(input())

# if (a % 5) <= 3:
#     print('green')
# else:
#     print('red')

print('##################################')

# a = float(input())

# if (a % 5) <= 3:
#     print('green')
# else:
#     print('red')

print('##################################')

# m = '''1. Введение в Python
# 2. Строки и списки
# 3. Условные операторы
# 4. Циклы
# 5. Словари, кортежи и множества
# 6. Выход'''.split('\n')

# # print(m) # test

# n = input()

# if n == m[0][0]:
#     print(m[0])
# elif n == m[1][0]:
#     print(m[1])
# elif n == m[2][0]:
#     print(m[2])
# elif n == m[3][0]:
#     print(m[3])
# elif n == m[4][0]:
#     print(m[4])
# elif n == m[5][0]:
#     print(m[5])

print('##################################')

# a, b, c = map(int, input().split())

# if b >= a <= c:
#     print(a)
# elif a >= b <= c:
#     print(b)
# else:
#     print(c)

print('##################################')

# a = float(input())

# if a <= 60:
#     print(1)
# elif a <= 64:
#     print(2)
# elif a <= 69:
#     print(3)
# else:
#     print(4)

print('##################################')

# a = float(input())

# if a <= 60:
#     print(1)
# elif a <= 64:
#     print(2)
# elif a <= 69:
#     print(3)
# else:
#     print(4)

print('##################################')

# a = int(input())
# arr = 'понедельник, вторник, среда, четверг, пятница, суббота, воскресенье'.split(', ')

# if 1 == a:
#     print(arr[0])
# elif 2 == a:
#     print(arr[1])
# elif 3 == a:
#     print(arr[2])
# elif 4 == a:
#     print(arr[3])
# elif 5 == a:
#     print(arr[4])
# elif 6 == a:
#     print(arr[5])
# elif 7 == a:
#     print(arr[6])

print('##################################')

# a = int(input())
# arr = '31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31'.split(', ')

# if 1 == a:
#     print(arr[0])
# elif 2 == a:
#     print(arr[1])
# elif 3 == a:
#     print(arr[2])
# elif 4 == a:
#     print(arr[3])
# elif 5 == a:
#     print(arr[4])
# elif 6 == a:
#     print(arr[5])
# elif 7 == a:
#     print(arr[6])
# elif 8 == a:
#     print(arr[7])
# elif 9 == a:
#     print(arr[8])
# elif 10 == a:
#     print(arr[9])
# elif 11 == a:
#     print(arr[10])
# elif 12 == a:
#     print(arr[11])

print('##################################')

# m, n = map(int, input().split())
# month = list(map(int, '31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31'.split(', ')))

# _prev, _next, _month_prev, _month_next = (None for _ in range(4))

# if 1 == n:
#     _prev = month[m-2]
#     _month_prev = m-1
# else:
#     _prev = n - 1
#     _month_prev = m

# if month[m-1] == n:
#     _next = 1
#     _month_next = m+1 if 11 >= m else 1
# else:
#     _next = n+1
#     _month_next = m

# print(f'{_month_prev:02}.{_prev:02} {_month_next:02}.{_next:02}')

print('##################################')

# k = int(input())
# arr = 'понедельник, вторник, среда, четверг, пятница, суббота, воскресенье'.split(', ')
# print(arr[(k%7)-1])

print('##################################')

# print(
#     d:= a if (a:=float(input())) >= (b:=float(input())) else b
# )

print('##################################')

# print(
#     msg:= 'кратно 3' if not (a:=float(input())) % 3 else 'не кратно 3'
# )

print('##################################')

# print(
#     msg:= 'палиндром' if (a:=input().lower()) == a[::-1] else 'не палиндром'
# )

print('##################################')

# print(
#     msg:= 'True' if (a:=int(input())) == 1 else 'False'
# )

print('##################################')

# print(
#     msg:= a + 1 if 0 <=(a:=int(input())) < 59 else 0
# )

print('##################################')

# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# arr = map(int, input().split())

# func = lambda x: '#'+x if x in 'дофа' else x

# print(
#     *(func(m[i-1]) for i in arr)
# )

print('##################################')

# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# arr = map(int, input().split())

# func = lambda x: '#'+x if x in 'дофа' else x

# print(
#     *(func(m[i-1]) for i in arr)
# )

print('##################################')

# n, m = map(int, input().split())

# while n <= m:
#     print(n**2, end=' ')
#     n += 1
# print()

print('##################################')

n, m = map(int, input().split())

while n <= m:
    print(n**2, end=' ')
    n += 1
print()

print('##################################')