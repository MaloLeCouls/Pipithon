import asyncio
import inspect

from solution_user import sample_all


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_sample_all_is_coroutine_function():
    assert inspect.iscoroutinefunction(sample_all)


def test_returns_values_in_order():
    assert _run(sample_all(["cpu", "mem", "disk"])) == [3, 3, 4]


def test_empty_input_returns_empty_list():
    assert _run(sample_all([])) == []


def test_single_probe():
    assert _run(sample_all(["latency"])) == [7]


def test_results_match_each_name():
    names = ["a", "bb", "ccc", "dddd"]
    assert _run(sample_all(names)) == [1, 2, 3, 4]
