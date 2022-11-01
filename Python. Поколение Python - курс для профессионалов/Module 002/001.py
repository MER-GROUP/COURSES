'''
Функция hide_card()
Реализуйте функцию hide_card(), которая принимает один аргумент:

card_number — строка, представляющая собой корректный 
номер банковской карты из 16 цифр, между которыми могут 
присутствовать символы пробела
Функция должна заменять первые 12 цифр в строке card_number 
на символ * и возвращать полученный результат. Если между цифрами 
в номере имелись символы пробела, их следует удалить.

Примечание 1. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию hide_card(), но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.
https://stepik.org/media/attachments/lesson/569748/tests_2310066.zip

Sample Input 1:
card = '1234567890123456'
print(hide_card(card))
Sample Output 1:
************3456

Sample Input 2:
card = '3456 9012 5678 1234'
print(hide_card(card))
Sample Output 2:
************1234

Sample Input 3:
card = '905 678123 45612 56'
print(hide_card(card))
Sample Output 3:
************1256
'''
def hide_card(card_number: str) -> str:
    return '*' * 12 + ''.join(card_number.split())[-4 : ]

if __name__ == '__main__':
    card = '1234567890123456'
    print(hide_card(card))
    card = '3456 9012 5678 1234'
    print(hide_card(card))
    card = '905 678123 45612 56'
    print(hide_card(card))