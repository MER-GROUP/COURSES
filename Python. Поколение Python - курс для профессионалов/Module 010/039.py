'''
Функция filter_names()
Реализуйте генераторную функцию filter_names(), которая принимает три аргумента 
в следующем порядке:

names — список имен
ignore_char — одиночный символ
max_names — натуральное число

Функция должна возвращать генератор, порождающий max_names имён из списка names, 
игнорируя имена, которые

начинаются на ignore_char (в любом регистре)
содержат хотя бы одну цифру

Если max_names больше количества имен в списке names, то генератор должен породить 
все возможные имена из данного списка. 

Примечание 1. Имена в возвращаемом функцией генераторе должны располагаться в 
своем исходном порядке.

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию filter_names(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_2783806.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.7

Sample Input 1:
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))
Sample Output 1:
Timur Arthur Arina

Sample Input 2:
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 't', 20))
Sample Output 2:
Dima Arthur Arina German Ruslan

Sample Input 3:
data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']
print(*filter_names(data, 'A', 100))
Sample Output 3:
'''
from _collections_abc import Generator

def filter_names(names: list[str], ignore_char: chr, max_names: int) -> Generator:
    _names_ignore_char = (
        name 
        for name in names 
        if not str.lower(name[0]) == str.lower(ignore_char)
    )
    _names_ignore_digits = (
        name
        for name in _names_ignore_char
        if name.isalpha()
    )
    return (
        name
        for i, name in enumerate(_names_ignore_digits)
        if i < max_names
    )

if __name__ == '__main__':
    data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
    print(*filter_names(data, 'D', 3))

    data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
    print(*filter_names(data, 't', 20))

    data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']
    print(*filter_names(data, 'A', 100))