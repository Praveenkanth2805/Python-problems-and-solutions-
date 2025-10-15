#question:

"""def isnegative(func):
    def wraper(a,b,c):
        print('decoreter start')
        if a<0 or b<0 or c<0:
            print("negative num is occured")
            return Exception
        func(a,b,c)
        print('decoreter end')
    return wraper

@isnegative
def add(a,b,c):
    d=a+b+c
    print(d)

add(10,20,3)
add(10,20,-23)"""

#it is cant perform like more arguments so we every time adjust the arguments
#but i want to perform any arguments ?

'''answer:'''

def isnegative(func):
    def wraper(*args):
        print('decoreter start')
        for i in args:
            #print(i)
            if i<0:
                print("negative num is occured",i)
                return Exception
        func(*args)
        print('decoreter end')
    return wraper

@isnegative
def add(*args):
    c=sum(args)
    print(c)
    
add(10,20,3,4)
add(10,20,3,-33)

