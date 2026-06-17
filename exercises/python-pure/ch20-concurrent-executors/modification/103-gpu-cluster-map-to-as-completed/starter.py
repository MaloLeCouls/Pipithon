"""Tu utilises `ex.map` pour récupérer les résultats de tes jobs GPU.
Mais `map` te force à attendre la PROCHAINE ATTENDUE (selon ordre de
soumission). Si le job 0 est lent et que le 5 finit le premier, tu ne
verras le 5 que quand le 0 sera prêt — pas idéal pour un monitor live.

Refactore : utilise `submit + as_completed` pour traiter dans l'ordre
de FIN. Le retour est `list[tuple[int, int]]` (job_id, output) dans
l'ordre d'arrivée.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor


def run_job(job_id: int, runtime: float) -> tuple[int, int]:
    time.sleep(runtime)
    return job_id, int(runtime * 1000)


def report(jobs: list[tuple[int, float]]) -> list[tuple[int, int]]:
    # Anti-pattern : ex.map bloque sur l'ordre de soumission.
    with ThreadPoolExecutor(max_workers=4) as ex:
        return list(ex.map(lambda j: run_job(j[0], j[1]), jobs))
