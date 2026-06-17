import asyncio
import inspect

from solution_user import schedule_all


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_is_coroutine_function():
    assert inspect.iscoroutinefunction(schedule_all)


def test_all_jobs_run():
    sink = _run(schedule_all([10, 20, 30]))
    assert sorted(sink) == [10, 20, 30]


def test_empty_input_no_error():
    assert _run(schedule_all([])) == []


def test_jobs_run_in_order_called():
    # Avec sleep(0), l'ordre d'exécution est l'ordre du scheduling FIFO.
    sink = _run(schedule_all([1, 2, 3, 4, 5]))
    assert sink == [1, 2, 3, 4, 5]


def test_uses_create_task():
    import ast
    tree = ast.parse(inspect.getsource(schedule_all))
    has_create_task = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr == "create_task":
            has_create_task = True
            break
    assert has_create_task, "Utilise `asyncio.create_task`, pas `await coro` direct."
