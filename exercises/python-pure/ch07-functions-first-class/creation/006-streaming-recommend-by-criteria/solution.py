"""Choix de design :
- Comprehension de filtre, le critère est appelé une fois par film.
- Aucune connaissance du critère côté algo : c'est la beauté de l'HOF.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Movie:
    title: str
    duration_min: int
    genre: str


def recommend(movies: list[Movie], criteria: Callable[[Movie], bool]) -> list[Movie]:
    return [m for m in movies if criteria(m)]
