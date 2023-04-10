'''
Функция is_power()
Реализуйте функцию is_power() с использованием рекурсии, 
которая принимает один аргумент:

number — натуральное число

Функция должна возвращать значение True, если number является 
степенью числа 2, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию is_power(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2627571.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.13

Sample Input 1:
print(is_power(512))
Sample Output 1:
True

Sample Input 2:
print(is_power(15))
Sample Output 2:
False

Sample Input 3:
print(is_power(1))
Sample Output 3:
True
'''
def is_power(number: int) -> bool:
    def rec(n: int = number) -> bool:
        if 2 > n:
            if 1 == n:
                return True
            else:
                return False
        else:
            return rec(n/2)
    return rec(number)

if __name__ == '__main__':
    print(is_power(512))
    print(is_power(15))
    print(is_power(1))