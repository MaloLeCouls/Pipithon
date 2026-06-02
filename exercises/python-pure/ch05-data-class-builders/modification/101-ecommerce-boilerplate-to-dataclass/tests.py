from solution_user import Product


def test_fields_preserved():
    p = Product("A1", 9.9)
    assert p.product_id == "A1"
    assert p.price == 9.9


def test_repr_preserved():
    assert repr(Product("A1", 9.9)) == "Product(product_id='A1', price=9.9)"


def test_eq_preserved():
    assert Product("A1", 9.9) == Product("A1", 9.9)
    assert Product("A1", 9.9) != Product("A1", 10.0)


def test_is_a_dataclass():
    assert "__dataclass_fields__" in vars(Product)


def test_keyword_construction_edge():
    assert Product(product_id="Z", price=1.0) == Product("Z", 1.0)
