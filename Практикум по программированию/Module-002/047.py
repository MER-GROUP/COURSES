'''
Билеты на метро
Билет на одну поездку в метро стоит 15 рублей, 
билет на 10 поездок стоит 125 рублей, 
билет на 60 поездок стоит 440 рублей. 
Пассажир планирует совершить n поездок. 
Определите, сколько билетов каждого вида он должен приобрести, 
чтобы суммарное количество оплаченных поездок было не меньше n, 
а общая стоимость приобретенных билетов – минимальна.

Входные данные
Дано одно число n - количество поездок.

Выходные данные
Выведите три целых числа, равные необходимому количеству 
билетов на 1, на 10, на 60 поездок.

Sample Input:
129
Sample Output:
0 1 2
'''
# n = int(input())
# n_start = n
# one, ten, sixty = [0] * 3
# print(one, ten, sixty)

# if n % 60 < 60:
#     sixty = n // 60
#     print(f'sixty = {sixty}')
#     n = n % 60
#     print(f'n = {n}')

# if n % 10 < 10:
#     ten = n // 10
#     if 4 < ten:
#         ten = 0
#         sixty +=1
#     print(f'ten = {ten}')
#     n = n % 10
#     print(f'n = {n}')

# one = n
# print(f'one = {one}')
# print(one, ten, sixty)

# if 0 == one: 
#     if 440 < ten * 125:
#         ten = 0
#         sixty += 1
#     print(one, ten, sixty)
# elif one in range(1, 9):
#     if 440 < ten * 125:
#         ten = 0
#         sixty += 1
#     if 440 <  one * 15 + ten * 125:
#         one = 0
#         ten = 0
#         sixty += 1
#     if n_start <= sixty * 60:
#         one = 0
#     print(one, ten, sixty)
# else:
#     one = 0 
#     ten += 1
#     if 440 < ten * 125:
#         ten = 0
#         sixty += 1
#     print(one, ten, sixty)




n = int(input())
n_start = n
one, ten, sixty = [0] * 3

if n % 60 < 60:
    sixty = n // 60
    n = n % 60
if n % 10 < 10:
    ten = n // 10
    if 4 < ten:
        ten = 0
        sixty +=1
    n = n % 10
one = n

if 0 == one: 
    if 440 < ten * 125:
        ten = 0
        sixty += 1
    print(one, ten, sixty)
elif one in range(1, 9):
    if 440 < ten * 125:
        ten = 0
        sixty += 1
    if 440 <  one * 15 + ten * 125:
        one = 0
        ten = 0
        sixty += 1
    if n_start <= sixty * 60:
        one = 0
    print(one, ten, sixty)
else:
    one = 0 
    ten += 1
    if 440 < ten * 125:
        ten = 0
        sixty += 1
    print(one, ten, sixty)