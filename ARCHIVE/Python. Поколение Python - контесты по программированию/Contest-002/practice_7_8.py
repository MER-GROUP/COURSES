'''
Исходник: hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd
Расставил куда надо знаки +, * и апострофы и получил 
'hi'+2*('priv'+3*('d'+3*('i')+'dd')+'qq')+'b'+0*('pr')+'qwqdd', 
затем применил функцию eval(). Кто не знаком, рекомендую погуглить.
И результат:
hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd
'''
s = input()
i = 0
while len(s) - 1 > i:
    if s[i].isalpha() and s[i + 1].isdigit():
        s = s[:i + 1] + '\'+' + s[i + 1:]  # ставим '+ между буквой и цифрой
    i += 1
s = s.replace('(', '*(\'').replace(')', '\')+\'') + '\''  # заменяем ( на *(' и ) на ')+'
                                                          # в конец вставляем '
if s[0].isalpha():  # если начинается с буквы, то в начало вставляем '
    s = '\'' + s
for i in range(10):
    s = s.replace('\'' + str(i), str(i))  # заменяем если есть: 'цифра на цифра
print(eval(s))