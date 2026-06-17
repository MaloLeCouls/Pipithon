"""La règle d'or de `__repr__` : si possible, `eval(repr(obj))` doit
reconstruire un objet équivalent. Sinon, au minimum, le `__repr__` doit
ressembler à un APPEL DE CONSTRUCTEUR valide.

Contrat :

- Classe `Chair(ref: str, price: int)`.
- `__repr__(self) -> str` : renvoie `f"Chair(ref='A1', price=99)"` (avec
  les vrais champs). Utilise `!r` pour `ref` (force les guillemets).
"""
from __future__ import annotations


class Chair:
    def __init__(self, ref: str, price: int) -> None:
        self.ref = ref
        self.price = price

    def __repr__(self) -> str:
        raise NotImplementedError("À implémenter")
