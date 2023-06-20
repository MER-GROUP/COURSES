'''
Просто Дима 🙂
Дима решил выучить английский алфавит, и чтобы изучение шло быстрее, он придумал упражнение: 
он берет произвольное английское слово и расставляет в нем все буквы в лексикографическом 
порядке. Иногда Дима берет слова повторно, так как не помнит, брал ли их раньше.

Напишите программу, которая принимает на вход произвольное количество английских слов и в 
каждом расставляет буквы в лексикографическом порядке.

Форматы входных данных
На вход программе подается произвольное количество английских слов, каждое на отдельной строке. 

Форматы выходных данных
Программа должна в каждом введенном слове расположить все буквы в лексикографическом порядке 
и вывести полученный результат. Слова должны быть расположены в исходном порядке, каждое 
на отдельной строке.

Примечание 1. Обратите внимание, что в задаче установлено ограничение по времени в одну секунду.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/751476/tests_3131734.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.9/Module_9.9.24

Sample Input 1:
tutorial
pattern
add
Sample Output 1:
ailorttu
aenprtt
add

Sample Input 2:
forget
forget
forget
forget
imagine
Sample Output 2:
efgort
efgort
efgort
efgort
aegiimn
'''
from functools import lru_cache
from sys import stdin

# stdin = open(file='054-test.csv', mode='rt', encoding='utf-8', newline='')

@lru_cache
def abc(word: str) -> str:
    return "".join(sorted(word)).strip()

if __name__ == '__main__':
    for _str in stdin:
        print(abc(_str))