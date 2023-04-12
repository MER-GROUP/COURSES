'''
Функция linear()
Линеаризация — это процесс преобразования списка, который может содержать 
несколько уровней вложенных списков, в список, содержащий все те же элементы 
без какой-либо вложенности.

Например, список:

[1, [2, 3], [4, [5, 6, [7, 8, 9]]]]

после линеаризации будет иметь вид:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

Реализуйте linear() с использованием рекурсии, которая принимает один аргумент:

nested_lists — список, элементами которого являются целые числа или списки, 
элементами которых, в свою очередь, также являются либо целые числа, либо списки; 
вложенность может быть произвольной

Функция должна возвращать новый список, представляющий собой линеаризованный 
список nested_lists.

Примечание 1. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию linear(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594680/tests_2429560.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.4/Module_8.4.5

Sample Input 1:
my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))
Sample Output 1:
[3, 4, 5, 6, 7, 8]

Sample Input 2:
my_list = [10, 20, 30, 40, 50]
print(linear(my_list))
Sample Output 2:
[10, 20, 30, 40, 50]
'''
def linear(nested_lists: list) -> list:
    _list = list()
    def rec(arr: list = nested_lists) -> list:
        for i in arr:
            if isinstance(i, list):
                rec(i)
            else:
                _list.append(i)
    rec()
    return _list

if __name__ == '__main__':
    my_list = [3, [4], [5, [6, [7, 8]]]]
    print(linear(my_list))

    my_list = [10, 20, 30, 40, 50]
    print(linear(my_list))