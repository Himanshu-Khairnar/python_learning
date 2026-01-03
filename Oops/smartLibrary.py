class Library:
    def __init__(self, title, id):
        self.title = title
        self.id = id
        self.browwed = False
    
    def checkOut(self):
        if self.browwed: print("Already browwed")
        else: self.browwed = True
    
    def returnBook(self):
        if self.browwed : self.browwed = False
        else: print("Book was not browwed")


class Book(Library):
    def calulateFine(self,daysLate):
        total = daysLate * 2
        print(f"Total fine is {total}")


class Dvd(Library):
    def calulateFine(self,daysLate):
        total = daysLate * 5
        print(f"Total fine is {total}")


book = Book("Book",1)
Dvd = Dvd("Dvd",2)

book.checkOut()
book.checkOut()
book.returnBook()

Dvd.checkOut()

book.calulateFine(4)
Dvd.calulateFine(3)


