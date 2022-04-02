'''
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
'''
import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	# out = re.match(r'\b((\w)(\w)(\w*))\b', line)
	# print(out.groups())
	# find = re.findall(r'\b((\w)(\w)(\w*))\b', line)
	# print(find)
	# res = re.sub(r'\b(\w)(\w)', r'\2\1', line)
	res = re.sub(r'\b((\w)(\w)(\w*))\b', r'\3\2\4', line)
	print(res)