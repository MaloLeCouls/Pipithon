"""Tu schedules des jobs GPU « fire-and-forget » sur ton cluster. Chaque
`schedule_job(job_id)` crée une Task asyncio... mais si tu ne gardes pas
sa référence, le GC peut la collecter avant qu'elle finisse — le job est
silencieusement perdu (cf. note du dev guide asyncio).

Contrat :

- `async def run_job(job_id: int, sink: list[int]) -> None` est fournie :
  attend `asyncio.sleep(0)`, puis fait `sink.append(job_id)`.
- `async def schedule_all(job_ids: list[int]) -> list[int]` :
  - crée un `set[asyncio.Task[None]]` pour garder les refs ;
  - pour chaque `jid` dans `job_ids` : crée une Task via `asyncio.create_task`,
    ajoute-la au set, attache un `add_done_callback(set.discard)` pour
    libérer la ref une fois finie ;
  - `await asyncio.gather(*tasks)` pour attendre que tout finisse ;
  - renvoie `sink` (rempli par les jobs).
"""
from __future__ import annotations

import asyncio


async def run_job(job_id: int, sink: list[int]) -> None:
    await asyncio.sleep(0)
    sink.append(job_id)


async def schedule_all(job_ids: list[int]) -> list[int]:
    raise NotImplementedError("À implémenter")
