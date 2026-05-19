from dataclasses import FrozenInstanceError

import pytest

from solution_user import BookId


def test_fields():
    b = BookId("978-1", 3)
    assert b.isbn == "978-1"
    assert b.copy_no == 3


def test_frozen():
    b = BookId("978-1", 3)
    with pytest.raises(FrozenInstanceError):
        b.copy_no = 4


def test_hashable_as_set_member():
    s = {BookId("978-1", 1), BookId("978-1", 1), BookId("978-1", 2)}
    assert len(s) == 2


def test_dict_key():
    d = {BookId("978-1", 1): "loaned"}
    assert d[BookId("978-1", 1)] == "loaned"


def test_equality():
    assert BookId("978-1", 1) == BookId("978-1", 1)
    assert BookId("978-1", 1) != BookId("978-1", 2)


def test_hash_consistent_with_eq():
    # edge : contrat a==b => hash(a)==hash(b), généré par frozen
    a, b = BookId("x", 1), BookId("x", 1)
    assert hash(a) == hash(b)
