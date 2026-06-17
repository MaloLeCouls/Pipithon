import asyncio
import ast
import inspect

import pytest

from solution_user import GPULease, run_job


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


async def _noop() -> None:
    return None


async def _boom() -> None:
    raise RuntimeError("kaboom")


def test_behavior_happy_path():
    events: list[str] = []
    _run(run_job("gpu-0", events, _noop()))
    assert events == ["acquire:gpu-0", "release:gpu-0"]


def test_behavior_release_on_exception():
    events: list[str] = []
    with pytest.raises(RuntimeError, match="kaboom"):
        _run(run_job("gpu-1", events, _boom()))
    assert events == ["acquire:gpu-1", "release:gpu-1"]


def test_form_uses_async_with():
    src = inspect.getsource(run_job)
    tree = ast.parse(src)
    assert any(isinstance(n, ast.AsyncWith) for n in ast.walk(tree)), \
        "`run_job` doit utiliser `async with`."


def test_form_no_try_finally_in_run_job():
    src = inspect.getsource(run_job)
    tree = ast.parse(src)
    assert not any(isinstance(n, ast.Try) for n in ast.walk(tree)), \
        "Plus de `try/finally` — c'est le rôle d'`__aexit__`."


def test_gpulease_has_aenter_aexit():
    lease = GPULease("g", [])
    assert inspect.iscoroutinefunction(lease.__aenter__)
    assert inspect.iscoroutinefunction(lease.__aexit__)
