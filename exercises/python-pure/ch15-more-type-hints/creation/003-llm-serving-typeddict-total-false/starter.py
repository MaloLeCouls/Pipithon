"""Une `SamplingConfig` envoyée par l'API user a `temperature` OBLIGATOIRE,
et `top_k`/`top_p`/`seed` OPTIONNELS. `TypedDict` supporte ce mélange
via `NotRequired[...]`.

Contrat :

- Déclare `SamplingConfig(TypedDict)` avec :
  - `temperature: float` (obligatoire),
  - `top_k: NotRequired[int]`,
  - `top_p: NotRequired[float]`,
  - `seed: NotRequired[int]`.
- Écris `is_greedy(cfg: SamplingConfig) -> bool` :
  True si `temperature == 0.0` ET `top_k` absent ET `top_p` absent.
  (Astuce : `cfg.get("top_k") is None and cfg.get("top_p") is None`).
"""
from __future__ import annotations

from typing import NotRequired, TypedDict


class SamplingConfig(TypedDict):
    ...


def is_greedy(cfg: SamplingConfig) -> bool:
    raise NotImplementedError("À implémenter")
