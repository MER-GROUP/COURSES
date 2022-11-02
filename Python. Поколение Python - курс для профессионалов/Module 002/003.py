'''
Функция is_valid()
Будем считать, что PIN-код является корректным, 
если он удовлетворяет следующим условиям:

состоит из 4, 5 или 6 символов
состоит только из цифр (0−9)
не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать значение True, если строка string 
представляет собой корректный PIN-код, или False в противном случае.

Примечание 1. Если в функцию передается пустая строка, 
функция должна возвращать значение False.

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию is_valid(), 
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310081.zip

Sample Input 1:
print(is_valid('4367'))
Sample Output 1:
True

Sample Input 2:
print(is_valid('92134'))
Sample Output 2:
True

Sample Input 3:
print(is_valid('89abc1'))
Sample Output 3:
False

Sample Input 4:
print(is_valid('900876'))
Sample Output 4:
True

Sample Input 5:
print(is_valid('49 83'))
Sample Output 5:
False
'''
def is_valid(string: str) -> bool:
    return string.isdigit() and 4 <= len(string) <= 6

if __name__ == '__main__':
    print(is_valid('4367'))
    print(is_valid('92134'))
    print(is_valid('89abc1'))
    print(is_valid('900876'))
    print(is_valid('49 83'))
    print(is_valid(''))
    print(is_valid(' '))
