from solution_user import Chair


def test_init_stores_attributes():
    c = Chair("A1", 99)
    assert c.ref == "A1"
    assert c.price == 99


def test_repr_exact_format():
    assert repr(Chair("A1", 99)) == "Chair(ref='A1', price=99)"


def test_repr_quotes_ref_not_price():
    r = repr(Chair("DESK-204", 250))
    assert "'DESK-204'" in r
    assert "price=250" in r
    assert "price='250'" not in r


def test_repr_returns_str():
    assert isinstance(Chair("X", 1).__repr__(), str)


def test_repr_handles_ref_with_apostrophe():
    # edge case : une ref exotique ne doit pas casser le repr
    assert repr(Chair("O'1", 10)) == 'Chair(ref="O\'1", price=10)'
