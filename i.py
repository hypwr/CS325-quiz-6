class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class CatalogEditor:
    def link_catalog(self, catalog): #initialize with the catalog
        raise NotImplementedError("Error: implimentation of link_catalog() failed")
                
    def add_book(self,book):
        raise NotImplementedError("Error: implimentation of add_book() failed")

    def remove_book(self, book):
        raise NotImplementedError("Error: ")

class Search:
    def link_catalog(self, catalog): #initialize with the catalog
        raise NotImplementedError("Error: implimentation of link_catalog() failed")

    def search_title(self, title): 
        raise NotImplementedError("Error: implimentation of search_title() failed")
    
    def search_author(self, author): 
        raise NotImplementedError("Error: implimentation of search_author() failed")
    
    def show_books(self):
        raise NotImplementedError("Error: implimentation of show_books() failed")

class BorrowAndReturn:
    def link_catalog(self, catalog): #initialize with the catalog
        raise NotImplementedError("Error: implimentation of link_catalog() failed")

    def link_user(self, user):
        raise NotImplementedError("Error: implimentation of link_user() failed")

    def borrow_book(self, book):
        raise NotImplementedError("Error: implimentation of borrow_book() failed")

    def return_book(self, book):
        raise NotImplementedError("Error: implimentation of return_book() failed")

class GenerateReport:
    def get_report_data():
        raise NotImplementedError("Error: implimentation of get_report_data() failed")

    def print_report():
        raise NotImplementedError("Error: implimentation of print_report() failed")

class Guest(Search):
    def link_catalog(self, catalog): #initialize with the catalog
        self.catalog = catalog #ideally this catalog is in a seperate database

    def search_title(self, title): 
        books_found=[]
        for book in self.catalog:
            if (book.title==title):
                books_found.append(book)
                print(book.title,"is in the catalog")
        return books_found
    
    def search_author(self, author): 
        books_found=[]
        for book in self.catalog:
            if (book.author==author):
                books_found.append(book)
                print(book.title,"is in the catalog")
        return books_found
    
    def show_books(self):
        for book in self.catalog:
            print(book)

class RegisteredUser(Search,BorrowAndReturn):
    def link_catalog(self, catalog): #initialize with the catalog
        self.catalog = catalog #ideally this catalog is in a seperate database

    def search_title(self, title): 
        books_found=[]
        for book in self.catalog:
            if (book.title==title):
                books_found.append(book)
                print(book.title,"is in the catalog")
        return books_found
    
    def search_author(self, author): 
        books_found=[]
        for book in self.catalog:
            if (book.author==author):
                books_found.append(book)
                print(book.title,"is in the catalog")
        return books_found
    
    def show_books(self):
        for book in self.catalog:
            print(book)

#//////////////////////////////////////////////////
    
    def link_user(self, user):
        self.user = user

    def borrow_book(self, book):
        print(self.user,"has borrowed",book.title)

    def return_book(self, book):
        print(self.user,"has returned",book.title)

class LibraryWorker(CatalogEditor,GenerateReport,Search):
    def link_catalog(self, catalog): #initialize with the catalog
        self.catalog = catalog #ideally this catalog is in a seperate database
                
    def add_book(self,book):
        self.catalog.append(book)

    def remove_book(self, book):
         self.catalog.remove(book)

#//////////////////////////////////////////////////
         
    def get_report_data(self):
        print("Accessing Data")

    def print_report(self):
        print("Here is the report: ")

#//////////////////////////////////////////////////

    def search_title(self, title): 
        books_found=[]
        for book in self.catalog:
            if (book.title==title):
                books_found.append(book)
        print("The book might have been found.")
        return books_found
    
    def search_author(self, author): 
        books_found=[]
        for book in self.catalog:
            if (book.author==author):
                books_found.append(book)
        print("Books by this author might have been found.")
        return books_found
    
    def show_books(self):
        for book in self.catalog:
            print(book.title,"by:",book.author)

def main():
    x = Book("Fahrenheit 451","Ray Bradbury")
    y = Book("Odyssey","Homer")
    z = Book("The Hobbit","J.R.R. Tolkin")

    catalog = [x,y,z]
    
    John = Guest()
    Bob = RegisteredUser()
    Pat = LibraryWorker()

    John.link_catalog(catalog)
    Bob.link_catalog(catalog)
    Bob.link_user("Bob")
    Pat.link_catalog(catalog)

    John.search_title("The Hobbit")
    Bob.borrow_book(x)
    Pat.get_report_data()
    Pat.print_report()
    Pat.show_books()

main()