from solution_user import Book


def test_basic_parse():
    b = Book.from_csv_line("978-001,Refactoring")
    assert b.isbn == "978-001"
    assert b.title == "Refactoring"


def test_title_with_comma_preserved():
    b = Book.from_csv_line("978-002,Hello, World")
    assert b.isbn == "978-002"
    assert b.title == "Hello, World"


def test_returns_correct_class():
    b = Book.from_csv_line("1,A")
    assert type(b) is Book


def test_polymorphic_via_cls():
    class RareBook(Book):
        pass

    rb = RareBook.from_csv_line("1,A")
    assert type(rb) is RareBook
    assert rb.isbn == "1"
    assert rb.title == "A"
