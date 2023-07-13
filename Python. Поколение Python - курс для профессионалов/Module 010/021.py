'''
Итератор Alphabet 🌶️
Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:

language — код языка: ru — русский, en — английский

Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:

русского алфавита, если language имеет значение ru
английского алфавита, если language имеет значение en

Примечание 1. Буква ё в русском алфавите не учитывается.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый класс Alphabet.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/669733/tests_2778511.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_10/Module_10.4/Module_10.4.16

Sample Input 1:
ru_alpha = Alphabet('ru')
print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))
Sample Output 1:
а
б
в

Sample Input 2:
en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(28)]
print(*letters)
Sample Output 2:
a b c d e f g h i j k l m n o p q r s t u v w x y z a b
'''
pass

if __name__ == '__main__':
    pass