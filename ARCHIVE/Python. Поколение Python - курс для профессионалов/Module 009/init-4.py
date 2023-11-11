print('------------------')

expression = '7 + 10'

result = eval(expression)

print(type(result))
print(result)

print('------------------')

expression1 = "print('Привет из функции eval()')"
expression2 = "len([1, 1, 1, 1, 1])"

result1 = eval(expression1)
result2 = eval(expression2)

print(result1)
print(result2)

print('------------------')

from math import pi

n = 10
nums = [1, 2, 3, 4, 5]

expression1 = "n + 7"
expression2 = "[i**2 for i in nums]"
expression3 = "pi / 2"

result1 = eval(expression1)
result2 = eval(expression2)
result3 = eval(expression3)

print(result1)
print(result2)
print(result3)

print('------------------')

# num = 17

# eval('if num == 10: print(num)')

print('------------------')

list_data = eval("['Python', 'C#', 'Java']")
tuple_data = eval('(1, 2, 3, 4, 5)')
dict_data = eval("{1: 'January', 2: 'February'}")

print(type(list_data), len(list_data))
print(type(tuple_data), max(tuple_data))
print(type(dict_data), dict_data[2])

print('------------------')

code = '''a = 10
b = 20
print(a + b)'''

exec(code)

print('------------------')

code = '100 + 10*7 - 14'

result = exec(code)

print(result)

print('------------------')

code1 = 'print(sorted([3, 5, 4, 1, 2]))'
code2 = 'print(sum([3, 5, 4, 1, 2]))'
code3 = 'print(len([3, 5, 4, 1, 2]))'

exec(code1)
exec(code2)
exec(code3)

print('------------------')

numbers = [1, 2, 3, 4, 5]
info = {'name': 'Timur', 'surname': 'Guev'}

code1 = '''total = 0
for i in numbers:
    total += i
print(total)'''
code2 = 'print(info["name"], info["surname"])'

exec(code1)
exec(code2)

print('------------------')