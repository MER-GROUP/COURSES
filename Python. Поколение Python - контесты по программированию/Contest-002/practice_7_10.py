'''
Регулярки + Рекурсия. Ищем вхождение шаблона 
"число(строка)" и заменяем его вхождения на строку "строка * число", после чего рекурсивно вызываем до тех пор, пока шаблон встречается.
'''
import re

def repl(string):
    x = re.findall("([0-9]+)[(]([a-z]+)[)]", string)
    if (len(x) == 0):
        return string
    else:
        for i in x:
            string = string.replace(i[0] + "(" + i[1] + ")", i[1] * int(i[0]))
        return repl(string)

x = str(input())
print(repl(x))