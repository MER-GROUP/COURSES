'''
Напишите функцию is_num, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает значение True, если переданный аргумент является числом (целым или вещественным) и False в противном случае.

Примечание 1. Следующий программный код:
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))

должен выводить:
False
True
True
True
True
False
False
True
False

Примечание 2. Используйте вспомогательную функцию из прошлого степа.

Примечание 3. Вызывать анонимную функцию не нужно.
'''
# Решение
# is_num = ...
is_num = lambda x: str(x).isdecimal() or \
    (
        1 >= str(x).count('.') and \
        1 >= str(x).count('-') and \
        all(str(i).isdigit() for i in x if not i in '.-') and \
        not '-' in x[1 : ]
    )

print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print('---------------------')
print(is_num('.-111'))
print(is_num('111-'))