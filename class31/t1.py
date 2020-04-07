a=input('Enter list:').split()
aList=[]
for i in range (0,len(a)):
	aList.append(int(a[i]))
print(aList)
print(max(a),'- max number',min(a),'- min number')
#
