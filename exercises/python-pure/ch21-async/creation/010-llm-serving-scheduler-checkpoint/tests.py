import asyncio
import inspect

from solution_user import LLMScheduler


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_scheduler_is_async_context_manager():
    sched = LLMScheduler(max_concurrent=2)
    assert inspect.iscoroutinefunction(sched.__aenter__)
    assert inspect.iscoroutinefunction(sched.__aexit__)


def test_infer_many_preserves_order():
    async def driver():
        async with LLMScheduler(max_concurrent=2) as sched:
            return await sched.infer_many(["hi", "hello", "world!"])

    assert _run(driver()) == [2, 5, 6]


def test_infer_many_empty():
    async def driver():
        async with LLMScheduler(max_concurrent=2) as sched:
            return await sched.infer_many([])

    assert _run(driver()) == []


def test_as_they_complete_yields_all_indices():
    async def driver() -> list[tuple[int, int]]:
        async with LLMScheduler(max_concurrent=3) as sched:
            out: list[tuple[int, int]] = []
            async for item in sched.as_they_complete(["a", "bb", "ccc"]):
                out.append(item)
            return out

    items = _run(driver())
    assert sorted(items) == [(0, 1), (1, 2), (2, 3)]


def test_as_they_complete_is_async_generator():
    sched = LLMScheduler(max_concurrent=2)
    assert inspect.isasyncgenfunction(sched.as_they_complete)


def test_infer_one_respects_semaphore():
    """Vérifie qu'on ne dépasse jamais max_concurrent en vol."""
    sched = LLMScheduler(max_concurrent=2)
    peak = [0]
    active = [0]

    # On wrappe infer_one pour observer le pic réel
    original_infer_one = sched.infer_one

    async def spying_infer_one(prompt: str) -> int:
        async with sched._sem:
            active[0] += 1
            peak[0] = max(peak[0], active[0])
            await asyncio.sleep(0)
            try:
                return len(prompt)
            finally:
                active[0] -= 1

    sched.infer_one = spying_infer_one  # type: ignore[method-assign]

    async def driver():
        return await sched.infer_many(["a", "b", "c", "d", "e"])

    _run(driver())
    assert peak[0] <= 2

    sched.infer_one = original_infer_one  # type: ignore[method-assign]


def test_uses_gather_and_as_completed_and_semaphore():
    """Coquetterie : check AST que les bons appels sont là."""
    import ast
    src = inspect.getsource(LLMScheduler)
    tree = ast.parse(src)
    attrs = {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    assert "gather" in attrs, "infer_many doit utiliser asyncio.gather"
    assert "as_completed" in attrs, "as_they_complete doit utiliser asyncio.as_completed"
    assert "Semaphore" in attrs, "Le scheduler doit utiliser asyncio.Semaphore"
