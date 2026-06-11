"""Choix de design :
- list[int] : syntaxe PEP 585 (3.9+), préférée à typing.List[int].
- sum() sur générateur booléen : True = 1, False = 0.
"""
from __future__ import annotations


def count_urgent(priorities: list[int]) -> int:
    return sum(1 for p in priorities if p == 1)
