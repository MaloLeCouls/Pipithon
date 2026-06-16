"""Sampler à *online accumulation* : pendant qu'un modèle stream les logprobs
des tokens générés, on entretient leur moyenne courante côté serveur — sans
stocker l'historique.

Implémente `make_logprob_accumulator()` :
- retourne une **coroutine classique** déjà prête à recevoir des valeurs.
- `coro.send(lp)` (où `lp: float`) accumule `lp` et renvoie la moyenne
  courante.
- `coro.close()` ferme proprement la coroutine sans erreur.
- L'**état** (somme, compteur) est interne à la coroutine — aucune variable
  globale.

Conditions :
- Le tout premier `.send(lp)` doit fonctionner — pense au piège du chapitre
  qui consiste à oublier l'amorçage (`next(coro)` initial).
- La fonction renvoyée par `make_logprob_accumulator()` doit déjà être
  amorcée : l'utilisateur n'a **pas** à faire `next()` avant son premier
  `send`.
"""
from __future__ import annotations

from collections.abc import Generator


def make_logprob_accumulator() -> Generator[float, float, None]:
    raise NotImplementedError("À implémenter")
