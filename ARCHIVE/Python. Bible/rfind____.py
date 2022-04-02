#ищет индекс с конца строки
s = 'foo bar foo baz'
print(s.rfind('oo'))
print(s.rfind('oo', 0, 8))
print(s.rfind('gf'))