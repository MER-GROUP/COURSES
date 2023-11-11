'''
Декоратор repeat
Реализуйте декоратор repeat, который принимает один аргумент:

times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор repeat, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129778.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.19

Sample Input 1:
@repeat(3)
def say_beegeek():
    'documentation'
    print('beegeek') 
say_beegeek()
Sample Output 1:
beegeek
beegeek
beegeek

Sample Input 2:
@repeat(4)
def say_beegeek():
    'documentation'
    print('beegeek')   
print(say_beegeek.__name__)
print(say_beegeek.__doc__)
Sample Output 2:
say_beegeek
documentation
'''
from functools import wraps

# def repeat(times: int):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             [func(*args, **kwargs) for _ in range(times-1)]
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

def repeat(times):
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            for i in range(times):
                res = fun(*args, **kwargs)
            return res
        return wrapper
    return decorator

if __name__ == '__main__':
    @repeat(3)
    def say_beegeek():
        '''documentation'''
        print('beegeek') 
    say_beegeek()

    @repeat(4)
    def say_beegeek():
        '''documentation'''
        print('beegeek')   
    print(say_beegeek.__name__)
    print(say_beegeek.__doc__)