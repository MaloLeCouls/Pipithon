from solution_user import Book


def test_init_stores_attributes():
    b = Book("978-2", "Dune")
    assert b.isbn == "978-2"
    assert b.title == "Dune"


def test_repr_exact_format():
    assert repr(Book("978-2", "Dune")) == "Book(isbn='978-2', title='Dune')"


def test_repr_quotes_both_fields():
    r = repr(Book("978-0-13", "Fluent Python"))
    assert "'978-0-13'" in r
    assert "'Fluent Python'" in r


def test_repr_returns_str():
    assert isinstance(Book("x", "y").__repr__(), str)


def test_repr_handles_title_with_apostrophe():
    # edge case : un titre avec apostrophe ne casse pas le repr
    assert repr(Book("1", "L'Étranger")) == 'Book(isbn=\'1\', title="L\'Étranger")'
