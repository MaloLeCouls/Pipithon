"""Une plateforme de streaming affiche ses films dans des logs de debug.
Certains films ne sont pas encore notés (rating=None).

Implémente la classe `Movie` :
- `__init__(self, title: str, rating: float | None = None)`.
- `__repr__` :
    * si rating est défini   -> Movie(title='Dune', rating=8.5)
    * si rating vaut None    -> Movie(title='Tenet', rating=unrated)
"""


class Movie:
    def __init__(self, title: str, rating: float | None = None) -> None:
        ...

    def __repr__(self) -> str:
        ...
