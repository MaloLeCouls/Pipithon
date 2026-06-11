from solution_user import Route, next_hop


def test_next_hop_first_stop():
    r = Route(depot="Paris", stops=["Lyon", "Marseille"])
    assert next_hop(r) == "Lyon"


def test_next_hop_no_stops_returns_depot():
    r = Route(depot="Paris", stops=[])
    assert next_hop(r) == "Paris"


def test_name_is_next_hop_not_lambda():
    # Le coeur du refactor : __name__ propre, pas '<lambda>'.
    assert next_hop.__name__ == "next_hop"


def test_callable():
    assert callable(next_hop)


def test_is_a_function_not_a_lambda_constant():
    import inspect
    # une fn def a un __qualname__ = "next_hop" ; un lambda assigné à next_hop
    # aurait __qualname__ = "<lambda>".
    assert inspect.isfunction(next_hop)
    assert next_hop.__qualname__ == "next_hop"
