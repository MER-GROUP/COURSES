# Функции
def append(element, seq=[]):
    seq.append(element)
    return seq

print('---------------------------')
print(append(10, [1, 2, 3]))
print(append(5, [1]))
print(append(1, []))
print(append(3, [4, 5]))

print('---------------------------')
print('Значение по умолчанию', append.__defaults__)
print(append(10))
print('Значение по умолчанию', append.__defaults__)
print(append(5))
print('Значение по умолчанию', append.__defaults__)
print(append(1))
print('Значение по умолчанию', append.__defaults__)

print('---------------------------')
def append(element, seq=None):
    if seq is None:
        seq = []
    seq.append(element)
    return seq

print('---------------------------')
print('Значение по умолчанию', append.__defaults__)
print(append(10))
print('Значение по умолчанию', append.__defaults__)
print(append(5))
print('Значение по умолчанию', append.__defaults__)
print(append(1))
print('Значение по умолчанию', append.__defaults__)