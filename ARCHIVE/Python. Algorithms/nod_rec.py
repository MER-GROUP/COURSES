# наибольший общий делитель
def gcd(a, b):
	if (0 == b):
		return a
	else:
		return gcd(b, a % b)

a = 10
b = 15
print("Greatest common divisor of %d and %d is %d" %(a, b, gcd(a, b)))