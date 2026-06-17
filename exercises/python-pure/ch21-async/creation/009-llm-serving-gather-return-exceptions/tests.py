import asyncio
import inspect

from solution_user import robust_batch


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_is_coroutine_function():
    assert inspect.iscoroutinefunction(robust_batch)


def test_all_success():
    res = _run(robust_batch(["hi", "hello"]))
    assert res == [("hi", True, 2), ("hello", True, 5)]


def test_one_failure_does_not_break_others():
    res = _run(robust_batch(["ok", "", "world"]))
    assert res[0] == ("ok", True, 2)
    assert res[1][0] == ""
    assert res[1][1] is False
    assert "empty prompt" in res[1][2]
    assert res[2] == ("world", True, 5)


def test_empty_batch():
    assert _run(robust_batch([])) == []


def test_all_failures():
    res = _run(robust_batch(["", ""]))
    assert all(not ok for _, ok, _ in res)
    assert all("empty" in msg for _, _, msg in res)


def test_does_not_raise_on_failures():
    # Sans return_exceptions=True, un seul "" ferait tout péter.
    # Le test passe = la solution gère bien le cas.
    _run(robust_batch([""]))  # ne doit PAS lever
