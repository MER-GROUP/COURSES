'''
Декоратор takes_positive
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, 
передаваемые в декорируемую функцию, являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, 
декоратор должен возбуждать исключение:

TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю

Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента 
обоим условиям или при наличии разных аргументов, несоответствующих 
разным условиям: TypeError, затем ValueError.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать возвращаемое 
значение декорируемой функции, а также должен уметь декорировать функции с 
произвольным количеством позиционных и именованных аргументов.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимый 
декоратор takes_positive, но не код, вызывающий его.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640039/tests_2723006.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.7/Module_9.7.24

Sample Input 1:
@takes_positive
def positive_sum(*args):
    return sum(args)  
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
Sample Output 1:
55

Sample Input 2:
@takes_positive
def positive_sum(*args):
    return sum(args)   
try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))
Sample Output 2:
<class 'ValueError'>

Sample Input 3:
@takes_positive
def positive_sum(*args):
    return sum(args)   
try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))
Sample Output 3:
<class 'TypeError'>
'''
def takes_positive(func):
    def wrapper(*args, **kwargs):
        try:
            if not all(map(lambda x: isinstance(x, int), args)):     
                raise TypeError
            elif not all(map(lambda x: isinstance(x, int), kwargs.values())):
                raise TypeError
            elif any(map(lambda x: 1 > int(x), args)):      
                raise ValueError
            elif any(map(lambda x: 1 > int(x), kwargs.values())):
                raise ValueError
            else:
                return func(*args, **kwargs)
        except TypeError:
            return TypeError
        except ValueError:
            return ValueError
    return wrapper

if __name__ == '__main__':
    @takes_positive
    def positive_sum(*args):
        return sum(args)  
    print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    @takes_positive
    def positive_sum(*args):
        return sum(args)   
    try:
        print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
    except Exception as err:
        print(type(err))

    @takes_positive
    def positive_sum(*args):
        return sum(args)   
    try:
        print(positive_sum('10', 20, 10))
    except Exception as err:
        print(type(err))

    # test 10 (ans: <class 'ValueError'>)
    @takes_positive
    def positive_sum(*args, **kwargs):
        return sum(args) + sum(kwargs.values())
    try:
        print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=-40))
    except Exception as err:
        print(type(err))