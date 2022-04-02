'''
Вам дана последовательность строк.
Выведите строки, содержащие двоичную запись числа, кратного 3.
'''
import re
import sys

for line in sys.stdin:
	try:
		line = line.rstrip()
		#if re.match(r'([01])\1*', line):
		#if re.match(r'([01])+', line):
		#if re.match(r'([01])+$', line):
		if re.fullmatch(r'^(1(01*0)*1|0)*$', line[ : : -1]):
			'''
			digit = int(line, 2)
			#print('digit =', digit)
			if 0 == digit % 3:
				print(line)
			'''
			print(line)
	except ValueError:
		pass