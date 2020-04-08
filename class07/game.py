###module for 1 task
def plus(a,b):

	print('Сума =',a+b)
def minus(a,b):

	print('Різниця =',a-b)
def dil(a,b):

	print('Ділення =',a/b)
def mnog(a,b):

	print('Множина =',a*b)
###module for 2 task
def aud(x):
	""""Generate random int number"""
	def do():
		print (x)
		c=int(input('Number:'))
		if x!=c:
			print('try again')
			do()
		else:
			print('You win')
	do()

	