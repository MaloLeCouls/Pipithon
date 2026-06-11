"""Choix de design :
- WeakValueDictionary : les valeurs sont des références faibles. Si toutes les
  références fortes (extérieures) à un Book disparaissent, l'entrée correspondante
  est automatiquement retirée de l'index.
- Indexation par ISBN (str).
"""
from __future__ import annotations

import weakref


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title


def build_index(books: list[Book]) -> weakref.WeakValueDictionary[str, Book]:
    index: weakref.WeakValueDictionary[str, Book] = weakref.WeakValueDictionary()
    for b in books:
        index[b.isbn] = b
    return index
