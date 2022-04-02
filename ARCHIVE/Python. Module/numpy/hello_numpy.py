import numpy
# создание одномерного массива из списка целых чисел
a = numpy.array([2, 3, 4])
print(a)
print(type(a))
# размерность массива (одномерный, двумерный и т.д.)
print(a.ndim)
print(type(a.ndim))
# размеры массива (число строк, столбцов и т.д )
print(a.shape)
print(type(a.shape))
# общее количество элементов
print(a.size)
print(type(a.size))
# создание двумерного массива из двух последовательностей чисел
b = numpy.array([(1.5, 2, 3), (4, 5, 6)])
#все числа имеют один тип - число с плавабщей точкой
print(b)
print(type(b))
print(b.ndim)
print(type(b.ndim))
print(b.shape)
print(type(b.shape))
print(b.size)
print(type(b.size))
# создание двумерного массива 3х2 заполненного нулями
z = numpy.zeros((3, 2))
print(z)
print(type(z))
# функция arange() аналогична функции range() но возвращает массив
print(numpy.arange(10, 30, 5))
print(type(numpy.arange(10, 30, 5)))
#генерирует 9 чисел на отрезке от 0 до 2 с равным шагом
print(numpy.linspace(0, 2, 9))
print(type(numpy.linspace(0, 2, 9)))
# заполнение двумерного массива
b = numpy.arange(12).reshape(4, 3)
print(b)
print(type(b))
# операции над массивами
a = numpy.array([10, 20, 30])
b = numpy.arange(3)
print(a)
print(b)
# арифметические операции над массивом выполняются поэлементно
print(a + b)
print(a - b)
# возводим массив в квадрат
print(a ** 2)
# вычисление синуса
print(2 *  numpy.sin(a))
# работа с булевыми операторами
print(20 > a)