import asyncio
import inspect

from solution_user import infer, serve


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_serve_is_coroutine_function():
    assert inspect.iscoroutinefunction(serve)
    assert inspect.iscoroutinefunction(infer)


def test_serve_returns_values_in_order():
    res = _run(serve(["hi", "hello", "world!"], max_concurrent=2))
    assert res == [2, 5, 6]


def test_serve_empty():
    assert _run(serve([], max_concurrent=3)) == []


def test_serve_respects_concurrency_limit():
    """Test du pic via Semaphore espion : on monkey-patche tracker en
    observant son len à chaque entrée d'`infer`."""

    class SpySemaphore:
        """Wrap d'asyncio.Semaphore qui compte les entrées concurrentes."""

        def __init__(self, k: int) -> None:
            self._sem = asyncio.Semaphore(k)
            self.peak = 0
            self.active = 0

        async def __aenter__(self):
            await self._sem.__aenter__()
            self.active += 1
            self.peak = max(self.peak, self.active)
            return self

        async def __aexit__(self, *exc):
            self.active -= 1
            return await self._sem.__aexit__(*exc)

    spy = SpySemaphore(2)
    tracker: list[int] = []

    async def driver():
        coros = [infer(p, spy, tracker) for p in ["a", "bb", "ccc", "dddd"]]
        return await asyncio.gather(*coros)

    _run(driver())
    # Avec max_concurrent=2, le pic doit être 2 (pas 4).
    assert spy.peak <= 2, f"pic {spy.peak} > limite 2 — le sem est court-circuité ?"


def test_serve_concurrent_one_means_serial():
    spy_tracker_peaks: list[int] = []

    class Spy:
        def __init__(self):
            self._sem = asyncio.Semaphore(1)
            self.active = 0

        async def __aenter__(self):
            await self._sem.__aenter__()
            self.active += 1
            spy_tracker_peaks.append(self.active)
            return self

        async def __aexit__(self, *exc):
            self.active -= 1
            return await self._sem.__aexit__(*exc)

    spy = Spy()
    tracker: list[int] = []

    async def driver():
        coros = [infer(p, spy, tracker) for p in ["x", "y", "z"]]
        return await asyncio.gather(*coros)

    _run(driver())
    assert max(spy_tracker_peaks) == 1
