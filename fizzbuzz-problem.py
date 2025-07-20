n=int(input("Give a range:))
for i in range(1,n+1):
    if (i%3==0 and i%5==0):
        print("Fizz and Buzz")
        continue
    elif(i%5==0):
	print("Buzz")
	continue
    elif(i%3==0):
	print("Fizz")
	continue
    else:
	print(i)
