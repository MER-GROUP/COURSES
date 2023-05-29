'''
Это упражнение на написание декоратора.

Напишите декоратор optional_introduce, который делает так, 
что у задекорированной функции появляется дополнительный 
параметр introduce со значением False по умолчанию (именованный параметр), 
причём если функция вызвана с introduce=True, то она перед 
возвращением результата напечатает своё имя в стандартный 
поток вывода ("представится"), а если с introduce=False или 
без явного указания introduce вовсе, то она просто вернёт результат.

Мы предполагаем, что у исходной функции параметра с именем introduce не было.

def optional_introduce('...'):
    '...'


Примеры ожидаемого поведения

@optional_introduce
def identity(x):
    return x
        
print(identity(20))
>>> 20

print(identity(42, introduce=True))
>>> identity
42
'''
# def optional_introduce(func):
#     def wrapper(*args, **kwargs):
#         if 'introduce' in kwargs and kwargs['introduce']:
#             print(func.__name__)
#         return func(*args)
#     return wrapper

def optional_introduce(func):
    def wrapper(*args, introduce=False, **kwargs):
        if introduce:
            print(func.__name__)
        return func(*args, **kwargs)  
    return wrapper

@optional_introduce
def identity(x):
    return x

if __name__ == '__main__':
    print(identity(20))
    print(identity(42, introduce=True))
    print(identity(42, introduce=False))