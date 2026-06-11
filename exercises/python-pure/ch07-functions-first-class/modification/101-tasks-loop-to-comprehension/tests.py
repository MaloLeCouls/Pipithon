import ast
import inspect

from solution_user import assigned_to


def test_filters_by_assignee():
    tasks = [
        {"title": "a", "assignee": "alice"},
        {"title": "b", "assignee": "bob"},
        {"title": "c", "assignee": "alice"},
    ]
    assert assigned_to(tasks, "alice") == [
        {"title": "a", "assignee": "alice"},
        {"title": "c", "assignee": "alice"},
    ]


def test_no_match_returns_empty():
    assert assigned_to([{"title": "x", "assignee": "alice"}], "bob") == []


def test_uses_comprehension_not_append():
    src = inspect.getsource(assigned_to)
    tree = ast.parse(src)
    # plus aucun .append dans le corps.
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            assert node.func.attr != "append", "remplace .append par une comprehension"


def test_returns_distinct_list():
    tasks = [{"title": "a", "assignee": "alice"}]
    assert assigned_to(tasks, "alice") is not tasks


def test_empty_input():
    assert assigned_to([], "alice") == []
