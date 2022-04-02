from random import random,randint

def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
		
while True:
	iMin=input('Введите целое число 1 : ')
	if iMin=='q':
		break
	iMax=input('Введите целое число 2 : ')
	if iMin.isdigit() and iMax.isdigit():
		iMin=int(iMin)
		iMax=int(iMax)
		'''
		if iMin>iMax:
			tmp=iMax
			iMax=iMin
			iMin=tmp
		'''
		if iMin>iMax:
			iMin,iMax=iMax,iMin
		print('randint =',randint(iMin,iMax))
	fMin=input('Введите дроб. число 1 : ')
	fMax=input('Введите дроб. число 2 : ')
	if isFloat(fMin) and isFloat(fMax):
		fMin=float(fMin)
		fMax=float(fMax)
		if fMin>fMax:
			tmp=fMax
			fMax=fMin
			fMin=tmp
		print('random =',random()*(fMax-
		          fMin)+fMin)
	else:
		print('Некоректный ввод')
 