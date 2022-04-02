# метод монте-карло
# пример 1
import random

n = 1000
k = 0
s0 = 1

for _ in range(n):
    # случайное число с плавающей точкой от 0 до 1
    x = random.uniform(0, 1)
    # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(0, 1)
	# если попадает в нужную область
    if y <= x**2:
        k += 1

print((k/n)*s0)