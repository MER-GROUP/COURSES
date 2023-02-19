'''
Второе вхождение
Дана строка. Найдите в этой строке второе вхождение буквы f, 
и выведите индекс этого вхождения. Если буква f в данной строке встречается 
только один раз, выведите число -1, а если не встречается ни разу, 
выведите число -2.

При решении этой задачи нельзя использовать метод count.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input 1:
comfort
Sample Output 1:
-1

Sample Input 2:
coffee
Sample Output 2:
3
'''
import sys

# sys.stdin = open(file='030.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

if 'f' in arr:
    _count = 0
    for i, el in enumerate(arr):
        if 'f' == el:
            _count += 1
            if 2 == _count:
                print(i)
                break
    else:
        print(-1)
else:
    print(-2)