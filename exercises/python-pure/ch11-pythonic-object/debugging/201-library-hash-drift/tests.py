import pytest

from solution_user import Book


def test_title_is_readonly():
    """Le fix doit empêcher la mutation directe."""
    b = Book("1", "A")
    with pytest.raises(AttributeError):
        b.title = "B"  # type: ignore[misc]


def test_isbn_is_readonly():
    b = Book("1", "A")
    with pytest.raises(AttributeError):
        b.isbn = "2"  # type: ignore[misc]


def test_set_membership_stable():
    """Même après tentative de mutation, le set retrouve l'objet."""
    b = Book("1", "A")
    s = {b}
    # L'attempt de mutation est rejetée (AttributeError), donc le hash
    # reste stable et l'objet reste retrouvable.
    try:
        b.title = "B"  # type: ignore[misc]
    except AttributeError:
        pass
    assert b in s


def test_eq_and_hash_consistent():
    a = Book("1", "A")
    b = Book("1", "A")
    assert a == b
    assert hash(a) == hash(b)
