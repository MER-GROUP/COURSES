"""
Функция expand()
Реализуйте функцию expand(), которая принимает 
произвольное количество позиционных аргументов, 
каждый из которых является строкой,  
а так же один необязательный именованный аргумент sep, 
который является разделителем между объединенными 
строками и по умолчанию равный символу пробела.

Функция должна возвращать единственную строку, 
которая получается путем конкатенации всех переданных строк, 
умноженных на их количество и разделенных между собой разделителем sep.

Примечание 1. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию expand(), 
но не код, вызывающий ее.

Sample Input 1:
print(expand('bee', 'geek', sep='!'))
Sample Output 1:
beegeek!beegeek

Sample Input 2:
print(expand('Ti', 'mur', sep=' Guev '))
Sample Output 2:
Timur Guev Timur

Sample Input 3:
print(expand())
Sample Output 3:

Sample Input 4:
print(expand(sep='Hello!'))
Sample Output 4:
"""
from functools import reduce
import operator
def expand(*args, sep=' '):
    return str(sep).join(
        [(reduce(operator.add, args) if 0 < len(args) else '')] * len(args)
    )

print(expand('bee', 'geek', sep='!'))
print(expand('Ti', 'mur', sep=' Guev '))
print(expand())
print(expand(sep='Hello!'))
