class Library:

    def __init__(self):
        self.availablebooks = ['book1','book2'
            ,'book3','book4','book5','book6',
             'book7','book8']

    def getAvailableBooks(self):
        return  self.availablebooks

    def displayAvailablebooks(self):
        print('total books are ', len(self.availablebooks))
        for book in self.availablebooks:
            print(book)

    def lendAbook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print("Great! you can take this book..")
            self.availablebooks.remove(requestedBook)
        else:
            print("sorry, currently this book is not in our database, next time it will be available!!!")
            self.availablebooks.append(requestedBook)


    def addAbook(self,returningbook):
        if returningbook in self.availablebooks:
            print("we already have this book")
            quit()
        else:
            self.availablebooks.append(returningbook)
        print("we got the book back to us")

class Customer:

    def requestAbook(self):
        print("Enter your required book:")
        self.book = str(input())
        return  self.book

    def returnAbook(self,):
        lib = Library()
        print("Enter your required book to return :")
        self.book = input()
        if self.book in lib.availablebooks:             #defaultbooks want to take here
            print("yes this is our book. taking back from you")
            return self.book

        else:
            print("this is not our book!!")
            quit()

library =  Library()
customer = Customer()
while True:
    print("*" * 20)
    print('enter 1 to display available books.')
    print('enter 2 to request book.')
    print('enter 3 to return a book.')
    print('enter 4 to exit.')
    choice = int(input(''))
    if choice is 1:
        library.displayAvailablebooks()
    elif choice is 2:
        requestedBook = customer.requestAbook()
        library.lendAbook(requestedBook)
    elif choice is 3:
        returnedBook = customer.returnAbook()
        library.addAbook(returnedBook)
    elif choice is 4:
        quit()

