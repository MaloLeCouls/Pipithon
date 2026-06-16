"""Choix de design (correctif) :
- Une coroutine classique doit toujours être *amorcée* avant son premier
  `.send(...)` : appeler `next(coro)` une fois avance l'exécution jusqu'au
  premier `yield`, où elle attend une valeur.
- C'est la responsabilité de la *factory* (`make_token_counter`) — l'appelant
  ne doit pas avoir à se soucier de l'amorçage.
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
    next(coro)  # amorçage : avance jusqu'au premier yield
    return coro
