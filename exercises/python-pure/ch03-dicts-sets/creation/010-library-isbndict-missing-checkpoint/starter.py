"""CHECKPOINT chapitre 3 — si tu fais ça sans réfléchir, dicts & __missing__
sont acquis.

Une bibliothèque indexe ses livres par ISBN. Les ISBN sont stockés en
str, mais le code appelant passe parfois un int. On veut un mapping
TOLÉRANT : `d[978]` doit trouver la clé "978".

Implémente `IsbnDict(dict)` :
- `__missing__(self, key)` : appelé UNIQUEMENT par d[k] sur clé absente.
    * si `key` est déjà une str -> KeyError (sinon récursion infinie) ;
    * sinon -> retente avec str(key).
- `get(self, key, default=None)` : cohérent avec __getitem__
  (tolérant au type, jamais d'exception).
- `__contains__(self, key)` : True si la clé OU sa version str existe.

Le stockage se fait normalement (d["978"] = "Dune").
"""


class IsbnDict(dict):
    def __missing__(self, key):
        raise NotImplementedError("À implémenter")

    def get(self, key, default=None):
        raise NotImplementedError("À implémenter")

    def __contains__(self, key):
        raise NotImplementedError("À implémenter")
