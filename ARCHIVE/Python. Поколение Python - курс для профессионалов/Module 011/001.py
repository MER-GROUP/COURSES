'''
Я в аду?
Напишите программу, которая в заданном тексте находит все телефонные номера, 
соответствующие следующим форматам:

7-ddd-ddd-dd-dd
8-ddd-dddd-dddd

где d — цифра от 0 до 9.

Формат входных данных
На вход программе подается строка произвольного содержания.

Формат выходных данных
Программа должна в введенном тексте найти все телефонные номера, 
соответствующие форматам, указанным в условии задачи, и вывести их в том порядке, 
в котором они были найдены, каждый на отдельной строке.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640164/tests_2829466.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_11/Module_11.1/Module_11.1.6

Sample Input 1:
Перезвони мне, пожалуйста: 7-919-667-21-19
Sample Output 1:
7-919-667-21-19

Sample Input 2:
Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911
Sample Output 2:
7-919-667-21-19
8-917-4864-1911
'''
from __future__ import annotations
from _collections_abc import Iterator, Generator

def is_phone(phone: str) -> bool:
    if not 15 == len(phone):
        return False
    
    arr = phone.split('-')
    if 5 == len(arr):
        if not '7' == arr[0]:
            return False
        else:
            if 3 == len(arr[1]) and 3 == len(arr[2]) and 2 == len(arr[3]) and 2 == len(arr[4]):
                return all(i.isdigit() for i in ''.join(arr))
            else:
                return False
    elif 4 == len(arr):
        if not '8' == arr[0]:
            return False
        else:
            if 3 == len(arr[1]) and 4 == len(arr[2]) and 4 == len(arr[3]):
                return all(i.isdigit() for i in ''.join(arr))
            else:
                return False
    else:
        return False
    
def find_phone(text: str) -> Generator:
    for i in range(len(text)):
        phone = text[i:i+15]
        if is_phone(phone):
            yield phone

if __name__ == '__main__':
    print(
        *find_phone(
            input()
        ),
        sep='\n'
    )