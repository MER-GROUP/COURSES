class A:
   def foo(self):
      print("A")

class B(A):
   #pass
   def lol(self):
   	print('B')
   	
class D:
   def foo(self):
      print("D")

class C(A):
   def foo(self):
      print("C")

class E(B, C, D):
   pass

E().foo()
#E.foo()
print(E.mro())