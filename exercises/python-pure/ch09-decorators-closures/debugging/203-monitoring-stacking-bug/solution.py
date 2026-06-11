"""Bug : `@timed` au lieu de `@timed('latency')`.

Fix : appelle la factory avec un label avant l'application.
"""
from __future__ import annotations

TIMINGS: list[tuple[str, object]] = []


def timed(label: str):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            TIMINGS.append((label, result))
            return result
        return wrapper
    return decorator


@timed("latency")
def ping() -> str:
    return "pong"
