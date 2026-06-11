"""Choix de design :
- 3 niveaux : retry(N) -> decorator -> wrapper.
- On capture `last_exc` puis on la relève après la boucle si on n'a pas réussi.
- Pas de backoff/sleep ici : ce serait une autre dimension.
"""
from __future__ import annotations


def retry(max_attempts: int = 3):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            last_exc: BaseException | None = None
            for _ in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:  # noqa: BLE001 — on relève après
                    last_exc = exc
            assert last_exc is not None
            raise last_exc
        return wrapper
    return decorator
