a = input(" ")
if(a<=1000):
	if str(a) == str(a)[::-1]:
		print('YES')
	else:
		print('NO')
else:
	print("invald")
