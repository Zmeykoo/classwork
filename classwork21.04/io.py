#Task3
ji=['1','2','7','8']
ri=[]
for i in ji: # append
	ri.append(int(i))
fi=[int(j) for j in ji]#list comprehension
si=list(map(lambda i: int(i), ji))#map

print(type(si[0]),si,'\n',type(fi[0]),fi)
print(type(ri),ri)