'''
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв " a" (регистр не важен), на слово " argh".

Примечание:
Обратите внимание на параметр count у функции sub.
'''
import re
import sys

for line in sys.stdin:
	line = line.rstrip()
	#print(re.sub((r'\b(a|A)+\b'), 'argh', line,  count=1))
	#print(re.sub((r'\b[aA]+\b'), 'argh', line,  count=1))
	print(re.sub((r'\b(a)+\b'), 'argh', line,  count=1, flags=re.IGNORECASE))