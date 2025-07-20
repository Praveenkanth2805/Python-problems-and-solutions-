"""
    Quition: Tarzan visits a vegetable shop with A number of 1 rupee coins, B number of 2 rupee coins, C number of 5 rupee coins and D number of 10 rupee coins.

He bought vegetables for X rupees. 

The program must accept the values of A, B, C, D and X as the input.

If Tarzan exactly has Rs.X in his hand, then the program must print Paid as the output.

If he has more amount than Rs.X, then print Paid with the amount remaining in hand as the output.

If he has less amount in hand than Rs.X, then print Not Paid followed by the amount in hand as the output.

Example Input/Output 1:

Input: 2   5    10   15   112

Output: Paid

Example Input/Output 2:

Input:

5   16   3    12    150

Output:Not  Paid   22

Example Input/Output 3:

Input:

10   13   15   20   411

Output:Not Paid  311


"""

a=1*int(input("1 rupee coin you have:"))
b=2*int(input("2 rupee coin you have:"))
c=5*int(input("5 rupee coin you have:"))
d=10*int(input("10 rupee coin you have:"))
x=int(input("you bought amount:"))

tot= a+b+c+d
if ( x == tot):
    print("Paid")
elif ( x < tot):
    print(f"Paid, Remaining:{tot-x}")
else:
    print(f"NotPaid, {tot}")
    
