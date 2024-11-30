class library:

    def __init__(self,books):
        self.books=books
        print("Welcom to the library")

    def display_books(self):
        print("/n Books available in the libarry")
        for books in self.books:
         print(f"books")

    def lend_book(self,book):
       if book in self.books:
          
                    