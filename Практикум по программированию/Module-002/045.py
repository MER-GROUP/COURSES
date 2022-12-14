'''
Тип треугольника
Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) 
с данными сторонами.

Входные данные
Даны три натуральных числа – стороны треугольника.

Выходные данные
Необходимо вывести одно из слов: right для прямоугольного треугольника, 
acute для остроугольного треугольника, obtuse для тупоугольного треугольника 
или impossible, если входные числа не образуют треугольника.

Sample Input:
3
4
5
Sample Output:
right
'''
triangle = sorted(int(input()) for _ in range(3))
if triangle[-1] < sum(triangle[:-1]):
    if triangle[-1]**2 == sum(map(lambda x: x**2, triangle[:-1])):
        print('right')
    elif triangle[-1]**2 > sum(map(lambda x: x**2, triangle[:-1])):
        print('obtuse')
    else:
        print('acute')
else:
    print('impossible')