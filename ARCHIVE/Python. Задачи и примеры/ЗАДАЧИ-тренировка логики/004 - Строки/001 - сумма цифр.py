from random import  randint

def Sum(digit):
	sum = 0
	for i in digit:
		sum += int(i)
	print(sum)

def Main():
	print('---Main---')
	digit = str(randint(100, 999))
	print(digit)
	Sum(digit)
	
Main()