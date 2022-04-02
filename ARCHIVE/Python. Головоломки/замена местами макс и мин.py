arr = [int(i) for i in input().split()] 
indMax = arr.index(max(arr))
indMin = arr.index(min(arr))
arr[indMax], arr[indMin] = arr[indMin], arr[indMax]
print(*arr)