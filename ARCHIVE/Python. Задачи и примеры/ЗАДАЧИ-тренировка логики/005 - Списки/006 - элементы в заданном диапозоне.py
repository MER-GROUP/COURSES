from random import randint

count = int()

def Enter():
	try:
		global count
		d = None
		if 1 == count:
			d = input('Min : ')
		else:
			d = input('Max : ')
		if 'q' == d:
			pass
		else:
			d = int(d)
	except ValueError:
		print('Некоректный ввод')
		d = None
	finally:
		return d
		
def Output(arr):
	count = int(1)
	for i in arr:
		print(f'{i : 3d}', end=' ')
		if 0 == count % 5:
			print()
		count += 1
		
def Count(mini, maxi, arr):
	count = int(1)
	for i in arr:
		if mini <= i <= maxi:
			count += 1
	print(count)
	
def Main():
	while True:
		print('---Main---')
		global count
		count += 1
		mini = None
		while mini is None:
			mini = Enter()
		if 'q' == mini:
			break
		count += 1
		maxi = None
		while maxi is None:
			maxi = Enter()
		if 'q' == maxi:
			break
		count = 0
		arr = [randint(0, 100) for i in range(30)]
		Output(arr)
		Count(mini, maxi, arr)
		
Main()