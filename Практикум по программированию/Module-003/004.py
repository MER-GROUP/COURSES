'''
Часовая стрелка
Часовая стрелка повернулась с начала суток на d градусов. 
Определите, сколько сейчас целых часов h и целых минут m.

Входные данные
На вход программе подается целое число d (0 ≤ d < 360).

Выходные данные
Выведите на экран фразу:

It is ... hours ... minutes.

Вместо многоточий программа должна выводить значения h и m, 
отделяя их от слов ровно одним пробелом.

Sample Input:
90
Sample Output:
It is 3 hours 0 minutes.
'''
import sys

# sys.stdin = open(file='004.csv', mode='rt', encoding='utf-8', newline='')
n = int(sys.stdin.read())

one_hour = 360 // 12
print(f'It is {n // one_hour} hours {n % one_hour * 2} minutes.')