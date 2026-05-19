"""Choix de design :
- __repr__ non ambigu (reconstruit mentalement l'objet) ; __str__ pour
  l'affichage humain. Sans __str__, print() retomberait sur __repr__ :
  on les sépare car les deux publics sont différents (dev vs utilisateur).
- to_string() disparaît : l'idiome Python est repr()/str(), pas une
  méthode maison que personne d'autre n'appellera.
"""


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    def __repr__(self) -> str:
        return f"Book(isbn={self.isbn!r}, title={self.title!r})"

    def __str__(self) -> str:
        return f"{self.title} ({self.isbn})"
