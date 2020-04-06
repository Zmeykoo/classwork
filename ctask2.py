name=input('Are you playing the banjo?\n')
listN=list(name)
for r in listN[0]:
	print('\nsearching...')
	if 'r' in listN[0]:
		print('true')
	elif 'R' in listN[0]:
		print('TRUE')
	else:
		print(False)
###Modern practise in develope...