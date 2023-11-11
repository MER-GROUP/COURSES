'''
Функция is_greater()
Реализуйте функцию is_greater(), которая принимает два аргумента в следующем порядке:

lists — список, элементами которого являются списки целых чисел
number — целое число

Функция должна возвращать True, если хотя бы в одном вложенном списке 
из списка lists сумма всех элементов больше number, или False в противном случае.

Примечание 1. В задаче удобно воспользоваться функцией any().

Примечание 2. В тестирующую систему сдайте программу, содержащую только 
необходимую функцию is_greater(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640035/tests_2655749.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.1/Module_9.1.10

Sample Input 1:
data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))
Sample Output 1:
True

Sample Input 2:
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))
Sample Output 2:
False

Sample Input 3:
data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
print(is_greater(data, 3))
Sample Output 3:
False
'''
def is_greater(lists: list, number: int) -> bool:
    # return any(number < sum(i) for i in lists)
    return any(map(lambda x: number < sum(x), lists))

if __name__ == '__main__':
    data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
    print(is_greater(data, 10))
    data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    print(is_greater(data, 2))
    data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
    print(is_greater(data, 3))