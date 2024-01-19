print('---------------------------')

data = [10, 15, 20, 30, 25, 30, 20, 15, 10, 5]
print(data)
import numpy as np
hist, bin_edges = np.histogram(data, bins=5)

print(hist) # [1 2 2 2 3] 
print(bin_edges) # [ 5. 10. 15. 20. 25. 30.]

print('---------------------------')

data = [10, 15, 20, 30, 25, 30, 20, 15, 10, 5]
import numpy as np 
percentiles = np.percentile(data, [25, 50, 75]) 
print(percentiles) # [11.25 17.5 23.75]

print('---------------------------')

a = np.array([1, 2, 3, 4, 5])
mean_a = np.mean(a)
print(mean_a)

print('---------------------------')

a = np.array([1, 2, 3, 4, 5])
median_a = np.median(a)
print(median_a)

print('---------------------------')

a = np.array([1, 2, 3, 4, 5])
std_a = np.std(a)
print(std_a)

print('---------------------------')

a = np.array([1, 2, 3, 4, 5])
var_a = np.var(a)
print(var_a)

print('---------------------------')

print(np.mean([3, 5, 7, 9]))
print(np.std([3, 5, 7, 9]))

print('---------------------------')

print(f'arr = {[1, 2, 3, 4, 5, 6]}')
print(np.histogram([1, 2, 3, 4, 5, 6], bins=1))
print(np.histogram([1, 2, 3, 4, 5, 6], bins=2))
print(np.histogram([1, 2, 3, 4, 5, 6], bins=3))
print(np.histogram([1, 2, 3, 4, 5, 6], bins=4))
print(np.histogram([1, 2, 3, 4, 5, 6], bins=5))
print(np.histogram([1, 2, 3, 4, 5, 6], bins=6))
print(np.histogram([1, 2, 3, 4, 5, 6], bins=7))

print('---------------------------')