numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {i: [j for j in range(1, i + 1) if 0 == i % j] for i in sorted(numbers)}
print(result)