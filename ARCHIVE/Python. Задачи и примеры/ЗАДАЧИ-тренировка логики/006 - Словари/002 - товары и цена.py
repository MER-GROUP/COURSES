from random import random

def Global():
	global price
	price = float()

def FoodDict():
	return {'Apple' : round(random() * 8 + 3, 2),
	             'Orange' : round(random() * 8 + 3, 2),
	             'Pineaple' : round(random() * 8 + 3, 2),
	             'Mango' : round(random() * 8 + 3, 2),
	             'Banana' : round(random() * 8 + 3, 2)}
	             
def OutputDict(food):
	for key, value in food.items():
		print(key, '=', value)
	
def EnterStr():
	try:
		s = input('введи фрукт : ')
		if Check(s): pass
		elif not s.isalpha(): raise Exception
		else: s = s.capitalize()
	except Exception:
		print('некоректный ввод')
		s = None
	finally:
		return s
	
def EnterInt():
	try:
		d = int(input('введи количество : '))
	except ValueError:
		print('некоректный ввод')
		d = None
	finally:
		return d
	
def Check(s):
	if 'q' == s: return True
	else: return False
	
def Price(food, d, foods):
	try:
		global price
		if food in foods.keys():
			print(food, '=', foods.get(food))
			price += foods.get(food) * d
			#price += foods[food] 
			#temp = foods.get(food)
			#price += temp
		else: raise Exception
	except Exception:
		print('фрукта нет')

def Main():
	while True:
		print('----------Main()----------')
		foods = FoodDict()
		OutputDict(foods)
		food = None
		while food is None:
			food = EnterStr()
		print('вы ввели :', food)
		if Check(food): break
		d = None
		while d is None:
			d = EnterInt()
		print('вы ввели :', d)
		#Global()
		Price(food, d, foods)
	print('общая стоимость :', price)

Global()				
Main()