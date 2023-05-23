'''
Функция cyclic_shift()
Реализуйте функцию cyclic_shift() с использованием аннотаций типов, 
которая принимает два аргумента в следующем порядке:

numbers — список целых или вещественных чисел
step — целое число

Функция должна изменять переданный список, циклически сдвигая 
элементы списка на step шагов, и возвращать значение None. 
Если step является положительным числом, сдвиг происходит вправо, 
если отрицательным — влево.

Примечание 1. Используйте встроенные типы (list, tuple, ...), а не 
типы из модуля typing. Также используйте нотацию |, а не тип Union из модуля typing.

Примечание 2. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию cyclic_shift(), но не код, вызывающий ее. 

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/655394/tests_2745410.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.6/Module_9.6.16

Sample Input 1:
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)
print(numbers)
Sample Output 1:
[5, 1, 2, 3, 4]

Sample Input 2:
numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)
print(numbers)
Sample Output 2:
[3, 4, 5, 1, 2]
'''
# def cyclic_shift(numbers: list[int|float], step: int) -> None:
#     for _ in range(abs(step)):
#         numbers.insert(
#             (len(numbers)-1, 0)[step > 0], 
#             numbers.pop((0, -1)[step > 0])
#         )

def cyclic_shift(numbers: list[int | float], step: int) -> None:
    for i in range(step % len(numbers)):
        numbers.insert(0, numbers.pop())

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    cyclic_shift(numbers, 1)
    print(numbers)

    numbers = [1, 2, 3, 4, 5]
    cyclic_shift(numbers, -2)
    print(numbers)