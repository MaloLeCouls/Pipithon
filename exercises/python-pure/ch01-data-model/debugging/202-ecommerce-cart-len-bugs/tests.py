from solution_user import Cart


def test_empty_cart_len_zero():
    assert len(Cart()) == 0


def test_single_add():
    c = Cart()
    c.add("SKU-1")
    assert len(c) == 1


def test_add_does_not_overwrite():
    c = Cart()
    c.add("SKU-1")
    c.add("SKU-2")
    assert c.items == ["SKU-1", "SKU-2"]
    assert len(c) == 2


def test_many_adds():
    c = Cart()
    for i in range(5):
        c.add(f"SKU-{i}")
    assert len(c) == 5


def test_duplicate_skus_kept():
    # edge : deux fois le même SKU = 2 lignes (pas une déduplication)
    c = Cart()
    c.add("SKU-1")
    c.add("SKU-1")
    assert len(c) == 2
