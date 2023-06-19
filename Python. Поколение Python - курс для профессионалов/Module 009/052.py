'''
Декоратор retry
Реализуйте декоратор retry, который принимает один аргумент:

times — натуральное число
Декоратор должен выполнять повторную попытку вызова декорируемой функции, 
если во время ее выполнения возникает ошибка. Декоратор должен вызывать ее 
до тех пор, пока не исчерпает количество попыток times, после чего должен 
возбуждать исключение MaxRetriesException.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор retry, но не код, вызывающий его. 

Примечание 3. Тестовые данные доступны по ссылкам:

PS:
Нужно выполнять функцию times раз, а потом бросать исключение, если не получилось.

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129782.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.25

class MaxRetriesException(Exception):
    pass

Sample Input 1:
@retry(3)
def no_way():
    raise ValueError
try:
    no_way()
except Exception as e:
    print(type(e))
Sample Output 1:
<class '__main__.MaxRetriesException'>

Sample Input 2:
@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')
beegeek()
Sample Output 2:
beegeek
'''
from functools import wraps

class MaxRetriesException(Exception):
    pass

def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator

if __name__ == '__main__':
    @retry(3)
    def no_way():
        raise ValueError
    try:
        no_way()
    except Exception as e:
        print(type(e))

    @retry(8)
    def beegeek():
        beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
        if beegeek.calls < 5:
            raise ValueError
        print('beegeek')
    beegeek()