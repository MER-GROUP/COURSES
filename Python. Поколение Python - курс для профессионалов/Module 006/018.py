'''
Функция count_occurences()

Реализуйте функцию count_occurences(), которая принимает два аргумента в следующем порядке:

word — слово
words — последовательность слов, разделенных пробелом

Функция должна определять, сколько раз слово word встречается в последовательности words, 
и возвращать полученный результат.

Примечание 1. Функция должна игнорировать регистр. То есть, например, слова Python 
и python считаются одинаковыми.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию count_occurences(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/590120/tests_3090873.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.7/Module_6.7.16

Sample Input 1:
word = 'python'
words = 'Python Conferences python training python events'
print(count_occurences(word, words))
Sample Output 1:
3

Sample Input 2:
word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'
print(count_occurences(word, words))
Sample Output 2:
0
'''
from collections import Counter

pass