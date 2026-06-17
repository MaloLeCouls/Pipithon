"""Cette fn `is_pingable` utilise `hasattr` + `callable` pour vérifier
qu'un objet a une méthode `ping()`. Ça marche, mais c'est artisanal et
ne profite pas du système de typage. Refactore avec un Protocol
`@runtime_checkable`.

Contrat de la solution :
- Déclare `Pingable(Protocol)` avec `def ping(self) -> bool: ...`,
  décoré `@runtime_checkable`.
- `is_pingable(obj)` renvoie `isinstance(obj, Pingable)`.
- Sémantique INCHANGÉE : True si l'objet a `ping`, False sinon.
"""
from __future__ import annotations


def is_pingable(obj: object) -> bool:
    return hasattr(obj, "ping") and callable(getattr(obj, "ping", None))
