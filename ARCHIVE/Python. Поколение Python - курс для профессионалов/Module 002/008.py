'''
Функция index_of_nearest()
Реализуйте функцию index_of_nearest(), 
которая принимает два аргумента в следующем порядке:

numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее 
по значению число к числу number и возвращать его индекс. 
Если список numbers пуст, функция должна вернуть число − 1.

Примечание 1. Если в функцию передается список, 
содержащий несколько чисел, одновременно являющихся ближайшими 
к искомому числу, функция должна возвращать наименьший 
из индексов ближайших чисел.

Примечание 2. Рассмотрим третий тест. Ближайшими числами 
к числу 4 являются 5 и 3, имеющие индексы 1 и 2 соответственно. 
Наименьший из индексов равен 1.

Примечание 3. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию index_of_nearest(), 
но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310065.zip

Sample Input 1:
print(index_of_nearest([], 17))
Sample Output 1:
-1

Sample Input 2:
print(index_of_nearest([7, 13, 3, 5, 18], 0))
Sample Output 2:
2

Sample Input 3:
print(index_of_nearest([9, 5, 3, 2, 11], 4))
Sample Output 3:
1

Sample Input 4:
print(index_of_nearest([7, 5, 4, 4, 3], 4))
Sample Output 4:
2
'''
def index_of_nearest(numbers: list, number: int) -> int:
    num_1 = numbers[0] if 0 < len(numbers) else -1
    diff_1 = abs(numbers[0] - number) if 0 < len(numbers) else -1
    idx_1 = numbers.index(num_1) if 0 < len(numbers) else -1

    for i in range(1, len(numbers)):
        if (diff_1 > abs(numbers[i] - number)):
            num_1 = numbers[i]
            diff_1 = abs(numbers[i] - number)
            idx_1 = numbers.index(num_1)

    return idx_1

if __name__ == '__main__':
    print(index_of_nearest([], 17))
    print(index_of_nearest([7, 13, 3, 5, 18], 0))
    print(index_of_nearest([9, 5, 3, 2, 11], 4))
    print(index_of_nearest([7, 5, 4, 4, 3], 4))