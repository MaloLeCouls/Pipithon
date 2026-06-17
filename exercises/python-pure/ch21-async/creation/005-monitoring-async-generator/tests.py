import asyncio
import inspect

from solution_user import collect, stream_metrics


def _run(coro):
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_stream_is_async_generator_function():
    assert inspect.isasyncgenfunction(stream_metrics), \
        "`stream_metrics` doit être un async generator function (`async def` + `yield`)."


def test_collect_basic():
    assert _run(collect([1, 2, 3])) == [2, 4, 6]


def test_collect_empty():
    assert _run(collect([])) == []


def test_stream_can_be_iterated_directly():
    async def driver() -> list[int]:
        gen = stream_metrics([5, 10])
        out: list[int] = []
        async for x in gen:
            out.append(x)
        return out

    assert _run(driver()) == [10, 20]


def test_collect_uses_async_for():
    # Vérifie la PRÉSENCE syntaxique d'un `async for`. Coquetterie pédago.
    import ast
    tree = ast.parse(inspect.getsource(collect))
    assert any(isinstance(n, ast.AsyncFor) for n in ast.walk(tree)), \
        "Utilise `async for`, pas un while + __anext__ manuel."
