import inspect

from solution_user import dispatch


# --------------- Comportement préservé.
def test_behaviour_with_explicit_log():
    out = dispatch("X1", ["seed"])
    assert out == ["seed", "X1"]


def test_returns_log():
    out = dispatch("X2", [])
    assert out == ["X2"]


# --------------- Forme : plus de défaut mutable.
def test_default_is_not_a_list():
    sig = inspect.signature(dispatch)
    default = sig.parameters["log"].default
    assert default is None, f"le défaut doit être None, pas {default!r}"


def test_two_calls_without_log_do_not_share_state():
    # le cœur du refactor : deux appels successifs sans log ne partagent rien.
    a = dispatch("A")
    b = dispatch("B")
    assert a == ["A"]
    assert b == ["B"]


def test_explicit_log_not_replaced():
    src: list[str] = []
    out = dispatch("X", src)
    assert out is src  # même liste, on a ajouté dedans
