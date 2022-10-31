arr = range(5)
for right in arr[4 :]:
    print(right)
print('-----------------')
print(list(arr))
print(arr[-2])
print('-----------------')
arr = list(range(5))
arr_copy = arr.copy()
print(f'arr = {arr}')
print(f'arr_copy = {arr_copy}')
print('-----------------')
print('1 8 10 12 14 15 18')
print('28 18 6 9 22 24 17 1 1 14 8 23 10 3 26 30 2 12 23 14 1 25 7 1 15 24 3 10 11 18')
arr = [28, 18, 6, 9, 22, 24, 17, 1, 1, 14, 8, 23, 10, 3, 26, 30, 2, 12, 23, 14, 1, 25, 7, 1, 15, 24, 3, 10, 11, 18]
my_set = set(arr)
print(set(arr))
print(f'len arr = {len(arr)}')
print(f'len set = {len(my_set)}')
print('-----------------')
X =  [28, 18, 6, 9, 22, 24, 17, 1, 1, 14, 8, 23, 10, 3, 26, 30, 2, 12, 23, 14, 1, 25, 7, 1, 15, 24, 3, 10, 11, 18]
 
L = []
M = []
j = 1
 
while j < len(X):
  i = j
  N = X[:]
  while i < len(N)-1:
    if N[i] < N[i+1]: 
      M.append(N[i])
      i += 1
    else:
      N.pop(i+1)
      
  j+=1
  if len(L) < len(M):
    L = M
  M=[]
 
if X[-1] > L[-1]:
  L.append(X[-1])
  
if X[0] < L[0]:
  L.insert(0, X[0])
  
print(L)
print('-----------------')
def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)    # offset by 1 (j -> j-1)
    P = [None] * len(seq)

    # Since we have at least one element in our list, we can start by 
    # knowing that the there's at least an increasing subsequence of length one:
    # the first element.
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        # Binary search: we want the largest j <= L
        #  such that seq[M[j]] < seq[i] (default j = 0),
        #  hence we want the lower bound at the end of the search process.
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    # this will also set the default value to 0

        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]    # reversing

arr = [28, 18, 6, 9, 22, 24, 17, 1, 1, 14, 8, 23, 10, 3, 26, 30, 2, 12, 23, 14, 1, 25, 7, 1, 15, 24, 3, 10, 11, 18]
print(subsequence(arr))
print('-----------------')