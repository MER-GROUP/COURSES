def f(x):
	return x * x

def arr_filter(arr):
	filter = list()
	for i in arr:
		if i not in filter:
			filter.append(i)
	return filter

n = int(input())
arr = [int(input()) for _ in range(n)]
arr_k = arr_filter(arr)
arr_v = [f(i) for i in arr_k]
my_dict = dict(zip(arr_k, arr_v))
for i in arr:
	print(my_dict.get(i))