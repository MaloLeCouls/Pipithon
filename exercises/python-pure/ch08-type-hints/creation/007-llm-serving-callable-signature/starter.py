"""On veut une fonction qui pré-applique un scoring sur un batch de Logits.

Implémente `top_token_per_batch(batch, scorer)` :
- batch : Iterable[Logits]
- scorer : Callable[[Logits, GenerationConfig], int] (signature précise !)
- retour : list[int] (un token id par item du batch)

Utilise `GenerationConfig()` par défaut. Annote précisément avec
Callable[[...], ...]. Importe depuis pymistral.
"""
from __future__ import annotations


def top_token_per_batch(batch, scorer):
    ...
