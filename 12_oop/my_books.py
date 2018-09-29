class Book:
    """
    Represents a book type

    """

    def __init__(self, title, author, pages=1):
        """
        Initializes a book

        :param title: the title of the book
        :param author: the author of the book
        :param pages: the number of pages
        """
        self.title = title
        self.author = author
        self.pages = pages

    def book_info(self):
        print("{} by {} - {} pages".format(self.title, self.author, self.pages))


class Library:
    """
    collection of my books
    """

    def __init__(self, ownername='Peter'):
        self.owner = ownername
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_library(self):
        print("This is the library of {}".format(self.owner))
        print("It contains {} books:".format(len(self.books)))
        for b in self.books:
            b.book_info()


help(Book)
print("*" * 40)
print(Book.__doc__)


def load_data():
    library = Library(ownername='Anna')
    with open('books.txt', 'r') as books:
        for line in books:
            title, author, pages = tuple(line.strip('\n').split('\t'))
            pages = int(pages)
            # print(title, author, pages)
            book = Book(title, author, pages)
            library.add_book(book)
    library.show_library()
    print(library.__dict__)


if __name__ == '__main__':
    load_data()