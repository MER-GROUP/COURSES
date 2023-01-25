print('------------------')

from zipfile import ZipFile

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.printdir()

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    # размер начального файла в байтах
    print(info[6].file_size)  
    # размер сжатого файла в байтах              
    print(info[6].compress_size)  
    # имя файла          
    print(info[6].filename) 
    # дата изменения файла                
    print(info[6].date_time)                

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    print(*info)  

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    print(info[0].is_dir())
    print(info[6].is_dir())

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.namelist()
    print(*info, sep='\n')

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    # получаем названия всех файлов архива
    info = zip_file.namelist()    
    # получаем информацию об отдельном файле            
    last_file = zip_file.getinfo(info[-4])    
    print(last_file.file_size)
    print(last_file.compress_size)
    print(last_file.filename)
    print(last_file.date_time)

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read())

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    with zip_file.open('test/Разные файлы/astros.json') as file:
        print(file.read().decode('utf-8'))

print('------------------')

from zipfile import ZipFile

with ZipFile('archive.zip', mode='w') as zip_file:
    zip_file.write('program.py')
    zip_file.write('lse.jpeg')
    print(zip_file.namelist())

print('------------------')

from zipfile import ZipFile

with ZipFile('archive.zip', mode='w') as zip_file:
    # первый аргумент - это имя файла
    # второй аргумент - это имя файла в архиве
    zip_file.write('program.py', 'new_program.py')  
    # первый аргумент - это имя файла
    # второй аргумент - это имя файла в архиве
    zip_file.write('lse.jpeg', 'lse1.jpeg')         
    print(zip_file.namelist())  

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip', mode='a') as zip_file:
    zip_file.write('program.py', 'test/program.py')
    zip_file.write('lse.jpeg')
    print(*zip_file.namelist(), sep='\n')

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.extract('test/Картинки/avatar.png')
    zip_file.extract('test/Программы/image_util.py')
    zip_file.extract('lse.jpeg')

print('------------------')

from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    zip_file.extractall()

print('------------------')