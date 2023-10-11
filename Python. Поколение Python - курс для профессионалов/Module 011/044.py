'''
Социальные сети

Вам доступен набор популярных публикаций из социальной сети Твиттер, которые 
могут иметь следующий вид:

Люблю курсы BEEGEEK!
Когда курс по ООП? @timur_guev
BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
и т.д.

Напишите программу, которая определяет, в скольких публикациях содержится строка beegeek.

Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет 
очередную публикацию.

Формат выходных данных
Программа должна определить, в скольких введенных строках содержится строка beegeek 
в произвольном регистре, и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680263/tests_2896124.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.6/Module_11.6.20

Sample Input 1:
Люблю курсы BEEGEEK!
Когда курс по ООП? @beegeek
BEEGEEK, спасибо за курсы, вы лучшие! #python #BeeGeek
Sample Output 1:
3

Sample Input 2:
Нельзя быть дружелюбным соседом, если соседей нет
@everyone, посоветуйте курсы по программированию
Sample Output 2:
0
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='044-test.csv', mode='rt', encoding='utf-8', newline='')
    pattern = r'beegeek'

    print(
        sum(
            bool(re.search(pattern, line, re.IGNORECASE)) for line in stdin
        )
    )