"""Choix de design :
- Iterable[dict] : l'API ne dit plus que list ; elle dit « quelque chose
  qu'on peut itérer une fois ». Plus permissif, donc plus utilisable.
- Le retour reste list[str] (précis, garantissable).
"""
from __future__ import annotations

from collections.abc import Iterable


def titles(tasks: Iterable[dict]) -> list[str]:
    return [t["title"] for t in tasks]
