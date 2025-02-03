class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        
    def display_book_details(self):
        print(f"The title of the book is: {self.title}")
        print(f"The author of the book is: {self.author}")
        print(f"The Internation Standard Book Number(ISBN) is: {self.isbn}")

# input book details
book_name = input("Enter the book name: ")
author_of_the_book = input("Enter the author of the book: ")
isbn = input("Enter the ISBN number: ")

# creating object for the class Book
book = Book(book_name, author_of_the_book, isbn)

book.display_book_details()