# простое или составное число
def is_prime(d):
	for i in range(2, int((d + 1) ** 0.5)):
		if 0 == d % i:
			return False
	else: return True if not 1 == d else False
		
print(is_prime(1))
print(is_prime(2))
print(is_prime(17))
print(is_prime(57))
print(is_prime(103))