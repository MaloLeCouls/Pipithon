"""Ton scheduler GPU `dispatch` schedule N jobs via `create_task` puis
renvoie la liste des résultats. Problème : la liste est SYSTÉMATIQUEMENT
vide. Pourtant `create_task` semble bien faire son boulot.

Indices :
- `create_task` ENREGISTRE la coroutine sur la boucle, mais elle ne tourne
  pas tant qu'on ne lui cède pas le contrôle.
- Si `dispatch` `return` tout de suite, la boucle n'a jamais eu l'occasion
  de scheduler les jobs.
- Il faut **attendre** que les tasks aient fini avant de retourner. Une seule
  ligne à ajouter.
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
    # BUG : on retourne sans attendre les tasks -> results est vide.
    return results
