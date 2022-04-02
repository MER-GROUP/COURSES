'''Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
'''
import sys
import re

# ввод и вывод в консоль
for line in sys.stdin:
	line = line.rstrip()
	#if re.findall(r'(cat)[\w\s._@#₽&-+()/\%]*\1', line):
	if re.findall(r'(cat).*\1', line):
		print(line)