'''
Обратный порядок
Дана последовательность целых чисел. Напишите программу с использованием рекурсии, 
которая выводит эту последовательность в обратном порядке.

Формат входных данных
На вход программе подается последовательность целых чисел, каждое на отдельной строке. 
Концом последовательности является число 0. 

Формат выходных данных
Программа должна вывести введенные числа в обратном порядке, каждое на отдельной строке.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/637962/tests_2618486.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.2/Module_8.2.8

Sample Input 1:
1
2
3
4
0
Sample Output 1:
0
4
3
2
1

Sample Input 2:
0
Sample Output 2:
0
'''
import sys
# sys.stdin = open(file='004-test.txt', mode='rt', encoding='utf-8', newline='')
_arr = list()
for _i in sys.stdin:
    if not '0' == _i.strip():
        _arr.append(_i.strip())
    else:
        _arr.append(_i.strip())
        break
# print(_arr) # test

def _reverse(arr: list) -> None:
    def _rec(_i: int = 0) -> None:
        if _i < len(arr):
            _rec(_i+1)
            print(arr[_i])
    _rec()

if __name__ == '__main__':
    _reverse(_arr)