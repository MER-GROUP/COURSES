def Global():
	global price
	price = float()
	
def Foods():
	return {'Apple' : [4.5, 10],
				 'Orange' : [6.2, 5],
				 'Pineapple' : [10.0, 1],
				 'Mango' : [7.5, 2],
				 'Banana' : [3.8, 10]}
				 
def FoodsOut(foods):
	for k, v in foods.items():
		print(k, v[0], v[1])
		
def Check(s):
		return True if 'q' == s else False
		
def FoodEnter():
	try:
		s = input('введи название еды : ')
		if Check(s): pass
		elif not s.isalpha(): raise Exception
		else: s = s.capitalize()
	except Exception:
		print('некорректный ввод еды')
		s = None
	finally:
		return s
		
def FoodVolume():
	try:
		d = input('введи количество еды : ')
		if '0' == d[0] and 1 < len(d):
			raise Exception
		elif d[ : 2] in ('+0', '-0') and 2 < len(d):
			raise Exception
		else:
			d = int(d)
			if 0 > d: raise Exception
	except (ValueError, Exception):
		if type(d) == type(str):
			print('некоректный ввод количества еды')
		else:
			print('число не может быть отрицательным')
		d = None
	finally:
		return d
		
def FoodBuy(foods, food, volume):
	try:
		global price
		if foods.get(food)[1] < volume:
			print('такого количества нет')
		else:
			price += foods.get(food)[0] * volume
			foods.get(food)[1] -= volume
	except TypeError:
		print('Такой еды нет')
	
def Main():
	foods = Foods()
	while True:
		print('----------Main()----------')
		FoodsOut(foods)
		food = None
		while food is None:
			food = FoodEnter()
		if Check(food): break
		volume = None
		while volume is None:
			volume = FoodVolume()
		FoodBuy(foods, food, volume)
	FoodsOut(foods)
	print('всего заказано на сумму : ', price)
	
Global()
Main()