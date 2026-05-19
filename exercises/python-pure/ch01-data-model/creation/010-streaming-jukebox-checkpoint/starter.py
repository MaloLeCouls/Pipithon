"""CHECKPOINT chapitre 1 — si tu réussis ça sans réfléchir, le data model
est acquis.

Une plateforme de streaming expose un `Jukebox` : une collection de morceaux
qui se comporte comme une vraie séquence Python.

1. `Track` : un enregistrement immuable avec les champs `title` et `artist`
   (utilise collections.namedtuple ou typing.NamedTuple).

2. `Jukebox` :
   - `__init__(self, tracks: list[Track])`.
   - `__len__`.
   - `__getitem__(self, position)` indexé depuis 0.

Contrainte : tu n'as le DROIT d'écrire QUE __len__ et __getitem__ sur
Jukebox. Interdiction de définir __iter__, __contains__, __reversed__.
Tout doit quand même marcher : `for t in jb`, `t in jb`, `reversed(jb)`,
`random.choice(jb)`, `sorted(jb)`.
"""


def Track(*args, **kwargs):  # à remplacer : Track doit être un namedtuple
    raise NotImplementedError("À implémenter : définis Track comme namedtuple")


class Jukebox:
    def __init__(self, tracks: list) -> None:
        raise NotImplementedError("À implémenter")

    def __len__(self) -> int:
        raise NotImplementedError("À implémenter")

    def __getitem__(self, position):
        raise NotImplementedError("À implémenter")
