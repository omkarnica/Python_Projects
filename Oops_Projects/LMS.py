class Book:
    def __init__(self,author, title,isbn,available):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=available

    def display_info(self):

        print(f'Book Name - {self.title}')
        print(f'Book Author - {self.author}')
        print(f'Boog Unique Id- {self.isbn}')
        print(f'Book Availability - {self.available}')

    def mark_unavailable(self):
        self.available==False

    def mark_available(self):
        self.available==True

class Library:
    def __init__(self):
        self.book_list=[]

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, isbn):
        for b in self.book_list:
            if b.isbn==isbn:
                self.book_list.remove(b)
        
    def borrow_book(self, isbn):
        for b in self.book_list:
            if b.isbn==isbn:
                b.available=False

    def return_book(self, isbn):
        for b in self.book_list:
            if b.isbn==isbn:
                b.available=True

    def display_books(self):
        for b in self.book_list:
            b.display_info()




book1 = Book("Harry Potter", "J.K. Rowling", "12345", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890", True)

library = Library()

library.add_book(book1)
library.add_book(book2)

print("Initial Book List:")
library.display_books()

library.borrow_book("12345")
print("\nAfter Borrowing Harry Potter:")
library.display_books()

library.return_book("12345")
print("\nAfter Returning Harry Potter:")
library.display_books()

library.remove_book("67890")
print("\nAfter Removing To Kill a Mockingbird:")
library.display_books()
