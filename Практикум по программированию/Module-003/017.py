'''
Является ли строка палиндромом?
Дана строка, состоящая из строчных латинских букв и пробелов. 
Проверьте, является ли она палиндромом без учета пробелов 
(например, "аргентина манит негра").

Входные данные
На вход подается 1 строка длины не более 100, содержащая пробелы. 
Подряд может идти произвольное число пробелов.

Выходные данные
Необходимо вывести yes, если данная строка является палиндромом, 
и no в противном случае.

Sample Input:
ab a
Sample Output:
yes
'''
import sys

sys.stdin = open(file='017.csv', mode='rt', encoding='utf-8', newline='')
arr = ''.join(sys.stdin.read().strip().split())

pass