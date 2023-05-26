'''
Новый print
Напишите программу с использованием декоратора, которая 
переопределяет функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, 
чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. Не забывайте про то, что декоратор не должен поглощать 
возвращаемое значение декорируемой функции, а также должен уметь декорировать 
функции с произвольным количеством позиционных и именованных аргументов.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640039/tests_2717619.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.7/Module_9.7.20

Sample Input 1:
print('hi', 'there', end='!')
Sample Output 1:
HI THERE!

Sample Input 2:
print('are you in trouble?')
Sample Output 2:
ARE YOU IN TROUBLE?

Sample Input 3:
print(111, 222, 333, sep='xxx')
Sample Output 3:
111XXX222XXX333
'''
def decorator_print(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> str:
        _args = [str(i).upper() for i in args]
        _kwargs = {k: str(v).upper() for k, v in kwargs.items()}
        func(*_args, **_kwargs)
    return wrapper

if __name__ == '__main__':
    # @decorator_print # 1
    print = decorator_print(print) # 2
    print('hi', 'there', end='!')

    print('are you in trouble?')

    print(111, 222, 333, sep='xxx')