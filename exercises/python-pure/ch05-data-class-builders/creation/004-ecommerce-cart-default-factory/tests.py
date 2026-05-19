from solution_user import Cart


def test_starts_empty():
    assert Cart("C1").items == []


def test_add():
    c = Cart("C1")
    c.add("A1")
    c.add("B2")
    assert c.items == ["A1", "B2"]


def test_instances_are_independent():
    a = Cart("C1")
    b = Cart("C2")
    a.add("A1")
    assert b.items == []


def test_explicit_items():
    c = Cart("C1", ["X"])
    assert c.items == ["X"]


def test_two_default_lists_not_same_object():
    # edge : c'est tout l'enjeu de default_factory
    assert Cart("C1").items is not Cart("C2").items
