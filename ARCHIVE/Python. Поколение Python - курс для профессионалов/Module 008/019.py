'''
Функция is_palindrome()
Реализуйте функцию is_palindrome() с использованием рекурсии, 
которая принимает один аргумент:

string — произвольная строка

Функция должна возвращать значение True, если переданная строка 
является палиндромом, или False в противном случае.

Примечание 1. Палиндром — текст, одинаково читающийся в обоих 
направлениях.

Примечание 2. Пустая строка является палиндромом, как и строка, 
состоящая из одного символа.

Примечание 3. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию is_palindrome(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429279.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.15

Sample Input 1:
print(is_palindrome('stepik'))
Sample Output 1:
False

Sample Input 2:
print(is_palindrome('level'))
Sample Output 2:
True

Sample Input 3:
print(is_palindrome('122333221'))
Sample Output 3:
True
'''
def is_palindrome(string: str) -> bool:
    def rec(s: str = string) -> bool:
        if 1 >= len(s):
            return True
        elif not s[0] == s[-1]:
            return False
        else:
            return rec(s[1:-1])
    return rec(string)

if __name__ == '__main__':
    print(is_palindrome('stepik'))
    print(is_palindrome('level'))
    print(is_palindrome('122333221'))