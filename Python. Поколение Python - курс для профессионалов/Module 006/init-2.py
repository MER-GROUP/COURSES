print('------------------')

point = (3, 7)

print(point)
print(point[0], point[1])
print(type(point))

print('------------------')

from collections import namedtuple

# объявляем тип Point именованного кортежа
Point = namedtuple('Point', ['x', 'y'])     

# создаем именованный кортеж Point
point = Point(3, 7)                         

print(point)
print(point.x, point.y)
print(point[0], point[1])
print(type(point))

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'children'])

sveta = Person('Sveta Gueva', ['Larisa', 'Timur'])
print(sveta)

sveta.children.append('Soslan')
print(sveta)

print('------------------')

# from collections import namedtuple

# Person = namedtuple('Person', ['name', 'children'])

# sveta = Person('Sveta Gueva', ['Larisa', 'Timur'])
# sveta.children = ['Larisa', 'Timur', 'Soslan']

print('------------------')

from collections import namedtuple

# в качестве второго параметра передаем список
Point = namedtuple('Point', ['x', 'y'])    
point =  Point(2, 4)
# выводит Point(x=2, y=4)
print(point)                               

print('------------------')

from collections import namedtuple

# в качестве второго параметра передаем кортеж
Point = namedtuple('Point', ('x', 'y'))    
point =  Point(2, 4)
# выводит Point(x=2, y=4)
print(point)                               

print('------------------')

from collections import namedtuple

# в качестве второго параметра передаем словарь
Point = namedtuple('Point', {'x': 0, 'y': 69})    
point =  Point(2, 4)
# выводит Point(x=2, y=4)
print(point)                                      

print('------------------')

from collections import namedtuple

# в качестве второго параметра передаем строку
Point = namedtuple('Point', 'x y')    
point =  Point(2, 4)
# выводит Point(x=2, y=4)
print(point)                          

print('------------------')

from collections import namedtuple

# в качестве второго параметра передаем строку
Point = namedtuple('Point', 'x,y')     
point =  Point(2, 4)
# выводит Point(x=2, y=4)
print(point)                           

print('------------------')

from collections import namedtuple

# в качестве второго параметра передаем множество
Point = namedtuple('Point', {'x', 'y'})    
point =  Point(2, 4)
print(point)

print('------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
# позиционные аргументы
point1 = Point(2, 4)    
# именованные аргументы                      
point2 = Point(y=10, x=3)                     

print(point1)
print(point2)

print('------------------')

# from collections import namedtuple

# Point = namedtuple('Point', ['x', '_y'])

print('------------------')

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'if'])

print('------------------')

# from collections import namedtuple

# headers = ('name', 'surname', 'age', 'class')
# Student = namedtuple('Student', headers)

print('------------------')

from collections import namedtuple

headers = ('name', 'surname', 'age', 'class')

Student = namedtuple('Student', headers, rename=True)

stud = Student('Роман', 'Белых', 26, 10)
print(stud)

print('------------------')

from collections import namedtuple

headers = ('name', 'surname', 'age', 'class', 'with', 'color', 'name', 'class', 'if')

Student = namedtuple('Student', headers, rename=True)

stud = Student('Тимур', 'Гуев', 28, 11, 'sister', 'green', 'Tim', '11A', 'else')
print(stud)

print('------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], defaults=(0, 0))
point1 = Point()      # используем значения по умолчанию
point2 = Point(1, 9)

print(point1)
print(point2)

print('------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], defaults=(0,))
point =  Point(7)      # используем значения по умолчанию для y
print(point)

print('------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print(type(point))

print('------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'], module='customtypes')
point = Point(1, 2)
print(type(point))

print('------------------')

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'height'])

timur = Person('Тимур', 29, 170)

name, age, height = timur

print(name)
print(age)
print(height)

print('------------------')

from collections import namedtuple

Point = namedtuple('Point3D', ['x', 'y', 'z'])

point = Point(89, 54, -34)

print(point[1:])
print(point[:2])
print(point[1:2])

print('------------------')

from collections import namedtuple

unknowntype = namedtuple('Point', ['x', 'y'])
point = unknowntype(2, 4)
print(type(point))

print('------------------')

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 5)
print(point)

print('------------------')