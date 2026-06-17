import pytest

from solution_user import Book


def test_equal_books_have_equal_hash():
    a = Book("978-1", "Refactoring")
    b = Book("978-1", "Refactoring")
    assert a == b
    assert hash(a) == hash(b)


def test_different_books_unequal():
    assert Book("1", "A") != Book("2", "A")
    assert Book("1", "A") != Book("1", "B")


def test_usable_as_set_member():
    s = {Book("1", "A"), Book("1", "A"), Book("2", "B")}
    assert len(s) == 2  # dédup


def test_usable_as_dict_key():
    d = {Book("1", "A"): 1, Book("2", "B"): 2}
    assert d[Book("1", "A")] == 1


def test_isbn_is_readonly():
    b = Book("1", "A")
    with pytest.raises(AttributeError):
        b.isbn = "2"  # type: ignore[misc]


def test_title_is_readonly():
    b = Book("1", "A")
    with pytest.raises(AttributeError):
        b.title = "B"  # type: ignore[misc]


def test_not_equal_to_other_type():
    assert Book("1", "A") != ("1", "A")
