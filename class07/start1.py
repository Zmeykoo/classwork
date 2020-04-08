import game
def ts1(ch):
	if ch=='+':
		game.plus(a=int(input('Ведіть число a:')),b=int(input('Ведіть число b:')))
	elif ch=='-':
		game.minus(a=int(input('Ведіть число a:')),b=int(input('Ведіть число b:')))
	elif ch=='/':
		game.dil(a=int(input('Ведіть число a:')),b=int(input('Ведіть число b:')))
	elif ch=='*':
		game.mnog(a=int(input('Ведіть число a:')),b=int(input('Ведіть число b:')))
	
	ask=input('To repeat?\n')
	if ask=='yes':
		ts1(input('Виберіть оператор:'))
ts1(input('Виберіть оператор:'))