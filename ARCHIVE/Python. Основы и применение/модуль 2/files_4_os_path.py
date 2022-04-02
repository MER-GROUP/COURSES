import os
import os.path

# файлы в текущей директории
#print(os.listdir())
print('\n'.join(os.listdir()))

print('-----------------------------')

# файлы в конкретной папке
print(os.listdir('__pycache__'))

print('-----------------------------')

# определение в какой папке мы находимся
print(os.getcwd())

print('-----------------------------')

# существует ли файл
print(os.path.exists('files_3.py'))
print(os.path.exists('red.py'))

print('-----------------------------')

# существует ли директория
print(os.path.exists('__pycache__'))
print(os.path.exists('red'))

print('-----------------------------')

# проверка - файл ли это
print(os.path.isfile('files_3.py'))
print(os.path.isfile('__pycache__'))

print('-----------------------------')

# проверка - директория ли это
print(os.path.isdir('files_3.py'))
print(os.path.isdir('__pycache__'))

print('-----------------------------')

# абсолютный путь до файла
print(os.path.abspath('files_3.py'))

print('-----------------------------')

# смена директории
#os.chdir('__pycache__')
#print(os.listdir())

print('-----------------------------')

# просмотр всех подпапок в директории
for cur_dir, dirs, files in os.walk('.'):
	print(cur_dir, dirs, files)