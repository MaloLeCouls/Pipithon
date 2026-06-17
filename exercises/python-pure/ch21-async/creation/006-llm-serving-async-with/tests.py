import asyncio
import inspect

import pytest

from solution_user import InferenceSession, generate


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_aenter_aexit_are_coroutines():
    s = InferenceSession("s1")
    assert inspect.iscoroutinefunction(s.__aenter__)
    assert inspect.iscoroutinefunction(s.__aexit__)


def test_happy_path_opens_then_closes():
    s = InferenceSession("s1")

    async def driver():
        async with s as sess:
            out = await generate(sess, "hello")
            return out

    result = _run(driver())
    assert result == "HELLO"
    assert s.events == ["open:s1", "gen:hello", "close:s1"]


def test_close_called_on_exception():
    s = InferenceSession("s2")

    async def driver():
        async with s:
            raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        _run(driver())
    # Le close DOIT avoir été appelé, même si l'exception remonte.
    assert s.events == ["open:s2", "close:s2"]


def test_aexit_does_not_swallow_exception():
    s = InferenceSession("s3")

    async def driver():
        async with s:
            raise ValueError("nope")

    with pytest.raises(ValueError):
        _run(driver())


def test_returns_self_from_aenter():
    s = InferenceSession("s4")

    async def driver():
        async with s as sess:
            return sess is s

    assert _run(driver()) is True
