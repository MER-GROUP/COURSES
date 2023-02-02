#################################################

# Получает путь к домашней директории
from pathlib import Path

home_path = Path.home()
print(home_path)
print(type(home_path))

home_path_str = str(Path.home())
print(home_path_str)
print(type(home_path_str))

#################################################

# определение пути к папке Downloads
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")

# For python3+ mac or linux
from pathlib import Path
import os.path
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

#################################################