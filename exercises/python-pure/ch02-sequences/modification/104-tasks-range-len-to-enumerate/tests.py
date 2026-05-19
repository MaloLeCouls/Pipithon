import ast
import inspect

from solution_user import numbered


def test_behavior_preserved():
    assert numbered(["spec", "code", "ship"]) == ["1. spec", "2. code", "3. ship"]


def test_single():
    assert numbered(["only"]) == ["1. only"]


def test_no_range_call():
    tree = ast.parse(inspect.getsource(numbered))
    calls = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
        and n.func.id == "range"
    ]
    assert not calls, "supprime range() : utilise enumerate"


def test_uses_enumerate_and_comprehension():
    tree = ast.parse(inspect.getsource(numbered))
    uses_enum = any(
        isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
        and n.func.id == "enumerate" for n in ast.walk(tree)
    )
    has_listcomp = any(isinstance(n, ast.ListComp) for n in ast.walk(tree))
    assert uses_enum, "utilise enumerate"
    assert has_listcomp, "exprime-le en list comprehension"


def test_empty():
    # edge : pas de tâche -> liste vide
    assert numbered([]) == []
