import asyncio
import inspect

from solution_user import order_by_completion


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_is_coroutine_function():
    assert inspect.iscoroutinefunction(order_by_completion)


def test_completion_order_simple():
    # delays sont strictement croissants -> ordre par index croissant
    assert _run(order_by_completion([0.0, 0.01, 0.02])) == [0, 1, 2]


def test_completion_order_inverted():
    # Le plus court (index 2) finit le premier
    assert _run(order_by_completion([0.03, 0.02, 0.01])) == [2, 1, 0]


def test_empty_delays():
    assert _run(order_by_completion([])) == []


def test_all_indices_present():
    result = _run(order_by_completion([0.01, 0.02, 0.03, 0.0, 0.015]))
    assert sorted(result) == [0, 1, 2, 3, 4]
    # Le délai 0 (index 3) doit arriver en premier
    assert result[0] == 3
