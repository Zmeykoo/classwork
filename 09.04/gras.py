def simm(max):
	"""Generate list"""
	llist=[x for x in range (max+1) if max>0]
	print(llist,'Suma =',sum(llist))

simm(int(input("lim:")))