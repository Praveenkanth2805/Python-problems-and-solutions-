""" Quetion is reverse the number using only number not change the string """

n  = int(input("give a number for reverse:"))
r=0
while n!=0:
	m=n%10
	n=n//1
	r=r*10+m
print("reversed number is:",r)
