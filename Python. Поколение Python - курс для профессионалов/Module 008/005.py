'''
Функция triangle() 😥
Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:
h — натуральное число

Функция должна выводить звездный треугольник с высотой h в соответствии со следующим примером:
...
*****
****
***
**
*

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую 
функцию triangle(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылкам:
Архив с тестами
https://stepik.org/media/attachments/lesson/637962/tests_2618535.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_8/Module_8.2/Module_8.2.9

Sample Input 1:
triangle(3)
Sample Output 1:
***
**
*

Sample Input 2:
triangle(5)
Sample Output 2:
*****
****
***
**
*
'''
def triangle(h: int) -> None:
    def _rec(height: int) -> None:
        if 0 < height:
            print('*' * height)
            _rec(height-1)
    _rec(h)

if __name__ == '__main__':
    triangle(int(input()))