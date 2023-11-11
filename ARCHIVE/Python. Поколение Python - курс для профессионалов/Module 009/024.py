'''
Функция polynom()
Реализуйте функцию polynom(), которая принимает один аргумент:

x — вещественное число

Функция должна возвращать значение выражения x^2 + 1

Также функция должна иметь атрибут values, представляющий собой 
множество (тип set) всех значений функции, которые уже были вычислены.

Примечание 1. В тестирующую систему сдайте программу, содержащую 
только необходимую функцию polynom(), но не код, вызывающий ее. 

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
https://stepik.org/media/attachments/lesson/647292/tests_2742683.zip
GitHub
https://github.com/python-generation/Professional/tree/main/Module_9/Module_9.4/Module_9.4.17

Sample Input 1:
print(polynom(5))
print(polynom.values)
Sample Output 1:
26
{26}

Sample Input 2:
polynom(1)
polynom(2)
polynom(3)
print(*sorted(polynom.values))
Sample Output 2:
2 5 10

Sample Input 3:
for _ in range(10):
    polynom(10)
    
print(polynom.values)
Sample Output 3:
{101}
'''
def polynom(x):
    res = x**2 + 1
    # polynom.__dict__['values'] = polynom.__dict__.get('values', set()) | {res} # or
    polynom.values = polynom.__dict__.get('values', set()) | {res} # or
    return res 

if __name__ == '__main__':
    print(polynom(5))
    print(polynom.values)

    polynom(1)
    polynom(2)
    polynom(3)
    print(*sorted(polynom.values))

    for _ in range(10):
        polynom(10)
    print(polynom.values)