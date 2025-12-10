from myPackage.arithmeticOperations import add,sub,mul,div,power,floorDiv,mod

print("Simple Calculations")

a=int(input("give num 1:"))
b=int(input("give num 2:"))

print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(mod(a,b))
print(div(a,b))
print(floorDiv(a,b))
print(power(a,b))
