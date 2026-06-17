"""Cette routine `serve_one` est elle-même une coroutine, mais elle
appelle `asyncio.run(...)` pour wrapper une sous-coroutine. Conséquence
immédiate côté CPython : `RuntimeError: asyncio.run() cannot be called
from a running event loop`. Côté Pyodide : `RuntimeError` similaire car
la WebLoop est déjà active.

Indices :
- `asyncio.run` est fait pour le TOP LEVEL (un script, un main).
- Dans une coroutine, on `await` directement la sous-coroutine.
- Cherche la ligne fautive et remplace-la par `await`.
"""
from __future__ import annotations

import asyncio


async def _tokenize(prompt: str) -> int:
    await asyncio.sleep(0)
    return len(prompt)


async def serve_one(prompt: str) -> int:
    # BUG : asyncio.run sur une coroutine, depuis une coroutine -> RuntimeError.
    return asyncio.run(_tokenize(prompt))
