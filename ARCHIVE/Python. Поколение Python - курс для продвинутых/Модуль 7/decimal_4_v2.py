from decimal import *

num = Decimal(input())
cyphers = num.as_tuple().digits

print(max(cyphers) + min(cyphers) * (abs(num) >= 1))