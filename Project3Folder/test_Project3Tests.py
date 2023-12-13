def test_library_find_book():
    library = Library()
    book = Book("Test Book", "Author Name", 1234567890)
    library.add_book(book)
    found = library.find_book(1234567890)
    assert found == book

def test_library_find_book_not_found():
    library = Library()
    book = Book("Test Book", "Author Name", 1234567890)
    library.add_book(book)
    found = library.find_book(9876543210)
    assert found is None

def test_library_find_book_multiple_matches():
    library = Library()
    book1 = Book("Test Book 1", "Author Name", 1234567890)
    book2 = Book("Test Book 2", "Author Name", 1234567890)
    library.add_book(book1)
    library.add_book(book2)
    found = library.find_book(1234567890)
    assert found == book1  # Assuming the first match is returned