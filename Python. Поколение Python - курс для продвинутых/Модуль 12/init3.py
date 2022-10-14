print('---------------------------------')
# with open('myfile.txt', 'w', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik <3')
print('---------------------------------') 
# with open('myfile.txt', 'a', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik <3')
print('---------------------------------') 
with open('myfile.txt', 'r+', encoding='utf-8') as file:
    file.write('Python and beegeek forever\n')
    file.write('We love stepik.')
print('---------------------------------') 
with open('philosophers.txt', 'w', encoding='utf-8') as file:
    file.write('Джoн Локк\n')
    file.write('Дэвид Хьюм\n')
    file.write('Эдмyнд Берк\n')
print('---------------------------------') 
philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']
with open('philosophers.txt', 'w', encoding='utf-8') as file:
    file.writelines(philosophers)
print('---------------------------------') 
with open('philosophers.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', file=output)
    print('Дэвид Хьюм', file=output)
    print('Эдмyнд Берк', file=output)
print('---------------------------------') 
with open('philosophers.txt', 'w', encoding='utf-8') as output:
    print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', file=output)
print('---------------------------------') 