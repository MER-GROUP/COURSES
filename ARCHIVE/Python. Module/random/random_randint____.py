import random
from random import randint
from random import random

i=0
while i<10:
    i+=1
    result = randint (5, 6)
    print('result =',result)
print('------------')

i=0
while i<10:
    i+=1
    result = int(random()*6+5)
    print('result =',result)

print('--------------')
b=0
while b<10:
	b+=1
	result=int(random()*2+5)
	print('result =',result)