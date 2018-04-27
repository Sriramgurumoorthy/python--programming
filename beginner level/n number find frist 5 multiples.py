k=list()
a=input()
try:
	b=int(a)
except:
	print("invalid input")
else:
	for i in range(1,6):
		k.append(str(i*b))
	print(" ".join((k)))	
