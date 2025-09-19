class Bank:
    def __init__(s, balance):
        s.__balance = balance  # private
    def widrow(s,w):
        s.__balance=s.__balance-w                
    def show_balance(s):
        if s.__balance < w:
            print("insufficiant balance")
        else:
            print("Balance:", s.__balance)

acc = Bank(5000)
w=int(input(f"widrow amount:"))
acc.widrow(w)
acc.show_balance()
