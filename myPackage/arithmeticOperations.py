def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        return a/b
    except:
        print("cannot divide by zero(0)")
        
def floorDiv(a,b):
    try:
        return a//b
    except:
        print("cannot floor divide by zero(0)")
def power(a,b):
    return a**b
def mod(a,b):
    try:
        return a%b
    except:
        print("cannot modules by zero(0)")


