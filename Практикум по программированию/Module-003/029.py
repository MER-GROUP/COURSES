'''
Первое и последнее вхождение
Дана строка. Если в этой строке буква f встречается только один раз, 
выведите её индекс. Если она встречается два и более раз, 
выведите индекс её первого и последнего появления. 
Если буква f в данной строке не встречается, ничего не выводите.

При решении этой задачи нельзя использовать метод count и циклы.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
comfort
Sample Output 1:
3

Sample Input 2:
office
Sample Output 2:
1 2
'''
import sys

# sys.stdin = open(file='029.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

if -1 != arr.find('f') == arr.rfind('f'):
    print(arr.find('f'))
elif not -1 == arr.find('f') and not -1 == arr.rfind('f'):
    print(arr.find('f'), arr.rfind('f'))
else:
    pass