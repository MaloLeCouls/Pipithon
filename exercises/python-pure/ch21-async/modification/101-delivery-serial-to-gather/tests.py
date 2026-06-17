import asyncio
import ast
import inspect

from solution_user import dispatch_all


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_behavior_preserves_order():
    assert _run(dispatch_all(["A", "B", "C"])) == [
        "shipped:A",
        "shipped:B",
        "shipped:C",
    ]


def test_behavior_empty():
    assert _run(dispatch_all([])) == []


def test_behavior_single_package():
    assert _run(dispatch_all(["X"])) == ["shipped:X"]


def test_form_uses_gather():
    src = inspect.getsource(dispatch_all)
    tree = ast.parse(src)
    has_gather = any(
        isinstance(n, ast.Attribute) and n.attr == "gather" for n in ast.walk(tree)
    )
    assert has_gather, "Utilise `asyncio.gather` pour paralléliser."


def test_form_no_await_in_loop():
    """L'anti-pattern visé : `await` dans un for/while = séquentiel."""
    src = inspect.getsource(dispatch_all)
    tree = ast.parse(src)
    for loop_node in ast.walk(tree):
        if isinstance(loop_node, (ast.For, ast.AsyncFor, ast.While)):
            has_await = any(isinstance(n, ast.Await) for n in ast.walk(loop_node))
            assert not has_await, (
                "Plus d'`await` à l'intérieur d'une boucle — utilise gather."
            )
