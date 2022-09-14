# Функции
print('---------------------------------')
num = 17
numbers = [1, 2, 3]
colors = (1, 2, 3)
name = 'Python'

print(type(num))
print(type(numbers))
print(type(colors))
print(type(name))
print('---------------------------------')
print(type(print))
print(type(sum))
print(type(abs))
print('---------------------------------')
def hello():
    print('Hello from function')

print(type(hello))
print('---------------------------------')
def hello():
    print('Hello from function')
# присваиваем переменной func функцию hello
func = hello  
# вызываем функцию   
func()           
print('---------------------------------')
# как в языке Pascal 😀
writeln = print            

writeln('Hello world!')
writeln('Python')
print('---------------------------------')
numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print('---------------------------------')
# Продемонстрируем вышесказанное на примере кода:
numbers = [10, -7, 8, -100, -50, 32, 87, 117, -210]
#  указываем функцию abs в качестве компаратора
print(max(numbers, key=abs))  
#  указываем функцию abs в качестве компаратора      
print(min(numbers, key=abs))  
#  указываем функцию abs в качестве компаратора      
print(sorted(numbers, key=abs))   
print('---------------------------------')
# Таким образом, приведенный ниже код:
points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#  сортируем список точек на месте
points.sort()    
print(points)
print('---------------------------------')
def compare_by_second(point):
    return point[1]

def compare_by_sum(point):
    return point[0] + point[1]

points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
# сортируем по второму значению кортежа
print(sorted(points, key=compare_by_second))   
# сортируем по сумме кортежа
print(sorted(points, key=compare_by_sum))  
print('---------------------------------')
def generator():
    def hello():
        print('Hello from function!')
    return hello

func = generator()
func()
print('---------------------------------')
def generator_square_polynom(a, b, c):
    def square_polynom(x):
        return a*x**2 + b*x + c
    return square_polynom
# Приведенный ниже код:
f = generator_square_polynom(a=1, b=2, c=1)
g = generator_square_polynom(a=2, b=0, c=-3)
h = generator_square_polynom(a=-3, b=-10, c=50)

print(f(1))
print(g(2))
print(h(-1))
print('---------------------------------')
def comparator(item):
    return item[0]

data = [('red', 1), ('blue', 2), ('green', 5), ('blue', 1)]
# сортируем по первому полю
data.sort(key=comparator)   

print(data)

data = [('5', 4), ('5', 2), ('7', 5), ('7', 1)]
# сортируем по первому полю
data.sort(key=comparator)   

print(data)

data = [(5, 4), (5, 2), (7, 5), (7, 1)]
# сортируем по первому полю
data.sort(key=comparator)   

print(data)

data = [(5, 4), (5, 2), (7, 5), (7, 1)]
# сортируем по первому полю
data.sort()   

print(data)
print('---------------------------------')
print(input)
print(comparator)
print('---------------------------------')
for e in __builtins__.__dict__:
    print(e)
print('---------------------------------')
s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'
 
print(min(s1, s2, s3))
print(max(s1, s2, s3))
print('---------------------------------')
print(-2**2+1)
print('---------------------------------')
from statistics import mean
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

print(*(func(numbers, key=mean) for func in (min, max)), sep='\n')
print('---------------------------------')
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]

def num(*args):
  min_arg = []
  def fmean(x):
    return sum(x) / len(x)
  for i in args:
    print(f'len = {len(args)}')
    print(f'args = {args}')
    print(type(args))
    min_arg.append(min(i,key=fmean))
    min_arg.append(max(i,key=fmean))
    print(f'min_arg = {min_arg}')

  return min_arg

print(*num(numbers),sep='\n')
print('---------------------------------')