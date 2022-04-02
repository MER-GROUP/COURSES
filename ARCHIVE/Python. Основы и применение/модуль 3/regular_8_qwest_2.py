'''
Вам дана последовательность строк.
Выведите строки, содержащие " cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B (notalphanumeric or alphamumeric).
'''
import re
import sys

# \b набор символов notalphanumeric
# \B кроме символов alphamumeric
for line in sys.stdin:
	line = line.rstrip()
	#print(line)
	if re.search(r'\b(cat)\b', line):
		print(line)