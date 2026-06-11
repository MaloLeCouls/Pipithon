"""KVCache — cache par couche, jouet. Chapitres 11 (Pythonic object) & 15 (generics).

Pas de vraie attention : on stocke des séquences de tokens par couche, pour
simuler le coût mémoire et l'éviction. Le mapping `layer -> list[Token]` est
exposé via `get` / `append` / `clear` ; jamais d'accès direct au dict interne.
"""
from __future__ import annotations

from pymistral.tokens import Token


class KVCache:
    """Cache par couche, indexé `0..num_layers-1`."""

    def __init__(self, num_layers: int) -> None:
        if num_layers <= 0:
            raise ValueError(f"num_layers must be > 0, got {num_layers}")
        self._num_layers = num_layers
        self._cache: dict[int, list[Token]] = {i: [] for i in range(num_layers)}

    @property
    def num_layers(self) -> int:
        return self._num_layers

    def _check_layer(self, layer: int) -> None:
        if not 0 <= layer < self._num_layers:
            raise IndexError(
                f"layer {layer} out of range [0, {self._num_layers})"
            )

    def get(self, layer: int) -> list[Token]:
        """Renvoie une *copie* — l'appelant ne peut pas muter le cache."""
        self._check_layer(layer)
        return list(self._cache[layer])

    def append(self, layer: int, token: Token) -> None:
        self._check_layer(layer)
        self._cache[layer].append(token)

    def clear(self, layer: int | None = None) -> None:
        """Vide une couche (ou tout si `layer is None`)."""
        if layer is None:
            for lst in self._cache.values():
                lst.clear()
        else:
            self._check_layer(layer)
            self._cache[layer].clear()

    def __len__(self) -> int:
        """Nombre total de tokens stockés, toutes couches confondues."""
        return sum(len(lst) for lst in self._cache.values())

    def __repr__(self) -> str:
        return f"KVCache(num_layers={self._num_layers}, total_tokens={len(self)})"
