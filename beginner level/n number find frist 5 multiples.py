e=list()
d=input()
try:
	b=int(d)
except:
	print("invalid input")
else:
	for i in range(1,6):
		e.append(str(i*b))
	print(" ".join((e)))	
