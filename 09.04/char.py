def double_char(s):
	b=[i*2 for i in s ]
	print('Origin =',(s))
	res=''
	for a in range(0,len(b)):
		res+=b[a]
	print('Changed =',res)
double_char(input(('Enter word:')))