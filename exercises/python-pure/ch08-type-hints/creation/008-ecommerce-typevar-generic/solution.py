"""Choix de design :
- TypeVar T : Iterable[T] -> T, default: T. mypy vérifie la cohérence.
- next(iter(...), default) est la one-liner idiomatique pour ce besoin.
"""
from __future__ import annotations

from collections.abc import Iterable
from typing import TypeVar

T = TypeVar("T")


def first_or_default(items: Iterable[T], default: T) -> T:
    return next(iter(items), default)
