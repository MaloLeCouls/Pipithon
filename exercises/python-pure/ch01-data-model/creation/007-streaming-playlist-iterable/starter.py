"""Une plateforme de streaming veut une Playlist qu'on peut parcourir
(`for track in playlist`), tester (`"X" in playlist`) et trancher
(`playlist[1:3]`) — SANS écrire __iter__ ni __contains__.

Implémente la classe `Playlist` :
- `__init__(self, tracks: list[str])`.
- `__len__` : nombre de morceaux.
- `__getitem__(self, key)` : si `key` est un int -> le morceau ;
  si `key` est une slice -> une nouvelle Playlist avec les morceaux tranchés.

Piège signalé : un slicing naïf renverrait une list. On veut une Playlist.
"""


class Playlist:
    def __init__(self, tracks: list[str]) -> None:
        raise NotImplementedError("À implémenter")

    def __len__(self) -> int:
        raise NotImplementedError("À implémenter")

    def __getitem__(self, key):
        raise NotImplementedError("À implémenter")
