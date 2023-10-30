'''
Умножение строк

Назовем умножением строки на число запись в формате n(string), 
где n — неотрицательное целое число, а string — строка, 
которая должна быть записана n раз. Раскрытием умножения будем 
считать развернутый вариант данной записи, например, строка ti2(Be)3(Ge) 
после раскрытия в ней всех умножений будет иметь вид tiBeBeGeGeGe.

Напишите программу, которая раскрывает все умножения 
в тексте и выводит полученный результат.

Формат входных данных
На вход программе подается одна строка, содержащая строчные 
латинские буквы, числа и скобки.

Формат выходных данных
Программа должна вывести строку, в которой раскрыты все умножения 
с учетом приоритетности операций.

Примечание 1. Гарантируется, что умножение в подаваемой строке 
всегда записано корректно, то есть строго в формате n(string). 
Записи вида 4(2), 3q, (fg)7 не корректны.

Примечание 2. Рассмотрим третий тест. С учетом приоритетности 
операций сначала раскрываем умножение 2(a) и получаем промежуточную 
строку bbbb10(aa)bbb, далее раскрываем умножение 10(aa) и получаем 
конечный результат в виде строки bbbbaaaaaaaaaaaaaaaaaaaabbb.

Примечание 3. Строка, в которой раскрыты все умножения, всегда 
содержит исключительно строчные латинские буквы.

Примечание 4. Максимальная длина результирующей строки не 
превосходит 450000450000 символов.

Примечание 5. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/680266/tests_2907188.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.8/Module_11.8.13

Sample Input 1:
hello3(world)hi
Sample Output 1:
helloworldworldworldhi

Sample Input 2:
0(s)he0(be)lie0(ve)d
Sample Output 2:
helied

Sample Input 3:
bbbb10(2(a))bbb
Sample Output 3:
bbbbaaaaaaaaaaaaaaaaaaaabbb

Sample Input 4:
hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd
Sample Output 4:
hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd

Sample Input 5:
hhhhhh
Sample Output 5:
hhhhhh
'''
import __future__
# from _collections_abc import Sequence
import re
from sys import stdin

def func(string: str) -> str:
    # return re.sub(
    #     pattern=rf'(\d+)\(([a-z]+)\)',
    #     repl=rf'\g<2>' + rf'\g<1>',
    #     string=string
    # )
    pattern=rf'(\d+)\(([a-z]+)\)'
    digit, abc = re.search(pattern, string).group(1, 2)
    return re.sub(
        pattern=rf'(\d+)\(([a-z]+)\)',
        repl=abc * int(digit),
        string=string,
        count=1
    )


if __name__ == '__main__':
    stdin = open(file='057-test.csv', mode='rt', encoding='utf-8', newline='')
    # sentense = map(str, stdin)
    sentense = stdin.read()
    print(sentense) # test
    print('------') # test
    pattern = rf''

    while sentense != func(sentense):
        sentense = func(sentense)

    print(func(sentense))