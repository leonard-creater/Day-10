class library:

    def __init__(self,books):
        self.books=books
        print("Welcom to the library")

    def display_books(self):
        print("\n Books available in the libarry")
        for books in self.books:
         print(f"{books}")
         print()

    def lend_book(self,book):
       if book in self.books:
           self.book.remove(book)
           print(f"you have borrowed '{book}',have fun reading.")
             
        

    def return_book(self,book):
        self.books.append(book)
        print(f"thanks for returning the '{book}'.")

    def add_book(self,book):
        self.books.append(book)
        print(f"the book '{book}',has been added to the library")

    def _del_(self):
        print("thank you for using our library.See you soon,bye.")
library=library(["the 13 reality","whimpy kid","Dork dairies","harry porter","jake and jill","parcy jackson"])
library.display_books()                   