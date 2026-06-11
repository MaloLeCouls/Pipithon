"""Choix de design :
- Sampler est un Protocol défini dans pymistral.sampling. Importé tel quel,
  il sert d'annotation à `sampler` — n'importe quelle callable au bon
  protocole satisfait le typage.
- Le retour est int (token id).
"""
from __future__ import annotations

from pymistral import GenerationConfig, Logits
from pymistral.sampling import Sampler


def sample_next(logits: Logits, config: GenerationConfig, sampler: Sampler) -> int:
    return sampler(logits, config)
