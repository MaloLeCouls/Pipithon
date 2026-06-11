"""Une pipeline ML loop sur des Sample et appelle un callback pour chaque.

Bug d'annotation : le callback est typé `Callable` nu — mypy --strict refuse,
car il ne sait pas combien d'args attendre ni quel retour vérifier.

Refactor : précise la signature en `Callable[[Sample], None]`.
"""
from collections.abc import Callable, Iterable
from dataclasses import dataclass


@dataclass
class Sample:
    feature: float


def process(samples: Iterable[Sample], callback: Callable) -> None:
    for s in samples:
        callback(s)
