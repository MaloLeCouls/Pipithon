from solution_user import make_router


def test_first_call_returns_expected():
    r = make_router("Paris")
    assert r("Lyon") == "Paris -> Lyon (delivered)"


def test_calls_do_not_share_extras():
    # le coeur du bug : deux appels successifs ne doivent rien partager.
    r = make_router("Paris")
    r("Lyon")
    out = r("Marseille")
    assert out == "Paris -> Marseille (delivered)"  # PAS "delivered,delivered"


def test_explicit_extras_respected():
    r = make_router("Paris")
    assert r("Lyon", extras=["fragile"]) == "Paris -> Lyon (fragile,delivered)"


def test_routers_with_different_depots_are_independent():
    paris = make_router("Paris")
    lyon = make_router("Lyon")
    assert paris("X") == "Paris -> X (delivered)"
    assert lyon("X") == "Lyon -> X (delivered)"
