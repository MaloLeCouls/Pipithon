from solution_user import Order, top_orders


def test_sorts_descending_by_total():
    orders = [Order("a", 30), Order("b", 100), Order("c", 50)]
    out = top_orders(orders)
    assert [o.id for o in out] == ["b", "c", "a"]


def test_does_not_raise_on_objects():
    # le coeur du bug : itemgetter() lèverait TypeError sur Order.
    orders = [Order("a", 1)]
    top_orders(orders)


def test_empty():
    assert top_orders([]) == []


def test_does_not_mutate_input():
    orders = [Order("a", 1), Order("b", 2)]
    top_orders(orders)
    assert [o.id for o in orders] == ["a", "b"]
