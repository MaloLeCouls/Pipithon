"""Premier exo qui utilise le framework pymistral !

Implémente `sample_next(logits, config, sampler) -> int` :
- accepte un Sampler (protocol de pymistral.sampling),
- l'appelle avec (logits, config),
- renvoie le token id choisi.

Annote tous les paramètres et le retour. Importe les types depuis pymistral.
"""
from __future__ import annotations


def sample_next(logits, config, sampler):
    ...
