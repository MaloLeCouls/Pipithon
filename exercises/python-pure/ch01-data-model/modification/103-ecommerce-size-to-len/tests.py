from solution_user import Cart


def test_add_behavior_preserved():
    c = Cart()
    c.add("SKU-1")
    c.add("SKU-2")
    assert c.items == ["SKU-1", "SKU-2"]


def test_len_works():
    c = Cart()
    c.add("SKU-1")
    assert len(c) == 1


def test_size_and_empty_removed():
    assert not hasattr(Cart, "size"), "size() doit disparaître"
    assert not hasattr(Cart, "empty"), "empty() doit disparaître"


def test_truthiness_via_len_fallback():
    assert bool(Cart()) is False
    c = Cart()
    c.add("x")
    assert bool(c) is True


def test_no_explicit_bool_defined():
    # edge : la vérité doit venir du fallback __len__, pas d'un __bool__ ajouté
    assert "__bool__" not in Cart.__dict__
