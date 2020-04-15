word=list(input('enter:'))
big=[word[j].upper() for j in range(len(word))]
if word==big:
	print('True')
else:
	print('False')