from math import sqrt

a=float(input('Введите первый '
                        'катет а : '))
b=float(input('Введите второй '
                        'катет b : '))
c=sqrt(a**2+b**2)
print('Длина с ={0:.2f}'.format(round(c,2)))
'''
print('Площадь пр. треугольника : ',
          round((a*b)/2,2))
'''
print('Площадь пр. '
          'треугольника : {0:.2f}'.format
          ((a*b)/2))
print('Периметр пр. треугольника : ',
          round(a+b+c,2))