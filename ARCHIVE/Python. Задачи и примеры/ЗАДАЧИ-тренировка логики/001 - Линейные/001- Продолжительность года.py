from math import pi

while True:
	r=input('Введите радиус орбиты (млн'                    '.км. : ')
	if r.isdigit():
		r=float(r)
		break
	else:
		print('Некорректный ввод '
		          'введите числовое значение')
		continue
		
while True:
	v=input('Введите орбитальную '
	               'скорость (км/с) : ')
	if v.isdigit():
		v=float(v)
		break
	else:
		print('Некорректный ввод '
		          'введите числовое значение')
		continue
		
r*=1000000
year=2*pi*r/v
year/=(60*60*24)
print('Продолжительность года = ',
          round(year))