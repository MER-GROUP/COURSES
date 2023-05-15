'''
Функция sort_priority() 🌶️
Реализуйте функцию sort_priority(), которая принимает 
два аргумента в следующем порядке:

values — список чисел
group — список, кортеж или множество чисел

Функция должна сортировать по неубыванию список чисел values, 
делая при этом приоритетной группу чисел из group, которая должна следовать первой.

Примечание 1. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию sort_priority(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/651459/tests_3131754.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.5/Module_9.5.20

PS:
Формулировка задачи кажется недостаточно четкой. 
Потребовалось время,  чтобы понять ее... В общем  так:  есть 2 группы  
товарищей  'блатные' (group) и общий список (values). Эти группы могут 
пересекаться,  а могут и нет.  Надо отсортировать общий список так, 
что бы 'блатные' (если они там есть) обслуживались  раньше простых смертных. 

Sample Input 1:
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)
Sample Output 1:
[2, 3, 5, 7, 1, 4, 6, 8]

Sample Input 2:
numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])
print(numbers)
Sample Output 2:
[200, 300, 50, 150, 1000, 20000]

Sample Input 3:
numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))
print(numbers)
Sample Output 3:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
def sort_priority(values: list, group: (list | tuple | set)):
    values.sort()
    def inner(arr):
        arr.sort(key=lambda x: (x not in group))
    inner(values)

if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {5, 7, 2, 3}
    sort_priority(numbers, group)
    print(numbers)

    numbers = [150, 200, 300, 1000, 50, 20000]
    sort_priority(numbers, [300, 100, 200])
    print(numbers)

    numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort_priority(numbers, (300, 100, 200))
    print(numbers)