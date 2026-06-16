"""Le service de livraison filtre les colis en attente avec une *list
comprehension* — propre, mais le résultat est entièrement matérialisé en RAM
avant même le premier yield.

Refactor : transforme la list comprehension en **generator expression**.
Conserve la signature et le comportement (mêmes ids, dans le même ordre)."""
from __future__ import annotations

from collections.abc import Iterable, Iterator


class Package:
    def __init__(self, tracking_id: str, status: str) -> None:
        self.tracking_id = tracking_id
        self.status = status


def pending_tracking_ids(packages: Iterable[Package]) -> Iterator[str]:
    return [p.tracking_id for p in packages if p.status == "pending"]  # type: ignore[return-value]
