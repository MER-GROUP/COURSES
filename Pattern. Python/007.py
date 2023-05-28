'''
Это упражнение на написание декоратора

Напишите декоратор introduce_on_debug, который делает так, 
что задекорированная функция печатает своё имя при вызове 
в стандартный поток вывода ("представляется"), но только 
если встроенная константа (https://docs.python.org/3/library/constants.html) 
__debug__ имеет значение True (то есть если программа 
не запущена с флажком оптимизации -o).

Чтобы было проще всё это проверять, используйте в теле 
декоратора вместо встроенной константы __debug__ просто переменную 
debug (её значение будет установлено за вас).

Версию с честным __debug__ вместо debug можете протестировать, 
запустив у себя программу с флажком -ο и без него

def introduce_on_debug('...'):
    '...'
        'if debug \ if not debug:'
    '...'

@introduce_on_debug
def identity(x):
    return x
    
# debug == False
identity(239)
>>> 239

# debug == True
identity(57)
>>> identity
57
'''
def introduce_on_debug():
    ...

@introduce_on_debug
def identity(x):
    return x

if __name__ == '__main__':
    # debug == False
    identity(239)

    # debug == True
    identity(57)