'''
Функция txt_to_dict()
Вам доступен файл planets.txt, содержащий информацию о различных планетах. В первых четырех 
строках указаны характеристики первой планеты, после чего следует пустая строка, затем характеристики 
второй планеты, и так далее:

Name = Mercury
Diameter = 4879.4
Mass = 3.302×10^23
OrbitalPeriod = 0.241

Name = Venus
Diameter = 12103.6
Mass = 4.869×10^24
OrbitalPeriod = 0.615

...

Реализуйте генераторную функцию txt_to_dict(), которая не принимает никаких аргументов.

Функция должна возвращать генератор, порождающий последовательность словарей, каждый из 
которых содержит информацию об очередной планете из файла planets.txt, а именно ее название, 
диаметр, массу и орбитальный период. Например:

{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}

Примечание 1. Указанный файл доступен по ссылке.
https://stepik.org/media/attachments/lesson/673155/planets.txt

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию txt_to_dict(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/673155/tests_2784370.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.7/Module_10.7.11

Sample Input:
planets = txt_to_dict()
print(next(planets))

Sample Output:
{'Name': 'Mercury', 'Diameter': '4879.4', 'Mass': '3.302×10^23', 'OrbitalPeriod': '0.241'}
'''
from _collections_abc import Generator

def txt_to_dict() -> Generator:
    # with open(file='043-planets.txt', mode='rt', encoding='utf-8', newline='') as file_open:
    with open(file='planets.txt', mode='rt', encoding='utf-8', newline='') as file_open:
        keys, values = list(), list()
        for _string in file_open:
            if not _string.strip():
                continue

            k, v = _string.split('=')
            keys.append(k.strip())
            values.append(v.strip())

            if 4 == len(keys):
                yield dict(zip(keys, values))
                keys, values = list(), list()

if __name__ == '__main__':
    planets = txt_to_dict()
    print(next(planets))
    print(next(planets))
    print(next(planets))
    print(next(planets))
    print(next(planets))
    print(next(planets))
    print(next(planets))
    print(next(planets))
    print(next(planets))