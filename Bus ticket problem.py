"""
    quition : Write a program
    that checks the price of the bus ticket for that location,
    and then allows theuser to choose whether to buy the ticket or not

"""


vpm="villupuram"
tvm="tiruvannamalai"
kpm="kanchipuram"
user=input("where you go 'you are in thambaram':").lower()
if vpm==user:
    print(vpm,"Price:200")
    a=input("Do you want to buy a ticket:(y/n)").lower()
    if a =='y' or a=="yes":
        print("Ticket successfully buyed!")
    else:
        print("Not buyed!")
    
elif kpm==user:
    print(kpm,"Price:100")
    a=input("Do you want to buy a ticket:(y/n)").lower()
    if a =='y' or a=="yes":
        print("Ticket successfully buyed!")
    else:
        print("Not buyed!")

elif tvm==user:
    print(tvm,"Price:170")
    a=input("Do you want to buy a ticket:(y/n)").lower()
    if a =='y' or a=="yes":
        print("Ticket successfully buyed!")
    else:
        print("Not buyed!")
else:
    print(" This bus is not goes that place! ")
