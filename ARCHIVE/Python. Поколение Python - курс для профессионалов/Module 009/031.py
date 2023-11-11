'''
Функция get_digits()
Реализуйте функцию get_digits() c использованием аннотаций типов, 
которая принимает один аргумент:

number — положительное целое или вещественное число

Функция должна возвращать список, состоящий из цифр числа number.

Примечание 1. Используйте встроенные типы (list, tuple, ...), 
а не типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. Порядок следования цифр в списке должен совпадать 
с порядком следования их в исходном числе.

Примечание 3. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию get_digits(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/655394/tests_2745411.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.6/Module_9.6.14

Sample Input 1:
print(get_digits(16733))
Sample Output 1:
[1, 6, 7, 3, 3]

Sample Input 2:
print(get_digits(13.909934))
Sample Output 2:
[1, 3, 9, 0, 9, 9, 3, 4]

Sample Input 3:
annotations = get_digits.__annotations__
print(annotations['return'])
Sample Output 3:
list[int]
'''
def get_digits(number: int|float) -> list[int]:
    return list(map(int, list(str(number).replace('.', ''))))

if __name__ == '__main__':
    print(get_digits(16733))
    print(get_digits(13.909934))
    annotations = get_digits.__annotations__
    print(annotations['return'])