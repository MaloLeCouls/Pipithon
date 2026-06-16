"""Un serveur d'inférence (fake) veut un *streamer* paresseux : les tokens
sont livrés un par un comme s'ils étaient générés par un modèle.
C'est le cas canonique d'utilisation des générateurs côté LLM serving —
on n'attend pas la fin de la séquence pour afficher le premier token.

Implémente `stream_tokens(text, vocab)` :
- `text` : str d'entrée.
- `vocab` : `Vocabulary` (pymistral, mutable — on l'enrichit en passant).
- yield un `Token` pymistral par **caractère** de `text`. L'id du token est
  obtenu par `vocab.add(ch)` (auto-incrémente ; ré-utilise l'id si le
  caractère est déjà dans le vocab).

Pas de liste intermédiaire — c'est un générateur. Le client doit pouvoir
afficher les caractères au fur et à mesure, sans attendre la fin du texte.
"""
from __future__ import annotations

from collections.abc import Iterator

from pymistral import Token, Vocabulary


def stream_tokens(text: str, vocab: Vocabulary) -> Iterator[Token]:
    raise NotImplementedError("À implémenter")
