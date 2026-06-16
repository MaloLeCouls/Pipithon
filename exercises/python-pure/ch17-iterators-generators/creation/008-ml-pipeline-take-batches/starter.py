"""Pipeline ML : un `DataLoader` produit un flux paresseux de batches
(`list[int]`). On veut consommer **au plus `max_n` batches**, et **stopper
avant** dès qu'on rencontre un batch vide `[]` (sentinelle de fin de dataset).

Implémente `take_batches(dataset_stream, max_n)` :
- `dataset_stream` : iterator de `list[int]`.
- `max_n` : int ≥ 0, plafond de batches à consommer.
- retourne un Iterator qui yield jusqu'à `max_n` batches **non vides** ;
  s'arrête dès qu'un batch vide est rencontré (sans le yield).

⚠️ Piège du chapitre — *signalé* :
   itère **une seule fois** sur `dataset_stream`. Utilise deux outils
   d'`itertools` chaînés (penser : « stop-condition d'abord, plafond ensuite »).
"""
from __future__ import annotations

from collections.abc import Iterator


def take_batches(dataset_stream: Iterator[list[int]], max_n: int) -> Iterator[list[int]]:
    raise NotImplementedError("À implémenter")
