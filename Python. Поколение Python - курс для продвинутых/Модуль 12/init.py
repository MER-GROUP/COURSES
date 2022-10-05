print('---------------------------------')
path = 'C:\new\text.txt'
print(path)
print('---------------------------------')
path = r'C:\new\text.txt'
print(path)
print('---------------------------------')
file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w', encoding='utf-8')

print(file1.encoding)
print(file2.encoding)

file1.close()
file2.close()
print('---------------------------------')
file1 = open('students.txt', 'w')
file2 = open('customers.txt', 'w')

file1.close()

print(file1.closed)
print(file2.closed)

file2.close()   
print('---------------------------------')
file = open('info.txt', 'w', encoding='utf-8')    # открываем файл для записи

print(file)
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
content = file.read(1)
print(content)
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
language = file.readline()
print(language)
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')

line = file.readline()         # считываем первую строку

while line != '':              # пока не конец файла
    print(line.strip())        # обрабатываем считанную строку
    line = file.readline()     # читаем новую строку

file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
language = file.readline()
print(language.strip())
language = file.readline()
print(language.strip())
language = file.readline()
print(language.strip())
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')

for line in file:
    print(line.strip())
    
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')

print(file)
print(*file, sep='')
    
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
languages = file.readlines()
print(languages)
print(list(map(str.strip, languages)))
languages = [line.strip() for line in file.readlines()]
print(languages)
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
languages = [line.strip() for line in file.readlines()]
print(languages)
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
print(list(file))
file.close()
print('---------------------------------')
print('aaaaaa\nbb')
print('---------------------------------')
print('aaaaaa\rbb')
print('---------------------------------')
print(ord('\n'))
print(ord('\r'))
print('---------------------------------')