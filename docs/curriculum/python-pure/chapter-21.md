---
chapter: 21
title: "Asynchronous Programming"
fluent_python_pages: "757-810"   # approx, éd. 2 O'Reilly 2022
tier: S
status: active
prereqs: [17, 19]
---

## Concepts clés (à drill)
- `async def` / `await` ; event loop (ce que c'est vraiment)
- Native coroutines vs classic coroutines vs generators
- `asyncio` : `run`, `create_task`, `gather`, `wait`, `to_thread`
- Async iterables (`__aiter__`/`__anext__`), async generators, `async for`
- Async context managers (`__aenter__`/`__aexit__`), `async with`
- 3 types d'awaitables : coroutines, Tasks, Futures
- I/O concurrent massif (scraping, serveurs)

## Pièges classiques
- `await` oublié → coroutine jamais exécutée (warning « never awaited »)
- Code **bloquant** dans une coroutine → fige toute la boucle
- `asyncio.gather` sans `return_exceptions` → une erreur annule tout
- Créer une Task sans la garder → garbage-collectée avant la fin
- Mélanger sync et async (appeler `asyncio.run` dans une boucle déjà active)

## Thèmes recommandés
`llm-serving` (serveur d'inférence *fake* : streaming async de tokens — cas
canonique), `gpu-cluster` (scheduler async *fake*), `monitoring`.

## Référence « checkpoint » niveau 5
Reproduire le **probe/scraper asyncio** (ex. `blogdom` / drapeaux async) :
`gather`, `as_completed` async, `async with`, sémaphore — cf.
`fluentpython/example-code-2e` dossier `21-async`.

## Lien PyMistral
`pymistral_link: null`. **Base FastAPI / inference servers**
(`mapping-mistral.md` Couches 1 & 14, tier S). Thème `llm-serving` *fake*
central. Pont PyMistral à renseigner quand le framework arrivera.
