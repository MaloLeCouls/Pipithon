"""Choix de design :
- !r sur les deux champs : str -> guillemets corrects et robustes (apostrophes).
- Ordre des champs dans le repr = ordre du constructeur (lecture évidente).
"""


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    def __repr__(self) -> str:
        return f"Book(isbn={self.isbn!r}, title={self.title!r})"
