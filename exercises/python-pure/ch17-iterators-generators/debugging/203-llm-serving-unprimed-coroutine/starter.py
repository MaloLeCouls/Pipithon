"""La factory `make_token_counter()` retourne une coroutine classique qui
compte les Tokens reçus via `.send(...)`. À l'usage, le premier `.send(tok)`
explose :

    TypeError: can't send non-None value to a just-started generator

Trouve la cause et corrige. Le contrat attendu :
- `coro = make_token_counter()` retourne une coroutine *prête à recevoir*.
- `coro.send(token)` accumule et yield le compteur courant.
- `coro.close()` ferme proprement.
"""
from __future__ import annotations

from collections.abc import Generator

from pymistral import Token


def make_token_counter() -> Generator[int, Token, None]:
    def _coro() -> Generator[int, Token, None]:
        count = 0
        while True:
            try:
                yield count
            except GeneratorExit:
                return
            count += 1

    coro = _coro()
    # BUG : il manque l'amorçage. Sans `next(coro)`, le premier `.send(tok)`
    # côté appelant lève TypeError (yield jamais atteint encore).
    return coro
