from solution_user import Book, Catalog


def make_catalog():
    return Catalog([Book("978-2", "Dune"), Book("978-0", "Neuromancer")])


def test_book_repr():
    assert repr(Book("978-2", "Dune")) == "Book(isbn='978-2', title='Dune')"


def test_catalog_len():
    assert len(make_catalog()) == 2


def test_catalog_indexing_returns_book():
    first = make_catalog()[0]
    assert isinstance(first, Book)
    assert first.title == "Dune"


def test_catalog_repr_uses_len():
    assert repr(make_catalog()) == "Catalog(2 books)"


def test_non_empty_catalog_is_truthy():
    assert bool(make_catalog()) is True


def test_empty_catalog_is_falsy_via_len():
    # edge case : __bool__ absent -> fallback sur __len__, donc vide == falsy
    assert bool(Catalog([])) is False
