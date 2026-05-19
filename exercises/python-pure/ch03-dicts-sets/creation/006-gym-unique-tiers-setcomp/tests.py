import ast
import inspect

from solution_user import distinct_tiers


def test_dedup_and_normalize():
    members = [
        {"name": "A", "tier": "Gold"},
        {"name": "B", "tier": " gold "},
        {"name": "C", "tier": "PREMIUM"},
    ]
    assert distinct_tiers(members) == {"gold", "premium"}


def test_returns_set():
    assert isinstance(distinct_tiers([{"name": "A", "tier": "x"}]), set)


def test_empty():
    assert distinct_tiers([]) == set()


def test_uses_set_comprehension():
    tree = ast.parse(inspect.getsource(distinct_tiers))
    assert any(isinstance(n, ast.SetComp) for n in ast.walk(tree)), \
        "utilise une set comprehension"


def test_single_tier_many_members():
    # edge : 100 membres même formule -> un seul élément
    members = [{"name": str(i), "tier": "basic"} for i in range(100)]
    assert distinct_tiers(members) == {"basic"}
