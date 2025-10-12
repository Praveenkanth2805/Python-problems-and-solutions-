##def isnegative(func):
##    print('decoreter start')
##    func()
##    print('decoreter end')
##
##@isnegative
##def add():
##    c=10+20
##    print(c)
##
##

def isnegative(func):
    def wraper(*args):
        print('decoreter start')
        for i in args:
            #print(i)
            if i<0:
                print("negative num is occured",i)
                return Exception
        return func(*args)
        print('decoreter end')
    return wraper

##@isnegative
##def add(a,b,d):
##    c=a+b+d
##    print(c)

@isnegative
def add(*args):
    c=sum(args)
    return c


print(add(10,20,3,4))


