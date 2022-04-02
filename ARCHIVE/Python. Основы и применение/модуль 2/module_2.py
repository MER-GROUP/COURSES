import sys

print(type(sys.modules))
print('------------------------------')
print(sys.modules)
print('------------------------------')
print(sys.modules.keys())
print('------------------------------')
for k, v in sys.modules.items():
	print(k, '=', v)
print('------------------------------')
import fib
print('------------------------------')
print(sys.modules.keys())