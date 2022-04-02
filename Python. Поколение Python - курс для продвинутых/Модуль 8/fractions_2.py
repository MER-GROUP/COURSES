# Тип данных Fraction
# Для работы с рациональными числами в Python используется тип данных Fraction. Тип данных Fraction как и Decimal реализован программно, поэтому он в разы медленнее встроенных числовых типов данных int и float. Тип данных Fraction неизменяемый. Операции над данными этого типа приводят к созданию новых объектов, при этом старые не меняются.

# Чтобы использовать возможности типа данных Fraction нужно предварительно подключить модуль fractions:
from fractions import Fraction

# Создание Fraction
# Создать Fraction число можно несколькими способами:
'''
	из целых чисел, передав значения числителя и знаменателя дроби,
	из строки на основании десятичного представления;
	из строки на основании обыкновенной дроби;
	из числа с плавающей точкой (не рекомендуется).
'''

# Приведенный ниже программный код создает Fraction числа на основе целых чисел и строк:
print('********************')
from fractions import Fraction
# 3 - числитель, 4 - знаменатель
num1 = Fraction(3, 4)
num2 = Fraction('0.55')
num3 = Fraction('1/9')
print(num1, num2, num3, sep='\n')

# Нужно быть очень внимательным при создании Fraction чисел из чисел с плавающей точкой (float), потому что float числа округляются внутри до ближайшего возможного, а Fraction об этом ничего не знает, поэтому копирует содержимое float.
# Приведенный ниже программный код создает Fraction число на основе числа с плавающей точкой:
print('********************')
from fractions import Fraction

num = Fraction(0.34)
print(num)
# вместо ожидаемого вывода: 17/50
# код выводит: 6124895493223875/18014398509481984

# Не рекомендуется создавать Fraction числа из float чисел. В Fraction попадет уже неправильно округленное число. Создавать Fraction числа нужно из целых чисел, либо из строк!
# Обратите внимание на то, что при создании рационального числа Fraction, автоматически происходит сокращение числителя и знаменателя дроби.
print('********************')
from fractions import Fraction

num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')
print(num1, num2, num3, sep='\n')

# Так же стоит обратить внимание на вывод дробей, являющихся целыми числами.
print('********************')
from fractions import Fraction
# 5/1 = 5
num1 = Fraction(5, 1)
# 23/23 = 1
num2 = Fraction(23, 23)
print(num1, num2, sep='\n')

# Сравнение Fraction чисел
# Fraction числа можно сравнивать между собой точно так же, как и любые другие числа. Доступны 66 основных операторов сравнения:
'''
	>: больше;
	<: меньше;
	>=: больше либо равно;
	<=: меньше либо равно;
	==:  в точности равно;
	!=: не равно.
'''
print('********************')
from fractions import Fraction

num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8
print(num1 == num2)
print(num1 != num4)
print(num2 > num3)
print(num4 <= num1)
print(num1 < num5)
print(num6 > num4)
# Обратите внимание на то, что мы можем сравнивать Fraction числа и целые числа (числа с плавающей точкой) без явного приведения типов.

 # Арифметические операции над Fraction числами 
 # Тип данных Fraction отлично интегрирован в язык Python. С Fraction числами работают все привычные операции: сложение, вычитание, умножение, деление, возведение в степень.
print('********************')
from fractions import Fraction

num1 = Fraction('1/10')
num2 = Fraction('2/3')
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# Мы также можем совершать арифметические операции над Fraction и целыми числами (миксовать Fraction и int), но не рекомендуется смешивать их с float.
print('********************')
from fractions import Fraction

num = Fraction('3/8')
print(num + 1)
print(num - 1)
print(num * 2)
print(num ** 4)

# Обратите внимание, на то, что операция возведения в степень (**) для Fraction чисел может возвращать вещественный результат.
print('********************')
from fractions import Fraction

num1 = Fraction('3/8')
num2 = Fraction('1/2')
print(num1 ** num2)

# Математические функции
# Fraction числа можно передавать как аргументы функций, ожидающих float. Тогда они будут преобразованы во float. К примеру, модуль math оперирующий float числами, может работать и с Fraction числами.
print('********************')
from fractions import Fraction
from math import *

num1 = Fraction('1.44')
num2 = Fraction('0.523')
print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))
# Важно понимать, что результатом работы функций модуля math являются float числа, а не Fraction.

# Свойства numerator и denominator
# Для получения числителя и знаменателя Fraction числа используются свойства numerator и denominator.
print('********************')
from fractions import Fraction

num = Fraction('5/16')
print('Числитель дроби равен:', num.numerator)
print('Знаменатель дроби равен:', num.denominator)

# В Python 3.8 появился метод as_integer_ratio(), который возвращает кортеж, состоящий из числителя и знаменателя данного Fraction числа.
print('********************')
from fractions import Fraction

num = Fraction('-5/16')
print(num.as_integer_ratio())

# Метод limit_denominator()
# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь, чей знаменатель не превосходит переданного аргумента
print('********************')
from fractions import Fraction
import math

print('PI =', math.pi)
num = Fraction(str(math.pi))
print('No limit =', num)
for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)
# Метод limit_denominator() позволяет получить очень точные рациональные приближения иррациональных чисел, что очень удобно во многих математических задачах.

# Примечания
# Примечание 1. Для того, чтобы каждый раз не писать название типа, можно использовать следующий код:
print('********************')
from fractions import Fraction as F

num1 = F('1/5') + F('3/2')
num2 = F('1/4') * F('2/5')
print(num1)
print(num2)

# Примечание 2. В Python нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction. 
'''
from decimal import Decimal
from fractions import Fraction

num1 = Decimal('12.5')
num2 = Fraction(19, 3)

print(num1 + num2)
'''
# приводит к ошибке:
# TypeError: unsupported operand type(s) for +: 'Decimal' and 'Fraction'