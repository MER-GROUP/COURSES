if isinstance('5',str):
	print('объекты равны')
else:
	print('объекты не равны')
	
if isinstance('5',int):
	print('объекты равны')
else:
	print('объекты не равны')
	
if isinstance('5',(int,str)):
	print('объекты равны')
else:
	print('объекты не равны')
	
if type(None)==type(None):
	print('объекты равны')
else:
	print('объекты не равны')
	
if type('5')==type(str()):
	print('объекты равны')
else:
	print('объекты не равны')