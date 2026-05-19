"""Cette Playlist a 2 bugs. Les tests les exposent.
Corrige en chirurgie, sans réécrire from scratch.
"""


class Playlist:
    def __init__(self, tracks):
        self._tracks = list(tracks)

    def __len__(self):
        return len(self._tracks) - 1

    def __getitem__(self, index):
        return self._tracks[index + 1]
