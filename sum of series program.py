#sum of series program
n=int(input("give a value of n:"))
l=set()
for i in range(1,n+1):
    l.add(i)
print(sum(l))
