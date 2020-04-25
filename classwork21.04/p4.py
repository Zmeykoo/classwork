
mil=[float(i) for i in range(1,25,4)]
def myfun(h):
	h*1.6
km=list(map(myfun,mil))
klm=list(map(lambda x: x*1.6,mil))
print(km,klm)