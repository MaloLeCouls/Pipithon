"""Sampler — Protocol + stratégies. Chapitres 7 (HOF), 10 (patterns), 13 (Protocol).

Un `Sampler` est une callable `(Logits, GenerationConfig, Random | None) -> int`.
Trois stratégies fournies : greedy (argmax), top-k, top-p (nucleus).

`Protocol` permet à des fonctions et à des classes call-ables de satisfaire le
même type sans héritage explicite (duck typing statique).
"""
from __future__ import annotations

import random
from typing import Protocol, runtime_checkable

from pymistral.config import GenerationConfig
from pymistral.logits import Logits


@runtime_checkable
class Sampler(Protocol):
    """Stratégie de sampling : prend un Logits + config, renvoie un id."""

    def __call__(
        self,
        logits: Logits,
        config: GenerationConfig,
        rng: random.Random | None = None,
    ) -> int: ...


def greedy_sampler(
    logits: Logits,
    config: GenerationConfig,  # noqa: ARG001
    rng: random.Random | None = None,  # noqa: ARG001
) -> int:
    """Toujours l'argmax — déterministe, rng ignoré."""
    return logits.argmax()


def top_k_sampler(
    logits: Logits,
    config: GenerationConfig,
    rng: random.Random | None = None,
) -> int:
    """Échantillonne parmi les `top_k` logits les plus hauts.

    `rng` requis pour la reproductibilité ; à défaut un Random nouveau est créé
    (avec la `config.seed` si fournie).
    """
    if config.top_k is None:
        raise ValueError("top_k_sampler requires config.top_k to be set")
    if rng is None:
        rng = random.Random(config.seed)
    probs = logits.softmax(temperature=config.temperature)
    indexed = sorted(enumerate(probs), key=lambda kv: kv[1], reverse=True)
    kept = indexed[: config.top_k]
    total = sum(p for _, p in kept)
    weights = [p / total for _, p in kept]
    choice_idx = _weighted_choice(weights, rng)
    return kept[choice_idx][0]


def top_p_sampler(
    logits: Logits,
    config: GenerationConfig,
    rng: random.Random | None = None,
) -> int:
    """Nucleus sampling : garde le plus petit ensemble dont la proba cumulée >= top_p."""
    if config.top_p is None:
        raise ValueError("top_p_sampler requires config.top_p to be set")
    if rng is None:
        rng = random.Random(config.seed)
    probs = logits.softmax(temperature=config.temperature)
    indexed = sorted(enumerate(probs), key=lambda kv: kv[1], reverse=True)
    kept: list[tuple[int, float]] = []
    cum = 0.0
    for i, p in indexed:
        kept.append((i, p))
        cum += p
        if cum >= config.top_p:
            break
    total = sum(p for _, p in kept)
    weights = [p / total for _, p in kept]
    choice_idx = _weighted_choice(weights, rng)
    return kept[choice_idx][0]


def _weighted_choice(weights: list[float], rng: random.Random) -> int:
    """Tirage pondéré déterministe — utilise rng.random() pour la reproductibilité."""
    r = rng.random()
    cum = 0.0
    for i, w in enumerate(weights):
        cum += w
        if r < cum:
            return i
    return len(weights) - 1
