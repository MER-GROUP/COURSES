'''
Конкатенация файлов 🌶️
На вход программе подается натуральное число n и n строк с названиями файлов. 
Напишите программу, которая создает файл output.txt и 
выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.

Формат входных данных
На вход программе подается натуральное число n и n строк названий существующих файлов.

Формат выходных данных
Программа должна создать файл с именем output.txt в соответствии с условием задачи.

Примечание. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
'''
# Решение
class File:
    def __init__(self, n: int=1) -> None:
        self.arr_files = self.__files(n)
        self.__write(self.arr_files)

    def __files(self, n: int=1) -> list:
        return [input() for i in range(n)]

    def __write(self, arr_files: list) -> None:
        with open('output.txt', 'at', encoding='utf-8') as file_out:
            for file in arr_files:
                with open(file, 'rt', encoding='utf-8') as file_in:
                    file_out.write(file_in.read())

if __name__ == '__main__':
    File(int(input()))