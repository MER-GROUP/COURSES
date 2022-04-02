def Enter():
	try:
		d = input()
		if 'q' == d:
			pass
		else:
			if '0' == d[0] and 1 < len(d):
				#print('test1')
				raise ValueError
			elif d[ : 2] in ('-0', '+0') and 2 < len(d):
				#print('test2')
				raise ValueError
			elif 0 < d.find('.'):
				raise ValueError
			else:
				d = int(d)
				if 0 <= d <= 1:
					raise ValueError
	except ValueError:
		if type(str()) == type(d):
			print('Некоректный ввод')
		else:
			print('0 и 1 неотносятся к простым и состпвным числам')
		d = None
	finally:
		return d
		
def EnterArr(d):
	arr = [i for i in range(d + 1)]
	arr[1] = 0
	return arr
	
def Eratos(arr):
	i = 2
	n = len(arr) - 1
	while i <= n:
		if not 0 == arr[i]:
			j = i + i
			while j <= n:
				arr[j] = 0
				j = j + i
		i += 1
		
def EratosSet(arr):
	for i in range(arr.count(0)):
		arr.remove(0)

def Main ():
	while True:
		print('---Main---')
		d = None
		while d is None:
			d = Enter()
		if 'q' == d:
			break
		else:
			#print('else')
			arr = EnterArr(d)
			print(arr)
			Eratos(arr)
			print(arr)
			EratosSet(arr)
			print(arr)
		
Main()