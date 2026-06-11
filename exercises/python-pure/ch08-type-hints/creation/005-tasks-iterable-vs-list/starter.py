"""Compte les tâches d'une certaine priorité.
Tu ne fais qu'itérer : exige le type le plus LARGE possible (Iterable),
pas list. Liskov style : accepte large, retourne précis.

Signature attendue :
- tasks    : Iterable[dict]
- priority : int
- retour   : int
"""
from __future__ import annotations


def count_at_priority(tasks, priority):
    ...
