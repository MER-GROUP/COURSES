'''
Лог файл 🌶️
Вам доступен текстовый файл logfile.txt с информацией 
о времени входа пользователя в систему и выхода из нее. 
Каждая строка файла содержит три значения, разделенные запятыми 
и символом пробела: имя пользователя, время входа, время выхода, 
где время указано в 24-часовом формате.

Напишите программу, которая создает файл output.txt и выводит 
в него имена всех пользователей (не меняя порядка следования), 
которые были в сети не менее часа.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем output.txt 
в соответствии с условием задачи.

Примечание 1. Считайте, что исполняемая программа 
и указанные файлы находятся в одной папке.

Примечание 2. Считайте, что каждый пользователь был 
только раз в системе, то есть в файле нет двух строк 
с одинаковым пользователем.

Примечание 3. Если бы файл logfile.txt содержал строки:

Тимур Гуев, 14:10, 15:50
Руслан Гриценко, 12:00, 12:59
Роман Гацалов, 09:10, 17:45
Габолаев Георгий, 11:10, 12:10

то файл output.txt имел бы вид:

Тимур Гуев
Роман Гацалов
Габолаев Георгий
Примечание 4. Указанный файл можно скачать по ссылке. 
https://stepik.org/media/attachments/lesson/519126/logfile.txt
'''
# Решение
from datetime import datetime 

class File:
    def __init__(self) -> None:
        self.__algo()
        # print(self.__difference_time('13:00', '14:10'))

    def __algo(self) -> None:
        with open('logfile.txt', 'rt', encoding='utf-8') as file_in,\
            open('output.txt', 'wt', encoding='utf-8') as file_out:
            for line in file_in:
                fio, start_time, end_time = line.strip().split(',')
                if(1 <= int(self.__difference_time(start_time.strip(), end_time.strip())[0])):
                    print(fio, file=file_out)

    def __difference_time(self, start_time: str, end_time: str) -> int:
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')
        difference_time = end_time - start_time
        # print(start_time)
        # print(type(start_time))
        # print(end_time)
        # print(type(end_time))
        # print(difference_time)
        # print(type(difference_time))
        return str(difference_time).split(', ')[-1]

if __name__ == '__main__':
    File()