count = int(input(""))
if count > 1:
    for i in range(2, count):
        if (count % i) == 0:
            print(count, "is not a prime number")
            break
    else:
        print(count, "is a prime number")
else:
    print(cout, "is not a prime number")
