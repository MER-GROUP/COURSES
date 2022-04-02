# аргументы функции по умолчанию
def printab_1(a, b):
	print(a)
	print(b)
	
def printab_2(a, b=20):
	print(a)
	print(b)
	
def printab_3(a = 10, b=20):
	print(a)
	print(b)
	
'''
# ошибка
def printab_4(a=10, b):
	print(a)
	print(b)
'''
	
print('----------')
printab_1(10, 20)
print('----------')
printab_2(10)
printab_2(10, 20)
print('----------')
printab_3()
printab_3(10, 20)
printab_3(10)
print('----------')