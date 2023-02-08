'''
Самое длинное слово
Дана строка, содержащая пробелы. Найдите в ней самое длинное слово, 
выведите  это слово и его длину. Если таких слов несколько, выведите первое из них.

Входные данные
Задана одна строка, содержащая пробелы. Слова разделены ровно одним пробелом. 
Пробелы в начале и конце строки допускаются.

Выходные данные
Необходимо вывести самое длинное слово в строке и его длину.

Sample Input:
one two three four five six
Sample Output:
three
5
'''
import sys

# sys.stdin = open(file='012.csv', mode='rt', encoding='utf-8', newline='')
# arr = sys.stdin.read()
# max_word = max(arr.split(), key=len)

# print(max_word, len(max_word), sep='\n')

arr = sys.stdin.read().split()
max_word = max(arr, key=len)

print(max_word, len(max_word), sep='\n')