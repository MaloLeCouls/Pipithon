"""Choix de design :
- `str | None` (PEP 604, 3.10+) : plus lisible que Optional[str].
- Sous `from __future__ import annotations`, marche aussi sur 3.9.
"""
from __future__ import annotations


def display_eta(eta: str | None) -> str:
    if eta is None:
        return "pending"
    return eta
