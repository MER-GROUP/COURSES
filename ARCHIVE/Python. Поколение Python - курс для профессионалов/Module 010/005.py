'''
Функция get_min_max() 😎
Реализуйте функцию get_min_max(), которая принимает один аргумент:

data — список произвольных объектов, сравнимых между собой

Функция должна возвращать кортеж, в котором первым элементом является индекс 
минимального элемента в списке data, вторым — индекс максимального элемента в списке data. 
Если список data пуст, функция должна вернуть значение None.

Примечание 1. Если минимальных / максимальных элементов несколько, следует вернуть индексы 
первого по порядку элемента.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию get_min_max(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640044/tests_2768651.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.2/Module_10.2.22

Sample Input 1:
data = [2, 3, 8, 1, 7]
print(get_min_max(data))
Sample Output 1:
(3, 2)

Sample Input 2:
data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))
Sample Output 2:
(0, 4)

Sample Input 3:
data = [9]
print(get_min_max(data))
Sample Output 3:
(0, 0)
'''
def get_min_max(data: list) -> tuple[int]|None:
    if data:
        _min, _max = float('inf'), float('-inf')
        i, i_min, i_max = [0] * 3
        for el in data:
            if _min > el:
                _min, i_min = el, i
            if _max < el:
                _max, i_max = el, i
            i += 1  
        return (i_min, i_max)
    return None

if __name__ == '__main__':
    data = [2, 3, 8, 1, 7]
    print(get_min_max(data))

    data = [1, 1, 2, 3, 8, 8]
    print(get_min_max(data))

    data = [9]
    print(get_min_max(data))