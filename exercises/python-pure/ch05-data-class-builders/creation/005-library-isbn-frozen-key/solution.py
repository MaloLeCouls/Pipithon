"""Choix de design :
- frozen=True : l'immutabilité fait générer un __hash__ cohérent avec
  __eq__ (sur tous les champs). On obtient gratuitement un objet-valeur
  utilisable comme clé de dict/set, sans écrire __hash__/__eq__ à la main.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class BookId:
    isbn: str
    copy_no: int
