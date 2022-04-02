from random import randint

def Enter():
	try:
		d = input()
		if 'q' == d:
			pass
		else:
			d = int(d)
			if 0 == d:
				raise IndexError
	except ValueError:
		print('Некоректный ввод')
		d = None
	except IndexError:
		print('Некоректный ввод')
		d = None
	finally:
		return d

def Main():
	while True:
		print('---Main---')
		nArr = None
		while nArr is None:
			nArr = Enter()
		if 'q' == nArr:
			break
		else:
			arr = [randint(0, 100) for i in range(nArr)]
			print(arr)
			arr.sort()
			print('Min =', arr[0])
			print('Max =', arr[-1])
			print('Min =', min(i for i in arr))
			print('Max =', max(i for i in arr))
		
Main()