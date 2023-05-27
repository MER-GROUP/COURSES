'''
Это простое упражнение на написание функции высшего порядка, 
использующей замыкания.

Напишите функцию composition(f, g), которая принимает 
на вход две функции: f и g, -- и возвращает их композицию.

Не вдаваясь в лишние сейчас детали,  назовём композицией f∘g 
двух заданных функций f, g  функцию h, для которой h(x)=f(g(x))

Определите функцию композиции, предполагая, что аргументы 
у функции g могут быть какие угодно, и любое возвращаемое 
функцией g значение будет корректным аргументом для функции f.

Когда вы определите функцию, убедитесь, что вы понимаете, 
в каком именно месте используются замыкания.

def composition(f, g):
    '<...>'


Примеры ожидаемого поведения

h = composition(lambda x: x**2, lambda x: x + 1)
print(h(5))

>>> 36

h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
print(h(5))

>>> 36

h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
print(h(2, 3, 9))

>>> 6592
'''
def composition(f, g):
    def inner(*args, **kwargs):
        return f(g(*args, **kwargs))
    return inner

if __name__ == '__main__':
    h = composition(lambda x: x**2, lambda x: x + 1)
    print(h(5))

    h = composition(lambda x: x, composition(lambda x: x**2, lambda x: x + 1))
    print(h(5))

    h = composition(sum, lambda x, y, z: (x**2, y**3, z**4))
    print(h(2, 3, 9))