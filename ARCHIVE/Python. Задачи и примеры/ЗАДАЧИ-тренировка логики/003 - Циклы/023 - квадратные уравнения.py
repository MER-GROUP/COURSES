from math import sqrt

count = 0

def Enter():
	try:
		global count
		digit = None
		if 1 == count:
			digit = input('Enter a1 : ')
			#print(count)
		elif 2 == count:
			digit = input('Enter a2 : ')
		elif 3 == count:
			digit = input('Enter b1 : ')
		elif 4 == count:
			digit = input('Enter b2 : ')
		elif 5 == count:
			digit = input('Enter c1 : ')
		else:
			digit = input('Enter c2 : ')
		if 'q' == digit and 1 == count:
			pass
		elif '0' == digit[0] and 1 < len(digit) or digit[0:2] in ('+0', '-0') and 2<len(digit):
			raise ValueError
		else:
			digit = int(digit)
	except ValueError:
		print('Error input !')
		digit = None
	finally:
		return digit
		
def Check(a1, a2, b1, b2, c1, c2):
		check = False
		if a2 < a1:
			print('a2 не должно быть меньше a1')
			check = True
		if b2 < b1:
			print('b2 не должно быть меньше b1')
			check = True
		if c2 < c1:
			print('c2 не должно быть меньше c1')
			check = True
		return check
		
def Uravnenie0(a, b, c):
	print('---Uravnenie---')
	for i in a:
		if 0 == i:
			continue
		for j in b:
			for k in c:
				print(i, j, k, end=' ')
				d = j * j - 4 * i * k
				if 0 <= d:
					x1 = (-j - sqrt(d)) / 2 * i
					x2 = (-j + sqrt(d)) / 2 * i
					x1 = round(x1, 2)
					x2 = round(x2, 2)
					print('Yes', x1, x2)
				else:
					print('No')
		
def Uravnenie(a, b, c):
	print('---Uravnenie---')
	for i in a:
		if 0 == i:
			continue
		else:
			for j in b:
				for k in c:
					print(i, j, k, end=' ')
					d = j * j - 4 * i * k
					if 0 <= d:
						x1 = (-j - sqrt(d)) / 2 * i
						x2 = (-j + sqrt(d)) / 2 * i
						x1 = round(x1, 2)
						x2 = round(x2, 2)
						print('Yes', x1, x2)
					else:
						print('No')
						
def Uravnenie2(a, b, c):
	print('---Uravnenie---')
	for i in a:
	    if i == 0:
	        continue
	    for j in b:
	        for k in c:
	            print(i, j, k, end=' ')
	            D = j * j - 4 * i * k
	            if D >= 0:
	                x1 = (-j - sqrt(D)) / (2 * i)
	                x2 = (-j + sqrt(D)) / (2 * i)
	                x1 = round(x1, 2)
	                x2 = round(x2, 2)
	                print('Yes', x1, x2)
	            else:
	                print('No')

def Main():
	while True:
		global count
		count = 1
		a1 = None
		while a1 is None:
			a1 = Enter()
		if 'q' == a1:
			break
		count += 1
		a2 = None
		while a2 is None:
			a2 = Enter()
		count += 1
		b1 = None
		while b1 is None:
			b1 = Enter()
		count += 1
		b2 = None
		while b2 is None:
			b2 = Enter()
		count += 1
		c1 = None
		while c1 is None:
			c1 = Enter()
		count += 1
		c2 = None
		while c2 is None:
			c2 = Enter()
		#объекты диапазоны
		a = range(a1, a2 + 1)
		b = range(b1, b2 + 1)
		c = range(c1, c2 + 1)
		#print(type(a))
		if Check(a1, a2, b1, b2, c1, c2):
			continue
		Uravnenie0(a, b, c)
		
Main()