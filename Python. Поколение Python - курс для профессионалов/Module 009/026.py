'''
Функция power()
Реализуйте функцию power(), которая принимает один аргумент:

degree — целое число

Функция power() должна возвращать функцию, которая принимает 
в качестве аргумента целое число x и возвращает значение x в степени degree.

Примечание 1. Рассмотрим пример из первого теста. Вызов power(2) 
возвращает функцию, которая принимает в качестве аргумента число и 
возводит его во вторую степень. Функция присваивается переменной square. 
Далее полученная функция вызывается с аргументом 5 и возвращает значение 5^2 = 25.

Примечание 2. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию power(), но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/651459/tests_3131750.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.5/Module_9.5.16

Sample Input 1:
square = power(2)
print(square(5))
Sample Output 1:
25

Sample Input 2:
print(power(3)(3))
Sample Output 2:
27

Sample Input 3:
result = power(4)(2)
print(result)
Sample Output 3:
16
'''
def power(degree: int):
    return lambda x: x**degree

if __name__ == '__main__':
    square = power(2)
    print(square(5))