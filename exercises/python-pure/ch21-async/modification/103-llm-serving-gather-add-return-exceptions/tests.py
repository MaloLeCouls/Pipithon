import asyncio
import ast
import inspect

from solution_user import batch


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_behavior_all_success():
    assert _run(batch(["hi", "yo"])) == [2, 2]


def test_behavior_mixed_with_failure():
    assert _run(batch(["hi", "", "world"])) == [2, None, 5]


def test_behavior_does_not_raise_on_failure():
    # Sans return_exceptions=True, le `""` ferait péter le batch.
    _run(batch([""]))  # doit terminer sans exception


def test_behavior_empty_batch():
    assert _run(batch([])) == []


def test_form_uses_return_exceptions():
    src = inspect.getsource(batch)
    tree = ast.parse(src)
    found = False
    for node in ast.walk(tree):
        if isinstance(node, ast.keyword) and node.arg == "return_exceptions":
            found = True
            break
    assert found, "Utilise `return_exceptions=True` dans `gather`."
