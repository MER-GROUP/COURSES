'''
Функция numbers_sum()
Реализуйте функцию numbers_sum(), которая принимает один аргумент:

elems — список произвольных объектов

Функция должна возвращать сумму чисел (типы int и float), находящихся 
в списке elems, игнорируя все нечисловые объекты. Если в списке elems нет чисел, 
функция должна вернуть число 0.

Также функция должна иметь следующую строку документации:

Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию numbers_sum(), но не код, вызывающий ее. 

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/647292/tests_2681409.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.4/Module_9.4.11

Sample Input 1:
print(numbers_sum([1, '2', 3, 4, 'five']))
Sample Output 1:
8

Sample Input 2:
print(numbers_sum(['beegeek', 'stepik', '100']))
Sample Output 2:
0

Sample Input 3:
print(numbers_sum.__doc__)
Sample Output 3:
Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
'''
def numbers_sum(elems: list) -> int:
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
    return sum(filter(lambda x: isinstance(x, (int, float)), elems), start=0)

if __name__ == '__main__':
    print(numbers_sum([1, '2', 3, 4, 'five']))
    print(numbers_sum(['beegeek', 'stepik', '100']))
    print(numbers_sum.__doc__)