"""Choix de design :
- Generator expression : sémantiquement équivalente à la list comp pour
  l'itération, mais paresseuse — aucun élément n'est calculé tant qu'on
  ne tire pas.
- Pas de `yield` : la fonction retourne directement l'iterator produit par
  la genexpr. C'est la forme la plus concise pour un filtre lazy.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Package:
    def __init__(self, tracking_id: str, status: str) -> None:
        self.tracking_id = tracking_id
        self.status = status


def pending_tracking_ids(packages: Iterable[Package]) -> Iterator[str]:
    return (p.tracking_id for p in packages if p.status == "pending")
