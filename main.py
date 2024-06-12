from library.book import Book
from library.member import Member
from library.library import Library

def main():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "1234567891")
    library.add_book(book1)
    library.add_book(book2)

    member1 = Member("Alice", "1")
    member2 = Member("Bob", "2")
    library.add_member(member1)
    library.add_member(member2)

    if library.borrow_book("1", "1234567890"):
        print("Alice borrowed The Great Gatsby")
    else:
        print("The book is not available")

    if library.return_book("1", "1234567890"):
        print("Alice returned The Great Gatsby")
    else:
        print("The book was not borrowed")

if __name__ == "__main__":
    main()
