'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
'''
import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	#res = re.sub(r'(\w)(\1{1,})', r'\1', line)
	res = re.sub(r'(\w)(\1)+', r'\1', line)
	print(res)