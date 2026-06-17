"""`__subclasshook__` permet à une ABC de reconnaître **structurellement**
toute classe qui implémente la bonne méthode — sans `register` manuel,
sans héritage. C'est exactement comme ça que `collections.abc.Iterable`
reconnaît tout itérable.

Contrat — ABC `TokenizerABC` :

- Hérite de `abc.ABC`.
- Déclare `@classmethod __subclasshook__(cls, C)` qui renvoie :
  - `True` si N'IMPORTE QUEL parent de C (= dans `C.__mro__`) a un
    attribut `tokenize`,
  - `NotImplemented` sinon (laisse les autres mécanismes décider).
- N'IMPOSE PAS d'héritage. N'IMPOSE PAS de register.

Le résultat : `isinstance(obj, TokenizerABC)` devient True pour TOUTE
classe qui a `tokenize` dans son MRO.

Note : `__subclasshook__` ne doit fonctionner QUE sur la classe ABC
elle-même (cf. piège : sous-classes héritent du hook). Vérifie
`cls is TokenizerABC` avant de répondre — sinon renvoie NotImplemented.
"""
from __future__ import annotations

import abc


class TokenizerABC(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C: type) -> bool | type(NotImplemented):  # type: ignore[valid-type]
        raise NotImplementedError("À implémenter")
