'''
Функция scrabble()
Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:

symbols — набор символов
word — слово

Функция должна возвращать True, если из набора символов symbols можно составить слово word, 
или False в противном случае.

Примечание 1. При проверке учитывается количество символов, которые нужны для составления слова, 
и не учитывается их регистр.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию scrabble(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/635441/tests_2606042.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_6/Module_6.8/Module_6.8.19

Sample Input 1:
print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
Sample Output 1:
True

Sample Input 2:
print(scrabble('begk', 'beegeek'))
Sample Output 2:
False

Sample Input 3:
print(scrabble('beegeek', 'beegeek'))
Sample Output 3:
True
'''
from collections import Counter

pass