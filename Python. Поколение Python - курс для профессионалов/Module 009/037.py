'''
Декоратор do_twice
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать 
возвращаемое значение декорируемой функции, а также должен уметь 
декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую 
только необходимый декоратор do_twice, но не код, вызывающий его. 

Примечание 3. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/640039/tests_2723283.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.7/Module_9.7.21

Sample Input 1:
@do_twice
def beegeek():
    print('beegeek')  
beegeek()
Sample Output 1:
beegeek
beegeek

Sample Input 2:
@do_twice
def beegeek():
    print('beegeek')   
print(beegeek())
Sample Output 2:
beegeek
beegeek
None
'''
def do_twice(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        for _ in range(2):
            _return = func(*args, **kwargs)
        return _return
    return wrapper

if __name__ == '__main__':
    @do_twice
    def beegeek():
        print('beegeek')  
    beegeek()

    @do_twice
    def beegeek():
        print('beegeek')   
    print(beegeek())

    @do_twice
    def beegeek():
        return 'beegeek'    
    print(beegeek())