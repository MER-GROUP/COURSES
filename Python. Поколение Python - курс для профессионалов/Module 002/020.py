'''
Файлы в файле 🌶️🌶️
Вам доступен текстовый файл files.txt, содержащий информацию о файлах. 
Каждая строка файла содержит три значения, разделенные символом 
пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...

Напишите программу, которая группирует данные файлы по расширению, 
определяя общий объем файлов каждой группы, и выводит полученные 
группы файлов, указывая для каждой ее общий объем. Группы должны 
быть расположены в лексикографическом порядке названий расширений, 
файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB

то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB

где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых 
крупных (максимально возможных) единицах измерения с округлением 
до целых. Другими словами, сначала следует определить суммарный 
объем всех файлов группы, скажем, в байтах, а затем перевести 
полученное значение в самые крупные (максимально возможные) 
единицы измерения. Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB

Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB

Примечание 5.
Указанный файл доступен по ссылке.
https://stepik.org/media/attachments/lesson/569749/files.txt
Ответ на задачу доступен по ссылке.
https://stepik.org/media/attachments/lesson/569749/clue.txt

Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.
'''
def print_dict(d): # for tests
    for k, v in d.items():
        for k2, v2 in v.items():
            print(k2, v2)
        print('----------')

if __name__ == '__main__':
    # get name files
    arr = list()
    with open('files.txt', 'rt', encoding='utf-8') as file:
        arr = list(map(str.strip ,file.readlines()))
    # print(arr) # test

    # DB
    dictonary = dict()
    for line in arr:
        name, size, unit = line.split()
        start, end = name.split('.')
        dictonary[end] = dictonary.get(end, dict())
        dictonary[end][unit] = dictonary.get(end, dict()).get(unit, []) + [int(size)]
        dictonary[end][end] = dictonary.get(end, dict()).get(end, []) + [name]
        # dictonary.setdefault(end, dict()).setdefault(unit, []).append(int(size))
        # dictonary.setdefault(end, dict()).setdefault(end, []).append(name)
    # print(dictonary, sep='\n') # test
    # print_dict(dictonary) # test

    # convert to bytes
    size_dict = {
        'B': 1 * 1 ** 1, 
        'KB': 1 * 1024 ** 1, 
        'MB': 1 * 1024 ** 2, 
        'GB': 1 * 1024 ** 3
        }

    # name of bytes
    name_of_bytes_dict = {
        'B': 1,
        'KB': 2,
        'MB': 3,
        'GB': 4
    }

    # sorted and count in DB
    for k, v in dictonary.items():
        size_bytes = 0
        name_of_bytes = 'B'
        convert_of_bytes = 0
        for k2, v2 in v.items():
            if k == k2:
                dictonary[k][k2] = sorted(v2)
            else:
                if (name_of_bytes_dict[name_of_bytes] < name_of_bytes_dict[k2]):
                    name_of_bytes = k2
                dictonary[k][k2] = sum(v2)
                if k2 in size_dict.keys():
                    size_bytes += dictonary[k][k2] * size_dict[k2]
        dictonary[k]['size_bytes'] = dictonary.get('size_bytes', 0) + size_bytes
        dictonary[k]['name_of_bytes'] = dictonary.get('name_of_bytes', str()) + name_of_bytes
        dictonary[k]['convert_of_bytes'] = round(
                                            dictonary.get('convert_of_bytes', 0) \
                                            + dictonary[k]['size_bytes'] \
                                            / size_dict[dictonary[k]['name_of_bytes']]
                                            )
    # print(dictonary, sep='\n') # test
    print_dict(dictonary) # test

    # # output
    # for k, v in dictonary.items():
    #     names_files = list()
    #     res = str()