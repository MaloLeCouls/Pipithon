import asyncio
import inspect

import pytest

from solution_user import BatchStream


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


BATCHES = [[1, 2], [3, 4], [5]]


def test_aiter_is_sync_and_returns_self():
    s = BatchStream(BATCHES)
    assert not inspect.iscoroutinefunction(s.__aiter__), \
        "`__aiter__` doit être sync (def), pas async."
    assert s.__aiter__() is s


def test_anext_is_coroutine():
    s = BatchStream(BATCHES)
    assert inspect.iscoroutinefunction(s.__anext__)


def test_async_for_iterates_all():
    s = BatchStream(BATCHES)

    async def driver() -> list[list[int]]:
        out: list[list[int]] = []
        async for b in s:
            out.append(b)
        return out

    assert _run(driver()) == BATCHES


def test_stop_async_iteration_at_end():
    s = BatchStream([[1]])

    async def driver() -> None:
        await s.__anext__()  # premier batch
        # le suivant doit lever StopAsyncIteration
        await s.__anext__()

    with pytest.raises(StopAsyncIteration):
        _run(driver())


def test_empty_stream_stops_immediately():
    s = BatchStream([])

    async def driver() -> list[list[int]]:
        out: list[list[int]] = []
        async for b in s:
            out.append(b)
        return out

    assert _run(driver()) == []
