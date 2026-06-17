import ast
import inspect

import pytest

from solution_user import extract_int


def test_behavior_returns_int():
    assert extract_int(42) == 42


def test_behavior_rejects_str():
    with pytest.raises(TypeError):
        extract_int("42")


def test_behavior_rejects_float():
    """bool est un int donc accepté ; float strict est rejeté."""
    with pytest.raises(TypeError):
        extract_int(3.14)


def test_form_no_cast_call():
    """`cast` ne doit plus être appelé dans la solution."""
    import solution_user
    tree = ast.parse(inspect.getsource(solution_user))
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            assert n.func.id != "cast", "Plus de `cast` — isinstance narrowe déjà."
