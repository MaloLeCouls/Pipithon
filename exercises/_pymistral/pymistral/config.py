"""GenerationConfig — paramètres de génération. Chapitre 5 (data class builders).

`frozen=True` -> hashable, partageable entre requêtes, immutabilité forcée.
Les valeurs par défaut suivent la convention Mistral (Couche 5 du mapping).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GenerationConfig:
    """Paramètres d'une session de génération.

    Attributs:
        temperature: > 0 contrôle l'aplatissement de la softmax (1.0 neutre).
        top_k: garde les k logits les plus hauts (None = pas de filtre).
        top_p: nucleus sampling : garde le plus petit ensemble de probabilité
            cumulée >= p (None = pas de filtre).
        max_tokens: budget de tokens à générer.
        seed: graine RNG (None = non déterministe).
    """

    temperature: float = 1.0
    top_k: int | None = None
    top_p: float | None = None
    max_tokens: int = 64
    seed: int | None = None

    def __post_init__(self) -> None:
        if self.temperature <= 0:
            raise ValueError(f"temperature must be > 0, got {self.temperature}")
        if self.top_k is not None and self.top_k <= 0:
            raise ValueError(f"top_k must be > 0 if set, got {self.top_k}")
        if self.top_p is not None and not 0 < self.top_p <= 1.0:
            raise ValueError(f"top_p must be in (0, 1], got {self.top_p}")
        if self.max_tokens <= 0:
            raise ValueError(f"max_tokens must be > 0, got {self.max_tokens}")
