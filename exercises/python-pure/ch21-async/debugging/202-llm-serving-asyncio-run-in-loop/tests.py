import asyncio

from solution_user import serve_one


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_serve_one_returns_token_count():
    assert _run(serve_one("hello")) == 5


def test_serve_one_empty_prompt():
    assert _run(serve_one("")) == 0


def test_serve_one_does_not_raise_runtime_error():
    # Le test passe = on n'appelle plus asyncio.run depuis une coroutine.
    _run(serve_one("ok"))


def test_serve_one_inside_gather():
    """Edge case : si serve_one re-créait un loop, gather le verrait."""

    async def driver():
        return await asyncio.gather(serve_one("a"), serve_one("bb"))

    assert _run(driver()) == [1, 2]
