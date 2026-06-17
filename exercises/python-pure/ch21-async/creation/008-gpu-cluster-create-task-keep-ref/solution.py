"""Choix de design :
- `tasks: set[asyncio.Task]` : on garde la ref forte ; sans ça, le runtime
  AVERTIT (et peut GC) la Task — c'est documenté dans la note du dev guide
  asyncio.
- `add_done_callback(tasks.discard)` : on libère la ref quand la Task finit,
  pour ne pas faire fuiter de la mémoire si on schedule en boucle.
- `gather(*tasks)` : attend que toutes les tasks soient terminées, dans
  l'ordre fourni — l'ordre d'arrivée dans `sink` reflète l'ordonnancement.
"""
from __future__ import annotations

import asyncio


async def run_job(job_id: int, sink: list[int]) -> None:
    await asyncio.sleep(0)
    sink.append(job_id)


async def schedule_all(job_ids: list[int]) -> list[int]:
    sink: list[int] = []
    tasks: set[asyncio.Task[None]] = set()
    for jid in job_ids:
        t = asyncio.create_task(run_job(jid, sink))
        tasks.add(t)
        t.add_done_callback(tasks.discard)
    if tasks:
        await asyncio.gather(*tasks)
    return sink
