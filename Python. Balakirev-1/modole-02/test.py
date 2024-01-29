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

# import sys

# # считывание списка из входного потока
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
# s = sys.stdin
# lst_in = [list(map(int, x.strip().split())) for x in s]

# # здесь продолжайте программу (используйте список lst_in)
# # 1
# # print(
# #     [
# #         lst_in[i][j] 
# #         for i in range(len(lst_in)-1, -1, -1)
# #             for j in range(len(lst_in)-1, -1, -1)
# #     ]
# # )

# # 2
# print(*sum(list(map(lambda x: list(reversed(*x)), zip(reversed(lst_in)))), []))

print('##################################')

# import sys

# # считывание списка из входного потока
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
# s = sys.stdin
# # lst_in = [list(map(int, x.strip().split())) for x in s]

# # lst_in = [list(map(int, x.strip().split())) for x in s.read()]
# lst_in = [list(map(int, x.strip().split())) for x in s.read().split()]
# print(lst_in)

# # здесь продолжайте программу (используйте список lst_in)
# # 1
# # print(
# #     [
# #         lst_in[i][j] 
# #         for i in range(len(lst_in)-1, -1, -1)
# #             for j in range(len(lst_in)-1, -1, -1)
# #     ]
# # )

# # 2
# # print(*sum(list(map(lambda x: list(reversed(*x)), zip(reversed(lst_in)))), []))

# # 3
# # import sys
# # print(
# #     list(
# #         map(
# #             int, 
# #             sys.stdin.read().split()
# #         )
# #     )[::-1]
# # )

print('##################################')

# import sys

# # считывание списка из входного потока
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
# s = sys.stdin
# lst_in = list(map(int, s.read().split()))
# # print(lst_in) # test

# # n = len(lst_in)
# n = int(len(lst_in) ** 0.5)

# arr = [
#     lst_in[i: i+n]
#     for i, item in enumerate(lst_in)
#         if not i % n
# ]
# print(arr)

print('##################################')

# t = ["– Скажи-ка, дядя, ведь не даром",
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]

# lst = [[j for j in i.split() if 3 < len(j)] for i in t]

# print(lst)

print('##################################')

# import sys

# # считывание списка из входного потока
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')
# s = sys.stdin
# lst_in = [list(map(int, x.strip().split())) for x in s]

# # здесь продолжайте программу (используйте список lst_in)
# A = [[lst_in[j][i] for j in range(len(lst_in))] for i in range(len(lst_in[0]))]
# for row in A:
#     print(*row)

print('##################################')

# d = input().split()
# # print(d)
# arr = tuple(map(lambda x: (x.split('=')[0], int(x.split('=')[1])), d))
# # print(arr)
# d = dict(arr)
# # print(d)
# print(*sorted(d.items()))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin))
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {
#     int(k): v 
#     for item in lst_in 
#         for k, v in [item.split('=')]
# }
# print(*sorted(d.items()))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().split()
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {
#     k: v 
#     for item in lst_in 
#         for k, v in [item.split('=')]
# }

# if  'house' in d and 'True' in d  and '5' in d:
#     print('ДА')
# else:
#     print('НЕТ') 

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().split()
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {
#     k: v 
#     for item in lst_in 
#         for k, v in [item.split('=')]
# }
# # print(d) # test

# while 'False' in d or '3' in d:
#     try:
#         del d['False']
#     except KeyError:
#         pass

#     try:
#         del d['3']
#     except KeyError:
#         pass

# print(*sorted(d.items()))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().split()
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for item in lst_in:
#     for k, v in [(item[:2], item)]:
#         # d[k] = d.setdefault(k, []) + [v]
#         d[k] = d.get(k, []) + [v]
# # print(d) # test

# print(*sorted(d.items()))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for item in lst_in:
#     for v, k in [item.split()]:
#         # d[k] = d.setdefault(k, []) + [v]
#         # d[k] = d.get(k, []) + [v]
#         d.setdefault(k, []).append(v)
# # print(d) # test

# print(*sorted(d.items()))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for k in map(int, lst_in):
#     if not k:
#         break
#     if not k in d:
#         d[k] = round(k**0.5, 2)
#         print(d[k])
#     else:
#         print(f'значение из кэша: {d[k]}')

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for k in map(str.strip, lst_in):
#     if not k in d:
#         d[k] = f'HTML-страница для адреса {k}'
#         print(d[k])
#     else:
#         print(f'Взято из кэша: {d[k]}')

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for k in map(str.strip, lst_in):
#     if not k in d:
#         d[k] = f'HTML-страница для адреса {k}'
#         print(d[k])
#     else:
#         print(f'Взято из кэша: {d[k]}')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().strip()
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {
#     ' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 
#     'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 
#     'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 
#     'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 
#     'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 
#     'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 
#     'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
# }

# _len = len(lst_in)
# for i, c in enumerate(map(str.upper, lst_in), 1):
#     if i == _len:
#         print(d[c])
#     else:
#         print(d[c], end=' ')

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().strip()
# # print(lst_in) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {
#     ' ': '-...-', 'Ё': '.', 'А': '.-', 'Б': '-...', 'В': '.--', 
#     'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..', 
#     'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 
#     'Н': '-.', 'О': '---', 'П': '.--.', 'Р': '.-.', 'С': '...', 
#     'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 
#     'Ч': '---.', 'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 
#     'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--', 'Я': '.-.-'
# }

# for m in lst_in.split():
#     i = tuple(d.values()).index(m)
#     k = tuple(d.keys())[i]
#     print(k.lower().replace('ё', 'е'), end='')
# print()

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().strip()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = dict.fromkeys(lst_in.split())

# print(*d.keys())

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read().strip()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = dict.fromkeys(lst_in.split())

# print(*d.keys())

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for line in lst_in:
#     k, v = line.split()
#     d.setdefault(int(k), []).append(v)

# for k, v in d.items():
#     print(f'{k}: {", ".join(v)}')

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# d = {}
# for line in lst_in:
#     k, v = line.split()
#     d.setdefault(int(k), []).append(v)

# for k, v in d.items():
#     print(f'{k}: {", ".join(v)}')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# N = int(lst_in) * 1000
# # print(N) # test

# s = 0
# d = {}
# for k, v in sorted(things.items(), key=lambda x: -x[1]):
#     s += v
#     if v >= N:
#         continue
#     elif s <= N:
#         d.setdefault(k, v)
#     elif s > N:
#         s -= v
#     elif s == N:
#         break
# print(*d)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# N = int(lst_in) * 1000
# # print(N) # test

# s = 0
# d = {}
# for k, v in sorted(things.items(), key=lambda x: -x[1]):
#     s += v
#     if v >= N:
#         continue
#     elif s <= N:
#         d.setdefault(k, v)
#     elif s > N:
#         s -= v
#     if s == N:
#         break
# print(*d)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t = (3.4, -56.7)
# t += tuple(map(int, lst_in.split()))
# print(t)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t = tuple(lst_in.split())
# if 'Москва' not in t:
#     t += 'Москва',
# print(*t)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t = tuple(lst_in.split())
# if 'Ульяновск' in t:
#     t = t[:t.index('Ульяновск')] + t[t.index('Ульяновск')+1:]
# print(*t)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t = tuple(w for w in lst_in.lower().split() if 'ва' in w)
# print(*t)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t = tuple(map(int, lst_in.split()))
# buff = []
# t2 = ()
# for i in t:
#     if i not in buff:
#         buff.append(i)
#         t2 += i,
# print(*t2)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t0 = tuple(map(int, lst_in.split()))
# t = tuple(i for i, item in enumerate(t0) if 1 < t0.count(item))
# print(*t)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(lst_in)

# t2 = ()
# for i in range(N):
#     buff = ()
#     for j in range(N):
#         buff += t[i][j],
#     t2 += tuple(buff), 

# for i in t2:
#     print(*i)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# menu = tuple(tuple(i.split()) for i in map(str.strip, lst_in))
# print(menu)

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# s = set(map(float, input().split()))
# print(*sorted(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# s = set(map(str, input().lower().split()))
# print(len(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# s = set(
#     map(
#         int,
#         filter(
#             lambda x: x.isdigit(), 
#             input()
#         )
#     )
# )
# if s:
#     print(*sorted(s))
# else:
#     print('НЕТ')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# s = set(map(str.strip, lst_in))
# print(len(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# s = set(map(lambda x: x.split(':')[0].strip(), lst_in))
# print(len(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# s = set(x for x in map(str.strip, lst_in) if not 'q' == x)
# print(len(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(line.split()) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# s = arr1 & arr2
# print(*sorted(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(int, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# s = arr1 - arr2
# print(*sorted(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(int, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# s = arr1 ^ arr2
# print(*sorted(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# print('ДА' if arr1 == arr2 else 'НЕТ')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (set(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# # print(arr2) # test

# print('ДОПУЩЕН' if '2' not in arr1 else 'НЕ ДОПУЩЕН')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (set(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# print('ДА' if arr2 >= arr1 else 'НЕТ')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (set(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# n = int(next(iter(arr1)))
# check1 = {2, 3, 5}
# check2 = {i for i in range(2, int(n**0.5) + 1) if not n % i}

# print('ДА' if check1 <= check2 else 'НЕТ')

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# d = {k: v for k, v in enumerate(arr1[1:], int(arr1[0]))}
# print(d.get(4))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# s = {*map(str.strip, lst_in)}
# print(len(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# s = {s.lower() for s in arr1 if 3 <= len(s)}
# print(len(s))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.lower().split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# d = {
#     k: arr1.count(k)
#     for k in set(arr1)
# }

# print(d.get('и', 0))

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# d = {
#     k: {line_copy.split(':')[1].strip() for line_copy in lst_in if line_copy.split(':')[0]==k}
#     for line in lst_in
#         for k, _ in [line.split(':')]
# }

# # print(d)

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def my_func():
#     print("It's my first function")
          
# my_func()

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def my_func():
#     name, last_name = input().split()
#     print(f'Уважаемый, {name} {last_name}! Вы верно выполнили это задание!')
          
# my_func()

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def my_func(weigth: float) -> None:
#     print(f'Предмет имеет вес: {weigth} кг.')
          
# my_func(float(input()))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def my_func(arr: list) -> None:
#     print(f'Min = {min(arr, key=int)}, max = {max(arr, key=int)}, sum = {sum(map(int, arr))}')
          
# my_func(input().split())

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def my_func(width: int, height: int) -> None:
#     print(f'Периметр прямоугольника, равен {2*(width+height)}')
          
# my_func(*map(int, input().split()))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def my_func(mail: str) -> None:
#     if 1 == mail.count('@') and 1 == mail.count('.'):
#         for c in mail:
#             # print(c) # test
#             if not 'a' <= c <= 'z'\
#                 and not 'A' <= c <= 'Z'\
#                 and not '0' <= c <= '9'\
#                 and not c in ('_', '.', '@'):
#                     print('НЕТ')
#                     break
#         else:
#             print('ДА')
#     else:
#         print('НЕТ')
          
# my_func(input())

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# passwd = input()
# if 8 <= len(passwd)\
#     and any(c == c.upper() for c in passwd if not c.isdigit())\
#     and any(c == c.lower() for c in passwd if not c.isdigit()):
#         print('YES')
# else:
#         print('NO')

# print([c == c.upper() for c in passwd if not c.isdigit()])

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(x: float) -> float:
#     return x ** 2

# print(func(float(input())))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def is_triangle(a: int, b: int, c: int) -> bool:
#     # return min(a, b, c) + (a + b + c - max(a, b, c) - min(a, b, c)) > max(a, b, c)
#     return sum(sorted([a, b, c])[:2]) > sorted([a, b, c])[2]

# print(is_triangle(*map(int, input().split())))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def is_large(s: str) -> bool:
#     return 2 < len(s)

# print(is_large(input()))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def is_even(x: int) -> bool:
#     return not x % 2

# for i in iter(input, '1'):
#     if is_even(int(i)):
#         print(i)

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def is_odd(x: int) -> bool:
#     return x % 2


# lst = [*filter(is_odd, map(int, input().split()))]
# print(*lst)

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# tp = input()
# if 'RECT' == tp:
#     def get_sq(a: int, b: int) -> int:
#         return a * b
# else:
#     def get_sq(a: int) -> int:
#         return a * a
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(s: str) -> bool:
#     return not 6 > len(s)

# lst = [*filter(func, input().split())]
# print(*lst)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(s: str) -> tuple:
#     return s, len(s)

# sentence = input()
# d = {k: v for k, v in map(func, sentence.split())}
# # print(d) # test

# a = sorted(d, key=lambda x: d[x])
# print(*a)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(_min: int, _max: int) -> int:
#     return int(_min) * int(_max)

# arr = input().split()
# print(func(min(arr, key=int), max(arr, key=int)))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(_min: int, _max: int) -> int:
#     return int(_min) * int(_max)

# arr = input().split()
# print(func(min(arr, key=int), max(arr, key=int)))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# s = "hello WORLD "
# print(len(s))
# print(s[len(s) // 2:] + s[:len(s) // 2])
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# print(('NO', 'YES')[any(map(str.isalpha, input()))])
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# sentence = input()
# n = len(sentence)
# s1 = sentence[:n//2]
# s2 = sentence[n//2:]
# print(s1.capitalize(), s2.capitalize(), sep='')
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def get_nod(a: int, b: int) -> int:
#     if a < b:
#         a, b = b, a
#     while not 0 == b:
#         a, b = b, a % b
#     return a

# print(get_nod(15, 121050))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def get_nod(a: int, b: int) -> int:
#     # if a < b:
#     #     a, b = b, a
#     while not 0 == b:
#         print(f'a = {a}, b = {b}')
#         a, b = b, a % b
#         print(f'a = {a}, b = {b}')
#     return a

# print(get_nod(121050, 15))
# print(get_nod(15, 121050))

# print('---------')
# print(121050%15)
# print(15%121050)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def get_rect_value(a: float, b: float, type=0):
#     if not type:
#         return 2 * (a + b)
#     return a * b
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def check_password(passwd: str, chars='$%!?@#') -> bool:
#     return any(c in chars for c in passwd) and 7 < len(passwd)

# print(check_password('12345678!'))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(sentense: str, sep: str='-') -> str:
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    
#     return ''.join(sep if ' ' == x else t.get(x, x) for x in sentense.lower())

# s = input()
# print(func(s))
# print(func(s, sep='+'))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(sentense: str, tag: str='h1') -> str:
#     return f'<{tag}>{sentense}</{tag}>'

# s = input()
# print(func(s))
# print(func(s, tag='div'))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def func(sentense: str, tag: str='h1', up: bool=True) -> str:
#     tag = tag.upper() if up else tag
#     return f'<{tag}>{sentense}</{tag}>'

# s = input()
# # print(func(s))
# print(func(s, tag='div'))
# print(func(s, tag='div', up=False))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def get_even(*args):
#     return [x for x in args if not x % 2]

# print(get_even(*map(int, '45 4 8 11 12 0'.split())))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def get_biggest_city(*args):
#     return max(args, key=len)

# print(get_biggest_city(*'Питер Москва Самара Воронеж'.split()))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
# lst_in = sys.stdin.readlines()
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# def get_data_fig(*args, **kwargs):
#     p = (sum(args), )
#     if 'type' in kwargs:
#         p += (kwargs['type'],)
#     if 'color' in kwargs:
#         p += (kwargs['color'],)
#     if 'closed' in kwargs:
#         p += (kwargs['closed'],)
#     if 'width' in kwargs:
#         p += (kwargs['width'],)
#     return p

# print(get_data_fig(1, 2, 3, 4, type=True))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.readlines()
# lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def is_isolate(i: int, j: int, arr: list) -> bool:
#     n = len(arr)
#     s = 0

#     # for i_1 in range(i-1, i-1+3):
#     #     for j_1 in range(j-1, j-1+3):
#     #         s += arr[i_1][j_1]
#     #         print(arr[i_1][j_1], end=' ') # test
#     #     print() # test
#     # print(f's = {s}') # test
#     # return False if 1 == s else True

#     if 0 == i:
#         start_i = i
#         end_i = start_i + 2
#     elif n-1 == i:
#         start_i = i-1
#         end_i = start_i + 2
#     else:
#         start_i = i-1
#         end_i = start_i + 3

#     if 0 == j:
#         start_j = j
#         end_j = start_j + 2
#     elif n-1 == j:
#         start_j = j-1
#         end_j = start_j + 2
#     else:
#         start_j = j-1
#         end_j = start_j + 3

#     for i_1 in range(start_i, end_i):
#         for j_1 in range(start_j, end_j):
#             s += arr[i_1][j_1]
#             # print(arr[i_1][j_1], end=' ') # test
#         # print() # test
#     # print(f's = {s}') # test
#     return False if 1 == s else True

# def verify(arr: list) -> bool:
#     for i, item_i in enumerate(arr):
#         for j, item_j in enumerate(item_i):
#             if 1 == item_j:
#                 if is_isolate(i, j, arr):
#                     return False
#     return True

# print(verify(lst_in))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.readlines()
# lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# # def is_isolate(i: int, j: int, arr: list) -> bool:
# #     n = len(arr)
# #     s = 0

# #     # for i_1 in range(i-1, i-1+3):
# #     #     for j_1 in range(j-1, j-1+3):
# #     #         s += arr[i_1][j_1]
# #     #         print(arr[i_1][j_1], end=' ') # test
# #     #     print() # test
# #     # print(f's = {s}') # test
# #     # return False if 1 == s else True

# #     if 0 == i:
# #         start_i = i
# #         end_i = start_i + 2
# #     elif n-1 == i:
# #         start_i = i-1
# #         end_i = start_i + 2
# #     else:
# #         start_i = i-1
# #         end_i = start_i + 3

# #     if 0 == j:
# #         start_j = j
# #         end_j = start_j + 2
# #     elif n-1 == j:
# #         start_j = j-1
# #         end_j = start_j + 2
# #     else:
# #         start_j = j-1
# #         end_j = start_j + 3

# #     for i_1 in range(start_i, end_i):
# #         for j_1 in range(start_j, end_j):
# #             s += arr[i_1][j_1]
# #             # print(arr[i_1][j_1], end=' ') # test
# #         # print() # test
# #     # print(f's = {s}') # test
# #     return False if 1 == s else True

# # def verify(arr: list) -> bool:
# #     for i, item_i in enumerate(arr):
# #         for j, item_j in enumerate(item_i):
# #             if 1 == item_j:
# #                 if is_isolate(i, j, arr):
# #                     return False
# #     return True

# # def is_isolate(matrix, x, y):
# #     n = len(matrix)
# #     for i in range(-1, 2):
# #         for j in range(-1, 2):
# #             if 0 <= x + i < n and 0 <= y + j < n:
# #                 if (i or j) and matrix[x + i][y + j]:
# #                     return False
# #     return True
    

# # def verify(matrix):
# #     n = len(matrix)
# #     for i in range(n):
# #         for j in range(n):
# #             if matrix[i][j] == 1 and not is_isolate(matrix, i, j):
# #                 return False
# #     return True

# def is_isolate(m):
#     for i in range(len(m) - 1):
#         k=''.join(map(str, map(sum, (zip(m[i], m[i + 1])))))
#         print(k) # test
#         if '2' in k or '11' in k: return False
#     return True

# def verify(m):
#     return is_isolate(m)

# print(verify(lst_in))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.readlines()
# lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def str_min(s1: str, s2: str) -> str:
#     return s1 if s1 < s2 else s2

# def str_min3(s1: str, s2: str, s3: str) -> str:
#     return str_min(s1, s2) if str_min(s1, s2) < s3 else s3

# def str_min4(s1: str, s2: str, s3: str, s4: str) -> str:
#     return str_min3(s1, s2, s3) if str_min3(s1, s2, s3) < s4 else s4
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# *lst, x, y, z = lst_in
# print(*lst)
    
print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# lst_c = (*lst_in,)
# print(lst_c)
    
print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# lst = [*range(lst_in[0], lst_in[-1]+1)]
# print(*lst)
    
print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# lst_in = list(map(str.split, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# lst = [*lst_in[0], *lst_in[-1]]
# print(*lst)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news', **dict(lst_in)}
# # print(menu)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news', **dict(lst_in)}
# print(menu)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.read().strip()
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# res = lst_in.find('Сакура')
# print(res if not -1 == res else 'Это письмо не Сакуре')
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def get_rec_N(N):
#     if 1 < N:
#         get_rec_N(N-1)
#     print(N)

# get_rec_N(lst_in)
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def get_rec_sum(arr, index=0):
#     if len(arr) == index+1:
#         return arr[index]
#     return arr[index] + get_rec_sum(arr, index+1)

# print(get_rec_sum(lst_in))
    
print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# lst_in = int(sys.stdin.read().strip())
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def fib_rec(N, f=[1,1]):
#     if N == len(f):
#         # print(f) # test
#         return f
#     return fib_rec(N, f+[sum((f[-1], f[-2]))])

# # print(fib_rec(lst_in))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# lst_in = int(sys.stdin.read().strip())
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def fact_rec(n):
#     return n * fact_rec(n-1) if n else 1

# print(fact_rec(lst_in))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# lst_in = int(sys.stdin.read().strip())
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

# def get_line_list(d,a=[]):
#     for i, item in enumerate(d):
#         # print(f'item = {item}') # test
#         # print(isinstance(item, list)) # test
#         if isinstance(item, list):
#             # get_line_list(item, a=a)
#             get_line_list(item)
#         else:
#             a.append(item)
#     return a

# print(get_line_list(d))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# lst_in = int(sys.stdin.read().strip())
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def get_path(n):
#     if 1 == n:
#         return 1
#     elif 2 == n:
#         return 2
#     else:
#         return get_path(n-1) + get_path(n-2)

# print(get_path(lst_in))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def merge_arr(arr1: list, arr2: list) -> list:
#     arr1_len = len(arr1)
#     arr2_len = len(arr2)
#     arr_new = []
#     arr1_it = 0
#     arr2_it = 0

#     while arr1_it < arr1_len and arr2_it < arr2_len:
#         if arr1[arr1_it] < arr2[arr2_it]:
#             arr_new += [arr1[arr1_it]]
#             arr1_it += 1
#         else:
#             arr_new += [arr2[arr2_it]]
#             arr2_it += 1
#     arr_new += arr1[arr1_it:]
#     arr_new += arr2[arr2_it:]

#     return arr_new

# def split_arr(arr: list):
#     middle = len(arr) // 2
#     arr1 = arr[:middle]
#     arr2 = arr[middle:]

#     if 1 < len(arr1):
#         arr1 = split_arr(arr1)
#     if 1 < len(arr2):
#         arr2 = split_arr(arr2)

#     return merge_arr(arr1, arr2)

# print(*split_arr(lst_in))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# get_sq = lambda x: x**2

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# get_div = lambda x, y: None if not y else x/y

print('##################################')

# import sys
# # sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# # print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# print((lambda x: -x if 0 > x else x)(float(input())))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# print((lambda x: 'ra' in x)(*lst_in))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)

#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)

#     return res

# # здесь продолжайте программу
# print(*filter_lst(lst_in))
# print(*filter_lst(lst_in, lambda x: 0 > x))
# print(*filter_lst(lst_in, lambda x: 0 <= x))
# print(*filter_lst(lst_in, lambda x: 3 <= x <= 5))

print('##################################')

# import sys
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# x = 0

# def outer():
#     global x
#     x = 1
#     def inner():
#         global x
#         x=2
#         print('inner:', x)
#     inner()
#     print('outer:', x)

# outer()
# print('global:', x)

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin
# WIDTH = int(input())


# def func1():
#     global WIDTH
#     WIDTH += 1
#     return WIDTH


# print(func1())

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def func1():
#     msg = input()


#     def func2():
#         nonlocal msg
#         msg = input()
#         print(msg)


#     func2()        
#     print(msg)


# func1()

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def create_global(x):
#     global TOTAL
#     TOTAL = x

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def counter_add():
#     def add_five(n):
#         return n + 5
#     return add_five

# cnt = counter_add()
# k = int(input())
# print(cnt(k))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def counter_add(n):
#     def inner(k):
#         return k + n
#     return inner

# print(counter_add(2)(int(input())))
# # cnt = counter_add(2)
# # k = int(input())
# # print(cnt(k))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def func(c='h1'):
#     def inner(s):
#         return f'<{c}>{s}</{c}>'
#     return inner

# print(func()(input()))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def func(c='h1'):
#     def inner(s):
#         return f'<{c}>{s}</{c}>'
#     return inner

# print(func(input())(input()))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def func(tp='list'):
#     def inner(s):
#         if 'list' == tp:
#             obj = list(map(int, s.split()))
#         else:
#             obj = tuple(map(int, s.split()))
#         return obj
#     return inner

# print(func(input())(input()))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def func_show(func):
#     def wrapper(*args, **kwargs):
#         print(f'Площадь прямоугольника: {func(*args, **kwargs)}')
#     return wrapper

# def get_sq(width, height):
#     return width * height

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def show_menu(func):
#     def wrapper(*args, **kwargs):
#         for i, item in enumerate(func(*args, **kwargs), 1):
#             print(f'{i}. {item}')
#     return wrapper

# @show_menu
# def get_menu(s):
#     return s.split()

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = sys.stdin.readlines()
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def decor_sort(func):
#     def wrapper(*args, **kwargs):
#         return sorted(func(*args, **kwargs))
#     return wrapper

# @decor_sort
# def get_list(s: str) -> list:
#     return list(map(int, s.split()))

# print(*get_list(lst_in))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# sys.stdin = _stdin

# def decor(func):
#     def wrapper(*args, **kwargs):
#         return dict(zip(*func(*args, **kwargs)))
#     return wrapper

# @decor
# def str_to_list(s1: str, s2: str) -> tuple[list, list]:
#     return s1.split(), s2.split()

# d = str_to_list(arr1, arr2)
# print(*sorted(d.items()))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)

# print(arr1) # test
# print(arr2) # test

# sys.stdin = _stdin

# def decor(func):
#     def wrapper(*args, **kwargs):
#         s = func(*args, **kwargs)
#         while '--' in s:
#             s = s.replace('--', '-')
#         return s
#     return wrapper

# @decor
# def kiril_to_latin(s: str) -> str:
#     t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#     # return ''.join(map(t.get, s.lower()))
#     return ''.join(
#         map(lambda x: t.get(x, '-') 
#             if x in r': ;.,_'
#             or x in t
#             else x,
#             s.lower()
#         )
#     )

# print(kiril_to_latin('Python - это круто!'))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# # arr1 = tuple(int(i) for i in lst_in.split())

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def decor_param(start: int=5):
#     from functools import wraps
#     def decor(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs) + start
#         return wrapper
#     return decor

# @decor_param()
# def str_to_int_sum(s: str) -> int:
#     return sum(map(int, s.split()))

# print(str_to_int_sum(lst_in))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# # arr1 = tuple(int(i) for i in lst_in.split())

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# # def decor_param(start: int=5):
# def decor_param(*args ,**kwargs):
#     # print('args =', len(args)) # test
#     # # print('args[0] =', args[0]) # test
#     # print('kwargs =', len(kwargs)) # test
#     # print('kwargs[start] =', *kwargs.values()) # test

#     from functools import wraps
#     if len(kwargs):
#         key, value = tuple(kwargs.items())[0]
#         def decor(func):
#             @wraps(func)
#             def wrapper(*args, **kwargs):
#                 return func(*args, **kwargs) + value
#             return wrapper
#         return decor
#     else:
#         value = 5
#         func = args[0]
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs) + value
#         return wrapper

# @decor_param
# def str_to_int_sum(s: str) -> int:
#     return sum(map(int, s.split()))

# print(str_to_int_sum(lst_in))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# # arr1 = tuple(int(i) for i in lst_in.split())

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# if lst_in.isdigit():
#     print('Это число')
# elif lst_in.isalpha():
#     print('Это слово')
# elif lst_in.isalnum():
#     print('Это буквы и цифры')
# elif lst_in.isspace():
#     print('Это строка из пробельных символов')
# else:
#     print('Это что-то странное')

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# # lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# lst_in = sys.stdin.read().split('\n')
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# # arr1 = tuple(int(i) for i in lst_in.split())

# print(arr1) # test
# print(arr2) # test

# sys.stdin = _stdin

# if arr1[0:len(arr2)] == arr2:
#     print(True)
# else:
#     print(False)

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = sys.stdin.read().split('\n')
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# # arr1 = tuple(int(i) for i in lst_in.split())

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# print(lst_in.replace('ё','е').replace('Ё','Е'))

print('##################################')

# import sys
# _stdin = sys.stdin
# sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# # считывание списка из входного потока
# # lst_in = sys.stdin.read()
# lst_in = sys.stdin.read().strip()
# # lst_in = int(sys.stdin.read().strip())
# # lst_in = sys.stdin.read().split()
# # lst_in = sys.stdin.read().split('\n')
# # lst_in = list(map(int, sys.stdin.read().split()))
# # lst_in = list(map(float, sys.stdin.read().split()))
# # lst_in = map(str.strip, sys.stdin.readlines())
# # lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# # lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# # lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# # lst_in = list(map(str.split, sys.stdin.readlines()))
# # lst_in = list(map(str.strip, sys.stdin.readlines()))

# print(lst_in) # test
# # print(lst_in.split()) # test

# # здесь продолжайте программу (используйте список lst_in)
# # arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# # arr1, arr2, *_ = lst_in
# # arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# # arr1 = tuple(int(i) for i in lst_in.split())

# # print(arr1) # test
# # print(arr2) # test

# sys.stdin = _stdin

# def decor_param(tag='h1'):
#     from functools import wraps
#     def decor(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#         return wrapper
#     return decor

# @decor_param(tag='div')
# def small_reg(s: str) -> str:
#     return s.lower()

# print(small_reg(s = input()))

print('##################################')

import sys
_stdin = sys.stdin
sys.stdin = open(file='test.csv', mode='rt', encoding='utf-8', newline='')

# считывание списка из входного потока
# lst_in = sys.stdin.read()
lst_in = sys.stdin.read().strip()
# lst_in = int(sys.stdin.read().strip())
# lst_in = sys.stdin.read().split()
# lst_in = sys.stdin.read().split('\n')
# lst_in = list(map(int, sys.stdin.read().split()))
# lst_in = list(map(float, sys.stdin.read().split()))
# lst_in = map(str.strip, sys.stdin.readlines())
# lst_in = list(map(lambda x: list(map(int, x.split())), sys.stdin.readlines()))
# lst_in = list(map(lambda x: x.strip().split('='), sys.stdin.readlines()))
# lst_in = map(lambda x: x.strip().split('='), sys.stdin.readlines())
# lst_in = list(map(str.split, sys.stdin.readlines()))
# lst_in = list(map(str.strip, sys.stdin.readlines()))

print(lst_in) # test
# print(lst_in.split()) # test

# здесь продолжайте программу (используйте список lst_in)
# arr1, arr2, *_ = (set(map(str.strip, line.split())) for line in lst_in)
# arr1, arr2, *_ = lst_in
# arr1, *_ = (tuple(map(str.strip, line.split())) for line in lst_in)
# arr1 = tuple(int(i) for i in lst_in.split())

# print(arr1) # test
# print(arr2) # test

sys.stdin = _stdin

pass

print('##################################')