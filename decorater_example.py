def isnegative(func):
    print('decoreter start')
    func()
    print('decoreter end')

@isnegative
def add():
    c=10+20
    print(c)




