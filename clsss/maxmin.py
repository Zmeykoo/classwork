
###Funk!
from test_docstring import __doc__
a=int(input('Enter a:'))
b=int(input('Enter b:'))
def foo():
	"""Deep DocStrings"""
	if a<b:
		print(b,'- max')
	elif a>b:
		print(a,'- min')
	else:
		print(a,'=',b)
	print(__doc__)
foo()