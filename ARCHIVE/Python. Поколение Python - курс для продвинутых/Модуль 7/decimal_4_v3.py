from decimal import *

num = Decimal(input())
cyphers = num.as_tuple().digits

if '0' not in str(num):
	print(max(cyphers) + min(cyphers))
else:
	print(max(cyphers))