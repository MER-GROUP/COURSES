'''
Функция number_of_frogs()
В первый год в пруду живет 77 лягушек. Каждый год 
из пруда вылавливают 30 лягушек, а оставшиеся размножаются, 
и их становится в три раза больше. Так, количество лягушек k-й год  
может быть описано формулой:

F_k = 3(F_{k-1} - 30)

Реализуйте функцию number_of_frogs() с использованием рекурсии, 
которая принимает один аргумент:

year — натуральное число

Функция должна возвращать единственное число — количество 
лягушек в пруду в году year.

Примечание 1. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию number_of_frogs(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/594137/tests_2429328.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.3/Module_8.3.8

Sample Input 1:
print(number_of_frogs(2))
Sample Output 1:
141

Sample Input 2:
print(number_of_frogs(10))
Sample Output 2:
629901

Sample Input 3:
print(number_of_frogs(1))
Sample Output 3:
77
'''
def number_of_frogs(year: int) -> int:
    def rec(n: int = year) -> int:
        if 1 == n:
            return 77
        else:
            return 3 * (rec(n-1) - 30)
    return rec(year)

if __name__ == '__main__':
    print(number_of_frogs(2))