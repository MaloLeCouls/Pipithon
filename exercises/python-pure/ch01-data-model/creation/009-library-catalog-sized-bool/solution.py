"""Choix de design :
- On ne définit PAS __bool__ sur Catalog : quand __bool__ est absent,
  Python se rabat sur __len__. Un catalogue vide est donc falsy
  gratuitement, et on garde une seule source de vérité (la taille).
- Catalog.__getitem__ délègue à la liste : indexation négative + IndexError
  corrects sans effort.
- Book.__repr__ est autonome ; Catalog.__repr__ ne dépend que de len(self).
"""


class Book:
    def __init__(self, isbn: str, title: str) -> None:
        self.isbn = isbn
        self.title = title

    def __repr__(self) -> str:
        return f"Book(isbn={self.isbn!r}, title={self.title!r})"


class Catalog:
    def __init__(self, books: list[Book]) -> None:
        self._books = list(books)

    def __len__(self) -> int:
        return len(self._books)

    def __getitem__(self, index: int) -> Book:
        return self._books[index]

    def __repr__(self) -> str:
        return f"Catalog({len(self)} books)"
