# bool в операторах if else
print('##########')
a = 100
b = 17

if b > a:
  print('b больше a')
else:
  print('b не больше a')
  
# bool и print
print('##########')
print(17 > 7)
print(17 == 7)
print(17 < 7)

# операторы and, or, not
print('##########')
a = True
b = False

print('a and b is', a and b)
print('a or b is', a or b)
print('not a is', not a)

# bool в виде чисел
print('##########')
print(True == 1)
print(False == 0)

# bool и арифметические операции
print('##########')
print(True + True + True - False)
print(True + (False / True))

# bool и арифметические операции
print('##########')
numbers = [1, 2, 3, 4, 5, 8, 10, 12, 15, 17]
res = 0

for num in numbers:
    res += (0 == num % 2)
print(res)