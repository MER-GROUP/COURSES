from random import random

rand=int(random()*900+100)
rand=str(rand)
print('rand =',rand)

i=0
sum=0
print('длина строки =',len(rand))

while i<len(rand):
	sum+=int(rand[i])
	i+=1
print('sum =',sum)