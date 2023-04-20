'''
Функция zip_longest()
Как уже известно, функция zip() объединяет элементы различных последовательностей. 
Особенностью функции является то, что при передаче последовательностей 
различной длины элементы последовательности большей длины будут отброшены.

Реализуйте функцию zip_longest(), которая принимает переменное количество 
позиционных аргументов, каждый из которых является списком, и один необязательный 
именованный аргумент fill, имеющий значение по умолчанию None.

Функция должна объединять элементы переданных последовательностей в кортежи, 
аналогично функции zip(), и возвращать в виде списка, но если последовательности 
имеют различную длину, недостающие элементы последовательностей меньшей длины 
должны принимать значение fill.

Примечание 1. Рассмотрим первый тест со следующим вызовом:

zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_')

Первый список имеет длину 5, второй — 3, то есть элементам 4 и 5 из 
первого списка нет пар из второго списка. В таком случае, функция должна 
сопоставить им значение fill, равное '_'. Итак, результатом работы функции будет список:

[(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию zip_longest(), но не код, вызывающий ее. 

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640035/tests_2655751.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.1/Module_9.1.15

Sample Input 1:
print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
Sample Output 1:
[(1, 'a'), (2, 'b'), (3, 'c'), (4, '_'), (5, '_')]

Sample Input 2:
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))
Sample Output 2:
[(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', None), (4, None, None), (5, None, None)]

Sample Input 3:
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))
Sample Output 3:
[(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', 'III'), (4, 'four', 'IV'), (5, 'five', 'V')]
'''
def zip_longest(*args, fill: str = None) -> list:
    _max_list = len(max(args, key=len))
    for i in range(len(args)):
        if _max_list > len(args[i]):
            args[i].extend([fill] * (_max_list - len(args[i])))
    return list(zip(*args))
    

if __name__ == '__main__':
    print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
    data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
    print(zip_longest(*data))
    data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
    print(zip_longest(*data))