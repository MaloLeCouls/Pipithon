from solution_user import Cart


def test_empty_cart_has_len_zero():
    assert len(Cart()) == 0


def test_len_reflects_additions():
    c = Cart()
    c.add("SKU-1")
    c.add("SKU-2")
    assert len(c) == 2


def test_duplicates_are_counted():
    c = Cart()
    c.add("SKU-1")
    c.add("SKU-1")
    assert len(c) == 2


def test_len_returns_int():
    c = Cart()
    c.add("SKU-1")
    assert isinstance(len(c), int)


def test_two_carts_are_independent():
    # edge case : pas d'état de classe partagé entre instances
    a, b = Cart(), Cart()
    a.add("SKU-1")
    assert len(a) == 1
    assert len(b) == 0
