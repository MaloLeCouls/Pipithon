"""Choix de design :
- Le cas None est traité dans le repr, pas dans __init__ : l'objet garde
  fidèlement None (utile pour distinguer 'pas noté' de 'noté 0').
- 'unrated' est un sentinel lisible, sans guillemets : ce n'est pas une str
  de donnée mais un état, donc pas de !r dessus.
"""


class Movie:
    def __init__(self, title: str, rating: float | None = None) -> None:
        self.title = title
        self.rating = rating

    def __repr__(self) -> str:
        rating = "unrated" if self.rating is None else self.rating
        return f"Movie(title={self.title!r}, rating={rating})"
