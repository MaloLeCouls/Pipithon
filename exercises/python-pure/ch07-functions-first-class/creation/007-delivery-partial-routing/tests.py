from solution_user import make_router, route_from


def test_router_appends_destination():
    f = make_router("Paris")
    assert f("Lyon") == "Paris -> Lyon"


def test_router_keeps_depot_per_call():
    paris = make_router("Paris")
    assert paris("Lyon") == "Paris -> Lyon"
    assert paris("Marseille") == "Paris -> Marseille"


def test_routers_with_different_depots_are_independent():
    paris = make_router("Paris")
    lyon = make_router("Lyon")
    assert paris("X") == "Paris -> X"
    assert lyon("X") == "Lyon -> X"


def test_uses_partial_not_inner_def():
    import inspect
    src = inspect.getsource(make_router)
    assert "partial" in src, "utilise functools.partial"


def test_underlying_route_from_still_works():
    # ne pas casser l'API de base.
    assert route_from("A", "B") == "A -> B"
