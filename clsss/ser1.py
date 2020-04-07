###Funk!Середнє арифметичне(+калькулятор переведення стрінги в інт)
def foo():
	intList=[]
	b=len(myList)
	for i in range(0,b):
		a=int(myList[i])
		intList.append(a)
	print(intList)
	ser=sum(intList)/b
	print(ser)
myList=input('Enter:').split()
foo()