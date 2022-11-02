'''
Функция same_parity()
Реализуйте функцию same_parity(), которая принимает один аргумент:

numbers — список целых чисел
Функция должна возвращать новый список, элементами 
которого являются числа из списка numbers, имеющие 
ту же четность, что и первый элемент этого списка.

Примечание 1. Числа в возвращаемом функцией списке 
должны располагаться в своем исходном порядке. 

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию same_parity(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310059.zip

Sample Input 1:
print(same_parity([]))
Sample Output 1:
[]

Sample Input 2:
print(same_parity([6, 0, 67, -7, 10, -20]))
Sample Output 2:
[6, 0, 10, -20]

Sample Input 3:
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
Sample Output 3:
[-7, 67, -9, -29]
'''
def same_parity(numbers):
    check = numbers[0] % 2 if 1 <= len(numbers) else None
    return list(
        filter(
            lambda x: check == x % 2, 
            numbers
        )
    )

if __name__ == '__main__':
    print(same_parity([]))
    print(same_parity([6, 0, 67, -7, 10, -20]))
    print(same_parity([-7, 0, 67, -9, 70, -29, 90]))