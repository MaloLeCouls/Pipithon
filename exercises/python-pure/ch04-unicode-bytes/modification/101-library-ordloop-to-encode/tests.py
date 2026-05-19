import ast
import inspect

from solution_user import to_bytes


def test_ascii_behavior_preserved():
    assert to_bytes("Dune") == b"Dune"


def test_accented_now_correct_utf8():
    assert to_bytes("Café") == "Café".encode("utf-8")


def test_returns_bytes():
    assert isinstance(to_bytes("x"), bytes)


def test_uses_encode():
    tree = ast.parse(inspect.getsource(to_bytes))
    calls = [
        n for n in ast.walk(tree)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "encode"
    ]
    assert calls, "utilise str.encode()"


def test_emoji_does_not_crash():
    # edge : l'ancien code levait ValueError ici
    assert to_bytes("ok✅") == "ok✅".encode("utf-8")
