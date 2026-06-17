"""Tu écris un `WordTokenizer` qui hérite de `BaseTokenizer` (ABC).
Tu implémentes `encode`... et à l'instanciation : TypeError.

Indices :
- `BaseTokenizer` déclare DEUX méthodes abstraites.
- Tu n'en as overridé qu'UNE.
- Ajoute l'implémentation de l'autre (décode l'inverse d'encode).
"""
from __future__ import annotations

import abc


class BaseTokenizer(abc.ABC):
    @abc.abstractmethod
    def encode(self, text: str) -> list[int]: ...

    @abc.abstractmethod
    def decode(self, ids: list[int]) -> str: ...


class WordTokenizer(BaseTokenizer):
    def encode(self, text: str) -> list[int]:
        return [len(w) for w in text.split()]

    # BUG : `decode` manque -> WordTokenizer() lève TypeError.
