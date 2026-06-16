"""Choix de design :
- Coroutine interne `_coro` qui maintient (total, count, avg) en variables
  locales : zéro état module-level, c'est l'esprit du chapitre 17.
- `avg = yield avg` : le yield renvoie d'abord la moyenne courante, puis
  reçoit la prochaine valeur via .send(). Sur la première itération avg=0.0,
  ce qui est cohérent avec « aucune valeur reçue encore ».
- Amorçage : `next(coro)` AVANT de retourner la coroutine. Ainsi le client
  fait directement `.send(x)` sur sa première interaction (sinon Python
  lèverait TypeError : "can't send non-None value to a just-started generator").
- `GeneratorExit` : levée par .close() dans le yield ; on `return` proprement.
"""
from __future__ import annotations

from collections.abc import Generator


def make_logprob_accumulator() -> Generator[float, float, None]:
    def _coro() -> Generator[float, float, None]:
        total = 0.0
        count = 0
        avg = 0.0
        while True:
            try:
                lp = yield avg
            except GeneratorExit:
                return
            total += lp
            count += 1
            avg = total / count

    coro = _coro()
    next(coro)  # amorçage : avance jusqu'au premier yield
    return coro
