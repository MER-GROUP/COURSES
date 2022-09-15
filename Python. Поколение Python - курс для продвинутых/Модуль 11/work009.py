'''
Напишите программу, которая сортирует список points координат точек плоскости 
в соответствии с расстоянием от начала координат (точки (0;0)). 
Программа должна вывести отсортированный список.
'''
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

def comporator(arr):
    return __import__('math').sqrt(arr[0]**2 + arr[1]**2)
points.sort(key=comporator)

print(points)