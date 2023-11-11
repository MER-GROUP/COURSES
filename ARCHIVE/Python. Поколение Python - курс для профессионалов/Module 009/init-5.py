print('------------------')

def hello(name):
    print(f'Привет, {name}!')

hello('Гвидо')

print('------------------')

hello = lambda name: print(f'Привет, {name}!')

hello('Деннис')

print('------------------')

# функция без параметров
f1 = lambda: 17  
# функция с двумя параметрами                        
f2 = lambda х, у: х**2 + у**2 
# функция с тремя параметрами           
f3 = lambda х, у, z: х * у * z           

print(f1())
print(f2(6, 8))
print(f3(5, 10, 30))

print('------------------')

numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

# указываем функцию abs в качестве компаратора
print(max(numbers, key=abs))    
# указываем анонимную функцию в качестве компаратора               
print(min(numbers, key=lambda x: x**2)) 
# указываем анонимную функцию в качестве компаратора       
print(sorted(numbers, key=lambda x: -x))        

print('------------------')

squares = map(lambda x: x ** 2, range(1, 10))
absolute = map(abs, [-5, 6, 7, -90, 34, 54, -21])
numbers = map(lambda s: s.replace('.', ''), ['12.3', '-45.3', '34', '34...90'])
capitals = map(lambda s: s.capitalize(), ['timur', 'artur', 'ruslan'])

print(*squares)
print(*absolute)
print(*numbers)
print(*capitals)

print('------------------')

summa = map(lambda x, y, z: x + y + z, [1, 2], [3, 4], [5, 6])
powers = map(pow, [2, 3, 4], [4, 2, 3])

print(*summa)
print(*powers)

print('------------------')

pairs = map(lambda x, y: (x, y), ['a', 'b'], [3, 4, 5, 6, 7])

print(*pairs)

print('------------------')

nums = [9, 3, 45, 67, 12, 90, 87, 12, 45, 67]
names = ['timur', 'anton', 'Alana', 'ruslan', '', 'Gvido', 'Alika']

filter1 = filter(lambda x: x % 2 == 0, nums)
filter2 = filter(lambda x: x % 2 == 1 and x > 10, nums)
filter3 = filter(lambda x: len(x) > 0 and x[0].lower() == 'a', names)

print(*filter1)
print(*filter2)
print(*filter3)

print('------------------')

data = [1, 0, 10, '', None, [], [1, 2, 3], ()]

filtered_data = filter(None, data)

print(*filtered_data)

print('------------------')

print((lambda x, y: x + y)(10, 7))
print(eval('(lambda num: num ** 2)(7)'))

print('------------------')

fact = lambda n: 1 if n == 0 else n*fact(n - 1)

for i in range(10):
    print(fact(i))

print('------------------')

squares = map(lambda x: x ** 2, range(1, 10))
evens = filter(lambda x: x % 2 == 0, [9, 3, 45, 67, 12, 90, 87, 12, 45, 67])

print('Первичная распаковка (итерация): ', *squares)
print('Вторичная распаковка (итерация): ', *squares)

print('Первичное преобразование в список (итерация): ', list(evens))
print('Вторичное преобразование в список (итерация): ', list(evens))

print('------------------')