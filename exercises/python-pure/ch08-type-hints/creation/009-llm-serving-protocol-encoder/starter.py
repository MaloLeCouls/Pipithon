"""On veut écrire une fonction qui accepte N'IMPORTE QUEL objet capable
d'encoder du texte en tokens — pas seulement BPETokenizer.

Définis :

1. Un `Protocol` `Encoder` avec une méthode :
       encode(self, text: str) -> list[Token]
   Marque-le `@runtime_checkable` (pour isinstance).

2. Une fonction `count_tokens(text: str, encoder: Encoder) -> int` qui
   renvoie le nombre de tokens produits par `encoder.encode(text)`.

Pas d'héritage de BPETokenizer : c'est du typing structurel.
"""
from __future__ import annotations


# Définis Encoder ici.


def count_tokens(text, encoder):
    ...
