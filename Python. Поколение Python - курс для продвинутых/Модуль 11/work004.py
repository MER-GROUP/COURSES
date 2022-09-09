'''
Напишите функцию mean(), которая принимает произвольное количество аргументов и 
возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.

Примечание 1. Обратите внимание, что функция должна принимать не список, 
а именно произвольное количество аргументов.

Примечание 2. Функция должна игнорировать аргументы всех типов, кроме int или float.

Примечание 3. Следующий программный код:

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
должен выводить:

0.0
7.0
2.0
0.0
3.5
5.5
Примечание 4. Для проверки типа можно использовать встроенную функцию type().

Примечание 5. Вызывать функцию mean() не нужно, требуется только реализовать.
'''
def mean(*args):
    try:
        return(
            sum(
                filter(
                    lambda x: type(x)==int or type(x)==float, args
                    )
                )/sum(True for i in args if (type(i)==int or type(i)==float))
            )
    except (ZeroDivisionError):
        return float(0)

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))