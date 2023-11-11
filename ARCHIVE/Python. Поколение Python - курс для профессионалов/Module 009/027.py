'''
Функция generator_square_polynom()
Рассмотрим семейство функций — квадратных трехчленов. 
Все эти функции имеют один и тот же вид:

f(x) = ax^2 + bx + c

Реализуйте функцию generator_square_polynom(), 
которая принимает три аргумента в следующем порядке:

a — вещественное число, коэффициент a
b — вещественное число, коэффициент b
c — вещественное число, коэффициент c

Функция generator_square_polynom() должна возвращать функцию, 
которая принимает в качестве аргумента вещественное число x 
и возвращает значение выражения ax^2 + bx + c.

Примечание 1. Рассмотрим пример из первого теста. 
Вызов generator_square_polynom(1, 2, 1) возвращает функцию, 
соответствующую квадратному трехчлену x^2 + 2x + 1x. 
Функция присваивается переменной f. Далее полученная функция 
вызывается с аргументом 5 и возвращает значение 5^2+5⋅2+1=36.

Примечание 2. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию generator_square_polynom(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/651459/tests_3131751.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.5/Module_9.5.17

Sample Input 1:
f = generator_square_polynom(1, 2, 1)
print(f(5))
Sample Output 1:
36

Sample Input 2:
print(generator_square_polynom(9, 52, 64)(8))
Sample Output 2:
1056

Sample Input 3:
f = generator_square_polynom(26, 83, 22)
print(f(55))
Sample Output 3:
83237
'''
def generator_square_polynom(a: int, b: int, c: int):
    # def inner(x: int):
    #     return a * x**2 + b * x + c
    # return inner
    return lambda x: a * x**2 + b * x + c

if __name__ == '__main__':
    f = generator_square_polynom(1, 2, 1)
    print(f(5))