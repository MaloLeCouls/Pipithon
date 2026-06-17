import asyncio

from solution_user import dispatch_all


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_returns_status_strings():
    result = _run(dispatch_all(["A", "B"]))
    assert result == ["shipped:A", "shipped:B"]


def test_returns_strings_not_coroutines():
    result = _run(dispatch_all(["X"]))
    assert isinstance(result[0], str), \
        f"attendu str, obtenu {type(result[0]).__name__} -> `await` manquant ?"


def test_empty_packages():
    assert _run(dispatch_all([])) == []


def test_preserves_order():
    pkgs = ["A", "B", "C", "D"]
    assert _run(dispatch_all(pkgs)) == [f"shipped:{p}" for p in pkgs]
