'''
Функция is_iterable()
Реализуйте функцию is_iterable(), которая принимает один аргумент:

obj — произвольный объект

Функция должна возвращать True, если объект obj является итерируемым объектом, 
или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию is_iterable(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/668595/tests_2768793.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.3/Module_10.3.14

Sample Input 1:
print(is_iterable(18731))
Sample Output 1:
False

Sample Input 2:
print(is_iterable('18731'))
Sample Output 2:
True

Sample Input 3:
objects = [(1, 13), 7.0004, [1, 2, 3]]
for obj in objects:
    print(is_iterable(obj))
Sample Output 3:
True
False
True
'''
def is_iterable(obj: callable) -> bool:
    return (False, True)[hasattr(obj, '__iter__')]

if __name__ == '__main__':
    print(is_iterable(18731))

    print(is_iterable('18731'))

    objects = [(1, 13), 7.0004, [1, 2, 3]]
    for obj in objects:
        print(is_iterable(obj))