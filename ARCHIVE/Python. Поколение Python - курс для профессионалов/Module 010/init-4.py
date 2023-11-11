print('------------------')

words = ['hello', 'beegeek', 'python']

# за кулисами вызывается магический метод __len__()
print(len(words)) 
# за кулисами вызывается магический метод __str__()        
print(str(words))         

print('------------------')

words = ['hello', 'beegeek', 'python']

print(words.__len__())
print(words.__str__())

print('------------------')

words = ['hello', 'beegeek', 'python']

print(dir(words))

print('------------------')

words = ['hello', 'beegeek', 'python']

# за кулисами вызывается метод words.__iter__()
iterator = iter(words)      

print(type(words))
print(type(iterator))

print('------------------')

words = ['hello', 'beegeek', 'python']

# за кулисами вызывается метод words.__iter__()
iterator = iter(words)      
# за кулисами вызывается метод iterator.__next__()
print(next(iterator))    
# за кулисами вызывается метод iterator.__next__()   
print(next(iterator))       

print('------------------')

# words = ['hello', 'beegeek', 'python']

# print(next(words))

print('------------------')

words = ['hello', 'beegeek', 'python']

# за кулисами вызывается метод words.__iter__()
iterator1 = iter(words)   
# за кулисами вызывается метод iterator1.__iter__()       
iterator2 = iter(iterator1)      

print(iterator1 == iterator2)

print('------------------')

zero_iterator = iter(int, -1)

for i in range(5):
    print(next(zero_iterator))

print(type(zero_iterator))

print(int())

print('------------------')

from random import choice

def test_iter():
    values = list(range(1, 11))
    return choice(values)

random_iterator = iter(test_iter, 2)

for num in random_iterator:
    print(num)

print('------------------')
# with open('data.txt') as file:
#     # читаем, пока не попадется пустая строка 
#     for line in iter(file.readline, ''):    
#         # Делаем что-то с line.
#         ...
print('------------------')