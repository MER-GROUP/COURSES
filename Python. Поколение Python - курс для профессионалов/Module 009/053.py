'''
Две функции
Вам доступна уже реализованная функция send_email(), которая принимает три аргумента 
в следующем порядке:

name — имя
email_address — адрес электронной почты
text — содержание письма

Функция отправляет письмо пользователю с именем name на адрес email_address с содержанием text.

1. Реализуйте функцию to_Timur() с помощью функции partial(), которая принимает один аргумент:

text — содержание письма

Функция должна отправлять письмо пользователю с именем Тимур на адрес timyrik20@beegeek.ru 
с содержанием text.

2. Реализуйте функцию send_an_invitation() с помощью функции partial(), 
которая принимает два аргумента в следующем порядке:

name — имя
email_address — адрес электронной почты

Функция должна отправлять письмо на имя name и на адрес email_address со следующим содержанием:

Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....

Примечание 1. Функции to_Timur() и send_an_invitation() должны являться partial объектами.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимые 
функции to_Timur() и send_an_invitation(), но не код, вызывающий их.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/751476/tests_3130314.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.9/Module_9.9.11

Sample Input 1:
print(to_Timur('когда курс?'))
Sample Output 1:
В письме для Тимур на адрес timyrik20@beegeek.ru сказано следующее: когда курс?

Sample Input 2:
print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))
Sample Output 2:
В письме для Тимур на адрес timyrik20@beegeek.ru сказано следующее: 
Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....
'''
from functools import partial

def send_email(name, email, text):

    return f'В письме для {name} на адрес {email} сказано следующее: {text}'

to_Timur = partial(send_email, "Тимур", "timyrik20@beegeek.ru")

send_an_invitation = partial(send_email, text="Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....")

if __name__ == '__main__':
    print(to_Timur('когда курс?'))

    print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))