import ast
import inspect
import unicodedata

from solution_user import is_match


def test_identical_preserved():
    assert is_match("Marie", "Marie") is True
    assert is_match("Marie", "Jean") is False


def test_canonical_equivalence_now_matched():
    a = "Zoé"
    b = unicodedata.normalize("NFD", "Zoé")
    assert a != b
    assert is_match(a, b) is True


def test_uses_normalize():
    tree = ast.parse(inspect.getsource(is_match))
    has_norm = any(
        isinstance(n, ast.Attribute) and n.attr == "normalize"
        for n in ast.walk(tree)
    )
    assert has_norm, "utilise unicodedata.normalize"


def test_still_distinguishes_real_differences():
    assert is_match("Zoé", "Zoe") is False


def test_returns_bool_empty():
    # edge
    assert is_match("", "") is True
