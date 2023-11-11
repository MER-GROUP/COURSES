'''
Функция is_correct_json()
Реализуйте функцию is_correct_json(), которая принимает один аргумент:

string — произвольная строка

Функция должна возвращать True, если строка string удовлетворяет формату JSON, 
или False в противном случае.

Примечание 1. Вспомните про конструкцию try-except из урока. 
https://stepik.org/lesson/570048/step/9?unit=564591

Примечание 2. В тестирующую систему сдайте программу, 
содержащую только необходимую функцию is_correct_json(), 
но не код, вызывающий ее.

Примечание 3. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/623073/tests_3072703.zip

Sample Input 1:
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))
Sample Output 1:
True

Sample Input 2:
print(is_correct_json('number = 17'))
Sample Output 2:
False
'''
import json

def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False

if __name__ == '__main__':
    data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
    print(is_correct_json(data))
    print(is_correct_json('number = 17'))