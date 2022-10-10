print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
line2 = file.readline()
file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
line2 = file.readline()
remaining_lines = file.read()    # считывание начинается с 3 строки до конца файла

file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
file.seek(0)               # переводим курсор в самое начало
line2 = file.readline()

print(line1, line2)

file.close()
print('---------------------------------')
file = open('languages.txt', 'r', encoding='utf-8')
print(file.tell())
line1 = file.readline()
print(file.tell())

file.close()
print('---------------------------------') 
file = open('languages.txt', 'r', encoding='utf-8')

for line in file:
    print(line)

file.close()              # ручное закрытие файла

print('Файл закрыт')
print('---------------------------------') 
with open('languages.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
                          # автоматическое закрытие файла
print('Файл закрыт')
print('---------------------------------') 