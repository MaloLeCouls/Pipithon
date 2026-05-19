from solution_user import Chair


def test_ref_is_stored():
    assert Chair("A1", 99).ref == "A1"


def test_price_is_stored():
    assert Chair("A1", 99).price == 99


def test_repr_does_not_raise():
    # le bug "price non stocké" faisait planter __repr__ par AttributeError
    assert isinstance(repr(Chair("A1", 99)), str)


def test_repr_quotes_ref_not_price():
    r = repr(Chair("A1", 99))
    assert r == "Chair(ref='A1', price=99)"
    assert "price='99'" not in r


def test_repr_with_apostrophe_ref():
    # edge : le fix doit rester correct pour une ref biscornue
    assert repr(Chair("O'1", 5)) == 'Chair(ref="O\'1", price=5)'
