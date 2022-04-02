def Enter():
	try:
		if 1==cnt:
			znak=input('Введите + - * / (q - выход) : ')
			if 'q'==znak: pass
			elif znak in ('+','-','*','/'):pass
			else: raise ValueError
		elif 2==cnt:
			znak=float(input('Введите x :'))
		elif 3==cnt:
			znak=float(input('Введите y :'))
	except ValueError:
		znak=None
		print('Некоректнвй ввод')
	finally:
		return znak
		
def Calc(znak,x,y):
	try:
		res=None
		if '+'==znak:
			res=x+y
		elif '-'==znak:
			res==x-y
		elif '*'==znak:
			res==x*y
		else:
			res=x/y
	except ZeroDivisionError:
		res=None
		print('Делить на ноль нельзя')
	finally:
		return res

def Main():
	while True:
		znak=None
		while None==znak:
			znak=Enter()
		if 'q'==znak:quit()
		global cnt
		cnt+=1
		x=None
		while None==x:
			x=Enter()
		cnt+=1
		y=None
		while None==y:
			y=Enter()
		cnt=1
		res=Calc(znak,x,y)
		if None==res: continue
		print(f'{res:.2f}')
	
cnt=1
Main()