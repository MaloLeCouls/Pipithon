"""Fix : `await asyncio.gather(*tasks)` avant le `return`.

C'est ce qui cède la main à la boucle pour qu'elle exécute les tasks,
ET attend leur terminaison. Sans ça, `dispatch` rend la main avant que
qui que ce soit ait pu tourner.

(Variante équivalente : await chaque task individuellement. `gather` est
juste l'idiomatique.)
"""
from __future__ import annotations

import asyncio


async def _run_job(job_id: int, results: list[int]) -> None:
    await asyncio.sleep(0)
    results.append(job_id)


async def dispatch(job_ids: list[int]) -> list[int]:
    results: list[int] = []
    tasks: list[asyncio.Task[None]] = []
    for jid in job_ids:
        tasks.append(asyncio.create_task(_run_job(jid, results)))
    if tasks:
        await asyncio.gather(*tasks)
    return results
