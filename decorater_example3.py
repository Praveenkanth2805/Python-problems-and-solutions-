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
def add(a,b):
    c=a+b
    print(c)

add(10,20)
add(10,-2)
