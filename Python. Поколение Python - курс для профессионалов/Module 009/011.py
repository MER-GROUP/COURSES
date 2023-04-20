'''
Необычная сортировка 🌶️
Дана строка, содержащая латинские буквы и цифры. Напишите программу, 
которая сортирует символы в строке согласно следующим правилам:

все отсортированные строчные буквы стоят перед заглавными буквами
все отсортированные заглавные буквы стоят перед цифрами
все отсортированные нечетные цифры стоят перед отсортированными четными

Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.

Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием 
задачи и вывести полученный результат.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640035/tests_2657880.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.1/Module_9.1.16

Sample Input 1:
Sorting1234
Sample Output 1:
ginortS1324

Sample Input 2:
n0tEast3rEgg
Sample Output 2:
aggnrsttEE30

Sample Input 3:
3DYrz34UXl
Sample Output 3:
lrzDUXY334
'''
import sys
# sys.stdin = open(file='011-tests.txt', mode='rt', encoding='utf-8', newline='')

def new_sort(s: str) -> str:
    # print(list(s)) # test
    res = sorted(s, key=lambda x: (
            x.isdigit(),
            x.isdigit() and not int(x)%2,
            x.isupper(),
            x.lower()           
        )
    )
    # print(res) # test
    return "".join(res)

if __name__ == '__main__':
    print(new_sort(sys.stdin.read())) 
    # Sorting1234
    # ginortS1324