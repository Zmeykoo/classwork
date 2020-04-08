import game, random
print('Hello gammer! Rules in my beauty game is easy. You just must gues number :3\nRandomNumber is generated! Let start!!!')
def ran():
	"""Функція, що генерую ціле число і підключає модуль"""
	x=random.randint(0,10)
	game.aud(x)
	

	again=input('Бажаєте зіграти ще раз?')
	if again=='yes':
		ran()
ran()