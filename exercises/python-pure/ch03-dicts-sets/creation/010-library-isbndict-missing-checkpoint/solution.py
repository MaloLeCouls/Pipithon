"""Choix de design (l'idée du chapitre 3) :
- __missing__ n'est invoqué que par d[k] quand k manque. Le garde-fou
  `isinstance(key, str)` -> KeyError casse la récursion : sans lui,
  str(key) absent rappellerait __missing__ à l'infini.
- get() et __contains__ NE doivent PAS s'appuyer sur __missing__ via
  d[k] sans filet : on réutilise __getitem__ en rattrapant KeyError, et
  __contains__ teste les deux formes — sinon `in` et get divergeraient
  de l'accès indexé (le bug classique de StrKeyDict).
"""


class IsbnDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return super().__contains__(key) or super().__contains__(str(key))
