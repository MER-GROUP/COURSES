from random import random

rand=int(random()*900+100)
print('Случайное число = ',rand)
a=rand//100
print('a =',a)
b=(rand//10)%10
print('b =',b)
c=rand%10
print('c =',c)
print('sum =',a+b+c)