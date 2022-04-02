def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
   
#print(s(b=31))
print(s(11, 10, b=10)) # 31
#print(s(b=31, 0))
print(s(11, 10, 10)) # 41
print(s(21)) # 31
print(s(5, 5, 5, 5, 1)) # 31
print(s(11, 10)) # 31
print(s(11, b=20)) # 31
print(s(0, 0, 31)) # 41