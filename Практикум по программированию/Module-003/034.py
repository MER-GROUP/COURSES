'''
Замена подстроки
Дана строка. Замените в этой строке все цифры 1 на слово one.

Входные данные
Вводится строка.

Выходные данные
Выведите ответ на задачу.

Sample Input:
1+1=2
Sample Output:
one+one=2
'''
import sys  

# sys.stdin = open(file='034.csv', mode='rt', encoding='utf-8', newline='')
arr = sys.stdin.read()
# print(arr) # test

print(arr.replace('1', 'one'))