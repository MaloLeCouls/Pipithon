"""Choix de design :
- typing.NamedTuple : champs nommés annotés, immuable, __repr__/__eq__/
  hash gratuits, et c'est toujours un tuple (indexable, déballable,
  utilisable comme clé). Idéal pour une valeur figée comme une adresse.
"""

from typing import NamedTuple


class Address(NamedTuple):
    street: str
    city: str
    zip_code: str
