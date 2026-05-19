"""Choix de design :
- __getitem__ distingue slice et int : sur une slice on réemballe dans
  Playlist pour rester fermé sur le type (un slice de Playlist est une
  Playlist) ; sur un int on renvoie l'élément brut.
- On NE définit ni __iter__ ni __contains__ : le protocole séquence ancien
  (getitem indexé depuis 0 + IndexError) suffit à Python pour `for` et `in`.
- list(tracks) : découplage de la liste du caller.
"""


class Playlist:
    def __init__(self, tracks: list[str]) -> None:
        self._tracks = list(tracks)

    def __len__(self) -> int:
        return len(self._tracks)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return Playlist(self._tracks[key])
        return self._tracks[key]
