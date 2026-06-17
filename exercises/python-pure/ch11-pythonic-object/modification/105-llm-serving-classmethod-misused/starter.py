"""Cette `TokenStats.validate_id` est décorée `@classmethod`... mais
son corps n'utilise PAS `cls`. C'est juste une fn utilitaire mal rangée.

Refactore : `@staticmethod`, supprime le param `cls`.

Bénéfice : intent plus clair, et un test typage / lint pourra repérer
quand quelqu'un commencera à utiliser `cls` (= il doit alors revenir
en classmethod).
"""
from __future__ import annotations


class TokenStats:
    def __init__(self, count: int) -> None:
        self.count = count

    @classmethod
    def validate_id(cls, token_id: int) -> bool:
        # n'utilise PAS cls -> doit être une staticmethod.
        return 0 <= token_id < 50_000
