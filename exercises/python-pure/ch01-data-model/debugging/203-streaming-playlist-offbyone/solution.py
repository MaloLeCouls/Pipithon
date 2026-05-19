"""Corrections (chirurgie minimale) :
- Bug 1 : __getitem__ faisait self._tracks[index + 1] -> indexation
  décalée (saute le 1er morceau, IndexError prématurée). On retire le +1.
- Bug 2 : __len__ faisait len(...) - 1 -> longueur fausse et incohérente
  avec l'itération. On retire le -1.
Le protocole séquence (for / in / reversed) redevient correct tout seul.
"""


class Playlist:
    def __init__(self, tracks):
        self._tracks = list(tracks)

    def __len__(self):
        return len(self._tracks)

    def __getitem__(self, index):
        return self._tracks[index]
