from random import random

def Enter():
	try:
		df = input('Введи вещественное число : ')
		if 'q' == df:
			pass
		else:
			df = float(df)
	except ValueError:
		print('Некоректный ввод')
		df = None
	finally:
		return df
		
def Random():
	df = round(random() * 1000, 3)
	return df
	
def MaxDigit(df):
	max_ = 0
	df = str(df)
	for i in df:
		if '.' == i:
			continue
		else:
			if max_ < int(i):
				max_ = int(i)
	return max_

def Main():
	while True:
		print('---Main---')
		print('Ввод E или рандом R')
		check = None	
		while not ('r' == check or 'e' == check or 'R' == check or 'E' == check):
			check = input()
		if 'R' == check or 'r' == check:
			df = Random()
		else:
			df = None
			while df is None:
				df = Enter()
			if 'q' == df:
				break
		print(df)
		print(MaxDigit(df))
	
Main()