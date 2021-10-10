class library:
    Booker={}
    List_of_Books=[]
    def __init__(self,Books1,library_name):
        for i in list(Books1):
            self.Books=library.List_of_Books.append(i)
        self.library=library_name
    def Display(self):
        print("List Of  Books in our library:")
        for i in enumerate(library.List_of_Books,start=1):
            print(i)
    def Lend(self):
        Book_name=input("Tell The Book Name:")
        lender=input("Tell Your name:")
        library.Booker[Book_name]=lender
        if Book_name in library.List_of_Books:
            print("Have the Book")
            print(library.Booker)
            library.List_of_Books.remove(Book_name)
        else:
            print("xyz Already Have this book")
    def Add(self):
        Book_add=input("Name of Book:")
        username = input("Enter Your Name:")
        print(f"{username} has added the book {Book_add}")
        library.List_of_Books.append(Book_add)
    def Return(self):
        Name_Of_book=input("Enter Book name:")
        username1=input("Enter Your Name:")
        try:
            del library.Booker[Name_Of_book]
            library.List_of_Books.append(Name_Of_book)
        except KeyError:
            print("This Book is not in our register")
        print("Thank You For returning the Book")
# x=input("Enter Your Library name:")
# libbooks=list(input("Enter the books You have:"))
# y=x+"Library"
# y=library(libbooks,x)
A=library(["rat","cat","fat"],"Akshay")
y=A
while True:
    print("Choose From the Following\n"
          "1:Display All Books\n"
          "2:Lend the books\n"
          "3:Add the Books\n"
          "4:return the Book")
    choice=int(input("Enter Yours Choice:"))
    if choice==1:
        y.Display()
    elif choice==2:
        y.Lend()
    elif choice==3:
        y.Add()
    elif choice==4:
        y.Return()
    elif choice==0:
        print("Quiting...")
        break
    else:
        print("Enter valid choice")
        continue
    print("-------------------------------------------")
