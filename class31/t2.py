for a in range (0,11):
	if a==0:
		print(a,'- / on anything')
	elif a%2==0:
		print(a,'- even number and /2')
	elif a%3==0:
		print(a,'- odd number and /3')
	elif a%2!=0 and a%3!=0:
		print(a,'- odd number but don*t /3, /2')