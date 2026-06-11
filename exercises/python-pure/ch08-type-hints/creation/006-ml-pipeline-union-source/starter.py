"""Une pipeline ML accepte une source de données qui peut être :
- une str (un chemin local — qu'on ne lit pas vraiment ici),
- ou des bytes (données déjà chargées).

Implémente `byte_size(source) -> int` :
- si source est str (chemin), renvoie len(source.encode('utf-8')) (le coût en
  bytes du chemin, simulation).
- si source est bytes, renvoie len(source).

Annote avec `str | bytes` (PEP 604).
"""
from __future__ import annotations


def byte_size(source):
    ...
