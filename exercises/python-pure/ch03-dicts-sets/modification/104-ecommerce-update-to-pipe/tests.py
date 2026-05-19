import ast
import inspect

from solution_user import merge_pricing


def test_behavior_preserved():
    assert merge_pricing({"A": 1.0}, {"B": 2.0}) == {"A": 1.0, "B": 2.0}


def test_extra_overrides():
    assert merge_pricing({"A": 1.0}, {"A": 9.0}) == {"A": 9.0}


def test_base_not_mutated():
    base = {"A": 1.0}
    merge_pricing(base, {"A": 9.0})
    assert base == {"A": 1.0}


def test_uses_pipe_operator():
    tree = ast.parse(inspect.getsource(merge_pricing))
    has_pipe = any(
        isinstance(n, ast.BinOp) and isinstance(n.op, ast.BitOr)
        for n in ast.walk(tree)
    )
    assert has_pipe, "utilise l'opérateur | de fusion de dicts"


def test_empty_extra_is_copy():
    # edge : extra vide -> copie de base, pas la même référence
    base = {"A": 1.0}
    out = merge_pricing(base, {})
    assert out == base and out is not base
