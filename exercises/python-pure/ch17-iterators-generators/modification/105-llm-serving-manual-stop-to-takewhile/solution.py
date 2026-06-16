"""Choix de design :
- `itertools.takewhile` est C-implémenté et paresseux : strictement
  équivalent à la boucle + return, mais en une expression.
- Pas de `yield` dans le corps : la fonction n'est plus une generator
  function, elle retourne directement l'iterator de `takewhile`.
- Le prédicat capture `eos_id` dans une closure (revoir ch.9).
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
from itertools import takewhile

from pymistral import Token


def gen_until_eos(stream: Iterable[Token], eos_id: int) -> Iterator[Token]:
    return takewhile(lambda t: t.id != eos_id, stream)
