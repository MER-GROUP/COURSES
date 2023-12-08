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

# x = float(input())
# i = 2
# while 11 > i:
#     print(round(x * i, 1), end=' ')
#     i += 1
# print()

print('##################################')

# s = 0
# while (n:= int(input())):
#     s += n
# print(s)

print('##################################')

# s = input()
# arr = []
# i = 0
# n = len(s)
# while i < n:
#     if 0 == i:
#         arr.append(s[i])
#     else:
#         if '-' == arr[-1] and '-' == s[i]:
#             pass
#         else:
#             arr.append(s[i])
#     i += 1
# print(''.join(arr))

print('##################################')

# n = int(input())
# m = 1
# while n:
#     m *= (n % 10)
#     n //= 10
# print(m)

print('##################################')

# n = int(input())
# a, b = 1, 1

# while n:
#     print(a, end=' ')
#     a, b = b, (a+b)
#     n -= 1
# print()

print('##################################')

# n = int(input())
# a = 1
# p = 1

# while 0 < n:
#     p *= 2
#     n -= 4
# print(p)

print('##################################')

# n = int(input())
# s = 1000

# while n:
#     s += s * 0.05
#     n -= 1
# print(round(s, 2))

print('##################################')

# n, m = map(int, input().split())

# n += (n%2) == 0
# while n <= m:
#     print(n, end=' ')
#     n += 2
# print()

print('##################################')

# i = 100
# while 1000 > i:
#     if 43 == i % 47 and not i %3:
#         print(i, end=' ')
#     i += 1
# print()

print('##################################')

# i = 100
# while 1000 > i:
#     if 43 == i % 47 and not i %3:
#         print(i, end=' ')
#     i += 1
# print()

print('##################################')

# p = [0] * 10
# c = 0

# while True:
#     i = int(input())
#     if 1 == p[i]:
#         continue
#     elif not 1 == p[i]:
#         c += 1
#         p[i] = 1
#     if 5 == c:
#         break

# print(*p)

print('##################################')

# s = 1

# while n:= int(input()):
#     if 0 > n:
#         continue
#     s *= n

# print(s)

print('##################################')

# arr = input().split()
# i, _len = 0, len(arr)
# while i < _len:
#     if 5 > len(arr[i]):
#         print('НЕТ')
#         break
#     i += 1
# else:
#     print('ДА')

print('##################################')

# arr = input().split()
# i, _len = 0, len(arr)
# while i < _len:
#     if arr[i][0].lower() == arr[i][-1].lower():
#         print('ДА')
#         break
#     i += 1
# else:
#     print('НЕТ')

print('##################################')

# n = int(input())
# i = 1
# while i <= n < 100:
#     if not i % 3 and not i % 5:
#         print(i, end=' ')
#     i += 1
# else:
#     if 100 <= n:
#         print('слишком большое значение n')
#     else:
#         print()

print('##################################')

# n = int(input())
# i = 1
# while i <= n < 100:
#     if not i % 3 and not i % 5:
#         print(i, end=' ')
#     i += 1
# else:
#     if 100 <= n:
#         print('слишком большое значение n')
#     else:
#         print()

print('##################################')

# n = int(input())
# i = 1
# while i <= n and 1 < n:
#     if i**2 > n:
#         print(i)
#         break
#     i += 1
# else:
#     print(2)

print('##################################')

# n = int(input())
# i = 1
# while i <= n and 1 < n:
#     if i**2 > n:
#         print(i)
#         break
#     i += 1
# else:
#     print(2)

print('##################################')

# n = int(input())
# i = 1
# x = 10
# while x <= n:
#     x += x * 0.1
#     i += 1
# print(i)

print('##################################')

# import sys

# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# # здесь продолжайте программу (используйте список lst_in)
# i, _len = 0, len(lst_in)
# while i < _len:
#     if ' ' in lst_in[i]:
#         i += 1
#         continue
#     print(lst_in[i], end=' ')
#     i += 1

print('##################################')

# print(*range(11))

print('##################################')

# print(*range(10, -1, -1))

print('##################################')

# print(*range(10, -1, -1))

print('##################################')

# print(*range(-10, -1, 2))

print('##################################')

# print(*range(1, 20, 3))

print('##################################')

# arr = map(int, input().split())
# s = 0
# for i in arr:
#     if i % 2:
#         s += i
# print(s)

print('##################################')

# arr = input().split()
# for i in arr:
#     print(len(i), end=' ')
# print()

print('##################################')

# n = int(input())
# for i in range(1, n+1):
#     if not n % i:
#         print(i)
# print()

print('##################################')

# n = int(input())
# for i in range(2, int(n**0.5)+1):
#     if not n % i:
#         print('НЕТ')
#         break
# else:
#     print('ДА')

print('##################################')

# n = int(input())
# for i in range(2, int(n**0.5)+1):
#     if not n % i:
#         print('НЕТ')
#         break
# else:
#     print('ДА')

print('##################################')

# # список - использование много раз
# _list = [1, 2, 3]
# print(_list) # [1, 2, 3]
# print(_list) # [1, 2, 3]
# print(_list) # [1, 2, 3]

# # список - использование много раз через распаковку
# # (эта тема еще будет дальше)
# print(*_list) # 1 2 3
# print(*_list) # 1 2 3
# print(*_list) # 1 2 3

# # итератор - создаем итератор 
# _it = iter(_list)

# # выводим ссылку на итератор - т.к. мы выводим ссылку то можно её много раз выводить
# print(_it) # <list_iterator object at 0x7f9ee98ffeb0>
# print(_it) # <list_iterator object at 0x7f9ee98ffeb0>
# print(_it) # <list_iterator object at 0x7f9ee98ffeb0>

# # итератор - использование только раз через распаковку
# # (эта тема еще будет дальше)
# print(*_it) # 1 2 3
# print(*_it) # ничего
# print(*_it) # ничего

# # цикл for когда перебирает итератор он сразу его распаковывает а map и есть итератор
# _map_iterator = map(int, '123')
# print(*_map_iterator) # 1 2 3
# print(*_map_iterator) # ничего
# print(*_map_iterator) # ничего

print('##################################')

# arr = input().lower().split()
# # print(arr) # tests

# prev, curr = None, None
# for i, a in enumerate(arr):
#     if 0 == i:
#         prev = a[-1] if not a[-1] in 'ьъы' else a[-2]
#         continue
#     curr = a[0]
#     # print(f'prev = {prev} curr = {curr}') # tests
#     if not prev == curr:
#         print('НЕТ')
#         break
#     prev = a[-1] if not a[-1] in 'ьъы' else a[-2]
# else:
#     print('ДА')

print('##################################')

# n = int(input())
# s = 0
# for i in range(1, n):
#     if not i % 3 or not i % 5:
#         s += i
# print(s) 

print('##################################')

# arr = input()
# prev, curr, check = None, None, False
# for i, c in enumerate(arr):
#     if 0 == i:
#         prev = c
#         continue
#     curr = c
#     if prev + curr == 'ра':
#         check = True
#         print(i - 1, end=' ')
#     prev = curr
# print('' if check else -1)

print('##################################')

# arr = input()
# for i, c in enumerate(arr):
#     if 0 == i and not '+' == c:
#         print('НЕТ')
#         break
#     elif 1 == i and not '7' == c:
#         print('НЕТ')
#         break
#     elif 2 == i and not '(' == c:
#         print('НЕТ')
#         break
#     elif 6 == i and not ')' == c:
#         print('НЕТ')
#         break
#     elif i in (10, 13) and not '-' == c:
#         print('НЕТ')
#         break
#     elif not i in (0, 1, 2, 6, 10, 13) and not c.isdigit():
#         print('НЕТ')
#         break
# else:
#     print('ДА')

print('##################################')

# s = '+7(xxx)xxx-xx-xx'
# n = input().rjust(len(s))
# for i, item in enumerate(n):
#     if s[i] == item or item.isdigit():
#     # if s[i] == item or s[i] == 'x' and item.isdigit():
#         continue
#     print('НЕТ')
#     break
# else:
#     print('ДА')

print('##################################')

# s = input()
# buf = ''
# res = 0
# check = True
# sign_prev, sign_curr = None, None

# for i, item in enumerate(s):
#     if 0 == i:
#         buf = item
#         continue
#     elif item.isdigit():
#         buf += item
#     elif ' ' == item:
#         if sign_prev is None and check:
#             check = False
#             res += int(buf)
#             buf = ''
#         continue
#     elif item in '-+':
#         if sign_prev is None and check:
#             check = False
#             res += int(buf)
#             buf = ''
#         sign_curr = item
#         if not sign_prev is None:
#             res += int(buf) if '+' == sign_prev else -int(buf)
#             buf = ''
#         sign_prev = sign_curr
# res += int(buf) if '+' == sign_prev else -int(buf)

# print(res)

print('##################################')

# # # version 1
# # arr = map(lambda x: int(x)**2, input().split())
# # print(*arr)

# # version 2
# arr = list(map(int, input().split()))
# for i, item in enumerate(arr):
#     arr[i] = item**2
# print(*arr)

print('##################################')

# # arr = list(map(int, input().split()))
# arr = input().split()
# for i in arr:
#     print((i + ' ') * 2, end='')
# print()

print('##################################')

# arr = list(map(float, input().split()))
# _min = float('inf')
# for i in arr:
#     if _min > i:
#         _min = i
# print(_min)

print('##################################')

# arr = list(map(float, input().split()))
# for i, item in enumerate(arr):
#     if 0 > item:
#         arr[i] = -1.0
# print(*arr)

print('##################################')

# arr = input().split()
# it = iter(arr)
# print(next(it))
# print(next(it))

print('##################################')

# arr = input()
# it = iter(arr)
# for i in it:
#     if ' ' == i: break
#     print(i, end='')
# print()

print('##################################')

# arr = input()
# print(*iter(arr))

print('##################################')

# n = int(input())
# arr = []

# for i in range(n):
#     buff = [1] * n
#     buff[n-1] = 5
#     arr.append(buff)

# for a in arr:
#     print(*a)

print('##################################')

# n = int(input())

# lst = [[1] * n] * n
# print(lst, sep='\n') # test
# lst[0][n-1] = 5
# print(lst, sep='\n') # test

# for i in lst:
#     print(*i)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin))
# # print(lst_in) # test 

# # здесь продолжайте программу (используйте список lst_in)
# for i, s in enumerate(lst_in):
#     while lst_in[i].count(' ') or lst_in[i].count('--'):
#         lst_in[i] = lst_in[i].replace('  ', ' ').replace(' ', '-').replace('--', '-')

# for s in lst_in:
#     print(s)

print('##################################')

# n = int(input())

# for i in range(2, n):
#     for j in range(2, int(i**0.5)+1):
#         # print(f'j = {j}') # test
#         if not i % j:
#             break
#     else:
#         print(i, end=' ')
# print()

print('##################################')

# import sys

# # считывание списка из входного потока
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
# s = sys.stdin
# lst_in = [list(map(int, x.strip().split())) for x in s]

# # здесь продолжайте программу (используйте список lst_in)
# # print(*lst_in, sep='\n') # test

# check = False
# n = 5

# # for y in range(n):
# #     for x in range(n):
# #         if lst_in[y][x]:
# #             if -1 not in (y-1, x-1) and 1 == lst_in[y-1][x-1]:
# #                 check = True
# #                 break
# #             elif -1 not in (y-1,) and 1 == lst_in[y-1][x]:
# #                 check = True
# #                 break
# #             elif -1 not in (y-1,) and n not in (x+1,) and 1 == lst_in[y-1][x+1]:
# #                 check = True
# #                 break

# #             elif -1 not in (x-1,) and 1 == lst_in[y][x-1]:
# #                 check = True
# #                 break
# #             elif n not in (x+1,) and 1 == lst_in[y][x+1]:
# #                 check = True
# #                 break

# #             elif -1 not in (x-1,) and n not in (y+1,) and 1 == lst_in[y+1][x-1]:
# #                 check = True
# #                 break
# #             elif n not in (y+1,) and 1 == lst_in[y+1][x]:
# #                 check = True
# #                 break
# #             elif n not in (x+1, y+1) and 1 == lst_in[y+1][x+1]:
# #                 check = True
# #                 break
# #     if check:
# #         break
# # else:
# #     print('ДА')

# for y in range(n):
#     for x in range(n):
#         if lst_in[y][x]:
#             y1 = y-1 if 0 <= y-1 else y
#             x1 = x-1 if 0 <= x-1 else x

#             y2 = 3 if -1 < y-1 < n and y+1 < n else 2
#             x2 = 3 if -1 < x-1 < n and x+1 < n else 2

#             # print(f'y = {y}, x = {x}') # test
#             # print(f'y1 = {y1}, x1 = {x1}') # test
#             # print(f'y2 = {y2}, x2 = {x2}') # test

#             _arr = []
#             for i in range(y1, y1+y2):
#                 _sum = 0
#                 for j in range(x1, x1+x2):
#                     # print(f'i = {i}', end=' ') # test
#                     # print(f'j = {j}') # test
#                     # if not n in (i, j):
#                     #     _sum += lst_in[i][j]
#                     _sum += lst_in[i][j]
#                 _arr.append(_sum)
#             # print(_arr) # test
#             # if _arr[-2]: 
#             #     _arr[-2] = 0

#             # print(_arr) # test
#             # print(_arr[-1]) # test
#             # print(_arr[-2]) # test

#             # if 0 < sum(_arr): 
#             #     check = True
#             #     break

#             if sum(_arr) > 1:
#                 check = True
#                 break 
#     if check:   
#         break
# else:
#     print('ДА')

# # print(*lst_in, sep='\n') # test
# if check: print('НЕТ')

print('##################################')

# import sys

# # считывание списка из входного потока
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
# s = sys.stdin
# lst_in = [list(map(int, x.strip().split())) for x in s]

# # здесь продолжайте программу (используйте список lst_in)
# # print(*lst_in, sep='\n')

# n = 5
# check = False
# for i in range(n):
#     for j in range(i, n-1):
#         # if i == j:
#         #     continue
#         if not lst_in[i][j+1] == lst_in[j+1][i]:
#             check = True
#             print('НЕТ')
#             break
#     if check:
#         break
# else:
#     print('ДА')

print('##################################')

# arr = list(map(int, input().split()))
# n = len(arr)
# for i in range(n-1):
#     for j in range(i+1, n):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
# print(*arr)

print('##################################')

# arr = list(map(int, input().split()))
# n = len(arr)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(*arr)

print('##################################')

# n = int(input())
# # n = 221
# arr = list(reversed([1, 2, 4, 8, 16, 32, 64]))
# res = []
# i = 0
# while n:
#     if 0 < n:
#         n -= arr[i]
#         res.append(arr[i])
#     elif 0 > n:
#         n += arr[i]
#         res.pop()
#         i += 1
# print(*res)

print('##################################')

# def get_str(lst):
#     return ' '.join(map(str, lst))


# size = 10
# pascal_triangle_lst = []

# for i in range(size):
#     row = [1] * (i + 1)
#     for j in range(1, i):
#         row[j] = pascal_triangle_lst[i - 1][j - 1] + pascal_triangle_lst[i - 1][j]
#     pascal_triangle_lst.append(row)

# width = len(get_str(pascal_triangle_lst[-1]))


# for line in pascal_triangle_lst:
#     print(get_str(line).center(width))

print('##################################')

# lst = [abs(float(x)) for x in input().split()]
# print(lst)

print('##################################')

# lst = [int(x) for x in input()]
# print(lst)

print('##################################')

# n= int(input())
# lst = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# for i in lst:
#     print(*i)

print('##################################')

# lst = [s for s in input().split() if 5 < len(s)]
# print(*lst)

print('##################################')

# lst = [s for s in input().split() if 5 < len(s)]
# print(*lst)

print('##################################')

# n = int(input())
# print(
#     *[
#         i for i in range(1, n+1)
#         if not n % i
#     ]
# )

print('##################################')

# n= int(input())
# lst = [[i]*n for i in range(n)]
# for i in lst:
#     print(*i)

print('##################################')

# print(*[item for i, item in enumerate(input().split()) if not i % 2])

print('##################################')

# arr1 = [int(x) for x in input().split()]
# arr2 = [int(x) for x in input().split()]
# # print(*[x + y for x, y in zip(arr1, arr2)])
# print(*[x + arr2[i] for i, x in enumerate(arr1)])

print('##################################')

# arr1 = [int(x) for x in input().split()]
# arr2 = [int(x) for x in input().split()]
# # print(*[x + y for x, y in zip(arr1, arr2)])
# print(*[x + arr2[i] for i, x in enumerate(arr1)])

print('##################################')

# it = iter(input().split())
# lst = [[x, int(next(it))] for x in it]
# print(lst)

print('##################################')

# print(...)

print('##################################')

import sys

# считывание списка из входного потока
sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
s = sys.stdin
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
print(
    [
        lst_in[i][j] 
        for i in range(len(lst_in)-1, -1, -1)
            for j in range(len(lst_in)-1, -1, -1)
    ]
)

print(
    *sum(...,[])
)

print('##################################')