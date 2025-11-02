from colorama import Fore, Style, init
init(autoreset=True)
def add_book():
    book = input("book name:")
    desc = input("book description:")
    with open("librery.txt","a") as f:
        f.write(f"{book}|{desc}\n")
    print(Fore.GREEN+"book added successfully!!")
def show_book():
    print(Fore.GREEN+"avilable books")
    with open ("librery.txt","r") as f:
        for l in f:
            b,d=l.strip().split("|")
            print(f"{Fore.CYAN+Style.BRIGHT+b} : {Fore.LIGHTYELLOW_EX+d}")
def search():
    bname=input("book name:").lower()
    found=False
    with open ("librery.txt","r") as f:
        for l in f:
            book,desc=l.strip().split("|")
            if bname in book.lower():
                print(f"{Fore.GREEN}book is founded\n bookname:{book},\n description:{desc}")
                found=True
            break
    if not found:
        print("book is not found")
def delete_book():
    with open("librery.txt","r")as f:
        books=f.readlines()
        show_book()
    d_book=input("what book you delete:").lower()
    deleted=False

    with open("librery.txt","w")as f:
        for l in books:
            b,d=l.strip().split("|")
            if d_book.strip()==b.strip().lower():
                deleted=True
            else :
                f.write(l)
    if not deleted:
        print(Fore.RED+"book is not found")
    else:
        print(Fore.MAGENTA+"book is deleted")
        
while "True":
    print("\n1. add book")
    print("2. show book")
    print("3 search")
    print("4.delete")
    print("to exit press 9")
    try:
        choice = int(input("what you do:"))
        if choice ==1:
            add_book()
        elif choice ==2:
            show_book()
        elif choice ==3:
            search()
        elif choice==4:
            delete_book()
        elif choice ==9:
            print(Fore.LIGHTMAGENTA_EX+"program finished successfully")
            break
        else :
            print(Fore.RED+"pleace enter valied number")
    except ValueError:
        print(Fore.RED+"please enter number not charecter")
