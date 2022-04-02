def h():
  #print(12)
  raise Exception

def f():
  g(h)

def g(a):
  a()

g(f)