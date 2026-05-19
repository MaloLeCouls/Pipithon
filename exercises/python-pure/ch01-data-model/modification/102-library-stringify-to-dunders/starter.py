"""Ce code marche mais réinvente l'affichage avec une méthode to_string().

Refactor :
1. Supprime to_string().
2. Ajoute __repr__ -> Book(isbn='1', title='Dune') (non ambigu, debug).
3. Ajoute __str__ -> Dune (1) (lisible, orienté humain).
4. Comportement des données inchangé.
"""


class Book:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title

    def to_string(self):
        return self.title + " (" + self.isbn + ")"
