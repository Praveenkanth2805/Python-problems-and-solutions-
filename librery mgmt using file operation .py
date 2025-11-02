def add_book():
    book = input("book name:")
    desc = input("book description:")
##    try
##    with open("librery.txt","x"):
##        print("librery file is createted")
    with open("librery.txt","a") as f:
        f.write(f"{book}|{desc}\n")
    print("book added successfully!!")

def show_book():
    print(FORE.CYAN + "avilable books")
    with open ("librery.txt","r") as f:
        print(f.read())
def search():
    bname=input("book name:").lower()
    found=False
    with open ("librery.txt","r") as f:
        for l in f:
            book,desc=l.strip().split("|")
            if bname in book.lower():
                print(f"book is founded\n bookname:{book},\n description:{desc}")
                found=True
            break
    if not found:
        print("book is not found")

while "True":
    print("\n1. add book")
    print("2. show book")
    print("3 search")
    print("to exit press 9")
    try:
        choice = int(input("what you do:"))
        if choice ==1:
            add_book()
        elif choice ==2:
            show_book()
        elif choice ==3:
            search()
        elif choice ==9:
            print("program finished successfully")
            break
        else :
            print("pleace enter valied number")
    except ValueError:
        print("please enter number not charecter")

    #to make update the book
