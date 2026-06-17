import ast
import inspect

from solution_user import track_all


def test_behavior_preserves_order():
    assert track_all(["A", "B", "C"]) == [
        "shipped:A",
        "shipped:B",
        "shipped:C",
    ]


def test_behavior_empty():
    assert track_all([]) == []


def test_form_uses_executor_map():
    src = inspect.getsource(track_all)
    tree = ast.parse(src)
    has_map = any(
        isinstance(n, ast.Attribute) and n.attr == "map" for n in ast.walk(tree)
    )
    assert has_map, "Utilise `ex.map(...)`."


def test_form_no_listcomp_calling_track_one():
    """Plus de comprehension qui appelle track_one directement."""
    src = inspect.getsource(track_all)
    tree = ast.parse(src)
    for n in ast.walk(tree):
        if isinstance(n, ast.ListComp):
            for sub in ast.walk(n):
                if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
                    assert sub.func.id != "track_one", \
                        "Pas de track_one direct dans une comprehension — utilise ex.map."
