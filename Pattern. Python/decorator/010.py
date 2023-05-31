'''
Это упражнение на написание декоратора.

В первой части урока (https://stepik.org/lesson/63305) был приведён 
пример использования декораторов в виде декоратора memoized, реализующего мемоизацию.

У той реализации был существенный недостаток: нельзя было никак ограничить 
объём выделяемой памяти,  то есть объём словаря memory мог расти 
неограниченно с ростом количества вызовов задекорированной функции 
на каких-то новых наборах аргументов.

Давайте это исправим. Определите новый декоратор memoized с именованным 
параметром maxsize, по умолчанию установленным в None.

Если задекорировать какую-то функцию func при помощи memoized(maxsize=n), 
где n -- какое-то целое положительное число, то количество элементов  
в словаре memory не будет превышать n (при поступлении нового набора 
аргументов в ситуации, когда memory уже содержит n элементов, поступивший 
набор и значение функции на нём должны заменить последнюю добавленную 
в memory пару ключ-значение). Если же maxsize=None, то ограничения 
на количество элементов в словаре memory нет.

Напомню реализацию memoized из прошлого урока:

def memoized(func):
    
    memory = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]
        
    return wrapper

В рамках этого упражнения достаточно будет предложенного выше преобразования 
аргументов в ключи (иногда, понятное дело, ровно такое преобразование 
провернуть не получится, или его будет недостаточно)

from functools import wraps

def memoized(maxsize=None):
    '...'

Примеры ожидаемого поведения

@memoized(maxsize=2)
def sum_of_two(a, b):
    print(a, b, end='; ')
    return a + b

print(sum_of_two(2, 0), '\n')
print(sum_of_two(2, 0), '\n')

print(sum_of_two(4, 2), '\n')
print(sum_of_two(4, 2), '\n')

print(sum_of_two(5, 0), '\n')
print(sum_of_two(5, 0), '\n')

print(sum_of_two(4, 2)) 

>>> 2 0; 2 # впервые поступают аргументы (2, 0). Результат подсчитывается
2 # значение на (2, 0) уже есть в памяти. Результат возвращается сразу. 
В памяти один элемент

4 2; 6 # впервые поступают аргументы (4, 2). Результат подсчитывается
6 # значение на (4, 2) уже есть в памяти. Результат возвращается сразу. 
В памяти два элемента

5 0; 5 # впервые поступают аргументы (5, 0). Результат подсчитывается. 
Чтобы не превысить ограничение, последняя добавленная запись заменяется на новую
5  # значение на (5, 0) уже есть в памяти. Результат возвращается сразу. 
В памяти два элемента

4 2; 6 # предыдущий добавленный ключ (5, 0) заменил последний 
из добавленных перед ним ключей -- (4, 2), так что значение считалось 
заново. Кроме того, чтобы не превысить ограничение, запись на ключе (4, 2) 
заменяет последнюю добавленную перед ним -- запись на (5, 0). В памяти два элемента

@memoized(maxsize=None) # ограничений на объём выделяемой памяти нет
def sum_of_two(a, b):
    print(a, b)
    return a + b
    
print(sum_of_two(2, 0), '\n')
print(sum_of_two(2, 0), '\n')

print(sum_of_two(4, 2), '\n')
print(sum_of_two(4, 2), '\n')

print(sum_of_two(5, 0), '\n')
print(sum_of_two(5, 0), '\n')

print(sum_of_two(4, 2)) 

>>> 2 0; 2
2 

4 2; 6
6 

5 0; 5
5 

6 # не потребовалось пересчитывать значение функции на аргументах 4, 2
'''
from functools import wraps

def memoized(maxsize=None):
    def new_memoized(func):
        memory = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in memory:
                if maxsize is None:
                    memory[key] = func(*args, **kwargs)
                else:
                    if maxsize < len(memory)+1:
                        memory.pop(tuple(memory.keys())[-1])
                    memory[key] = func(*args, **kwargs)
            return memory[key]
        return wrapper
    return new_memoized

if __name__ == '__main__':
    @memoized(maxsize=2)
    def sum_of_two(a, b):
        print(a, b, end='; ')
        return a + b

    print(sum_of_two(2, 0), '\n')
    print(sum_of_two(2, 0), '\n')

    print(sum_of_two(4, 2), '\n')
    print(sum_of_two(4, 2), '\n')

    print(sum_of_two(5, 0), '\n')
    print(sum_of_two(5, 0), '\n')

    print(sum_of_two(4, 2)) 

    print('----------')

    # ограничений на объём выделяемой памяти нет
    @memoized(maxsize=None) 
    def sum_of_two(a, b):
        print(a, b)
        return a + b
        
    print(sum_of_two(2, 0), '\n')
    print(sum_of_two(2, 0), '\n')

    print(sum_of_two(4, 2), '\n')
    print(sum_of_two(4, 2), '\n')

    print(sum_of_two(5, 0), '\n')
    print(sum_of_two(5, 0), '\n')

    print(sum_of_two(4, 2)) 