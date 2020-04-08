import game, random
print('\nHello gammer! Rules in my beauty game is easy.\nYou just must gues number(0,100) :3(9999 is exit number;1111 is answer)\nRandomNumber is generated!\n\nLet start!!!\n')

def ran():
	"""Функція, що генерую ціле число і підключає модуль"""
	x=random.randint(0,100)
	game.aud(x)
	

	again=input('Бажаєте зіграти ще раз?')
	if again=='yes':
		ran()
	elif again=='Yes':
		ran()
	elif again=='1':
		ran()
ran()