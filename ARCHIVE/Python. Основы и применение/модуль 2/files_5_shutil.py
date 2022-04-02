import shutil

# копирование файлов
shutil.copy('file_test.txt', 'red_alert.txt')

# копирование папки
shutil.copytree('__pycache__', '__pycache__/red')