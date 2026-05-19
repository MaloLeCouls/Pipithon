from solution_user import Sku, build_stock


def test_equality_by_fields():
    assert Sku("A1", "red") == Sku("A1", "red")
    assert Sku("A1", "red") != Sku("A1", "blue")


def test_hash_consistent_with_eq():
    a, b = Sku("A1", "red"), Sku("A1", "red")
    assert hash(a) == hash(b)


def test_usable_as_set_member():
    s = {Sku("A1", "red"), Sku("A1", "red"), Sku("A1", "blue")}
    assert len(s) == 2


def test_usable_as_dict_key():
    d = {Sku("A1", "red"): 5}
    assert d[Sku("A1", "red")] == 5


def test_repr():
    assert repr(Sku("A1", "red")) == "Sku(code='A1', variant='red')"


def test_build_stock_accumulates_same_sku():
    rows = [(("A1", "red"), 3), (("A1", "red"), 2), (("B2", "blue"), 1)]
    stock = build_stock(rows)
    assert stock[Sku("A1", "red")] == 5
    assert stock[Sku("B2", "blue")] == 1


def test_build_stock_distinct_keys():
    # edge : variant différent = clé différente, pas de fusion abusive
    rows = [(("A1", "red"), 1), (("A1", "blue"), 1)]
    assert len(build_stock(rows)) == 2
