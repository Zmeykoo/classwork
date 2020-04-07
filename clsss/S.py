###Funk!
import math
def fun():
	def returno():
		b=int(input('Бажаєте порахувати площину іншої фігури?\n(Yes-1;No-0):'))
		if b==0:
			print('Дякую за використування мого калькулятором')
		else:
			fun()	
	def kv(a,b,c,d):
		print('Відбувається пошук площини...')
		s=a+b+c+d
		print(s,'см - Площа квадрата')
	def tryk(a,b,c):
		print('Відбувається пошук площини...')
		p=(a+b+c)/2
		s=math.sqrt(p*(p-a)*(p-b)*(p-c))
		print(s,'см - Площа трикутника')
	def kolo(r):
		#r=int(input('Enter r:'))
		print('Відбувається пошук площини...')
		p='PI'
		s=r**2
		print(s,p,'см - Площа кола')

	ch=int(input('Площу якої фігури порахувати?\n1.Квадрат\n2.Трикутник\n3.Коло\n:'))
	if ch==1:
		print('Введіть сторони прямокутника:')
		kv(int(input('Enter a:\n')),int(input('Enter b:\n')),int(input('Enter c:\n')),int(input('Enter d:\n')))
	elif ch==2:
		print('Введіть сторони трикутника:')
		tryk(int(input('Enter a:\n')),int(input('Enter b:\n')),int(input('Enter c:\n',)))
	elif ch==3:
		print('Введіть радіус кола:')
		kolo(int(input('Enter r:')))
	else:
		print('Такого варіанта не існує')
	returno()
fun()
