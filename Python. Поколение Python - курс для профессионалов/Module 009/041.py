'''
Декоратор square
Реализуйте декоратор square, который возводит возвращаемое значение декорируемой 
функции во вторую степень. 

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции 
является объект типа int или float.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с 
произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор square, но не код, вызывающий его.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3128671.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.9

Sample Input 1:
@square
def add(a, b):
    return a + b
print(add(3, 7))
Sample Output 1:
100

Sample Input 2:
@square
def add(a, b):
    'прекрасная функция'
    return a + b
print(add(1, 1))
print(add.__name__)
print(add.__doc__)
Sample Output 2:
4
add
прекрасная функция
'''
from functools import wraps

def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)**2
    return wrapper

if __name__ == '__main__':
    @square
    def add(a, b):
        return a + b
    print(add(3, 7))

    @square
    def add(a, b):
        '''прекрасная функция'''
        return a + b
    print(add(1, 1))
    print(add.__name__)
    print(add.__doc__)