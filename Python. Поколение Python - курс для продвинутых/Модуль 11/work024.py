'''
Напишите функцию is_non_negative_num, используя синтаксис анонимных функций, 
которая принимает строковый аргумент и возвращает значение True, 
если переданный аргумент является неотрицательным числом (целым или вещественным) 
и False в противном случае.

Примечание 1. Следующий программный код:
print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))

должен выводить:
False
True
False
False
True
False
False
True

Примечание 2. Неотрицательные числа — это положительные числа и число нуль.

Примечание 3. Вызывать анонимную функцию не нужно.
'''
# Решение
# is_non_negative_num = ...
is_non_negative_num = lambda x: str(x).isdecimal() or \
                                (
                                    1 == str(x).count('.') and \
                                    not '-' in x and \
                                    all(str(i).isdigit() for i in x if not '.' == i)
                                )

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))

print('------------------------------------------------------')

is_non_negative_num = lambda q: str(q).replace('.', '', 1).isdigit()

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))