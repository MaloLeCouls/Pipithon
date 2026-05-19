from solution_user import purge_unavailable


def test_removes_zero_copies():
    stock = {"978-1": 3, "978-2": 0, "978-3": 1}
    assert purge_unavailable(stock) == {"978-1": 3, "978-3": 1}


def test_no_runtime_error_many_zeros():
    stock = {f"i{i}": (0 if i % 2 else 2) for i in range(20)}
    out = purge_unavailable(stock)
    assert all(v != 0 for v in out.values())


def test_mutates_in_place_and_returns_same_object():
    stock = {"a": 0, "b": 1}
    out = purge_unavailable(stock)
    assert out is stock
    assert stock == {"b": 1}


def test_nothing_to_purge():
    assert purge_unavailable({"a": 1, "b": 2}) == {"a": 1, "b": 2}


def test_all_zero_edge():
    # edge : tout retirer ne doit pas planter
    assert purge_unavailable({"a": 0, "b": 0}) == {}
