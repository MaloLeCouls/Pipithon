from solution_user import top_orders


def test_sorted_descending_by_total():
    orders = [
        {"id": "a", "total": 30},
        {"id": "b", "total": 100},
        {"id": "c", "total": 50},
    ]
    out = top_orders(orders)
    assert [o["id"] for o in out] == ["b", "c", "a"]


def test_uses_itemgetter_not_lambda():
    import inspect
    src = inspect.getsource(top_orders)
    assert "itemgetter" in src, "utilise operator.itemgetter, pas un lambda"


def test_does_not_mutate_input():
    orders = [{"id": "a", "total": 1}, {"id": "b", "total": 2}]
    top_orders(orders)
    assert [o["id"] for o in orders] == ["a", "b"]


def test_empty_input():
    assert top_orders([]) == []


def test_handles_ties_stably():
    orders = [{"id": "a", "total": 10}, {"id": "b", "total": 10}]
    # Tri stable : l'ordre relatif des ex-aequo est préservé.
    assert top_orders(orders) == orders
