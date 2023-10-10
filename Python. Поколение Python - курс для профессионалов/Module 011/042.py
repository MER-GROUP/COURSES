'''
Популярность

В онлайн-школе BEEGEEK мы всегда следим за тем, насколько растет наша популярность. 
Для этого мы собираем публикации из различных соцсетей, которые содержат вхождения 
строки beegeek в нижнем регистре. Мы оцениваем публикацию:

в 3 балла, если она начинается и заканчивается строкой beegeek
в 2 балла, если она только начинается или только заканчивается строкой beegeek
в 1 балл, если она содержит строку beegeek только внутри
в 0 баллов, если она не содержит строку beegeek
Напишите программу, которая определяет популярность онлайн-школы BEEGEEK путем суммирования 
баллов всех публикаций.

Формат входных данных
На вход программе подается произвольное число строк, каждая из которых представляет очередную публикацию.

Формат выходных данных
Программа должна определить, во сколько баллов оценивается каждая введенная публикация, 
и вывести сумму всех полученных баллов.

Примечание 1. Если публикация представляет собой просто строку beegeek, то она оценивается в 2 балла.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680263/tests_2896126.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.6/Module_11.6.13

Sample Input 1:
hi, beegeek
beegeek is an awesome place for programmers
beegeek rocks, rocks beegeek
i think beegeek is a great place to hangout
Sample Output 1:
8

Sample Input 2:
good morning everyone
i am going to school
and it is raining
Sample Output 2:
0
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

if __name__ == '__main__':
    stdin = open(file='042-test.csv', mode='rt', encoding='utf-8', newline='')
    three = (r'^(beegeek).*\1$', 3)
    two1 = (r'(^beegeek.*)|(.*beegeek$)', 2)
    two2 = (r'^(beegeek)$', 2)
    one = (r'.+beegeek.+', 1)
    count = 0
    
    for word in map(str.strip, stdin):
        for _tuple in (three, two1, two2, one):
            match = re.search(_tuple[0], word)
            if match:
                count += _tuple[1]
                break
    
    print(count)