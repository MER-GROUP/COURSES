'''
Билеты на метро - 2
Билет на одну поездку в метро стоит 15 рублей, 
билет на 5 поездок стоит 70 рублей, билет на 10 поездок стоит 125 рублей, 
билет на 20 поездок стоит 230 рублей, билет на 60 поездок стоит 440 рублей. 
Пассажир планирует совершить n поездок. Определите, сколько билетов каждого 
вида он должен приобрести, чтобы суммарное количество оплаченных поездок 
было не меньше n, а общая стоимость приобретенных билетов – минимальна.

Входные данные
Дано одно число n - количество поездок.

Выходные данные
Выведите пять целых чисел, равные необходимому количеству билетов 
на 1, на 5, на 10, на 20, на 60 поездок. Если для какого-то данного 
n существует несколько способов приобретения билетов одинаковой стоимости, 
необходимо вывести ту комбинацию билетов, которая дает большее число поездок.

Sample Input:
1
Sample Output:
1 0 0 0 0
'''
n = int(input())
c_60 = n // 60
# n -= c_60 * 60
n = n % 60
c_20 = n // 20
# n -= 20 * c_20
n = n % 20
c_10 = n // 10
# n -= 10 * c_10
n = n % 10
c_5 = n // 5
# n -= 5 * c_5
n  = n % 5
c_1 = n // 1

if c_1 * 15 >= 70:
    c_1 = 0
    c_5 += 1
if c_1 * 15 + c_5 * 70 >= 125:
    c_1 = 0
    c_5 = 0
    c_10 += 1
if c_1 * 15 + c_5 * 70 + c_10 * 125 >= 230:
    c_1 = 0
    c_5 = 0
    c_10 = 0
    c_20 += 1
if c_1 * 15 + c_5 * 70 + c_10 * 125 + c_20 * 230 >= 440:
    c_1 = 0
    c_5 = 0
    c_10 = 0
    c_20 = 0
    c_60 += 1
print(c_1, c_5, c_10, c_20, c_60)