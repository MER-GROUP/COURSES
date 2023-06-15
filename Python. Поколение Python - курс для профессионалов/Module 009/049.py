'''
Декоратор takes
Реализуйте декоратор takes, который принимает произвольное количество позиционных 
аргументов, каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, 
принадлежат одному из этих типов. Если хотя бы один аргумент не принадлежит 
одному из данных типов, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с 
произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор takes, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129777.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.22

Sample Input 1:
@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))
Sample Output 1:
beebeebee

Sample Input 2:
@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times
try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))
Sample Output 2:
<class 'TypeError'>
'''
from functools import wraps

pass

if __name__ == '__main__':
    pass