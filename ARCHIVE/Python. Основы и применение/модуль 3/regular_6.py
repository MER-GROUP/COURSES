# регулярные выражения
import re

# регулярные выражения с флагами
print('----- re.IGNORECASE -----')
match = re.match(r'text', 'TEXT', re.IGNORECASE)
print(match)

# регулярные выражения с флагами
print('----- re.DEBUG -----')
match = re.match(r'(te)*?xt', 'TEXT', re.IGNORECASE | re.DEBUG)
print(match)