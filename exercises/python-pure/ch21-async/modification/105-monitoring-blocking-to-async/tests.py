import asyncio
import ast
import inspect

from solution_user import aggregate


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_behavior_sum_correct():
    assert _run(aggregate([1, 2, 3, 4])) == 10


def test_behavior_empty():
    assert _run(aggregate([])) == 0


def test_behavior_negative_values():
    assert _run(aggregate([-1, 1, -2, 2])) == 0


def _module_tree():
    import solution_user
    return ast.parse(inspect.getsource(solution_user))


def test_form_no_time_sleep_call():
    """Détecte `time.sleep(...)` n'importe où dans le module."""
    tree = _module_tree()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "sleep" and isinstance(node.func.value, ast.Name):
                assert node.func.value.id != "time", (
                    "Plus de `time.sleep` — c'est bloquant pour la boucle."
                )


def test_form_uses_asyncio_sleep():
    src = inspect.getsource(aggregate)
    tree = ast.parse(src)
    has_async_sleep = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "sleep" and isinstance(node.func.value, ast.Name):
                if node.func.value.id == "asyncio":
                    has_async_sleep = True
                    break
    assert has_async_sleep, "Utilise `asyncio.sleep(0)` pour céder la main."
