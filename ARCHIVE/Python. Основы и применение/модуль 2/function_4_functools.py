from functools import partial
import operator as op

x = int('1101', base=2)
print(x)

int_2 = partial(int, base = 2)
x = int_2('1101')
print(x)

names = [('max', 'red', 'alert'), ('rock', 'xcoolio'), ('mary', 'lena', 'tanay')]

list_sort = partial(list.sort, key=op.itemgetter(-1))
print(names)
list_sort(names)
print(names)

test = ['abc', 'cba', 'ccb']
print(test)
list_sort(test)
print(test)