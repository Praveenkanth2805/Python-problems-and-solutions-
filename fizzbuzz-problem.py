"""
Quition : print n number of range and if number is divisible by 3 print fizz
            if number is divisible by 5 print buzz
            if number is divisible by 3 and 5 print fizz and buzz
            otherwise print a number.
"""

n=int(input("Give a range:"))
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
