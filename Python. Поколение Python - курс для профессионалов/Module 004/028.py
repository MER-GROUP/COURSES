'''
Элементы JSON
Напишите программу, которая принимает на вход описание одного объекта 
в формате JSON и выводит все пары ключ-значение этого объекта.

Формат входных данных
На вход программе подается корректное описание одного объекта в формате JSON.

Формат выходных данных
Программа должна вывести все пары ключ-значение введенного объекта, 
разделяя ключ и значение двоеточием, каждую на отдельной строке. 
Если значением ключа является список, то все его элементы должны быть выведены через запятую.

Примечание 1. Пары ключ-значение при выводе должны располагаться в своем исходном порядке.

Примечание 2. Для считывания произвольного числа строк используйте потоковый ввод sys.stdin.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/623073/tests_3072699.zip

Sample Input 1:
{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}
Sample Output 1:
size: 36
style: bold
name: text1
alignment: center

Sample Input 2:
{
 "type": "donut", 
 "name": "Cake", 
 "tastes": ["chocolate", "cream", "strawberry"]
}
Sample Output 2:
type: donut
name: Cake
tastes: chocolate, cream, strawberry
'''
import sys, json

# sys.stdin = open(file='028.csv', mode='rt', encoding='utf', newline='')
json_str = sys.stdin.read()
dictonary = json.loads(json_str)

for k, v in dictonary.items():
    if isinstance(v, list):
        print(k, ': ', ', '.join(map(str, v)), sep='')
    else:
        print(f'{k}: {v}')