from solution_user import Book


def test_equal_books_by_value():
    a = Book("1", "A")
    b = Book("1", "A")
    assert a == b


def test_unequal_books():
    assert Book("1", "A") != Book("2", "A")


def test_hash_matches_eq():
    a = Book("1", "A")
    b = Book("1", "A")
    assert hash(a) == hash(b)
    assert a == b


def test_set_dedup():
    s = {Book("1", "A"), Book("1", "A")}
    # Sans __eq__ cohérent : len == 2 (faux). Avec : len == 1.
    assert len(s) == 1


def test_dict_lookup_works():
    d = {Book("1", "A"): "value"}
    assert d[Book("1", "A")] == "value"


def test_form_defines_eq():
    # Vérifie que Book overrride __eq__ (et pas object.__eq__).
    assert Book.__eq__ is not object.__eq__
