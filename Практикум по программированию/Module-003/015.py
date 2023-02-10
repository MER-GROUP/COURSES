'''
Поиск подстроки
Даны две строки. Определите, является ли первая строка 
подстрокой второй строки.

Входные данные
На вход подается 2 строки длины не более 10000, состоящие только 
из маленьких букв латинского алфавита.

Выходные данные
Необходимо вывести  слово yes, если первая строка является 
подстрокой второй строки, или слово no в противном случае.

Sample Input:
abac
ababacaba
Sample Output:
yes
'''
import sys

# sys.stdin = open(file='015.csv', mode='rt', encoding='utf-8', newline='')
arr = tuple(map(str.strip, sys.stdin.readlines()))

print(('no', 'yes')[arr[0] in arr[1]])