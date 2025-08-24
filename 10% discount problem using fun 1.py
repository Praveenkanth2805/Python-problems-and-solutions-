'''
                Amount Paid by Customer
A customer buys three items in a shop.
If exactly two items have the same price,
then a 10% discount is applied to those two items.
The program must accept three integers X, Y and Z as the
price of the three items and
then the program must print the amountto be paid by the customer
with the precision up to two decimal places as the output.

Example Input/Output 1:

Input: 100 200 200
Output: 460.00
'''

a=int(input())
b=int(input())
c=int(input())
def per(a,b):
    tot=a+b
    p=tot/100*10
    return p
if a==b:
    p=per(a,b)
    print((a+b+c)-p)
elif a==c:
    p=per(a,c)
    print((a+b+c)-p)
elif b==c:
    p=per(b,c)
    print((a+b+c)-p)
else:
    tot=a+c+b
    print(tot)

