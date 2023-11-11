#################################################

# Получает путь к домашней директории
from pathlib import Path

home_path = Path.home()
print(home_path)
print(type(home_path))

home_path_str = str(Path.home())
print(home_path_str)
print(type(home_path_str))

print('----------------------------------------')

#################################################

# определение пути к папке Downloads
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")

# For python3+ mac or linux
from pathlib import Path
import os.path
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

print('----------------------------------------')

#################################################

from sys import platform

if platform == "linux" or platform == "linux2":
    print('linux')
    print(platform)
elif platform == "darwin":
    print('OS X')
elif platform == "win32":
    print('Windows')

print('----------------------------------------')

#################################################

from os.path import join

path = join('/Max/Man', 'Mother/Sun', 'Polo', 'Golf')
print(path)

print('----------------------------------------')

#################################################

from pathlib import Path

file = str(Path('./dir1/file.txt'))
print(file)

print('----------------------------------------')

#################################################

from pathlib import Path

downloads_path = str(Path.home() / "Downloads")
print(downloads_path)

#################################################