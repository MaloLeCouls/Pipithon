from solution_user import LineItem


def test_fields_set():
    li = LineItem("A1", 2, 9.9)
    assert li.sku == "A1"
    assert li.quantity == 2
    assert li.unit_price == 9.9


def test_repr_generated():
    assert repr(LineItem("A1", 2, 9.9)) == "LineItem(sku='A1', quantity=2, unit_price=9.9)"


def test_eq_generated():
    assert LineItem("A1", 2, 9.9) == LineItem("A1", 2, 9.9)
    assert LineItem("A1", 2, 9.9) != LineItem("A1", 3, 9.9)


def test_not_handwritten_init():
    # __init__ doit venir de @dataclass, pas être écrit à la main
    assert "__dataclass_fields__" in vars(LineItem)


def test_keyword_construction():
    # edge : construction par mots-clés (généré par dataclass)
    li = LineItem(sku="Z9", quantity=1, unit_price=5.0)
    assert li == LineItem("Z9", 1, 5.0)
