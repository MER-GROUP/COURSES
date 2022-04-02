# множественное наследование
class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

class Z(C, B): pass

print(A.mro())
print('-------------------')
print(Z.mro())