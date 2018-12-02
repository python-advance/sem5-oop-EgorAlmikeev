class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __repr__(self):
        return "Book: " + self.author + " – " + self.title

    def __str__(self):
        return "Book: " + self.author + " – " + self.title


class User:
    def __init__(self):
        self.__books = list()

    def show_books(self):
        for b in self.__books:
            print(b)

    def borrow_book(self, book):
        if not isinstance(book, Book):
            raise TypeException
        self.__books.append(book)


b1 = Book('Nick', 'book1')
b2 = Book('Egor', 'book2')
u1 = User()
u1.borrow_book(b1)
u1.borrow_book(b2)
u1.show_books()
