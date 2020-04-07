###Simple
def bus(cap,on,wait):
	"""cap is the amount of people the bus can hold excuding the driver
	on is the number of people on the bus
	wait is the number of people waiting to get on to the bus"""
	print(cap,on,wait)
	if cap>=on+wait:
		print ('He can fit all',wait,'passengers and +',cap-on-wait)
	elif cap<on+wait:
		print ('He can not fit',on-wait,'of',wait,'waiting')
bus(110,60,50)
###Modern
###in develop