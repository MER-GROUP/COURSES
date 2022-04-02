#входит ли подстрока в строку
print('-----in-----')
print('abc' in 'abcba')
print('abc' in 'abdef')

#индекс первого вхождения или -1
print('-----find-----')
print('deabc'.find('abc'))
print('deabc'.find('da'))
#print('abc'.find.__doc__)
print('deabc'.find('abc', 1))
print('deabc'.find('da', 1))

#индекс первого вхождения с конца строки или -1
print('-----rfind-----')
print('deabc'.rfind('abc'))
print('deabc'.rfind('da'))

#индекс первого вхождения или ValueError
print('-----index-----')
print('deabc'.index('abc'))
#print('deabc'.index('da'))

#индекс первого вхождения с конца строки или ValueError
print('-----rindex-----')
print('deabc'.rindex('abc'))
#print('deabc'.index('da'))

#проверка начало строки на вхождение
print('-----startswith-----')
print('Red Alert true forever'.startswith('Red Alert'))
print('Red Alert true forever'.startswith('red alert'))
#print('Red Alert true forever'.startswith.__doc__)
print('Red Alert true forever'.startswith('Red Alert', 0, 10))
print('Red Alert true forever'.startswith('Red Alert', 5, 10))
print('Red Alert true forever'.startswith(('Red Alert', 'Max', 'Shef')))
print('Max super man'.startswith(('Red Alert', 'Max', 'Shef')))
print('Nobody true forever'.startswith(('Red Alert', 'Max', 'Shef')))

#проверка конца строки на вхождение
print('-----endswith-----')
print('file.txt'.endswith('.txt'))
print('file.txt'.endswith('.png'))
#print('file.txt'.endswith.__doc__)

#количество вхождений в строку
print('-----count-----')
print('abcabcabc'.count('abc'))
print('ababa'.count('aba'))
print('abcabcabc'.count('z'))
#print('abcabcabc'.count.__doc__)