from decimal import *
s = input()
if '-' == s[0]: s = s[1:]
num = Decimal(s[::-1])
# print(num)

print(min(num.as_tuple().digits) + max(num.as_tuple().digits))

# print(num.as_tuple().digits)