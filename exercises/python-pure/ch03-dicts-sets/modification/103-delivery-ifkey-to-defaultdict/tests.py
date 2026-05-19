import ast
import inspect

from solution_user import by_driver

PKGS = [
    {"tracking": "A", "driver": "Sam"},
    {"tracking": "B", "driver": "Lee"},
    {"tracking": "C", "driver": "Sam"},
]


def test_behavior_preserved():
    assert by_driver(PKGS) == {"Sam": ["A", "C"], "Lee": ["B"]}


def test_order_preserved():
    assert list(by_driver(PKGS)) == ["Sam", "Lee"]


def test_uses_defaultdict():
    tree = ast.parse(inspect.getsource(by_driver))
    used = any(
        isinstance(n, ast.Name) and n.id == "defaultdict"
        for n in ast.walk(tree)
    )
    assert used, "utilise collections.defaultdict"


def test_no_if_key_check():
    tree = ast.parse(inspect.getsource(by_driver))
    assert not any(isinstance(n, ast.If) for n in ast.walk(tree)), \
        "supprime le if d not in groups"


def test_no_phantom_keys():
    # edge : pas de defaultdict renvoyé -> get sur clé absente ne crée rien
    out = by_driver(PKGS)
    _ = out.get("Ghost")
    assert "Ghost" not in out
