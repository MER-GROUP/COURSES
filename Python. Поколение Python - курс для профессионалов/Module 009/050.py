'''
Декоратор add_attrs
Реализуйте декоратор add_attrs, который принимает произвольное количество 
именованных аргументов и устанавливает их в качестве атрибутов декорируемой функции. 
Названием атрибута должно являться имя аргумента, значением атрибута — значение аргумента.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Вспомните про атрибут функции __dict__.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с произвольным 
количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор add_attrs, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640040/tests_3129783.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.8/Module_9.8.23

Sample Input 1:
@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'   
print(beegeek.attr1)
print(beegeek.attr2)
Sample Output 1:
bee
geek

Sample Input 2:
@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'  
print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
Sample Output 2:
bee
geek
beegeek
'''
from functools import wraps

def add_attrs(*argsz, **kwargsz):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__dict__.update(kwargsz)
        return wrapper
    return decorator

if __name__ == '__main__':
    @add_attrs(attr1='bee', attr2='geek')
    def beegeek():
        return 'beegeek'   
    print(beegeek.attr1)
    print(beegeek.attr2)

    @add_attrs(attr2='geek')
    @add_attrs(attr1='bee')
    def beegeek():
        return 'beegeek'  
    print(beegeek.attr1)
    print(beegeek.attr2)
    print(beegeek.__name__)