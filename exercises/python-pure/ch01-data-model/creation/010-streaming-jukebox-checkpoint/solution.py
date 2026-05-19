"""Choix de design (l'idée centrale du chapitre 1) :
- Track est un namedtuple : immuable, comparable, hashable, repr gratuit.
- Jukebox n'implémente QUE __len__ et __getitem__. Le protocole séquence
  "ancien" suffit à Python : `for`/`in`/`reversed` se déduisent de
  getitem(0..n-1) + IndexError ; random.choice et sorted n'ont besoin que
  de len + indexation. On délègue donc à une list interne et on ne
  réimplémente rien : c'est ça, "émuler les types built-in".
"""

from collections import namedtuple

Track = namedtuple("Track", ["title", "artist"])


class Jukebox:
    def __init__(self, tracks: list[Track]) -> None:
        self._tracks = list(tracks)

    def __len__(self) -> int:
        return len(self._tracks)

    def __getitem__(self, position):
        return self._tracks[position]
