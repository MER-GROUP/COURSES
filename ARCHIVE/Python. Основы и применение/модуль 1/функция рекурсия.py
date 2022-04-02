def rec(n, k):
	if 0 == k:
		return 1
	elif k > n:
		return 0
	return rec(n - 1, k) + rec(n -1, k - 1)
	
n, k = map(int, input().split())
print(rec(n, k))