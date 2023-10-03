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

    alist = [randint(1, 99) for x in range(N)]
    print(alist)
    k = max(alist)
    sorted_list = counting_sort(alist, k)
    print(sorted_list)
###############################################################################################