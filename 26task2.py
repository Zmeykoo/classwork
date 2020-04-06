def rev(a):
	print('Simle:',a)
	a.reverse()
	print('\nReverse:',a)
a=input('''Enter words to list\nUse ',' to separate:''').split(',')
rev(a)