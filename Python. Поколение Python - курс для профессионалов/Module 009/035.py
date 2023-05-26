'''
Декоратор sandwich
Реализуйте декоратор sandwich, который выводит тексты:

---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----

до и после вызова декорируемой функции соответственно.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать 
возвращаемое значение декорируемой функции, а также должен уметь 
декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую 
только необходимый декоратор sandwich, но не код, вызывающий его.

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640039/tests_2722998.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.7/Module_9.7.19

Sample Input 1:
@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))
add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
Sample Output 1:
---- Верхний ломтик хлеба ----
томат | салат | сыр | бекон
---- Нижний ломтик хлеба ----

Sample Input 2:
@sandwich
def beegeek():
    return 'beegeek'  
print(beegeek())
Sample Output 2:
---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
beegeek
'''
def sandwich(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> str:
        print('---- Верхний ломтик хлеба ----')
        _return = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return _return
    return wrapper

if __name__ == '__main__':
    @sandwich
    def add_ingredients(ingredients):
        print(' | '.join(ingredients))
    add_ingredients(['томат', 'салат', 'сыр', 'бекон'])

    @sandwich
    def beegeek():
        return 'beegeek'  
    print(beegeek())