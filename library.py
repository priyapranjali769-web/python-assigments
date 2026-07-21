class Book:
    def __init__(self, name):
        self.name = name
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.name, "added.")

    def borrow_book(self, name):
        for book in self.books:
            if book.name == name and book.available:
                book.available = False
                print(name, "borrowed.")
                return
        print("Book not available.")

    def return_book(self, name):
        for book in self.books:
            if book.name == name:
                book.available = True
                print(name, "returned.")
                return

    def show_books(self):
        for book in self.books:
            print(book.name, "-", "Available" if book.available else "Borrowed")


lib = Library()

lib.add_book(Book("Python"))
lib.add_book(Book("Java"))

lib.show_books()
lib.borrow_book("Python")
lib.show_books()
lib.return_book("Python")
lib.show_books()