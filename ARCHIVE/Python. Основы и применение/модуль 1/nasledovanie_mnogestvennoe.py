#методы isinstance и issubclass
class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

x = A()
print(isinstance(x, A))
print(isinstance(x, B))
print(isinstance(x, object))
print(isinstance(x, str))

print('-------------------')
print(issubclass(A, A))
print(issubclass(C, D))
print(issubclass(A, D))
print(issubclass(C, object))
print(issubclass(object, C))