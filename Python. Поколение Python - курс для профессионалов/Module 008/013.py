'''
Функция range_sum()
Реализуйте функцию range_sum() с использованием рекурсии, 
которая принимает три аргумента в следующем порядке:

numbers — список целых чисел
start — целое неотрицательное число
end — целое неотрицательное число

Функция должна суммировать все числа из списка numbers 
от numbers[start] до numbers[end] включительно и возвращать полученный результат.

Примечание 1. Рассмотрим первый тест. Диапазону индексов [3;7] 
в переданном списке принадлежат числа ​4,5,6,7,8​, сумма которых равна:
4+5+6+7+8=30

Примечание 2. Гарантируется, что start <= end.

Примечание 3. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию range_sum(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429570.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.9

Sample Input 1:
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
Sample Output 1:
30

Sample Input 2:
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
Sample Output 2:
45

Sample Input 3:
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
Sample Output 3:
1
'''
def range_sum(numbers: list[int], start: int, end: int):
    def rec(arr: list = numbers, left: int = start, right: int = end):
        if left == right:
            return arr[left]
        return arr[left] + rec(arr, left+1, right)
    return rec(numbers, start, end)

if __name__ == '__main__':
    print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))