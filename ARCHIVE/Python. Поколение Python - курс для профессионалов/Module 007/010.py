'''
Функция add_to_list_in_dict()
Реализуйте функцию add_to_list_in_dict() с использованием конструкции try-except, 
которая принимает три аргумента в следующем порядке:

data — словарь списков, то есть словарь, значением в котором является список
key — хешируемый объект
element — произвольный объект

Функция должна добавлять объект element в список по ключу key в словаре data. 
Если ключа key в словаре data нет, функция должна добавить его в словарь, 
присвоить ему в качестве значения пустой список и добавить в этот список объект element.

Примечание 1. Функция должна изменять переданный словарь и возвращать значение None.

Примечание 2. Элементы в список должны добавляться в конец.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию add_to_list_in_dict(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/744448/tests_3102368.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_7/Module_7.3/Module_7.3.21

Sample Input 1:
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'b', 7)
print(data)
Sample Output 1:
{'a': [1, 2, 3], 'b': [4, 5, 6, 7]}

Sample Input 2:
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
add_to_list_in_dict(data, 'c', 7)
print(data)
Sample Output 2:
{'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7]}
'''
def add_to_list_in_dict(data: dict, key: str, element: ...) -> None:
    try:
        data[key].append(element)
    except KeyError:
        data[key] = [element]

if __name__ == '__main__':
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    add_to_list_in_dict(data, 'c', 7)
    print(data)

    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    add_to_list_in_dict(data, 'b', 7)
    print(data)