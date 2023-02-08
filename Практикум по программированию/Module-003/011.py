'''
Количество слов
Дана строка, содержащая пробелы. Найдите, сколько в ней слов 
(слово – это последовательность непробельных символов, слова 
разделены одним пробелом, первый и последний символ строки – не пробел).

Входные данные
На вход подается несколько строк.

Выходные данные
Необходимо вывести  количество слов в первой из введенных строк.

Sample Input:
In the town where I was born
Sample Output:
7
'''
import sys

# sys.stdin = open(file='011.csv', mode='rt', encoding='utf-8', newline='')
# arr =list(map(lambda x: x.strip(), sys.stdin.readlines()))
# arr = sum([s.split() for s in arr], [])

# print(len(arr))   

print(len(input().split()))