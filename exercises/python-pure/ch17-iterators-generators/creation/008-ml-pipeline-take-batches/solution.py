"""Choix de design :
- Pipeline `takewhile -> islice` : composition de deux iterators du module
  `itertools`, C-implémentés et paresseux. Lis-le « tant que non vide,
  puis cape à max_n ».
- L'ordre `islice(takewhile(...), n)` est crucial : sinon on caperait
  *avant* de tester la sentinelle, et on consommerait potentiellement plus.
- Un seul passage sur `dataset_stream` — respect du contrat « iterator
  d'entrée à usage unique ».
"""
from __future__ import annotations

from collections.abc import Iterator
from itertools import islice, takewhile


def take_batches(dataset_stream: Iterator[list[int]], max_n: int) -> Iterator[list[int]]:
    return islice(takewhile(lambda b: len(b) > 0, dataset_stream), max_n)
