"""On veut instrumenter les samplers pymistral sans modifier leur code.

Implémente :
- une liste-module `SAMPLE_LOG: list[tuple[int, int]]` qui accumule des
  paires (token_id, n_logits).
- un décorateur `log_sampler` qui :
    * appelle le sampler décoré,
    * ajoute (result, len(args[0])) à SAMPLE_LOG (args[0] = les Logits),
    * renvoie le résultat.

Ne modifie pas pymistral. Décore `greedy_sampler` côté tests.
"""
from __future__ import annotations

SAMPLE_LOG: list[tuple[int, int]] = []


def log_sampler(fn):
    ...
