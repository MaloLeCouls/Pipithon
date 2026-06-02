import pytest
from dataclasses import FrozenInstanceError

from solution_user import Book


def test_construction_ok():
    b = Book("978-0-13-468599-1", "Fluent Python")
    assert b.isbn == "978-0-13-468599-1"
    assert b.title == "Fluent Python"


def test_isbn_norm_computed():
    b = Book("978-0-13-468599-1", "Fluent Python")
    assert b.isbn_norm == "9780134685991"


def test_still_frozen_outside():
    b = Book("0-13-468599-1", "x")
    with pytest.raises(FrozenInstanceError):
        b.title = "tampered"


def test_usable_as_dict_key():
    b = Book("0-13-468599-1", "x")
    d = {b: 1}
    assert d[Book("0-13-468599-1", "x")] == 1
