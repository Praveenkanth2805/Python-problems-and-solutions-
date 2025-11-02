with open("librery.txt","r") as f:
    for l in f:
        book,desc = l.strip().split("|")
        print(book)
        print(desc)
