import ast
import inspect

from solution_user import first


def test_behavior_returns_first_int():
    assert first([1, 2, 3]) == 1


def test_behavior_returns_first_str():
    assert first(["a", "b"]) == "a"


def test_form_uses_typevar():
    """Le source doit déclarer un TypeVar et l'utiliser sur first."""
    import solution_user
    tree = ast.parse(inspect.getsource(solution_user))
    has_typevar = False
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "TypeVar":
            has_typevar = True
            break
    assert has_typevar, "Déclare un TypeVar."


def test_form_no_any_annotation():
    """Plus d'Any dans la signature."""
    sig = inspect.signature(first)
    for p in sig.parameters.values():
        ann = str(p.annotation)
        assert "Any" not in ann, "Plus d'Any sur les params."
    assert "Any" not in str(sig.return_annotation)
