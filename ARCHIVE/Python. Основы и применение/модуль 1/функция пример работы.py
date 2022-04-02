def f1():
    print('f1')

def f2():
    print('f2')

x = f1
y = x
print(id(x) == id(y))  # True
x.a = 9
print(y.a)  # 9
print(y.__dict__)  # {'a': 9}
print(x.__name__)  # f1
x.__name__ = 'wtf?'
print(y.__name__)  # wtf?
x.__code__ = f2.__code__
y()  # f2