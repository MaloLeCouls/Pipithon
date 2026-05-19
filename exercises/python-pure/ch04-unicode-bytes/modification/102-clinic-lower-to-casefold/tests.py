import ast
import inspect

from solution_user import same_ci


def test_ascii_behavior_preserved():
    assert same_ci("Marie", "marie") is True
    assert same_ci("Marie", "Jean") is False


def test_hard_fold_now_correct():
    assert same_ci("Straße", "STRASSE") is True


def test_uses_casefold_not_lower():
    src = inspect.getsource(same_ci)
    tree = ast.parse(src)
    attrs = [n.func.attr for n in ast.walk(tree)
             if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)]
    assert "casefold" in attrs, "utilise casefold()"
    assert "lower" not in attrs, "n'utilise plus lower()"


def test_returns_bool():
    assert isinstance(same_ci("a", "a"), bool)


def test_empty_edge():
    assert same_ci("", "") is True
