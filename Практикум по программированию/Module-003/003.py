'''
k-я секунда суток
Идёт k-я секунда суток. Определите, сколько целых часов h и 
целых минут m прошло с начала суток. Например, если

k=13257=3⋅3600+40⋅60+57,

то h=3 и m=40.

Входные данные
На вход программе подается целое число k (0 ≤ k ≤ 86399).

Выходные данные
Выведите на экран фразу:

It is ... hours ... minutes.

Вместо многоточий программа должна выводить значения h и m, 
отделяя их от слов ровно одним пробелом.

Sample Input:
13257
Sample Output:
It is 3 hours 40 minutes.
'''
import sys

# sys.stdin = open(file='003.csv', mode='rt', encoding='utf-8', newline='')
n = int(sys.stdin.read())
# print(f'It is {n // 60 // 60} hours {n // 60 % 60} minutes.')


from datetime import datetime, timedelta

d = datetime(1, 1, 1, 0, 0, 0)
t = timedelta(seconds=n)
d += t
print(f'It is {d.hour} hours {d.minute} minutes.')