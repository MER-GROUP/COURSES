'''
Декоратор prefix

Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:

string — произвольная строка
to_the_end — булево значение, по умолчанию равное False

Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. 
Если to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции 
является объект типа str.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции 
с произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только 
необходимый декоратор prefix, но не код, вызывающий его.

Примечание 4. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129776.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.17

Sample Input 1:
@prefix('€')
def get_bonus():
    return '2000'   
print(get_bonus())
Sample Output 1:
€2000

Sample Input 2:
@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'    
print(get_bonus())
Sample Output 2:
2000$$$
'''
from functools import wraps

def prefix(string='RUB', to_the_end=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                res = func(*args, **kwargs) + string
            else:
                res = string + func(*args, **kwargs)
            return res
        return wrapper
    return decorator

if __name__ == '__main__':
    @prefix('€')
    def get_bonus():
        return '2000'   
    print(get_bonus())

    @prefix('$$$', to_the_end=True)
    def get_bonus():
        return '2000'    
    print(get_bonus())