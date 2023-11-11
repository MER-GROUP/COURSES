print('------------------')

print(issubclass(IndexError, LookupError))
print(issubclass(KeyError, Exception))
print(issubclass(ZeroDivisionError, ArithmeticError))

print(issubclass(IndexError, ArithmeticError))
print(issubclass(FloatingPointError, OverflowError))

print('------------------')

try:
    nums = [10, 5, 20, 25]
    print(nums[100])
except Exception:
    print('Произошла ошибка!')
except (KeyError, IndexError):
    print('Ошибка связанная с индексом!')

print('------------------')

try:
    nums = [10, 5, 20, 25]
    print(nums[100])
# записываем сгенерированное исключение в переменную err
except (KeyError, IndexError) as err:    
    print(err)
    print(type(err))

print('------------------')

try:
    print(1 / 0)
except ZeroDivisionError as err:
    print(dir(err))

print('------------------')

# try:
#     х = 1 / 0
# except as err:
#     print(err)

print('------------------')

try:
    х = 1 / 0
except Exception as err:
    print(err)

print('------------------')

from sys import exc_info

try:
    х = 1 / 0
except Exception as err:
    print(exc_info())

print('------------------')

print(dir(tuple))

print('------------------')

try:
    # возбуждение исключения вручную
    raise IndexError('ошибочка')             
except Exception as err:
    print(err)
    print(type(err)) 

print('------------------')

def get_month_name(index):
    if not str(index).isdigit():
        raise TypeError('Аргумент должен быть числом.')
    if index < 1 or index > 12:
        raise ValueError('Аргумент должен быть целым числом от 1 до 12.')
    ...

print('------------------')

try:
    x, y = 10, 0
    if y == 0:
        raise ZeroDivisionError('Произошло деление на ноль.')
except ZeroDivisionError as err:
    print(err)
    print(err.args)
    print(type(err.args))

print('------------------')

# try:
#     х = 1 / 0
# except Exception as err:
#    raise ZeroDivisionError('Описание исключения') from err

print('------------------')

# try:
#     х = 1 / 0
# except Exception as err:
#     # каким-то образом обработали перехваченное исключение
#     print(err) 
#     # пробрасываем исключение выше                 
#     raise                       

print('------------------')

# try:
#     х = 1 / 0
# except Exception as err:
#     # каким-то образом обработали перехваченное исключение
#     print(err) 
#     # пробрасываем исключение выше                 
#     raise                       

print('------------------')

try:
    raise ValueError('Произошла ошибка')
except ValueError as e:
    print(e)

print('------------------')

try:
    raise ValueError('Ой', 'Произошла ошибка')
except ValueError as e:
    print(e)

print('------------------')