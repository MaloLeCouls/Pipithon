"""Choix de design :
- str | bytes : Union explicite via PEP 604.
- isinstance discrimine au runtime ; mypy comprend le narrowing dans la branche.
"""
from __future__ import annotations


def byte_size(source: str | bytes) -> int:
    if isinstance(source, str):
        return len(source.encode("utf-8"))
    return len(source)
