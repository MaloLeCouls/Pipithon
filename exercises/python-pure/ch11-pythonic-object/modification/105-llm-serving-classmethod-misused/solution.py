"""Choix de design :
- `@staticmethod` : pas de `cls`, intent clair. Si demain un dev ajoute
  un usage de `cls`, il devra repasser en `classmethod` explicitement.
- Pratique courante en codebases Mistral/vLLM : staticmethod pour la
  validation/parsing pure rangée dans une classe par cohérence.
"""
from __future__ import annotations


class TokenStats:
    def __init__(self, count: int) -> None:
        self.count = count

    @staticmethod
    def validate_id(token_id: int) -> bool:
        return 0 <= token_id < 50_000
