import ast
import inspect

from solution_user import tag_counts

TASKS = [
    {"id": "1", "tags": ["bug", "ui"]},
    {"id": "2", "tags": ["bug"]},
]


def test_behavior_preserved():
    assert dict(tag_counts(TASKS)) == {"bug": 2, "ui": 1}


def test_empty():
    assert dict(tag_counts([])) == {}


def test_uses_counter():
    tree = ast.parse(inspect.getsource(tag_counts))
    used = any(
        isinstance(n, ast.Name) and n.id == "Counter" for n in ast.walk(tree)
    )
    assert used, "utilise collections.Counter"


def test_no_manual_if_increment():
    tree = ast.parse(inspect.getsource(tag_counts))
    assert not any(isinstance(n, ast.If) for n in ast.walk(tree)), \
        "supprime le if/else de comptage"


def test_absent_tag_zero():
    # edge : Counter -> 0 pour une clé absente
    assert tag_counts(TASKS)["doc"] == 0
