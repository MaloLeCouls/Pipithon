"""Cette classe Chair a 2 bugs. Les tests les exposent.
Corrige en chirurgie (le moins de lignes modifiées possible),
sans réécrire la classe from scratch.
"""


class Chair:
    def __init__(self, ref, price):
        self.ref = ref

    def __repr__(self):
        return f"Chair(ref={self.ref}, price={self.price})"
