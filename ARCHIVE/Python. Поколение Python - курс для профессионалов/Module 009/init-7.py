print('------------------')

def greet():
    greet.age = 17

print(greet.__dict__)

greet.value = 777
greet.numbers = [1, 2, 3]
greet.name = 'Timur'

print(greet.__dict__)

greet()

print(greet.__dict__)

print('------------------')

def fib_broken(num):
    if num < 2:
        return num
    if num not in fib_broken.__dict__:
        fib_broken.num = fib_broken(num - 1) + fib_broken(num - 2)
    return fib_broken.num

print(fib_broken(9))
print(fib_broken.__dict__)

print('------------------')

def fib(num):
    if num < 2:
        return num
    if num not in fib.__dict__:
        fib.__dict__[num] = fib(num - 1) + fib(num - 2)
    return fib.__dict__[num]

print(fib(9))
print(fib.__dict__)


print('------------------')