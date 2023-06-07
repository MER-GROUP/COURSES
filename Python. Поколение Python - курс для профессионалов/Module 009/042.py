'''
Декоратор returns_string
Реализуйте декоратор returns_string, который проверяет, что возвращаемое 
значение декорируемой функции принадлежит типу str. Если возвращаемое значение 
принадлежит какому-либо другому типу, декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с 
произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор returns_string, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3128670.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.10

Sample Input 1:
@returns_string
def beegeek():
    return 'beegeek'  
print(beegeek())
Sample Output 1:
beegeek

Sample Input 2:
@returns_string
def add(a, b):
    return a + b
try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))
Sample Output 2:
<class 'TypeError'>
'''
from functools import wraps

pass

if __name__ == '__main__':
    pass