'''
Функция get_id()
В онлайн-школе BEEGEEK имя ученика считается корректным, если оно начинается 
с заглавной латинской буквы, за которой следуют строчные латинские буквы. 
Например, имена Timur и Yo считаются корректными, а имена timyrik, Yo17, TimuRRR нет. 
Также у каждого ученика имеется идентификационный номер, представленный натуральным числом, 
который выдается при поступлении в школу. К примеру, если в школе обучается 10 учеников, 
то новый прибывший ученик получит идентификационный номер равный 11.

Реализуйте функцию get_id(), которая принимает два аргумента:

names — список имен учеников, обучающихся в школе
name — имя поступающего ученика

Функция должна возвращать идентификационный номер, который получит поступающий в школу ученик, при этом

если имя ученика name не является строкой (тип str), функция должна возбуждать исключение:
TypeError('Имя не является строкой')

если имя ученика name является строкой (тип str), но не представляет собой корректное имя, 
функция должна возбуждать исключение:
ValueError('Имя не является корректным')

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию get_id(), но не код, вызывающий ее. 

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640051/tests_3104348.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.4/Module_7.4.19

Sample Input 1:
names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'
print(get_id(names, name))
Sample Output 1:
4

Sample Input 2:
names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'
try:
    print(get_id(names, name))
except ValueError as e:
    print(e)
Sample Output 2:
Имя не является корректным

Sample Input 3:
names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']
try:
    print(get_id(names, name))
except TypeError as e:
    print(e)
Sample Output 3:
Имя не является строкой
'''
def is_name(name: str) -> bool:
    _count_upper_chr = 0
    _count_digit = 0
    _is_start_upper = False
    
    for _chr in name:
        if _chr == _chr.upper() and not _chr.isdigit():
            _count_upper_chr += 1
        if _chr.isdigit():
            _count_digit += 1
        if _chr == _chr.upper() and not _chr.isdigit() and not _is_start_upper:
            _is_start_upper = True

    return all((1 == _count_upper_chr, not(_count_digit), _is_start_upper))

def get_id(names: list, name: str) -> int:
    try:
        if not isinstance(name, str):
            raise TypeError('Имя не является строкой')
        elif not is_name(name):
            raise ValueError('Имя не является корректным')
        else:
            return len(names) + 1
    except TypeError:
        # raise TypeError('Имя не является строкой') # or
        raise # or
    except ValueError:
        # raise ValueError('Имя не является корректным') # or
        raise # or
    
if __name__ == '__main__':
    print('---TEST-1---')
    names = ['Timur', 'Anri', 'Dima']
    name = 'Arthur'
    print(get_id(names, name))

    print('---TEST-2---')
    names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
    name = ['E', 'd', 'u', 'a', 'r', 'd']
    try:
        print(get_id(names, name))
    except TypeError as e:
        print(e)

    print('---TEST-3---')
    names = ['Timur', 'Anri', 'Dima', 'Arthur']
    name = 'Ruslan1337'
    try:
        print(get_id(names, name))
    except ValueError as e:
        print(e)