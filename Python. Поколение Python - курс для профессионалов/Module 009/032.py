'''
Функция top_grade()
Реализуйте функцию top_grade() c использованием аннотаций типов, 
которая принимает один аргумент:

grades — словарь, содержащий данные об ученике, а именно имя 
по ключу name и список оценок по ключу grades

Функция должна возвращать словарь, содержащий имя ученика 
по ключу name и его самую высокую оценку по ключу top_grade.

Примечание 1. Используйте встроенные типы (list, tuple, ...), 
а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В возвращаемом функцией словаре сначала должно 
следовать имя, а затем — самая высокая оценка.

Примечание 3. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию top_grade(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/655394/tests_2745412.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.6/Module_9.6.15

Sample Input 1:
info = {'name': 'Timur', 'grades': [30, 57, 99]}
print(top_grade(info))
Sample Output 1:
{'name': 'Timur', 'top_grade': 99}

Sample Input 2:
print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))
Sample Output 2:
{'name': 'Ruslan', 'top_grade': 86}

Sample Input 3:
annotations = top_grade.__annotations__
print(annotations['grades'])
Sample Output 3:
dict[str, str | list[int]]
'''
def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    ...

if __name__ == '__main__':
    info = {'name': 'Timur', 'grades': [30, 57, 99]}
    print(top_grade(info))

    print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))

    annotations = top_grade.__annotations__
    print(annotations['grades'])