a=int(input(""))
b=int(input(""))
for count in range(a,b + 1):
   # prime numbers are greater than 1
   if count > 1:
       for i in range(2,count):
           if (count% i) == 0:
               break
       else:
           print(count)
