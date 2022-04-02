from decimal import Decimal

class Exam:
	def __init__(self, d):
		print(d.exp() + d.ln() + d.log10() + d.sqrt())
		
if __name__ == '__main__':
	Exam(Decimal(input()))