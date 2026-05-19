"""Un service de livraison modélise une adresse immuable.

Implémente `Address` avec typing.NamedTuple :
- champs : `street: str`, `city: str`, `zip_code: str`,
- doit être immuable (modifier un champ lève une erreur),
- reste un tuple (indexable, déballable).
"""

from typing import NamedTuple  # noqa: F401


class Address:
    ...
