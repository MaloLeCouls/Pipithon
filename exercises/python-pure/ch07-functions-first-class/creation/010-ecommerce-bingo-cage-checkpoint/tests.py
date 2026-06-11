import pytest

from solution_user import BingoCage


def test_pick_returns_an_item():
    cage = BingoCage(["A", "B", "C"], seed=1)
    pick = cage.pick()
    assert pick in {"A", "B", "C"}


def test_callable_is_alias_of_pick():
    # une instance s'utilise comme une fonction.
    cage = BingoCage(["X", "Y"], seed=0)
    assert callable(cage)
    out = cage()
    assert out in {"X", "Y"}


def test_deterministic_with_same_seed():
    a = BingoCage(["A", "B", "C", "D"], seed=42)
    b = BingoCage(["A", "B", "C", "D"], seed=42)
    assert [a() for _ in range(4)] == [b() for _ in range(4)]


def test_empty_after_consumption():
    cage = BingoCage(["A"], seed=0)
    cage()
    with pytest.raises(LookupError):
        cage()


def test_empty_init_raises_on_first_pick():
    cage = BingoCage([], seed=0)
    with pytest.raises(LookupError):
        cage()


def test_caller_list_is_isolated():
    # copie défensive : muter la source ne touche pas la cage.
    src = ["A", "B"]
    cage = BingoCage(src, seed=0)
    src.append("C")
    picked = {cage(), cage()}
    assert picked == {"A", "B"}


def test_each_pick_consumes_one():
    cage = BingoCage(["A", "B", "C"], seed=1)
    a = cage()
    b = cage()
    c = cage()
    assert {a, b, c} == {"A", "B", "C"}
    with pytest.raises(LookupError):
        cage()
