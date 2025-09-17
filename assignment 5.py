class book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def get_info(self):
        print("title = ", self.title, "author = ", self.author, "isbn = ", self.isbn, "availability = ", self.available)

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn


class member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(self.name, "borrowed", book.title)
        else:
            print(book.title, "is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(self.name, "returned", book.title)
        else:
            print(self.name, "does not have", book.title)

    def get_membership_id(self):
        return self.__membership_id




