'''
Функция is_good_password() 👀
Назовем пароль хорошим, если

его длина равна 99 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

string — произвольная строка

Функция должна возвращать True, если строка string представляет 
собой хороший пароль, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию is_good_password(), но не код, вызывающий ее. 

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640052/tests_2712434.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.5/Module_7.5.7

Sample Input 1:
print(is_good_password('41157082'))
Sample Output 1:
False

Sample Input 2:
print(is_good_password('мойпарольсамыйлучший'))
Sample Output 2:
False

Sample Input 3:
print(is_good_password('МойПарольСамыйЛучший111'))
Sample Output 3:
True
'''
def is_good_password(string: str):
    _len = len(string)
    _upper = False
    _lower = False
    _digit = False

    for _chr in string:
        if _chr == _chr.lower() and not _chr.isdigit() and not _lower:
            _lower = True
        if _chr == _chr.upper() and not _chr.isdigit() and not _upper:
            _upper = True
        if _chr.isdigit() and not _digit:
            _digit = True
        if all((_upper, _lower, _digit)):
            break

    return (False, True)[all((_upper, _lower, _digit, 8 < _len))]

if __name__ == '__main__':
    print('---TEST-1---')
    print(is_good_password('41157111082'))
    print('---TEST-2---')
    print(is_good_password('мойпарольсамыйлучший'))
    print('---TEST-3---')
    print(is_good_password('МойПарольСамыйЛучший111'))