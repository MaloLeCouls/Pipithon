import asyncio

from solution_user import dispatch


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_dispatch_collects_all_results():
    result = _run(dispatch([1, 2, 3]))
    assert sorted(result) == [1, 2, 3]


def test_dispatch_not_empty():
    result = _run(dispatch([42]))
    assert result, "results est vide — les tasks n'ont pas été awaitées."


def test_dispatch_empty_jobs():
    assert _run(dispatch([])) == []


def test_dispatch_preserves_count():
    result = _run(dispatch(list(range(10))))
    assert len(result) == 10
