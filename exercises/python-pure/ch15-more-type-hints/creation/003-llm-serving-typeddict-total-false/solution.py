"""Choix de design :
- `NotRequired[T]` : clé optionnelle, individuellement. C'est plus fin
  que `total=False` qui rend TOUTES les clés optionnelles.
- `is_greedy` lit via `.get(...)` pour gérer les clés absentes proprement.
- À runtime, c'est juste un dict ; le check `is None` matche aussi le
  cas où la clé est absente.
"""
from __future__ import annotations

from typing import NotRequired, TypedDict


class SamplingConfig(TypedDict):
    temperature: float
    top_k: NotRequired[int]
    top_p: NotRequired[float]
    seed: NotRequired[int]


def is_greedy(cfg: SamplingConfig) -> bool:
    return (
        cfg["temperature"] == 0.0
        and cfg.get("top_k") is None
        and cfg.get("top_p") is None
    )
