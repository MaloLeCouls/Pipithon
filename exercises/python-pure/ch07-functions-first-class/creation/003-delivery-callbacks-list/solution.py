"""Choix de design :
- Comprehension lisible et idiomatique : [cb(package_id) for cb in callbacks].
- Pas besoin de map() ici : la comprehension est plus expressive et compatible
  avec d'éventuels filtres futurs.
"""
from __future__ import annotations

from collections.abc import Callable


def notify_all(
    callbacks: list[Callable[[str], str]], package_id: str
) -> list[str]:
    return [cb(package_id) for cb in callbacks]
