import asyncio
import inspect

from solution_user import stream_batches


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_form_is_async_generator_function():
    assert inspect.isasyncgenfunction(stream_batches), \
        "`stream_batches` doit être une `async def` + `yield`, pas une classe."


def test_behavior_iterates_all_batches():
    batches = [[1, 2], [3, 4], [5]]

    async def driver() -> list[list[int]]:
        out: list[list[int]] = []
        async for b in stream_batches(batches):
            out.append(b)
        return out

    assert _run(driver()) == batches


def test_behavior_empty():
    async def driver() -> list[list[int]]:
        out: list[list[int]] = []
        async for b in stream_batches([]):
            out.append(b)
        return out

    assert _run(driver()) == []


def test_behavior_preserves_order():
    src = [[i] for i in range(5)]

    async def driver() -> list[list[int]]:
        return [b async for b in stream_batches(src)]

    assert _run(driver()) == src
