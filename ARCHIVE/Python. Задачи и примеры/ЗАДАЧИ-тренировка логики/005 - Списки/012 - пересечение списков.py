from random import randint, randrange

def RandAbc():
	ra = chr(randint(ord('a'), ord('d')))
	ba = randint(0, 1)
	if 1 == ba:
		ra = ra.upper()
	return ra

def Gen(myList):
	for i in range(randint(5, 6)):
		myList.append(RandAbc())
		
def GenTwo(myList):
	i = randrange(0, len(myList))
	myList[i] = [RandAbc(), RandAbc()]
	
def SetPer(list1, list2):
	myList = list()
	for i in list1:
		if i in myList:
			continue
		else:
			for j in list2:
				if i == j:
					myList.append(j)
					break
	print(myList)

def Main():
	for _ in range(5):
		print('---Main---') 
		list1 = list()
		Gen(list1)
		#print(list1)
		GenTwo(list1)
		print(list1)
		list2 = list()
		Gen(list2)
		GenTwo(list2)
		print(list2)
		SetPer(list1, list2)
		
		a = [1, 5, 'g', 5, 'h']
		b = [5, 0, 1, 'u', 'g']
		print(set(a))
		print(set(b))
		myList = list(set(a) & set(b))
		print(myList)
		
Main()