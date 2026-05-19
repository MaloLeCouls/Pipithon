from solution_user import Book


def test_attributes_preserved():
    b = Book("1", "Dune")
    assert b.isbn == "1"
    assert b.title == "Dune"


def test_repr_is_unambiguous():
    assert repr(Book("1", "Dune")) == "Book(isbn='1', title='Dune')"


def test_str_is_human_readable():
    assert str(Book("1", "Dune")) == "Dune (1)"


def test_to_string_removed():
    assert not hasattr(Book, "to_string"), "to_string() doit disparaître"


def test_print_uses_str_not_repr(capsys):
    # edge : print() doit passer par __str__ (lisible), pas __repr__
    print(Book("1", "Dune"))
    assert capsys.readouterr().out.strip() == "Dune (1)"
