###############################################################################################
# version 1
def count_sort(_arr, _min, _max):
	from collections import defaultdict

	count = defaultdict(int)
	
	for _i in _arr:
		count[_i] += 1
		
	_result = list()
	
	for j in range(_min, _max+1):
		_result += [j]* count[j]
		
	return _result
###############################################################################################
# version 2
def counting_sort(alist, largest):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[alist[i]] = c[alist[i]] + 1 # or
        # c[alist[i]] += 1 # or

    # Find the last index for each element
    c[0] = c[0] - 1 # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
 
    result = [None]*len(alist)
 
    # Though it is not required here,
    # it becomes necessary to reverse the list
    # when this function needs to be a stable sort
    for x in reversed(alist):
        result[c[x]] = x
        c[x] = c[x] - 1
 
    return result
###############################################################################################
# version 2 - test
# def counting_sort(alist, largest):
#     c = [0]*(largest + 1)
#     print(f'c1 = {c}') # test
#     for i in range(len(alist)):
#         c[alist[i]] = c[alist[i]] + 1 # or
#         # c[alist[i]] += 1 # or
#     print(f'c2 = {c}') # test

#     # Find the last index for each element
#     c[0] = c[0] - 1 # to decrement each element for zero-based indexing
#     print(f'c3 = {c}') # test

#     for i in range(1, largest + 1):
#         c[i] = c[i] + c[i - 1]
#     print(f'c4 = {c}') # test

#     result = [None]*len(alist)
#     print(f'result = {result}') # test
 
#     # Though it is not required here,
#     # it becomes necessary to reverse the list
#     # when this function needs to be a stable sort
#     print(f'alist = {alist}') # test
#     print(f'reversed(alist) = {list(reversed(alist))}') # test
#     print('----------------------------') # test
#     i=1
#     for x in reversed(alist):
#     # for x in alist:
#         print('*****')
#         print(f'i = {i}') # test
#         i += 1
#         print(f'reversed(alist) = {list(reversed(alist))}') # test
#         print(f'x = {x}') # test
#         print(f'c0 = {c}') # test
#         result[c[x]] = x
#         print(f'result = {result}') # test
#         c[x] = c[x] - 1
#         print(f'c = {c}') # test
#         print('*****')
#     print('----------------------------') # test
#     return result
###############################################################################################
# version 3

###############################################################################################
if __name__ == '__main__':
    from random import randint

    print('################################## v1')

    N = 10
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    
    print(a)
    print(count_sort(a, min(a), max(a)))

    print('################################## v2')

    # alist = [randint(1, 99) for x in range(N)]
    alist = [5, 3, 1, 6, 6,	7, 7, 6, 2,	6]
    print(alist)
    k = max(alist)
    sorted_list = counting_sort(alist, k)
    print(sorted_list)

    print('################################## v3')

###############################################################################################