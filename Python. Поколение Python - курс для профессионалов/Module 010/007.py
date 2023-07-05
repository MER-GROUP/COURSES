'''
Функция get_min_max() 😳
Реализуйте функцию get_min_max(), которая принимает один аргумент:

iterable — итерируемый объект, элементы которого сравнимы между собой

Функция должна возвращать кортеж, в котором первым элементом является 
минимальный элемент итерируемого объекта iterable, вторым — максимальный 
элемент итерируемого объекта iterable. Если итерируемый объект iterable пуст, 
функция должна вернуть значение None.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию get_min_max(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640044/tests_3134601.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.2/Module_10.2.23

Sample Input 1:
iterable = iter(range(10))
print(get_min_max(iterable))
Sample Output 1:
(0, 9)

Sample Input 2:
iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))
Sample Output 2:
(1, 33)

Sample Input 3:
iterable = iter([])
print(get_min_max(iterable))
Sample Output 3:
None
'''
"""
В помощь с 11-м тестом:
1. При такой вот записи num_min = min(num_min, i) и то же самое 
для max -> Среднее время выполнения get_min_max: 1.5607 сек.

2. При обычном сравнении с if -> Среднее время выполнения get_min_max: 0.2956 сек.

Не знаю, почему так, но разница существенная
"""
'''
почему встроенные функции мин, макс, работают медленнее чем If?

if — это простая проверка, а min и max — функции, которые вычисляют соответствующие значения. 
Их исходный код можно посмотреть здесь, 
(https://github.com/python/cpython/blob/3406f8cce542ea4edf4153c0fac5216df283a9b1/Python/bltinmodule.c#L1732),
это расставит точки, почему они выполняются не очень быстро. 
Точнее даже сказать, что происходит многократный вызов этих функций, 
на что затрачивается время, хотя быстрее просто проверить с помощью if
'''
def get_min_max(data: iter) -> tuple[int]|None:
    _min, _max = float('inf'), float('-inf')
    data = iter(data)
    try:
        _min, _max = [next(data)] * 2
        for el in data:
            # _min = min(_min, el) # Time Limit Error
            # _max = max(_max, el) # Time Limit Error
            if _min > el: _min = el
            if _max < el: _max = el
    except StopIteration:
        pass
    return ((_min, _max), None)[_min==float('inf') and _max==float('-inf')]

# import copy

# def get_min_max(iterable):
#     try:
#         C=copy.deepcopy(iterable)
#         return(min(C),max(iterable))
#     except:return None

if __name__ == '__main__':
    iterable = iter(range(10)) # 1
    print(get_min_max(iterable))

    iterable = [6, 4, 2, 33, 19, 1] # 2
    print(get_min_max(iterable))

    iterable = iter([]) # 3
    print(get_min_max(iterable))

    data = iter(range(100_000_000)) # 11
    print(get_min_max(data))

    data = iter(['a', 'b', 'c', 'aaa', 'abc', 'cbc', 'bbb']) # 12
    print(get_min_max(data))