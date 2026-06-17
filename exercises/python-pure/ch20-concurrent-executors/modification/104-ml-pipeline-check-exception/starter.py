"""Cette fn submit N jobs, attend qu'ils finissent — et compte tout
comme un succès. Les exceptions sont silencieuses (pas de result()
ni de exception()). Refactore pour distinguer succès et échecs.

Contrat solution :
- `run_all(payloads) -> tuple[int, int]` renvoie `(success_count, fail_count)`.
- Pour chaque future, vérifie `fut.exception()`.
"""
from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def run_one(payload: str) -> int:
    time.sleep(0.001)
    if payload == "BROKEN":
        raise RuntimeError("fail")
    return len(payload)


def run_all(payloads: list[str]) -> int:
    # Anti-pattern : on compte ALL en succès, sans vérifier exception().
    count = 0
    with ThreadPoolExecutor(max_workers=4) as ex:
        futures = [ex.submit(run_one, p) for p in payloads]
        for _fut in as_completed(futures):
            count += 1
    return count
