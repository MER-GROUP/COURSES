# перевод текста в нижний регистр
print('-----lower-----')
s = 'Red Alert'
print(s.lower())
#print(s.lower.__doc__)

# перевод текста в верхний регистр
print('-----upper-----')
s = 'Red Alert'
print(s.upper())
#print(s.upper.__doc__)

# поиск и замена слов в тексте
print('-----replace-----')
s = 'Red, Alert, '
print(s.replace(', ', ' '))
print(s.replace(', ', ' ', 1))
#print(s.replace.__doc__)

# разбиение строки на заданному разделителю
print('-----split-----')
s = '1, 2, 3'
print(s.split(','))
print(s.split(',', 1))
s = '1    \t   2     \n    3        '
print(s.split())
#print(s.split.__doc__)

# вывод непечатаемых символов
print('-----repr-----')
print('   	main cool	   ')
print(repr('    \tmain cool\t   '))
#print(repr.__doc__)

# удаление пробелов (заданных сисволов) с обоих сторон
print('-----strip-----')
s = '     Red Aleet     '
print(s.strip())
print(repr(s.strip()))
s = '****     Red Aleet    ****'
print(s.strip('*'))
print(repr(s.strip('*')))
#print(s.strip.__doc__)

# удаление пробелов (заданных сисволов) с левой стороны
print('-----lstrip-----')
s = '     Red Aleet     '
print(s.lstrip())
print(repr(s.lstrip()))
s = '****     Red Aleet     ****'
print(s.lstrip('*'))
print(repr(s.lstrip('*')))
#print(s.lstrip.__doc__)

# удаление пробелов (заданных сисволов) с правой стороны
print('-----rstrip-----')
s = '     Red Aleet     '
print(s.rstrip())
print(repr(s.rstrip()))
s = '****     Red Aleet     ****'
print(s.rstrip('*'))
print(repr(s.rstrip('*')))
#print(s.rstrip.__doc__)

# создание строки из строковых итераторов
print('-----join-----')
n = map(str, [1, 2, 3, 4, 5])
print(next(n))
print(' '.join(n))
#print(' '.join.__doc__)