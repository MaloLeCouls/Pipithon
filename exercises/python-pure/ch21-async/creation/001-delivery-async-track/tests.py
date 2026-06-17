import asyncio
import inspect

from solution_user import lookup


def _run(coro):
    """Helper portable CPython / Pyodide : `asyncio.run` refuse si une boucle
    tourne déjà (cas Pyodide). On crée un loop neuf et on le ferme proprement.
    """
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def test_lookup_is_coroutine_function():
    assert inspect.iscoroutinefunction(lookup), \
        "`lookup` doit être déclarée avec `async def`."


def test_lookup_known_tracking_id():
    assert _run(lookup("TRK-001")) == "delivered"


def test_lookup_unknown_tracking_id():
    assert _run(lookup("ZZZ-9")) == "unknown"


def test_lookup_empty_short_circuits():
    assert _run(lookup("")) == "invalid"


def test_calling_without_await_returns_coroutine():
    # On NE doit PAS l'appeler comme une fn sync — l'appel renvoie une
    # coroutine, pas une str. Test pédagogique : montre la trace d'erreur.
    result = lookup("TRK-2")
    assert inspect.iscoroutine(result), \
        "Sans await, `lookup(...)` renvoie une coroutine non exécutée."
    result.close()  # évite le RuntimeWarning « never awaited »
