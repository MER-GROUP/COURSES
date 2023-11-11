'''
Декоратор trace
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой 
функции во время ее выполнения, а именно: имя функции, переданные аргументы и 
возвращаемое значение в следующем формате:

TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, 
<словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с 
произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор trace, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_2723218.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.11

Sample Input 1:
@trace
def say(name, line):
    return f'{name}: {line}'
say('Jane', 'Hello, World')
Sample Output 1:
TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
TRACE: возвращаемое значение say(): 'Jane: Hello, World'

Sample Input 2:
@trace
def sub(a, b, c):
    'прекрасная функция'
    return a - b + c
    
print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)
Sample Output 2:
sub
прекрасная функция
TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
TRACE: возвращаемое значение sub(): 25
'''
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res = (res, f"'{res}'")[isinstance(res, str)]
        print(f'TRACE: вызов {wrapper.__name__}() с аргументами: {args}, {kwargs}',
            f'TRACE: возвращаемое значение {wrapper.__name__}(): {res}', sep='\n')
        return res.replace("'", "") if isinstance(res, str) else res
    return wrapper

if __name__ == '__main__':
    @trace
    def say(name, line):
        return f'{name}: {line}'
    say('Jane', 'Hello, World')

    @trace
    def sub(a, b, c):
        '''прекрасная функция'''
        return a - b + c
    print(sub.__name__)
    print(sub.__doc__)
    sub(20, 5, c=10)

    @trace
    def beegeek():
        '''beegeek docs'''
        return 'beegeek'

    print(beegeek())    
    print(beegeek.__name__)
    print(beegeek.__doc__)

