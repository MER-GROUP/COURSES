num = int(input())
arr, final = list(range(1, num*2)), list()

for i in range(1, num+1):
    final += arr[:i][::-1]
    arr = arr[i:]
    
print(*final[:num])