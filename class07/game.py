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
		c=int(input('Number:'))
		if x!=c:
			if c==9999:
				print('Do not to be sad. Lucky next time')
			elif c==1111:
				print('Random generate number is',x)
			elif c<x:
				print('Worng.Try again','x >',c)
				do()
			elif c>x:
				print('Worng.Try again','x <',c)
				do()
		else:
			print('You win')
	do()
###module for 3 task
def rec():
def tria():
def circ():
	