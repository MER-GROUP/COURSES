'''
Функция parse_ranges()
Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая 
граница диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит 
в себе все числа от a до b включительно. Например, диапазон 1-4 содержит 
числа 11, 22, 33 и 44.

Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:

ranges — строка, в которой через запятую указаны диапазоны чисел
Функция должна возвращать генератор, порождающий последовательность чисел, 
содержащихся в диапазонах ranges.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию parse_ranges(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_2783807.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.6

Sample Input 1:
print(*parse_ranges('1-2,4-4,8-10'))
Sample Output 1:
1 2 4 8 9 10

Sample Input 2:
print(*parse_ranges('1-10,2-10'))
Sample Output 2:
1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10

Sample Input 3:
print(*parse_ranges('7-32'))
Sample Output 3:
7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
'''
from _collections_abc import Generator

def parse_ranges(seq: str)-> Generator:
    _seq1 = (
        ab
        for ab in seq.split(',')
    )
    _seq2 = (
        s.split('-')
        for s in _seq1
    )
    return (
        i
        for a, b in _seq2
            for i in range(int(a), int(b)+1)
    )

if __name__ == '__main__':
    print(*parse_ranges('1-2,4-4,8-10'))

    print(*parse_ranges('1-10,2-10'))

    print(*parse_ranges('7-32'))